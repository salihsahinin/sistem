//! `pretool-altajan-okuma.sh` karşılığı: alt-ajan (agent_id var) başka bağlam pencerelerini okuyamaz (çıkış 2).
use crate::ortak::{Ortam, Sonuc, ekle_satir, ev_dizini, ilk_n, json_oku, py_dumps, py_isabs, py_truthy, realpath, sep, ts_yerel};
use serde_json::{Value, json};
use std::path::{Path, PathBuf};

fn kelime(c: char) -> bool {
    c.is_alphanumeric() || c == '_'
}
fn yol_kar(c: char) -> bool {
    kelime(c) || c == '.' || c == '-'
}

/// `<<-?\s*['"]?(\w+)['"]?.*?\n\1\s*$` (S|M) -> `<<HEREDOC>>` (geri-başvuru Rust regex'te yok, elle).
fn heredoc_sil(s: &str) -> String {
    let c: Vec<char> = s.chars().collect();
    let n = c.len();
    let mut cikti = String::new();
    let mut i = 0;
    while i < n {
        if c[i] == '<' && i + 1 < n && c[i + 1] == '<' && let Some(son) = heredoc_dene(&c, i + 2) {
            cikti.push_str("<<HEREDOC>>");
            i = son;
            continue;
        }
        cikti.push(c[i]);
        i += 1;
    }
    cikti
}

fn heredoc_dene(c: &[char], mut p: usize) -> Option<usize> {
    let n = c.len();
    if p < n && c[p] == '-' {
        p += 1;
    }
    while p < n && c[p].is_whitespace() {
        p += 1;
    }
    if p < n && (c[p] == '\'' || c[p] == '"') {
        p += 1;
    }
    let bas = p;
    while p < n && kelime(c[p]) {
        p += 1;
    }
    if p == bas {
        return None;
    }
    for uzun in (1..=(p - bas)).rev() {
        let kel = &c[bas..bas + uzun];
        let mut q = bas + uzun;
        if q < n && (c[q] == '\'' || c[q] == '"') {
            q += 1;
        }
        let mut i = q;
        while i < n {
            if c[i] == '\n' && i + 1 + uzun <= n && &c[i + 1..i + 1 + uzun] == kel {
                let a = i + 1 + uzun;
                let mut b = a;
                while b < n && c[b].is_whitespace() {
                    b += 1;
                }
                // açgözlü \s*, ardından $ (satır sonu ya da dize sonu) sağlayan en büyük konum
                let mut e = b;
                loop {
                    if e == n || c[e] == '\n' {
                        return Some(e);
                    }
                    if e == a {
                        break;
                    }
                    e -= 1;
                }
            }
            i += 1;
        }
    }
    None
}

fn yol_adaylari(cmd: &str) -> Vec<String> {
    let c: Vec<char> = cmd.chars().collect();
    let n = c.len();
    let mut sonuc = vec![];
    let mut p = 0;
    while p < n {
        let onceki_yasak = p > 0 && (kelime(c[p - 1]) || c[p - 1] == '@' || c[p - 1] == ':');
        if !onceki_yasak && let Some(e) = yol_dene(&c, p) {
            sonuc.push(c[p..e].iter().collect());
            p = e;
            continue;
        }
        p += 1;
    }
    sonuc
}

/// `(?:[A-Za-z]:)?/?[\w.\-]+(?:/[\w.\-]+)+` bu konumda eşleşirse bitiş konumu.
fn yol_dene(c: &[char], p: usize) -> Option<usize> {
    let n = c.len();
    let surucu_secenek: &[bool] = if p + 1 < n && c[p].is_ascii_alphabetic() && c[p + 1] == ':' { &[true, false] } else { &[false] };
    for &surucu in surucu_secenek {
        let pos = if surucu { p + 2 } else { p };
        let slash_secenek: &[bool] = if pos < n && c[pos] == '/' { &[true, false] } else { &[false] };
        for &slash in slash_secenek {
            let pos2 = if slash { pos + 1 } else { pos };
            let mut q = pos2;
            while q < n && yol_kar(c[q]) {
                q += 1;
            }
            if q == pos2 {
                continue;
            }
            let mut seg = 0;
            while q < n && c[q] == '/' {
                let mut r = q + 1;
                while r < n && yol_kar(c[r]) {
                    r += 1;
                }
                if r > q + 1 {
                    q = r;
                    seg += 1;
                } else {
                    break;
                }
            }
            if seg >= 1 {
                return Some(q);
            }
        }
    }
    None
}

pub fn kos(o: &Ortam) -> Sonuc {
    let mut s = Sonuc::bos();
    let Some(Value::Object(g)) = json_oku(&o.stdin_metin()) else { return s };
    let agent_id = g.get("agent_id").cloned().unwrap_or(Value::Null);
    if !py_truthy(&agent_id) {
        return s;
    }
    let arac = g.get("tool_name").and_then(Value::as_str).unwrap_or("").to_string();
    let ti = match g.get("tool_input") {
        Some(Value::Object(m)) => m.clone(),
        _ => Default::default(),
    };
    let repo = realpath(&o.repo);
    let home = ev_dizini();
    let kok: PathBuf = repo.parent().map(Path::to_path_buf).unwrap_or_default();
    let r = |p: &str| -> PathBuf { repo.join(p) };
    let yasak: Vec<PathBuf> = vec![
        home.join(".claude").join("projects"),
        kok.join("friday"),
        home.join("staj başlangıç"),
        home.join("Desktop").join("repo"),
        r("core").join("durum-kapsulu.md"),
        r("core").join("pano.md"),
        r("kuyruk").join("senaryo-defteri.md"),
        r("fikir-kutusu.md"),
        r("veri").join("bronz").join("hareket-olay.jsonl"),
        r("veri").join("bronz").join("baglam-olay.jsonl"),
        r("veri").join("bronz").join("altajan-okuma-olay.jsonl"),
        r("cc").join("gelen"),
        r("cc").join("devir"),
    ];
    let proj = format!("{}{}", home.join(".claude").join("projects").to_string_lossy(), sep());
    let tr = format!("{0}tool-results{0}", sep());
    let yasak_mi = |yol: &str| -> bool {
        if yol.is_empty() {
            return false;
        }
        let tam = if py_isabs(yol) { PathBuf::from(yol) } else { repo.join(yol) };
        let rp = realpath(&tam);
        let rs = rp.to_string_lossy().into_owned();
        if rs.contains(&tr) && rs.starts_with(&proj) {
            return false;
        }
        yasak.iter().any(|y| {
            let ys = y.to_string_lossy();
            rs == *ys || rs.starts_with(&format!("{ys}{}", sep()))
        })
    };
    let mut adaylar: Vec<String> = vec![];
    if matches!(arac.as_str(), "Read" | "Grep" | "Glob") {
        for k in ["file_path", "path"] {
            if let Some(Value::String(x)) = ti.get(k) {
                adaylar.push(x.clone());
            }
        }
    } else if arac == "Bash" {
        let ham = ti.get("command").and_then(Value::as_str).unwrap_or("");
        let cmd = heredoc_sil(ham);
        let ev = home.to_string_lossy().replace(sep(), "/");
        let cmd = cmd.replace('~', &ev).replace("$HOME", &ev).replace("${HOME}", &ev);
        adaylar = yol_adaylari(&cmd);
    }
    let mut kotu: Vec<String> = adaylar.into_iter().filter(|a| !a.is_empty() && yasak_mi(a)).collect();
    kotu.sort();
    kotu.dedup();
    if !kotu.is_empty() {
        if o.env("JARVIS_HOOK_TEST").is_none_or(str::is_empty) {
            let sid = g.get("session_id").and_then(Value::as_str).map(|x| ilk_n(x, 36)).unwrap_or_default();
            let satir = json!({"ts": ts_yerel(), "oturum": sid, "agent_id": agent_id,
                "agent_type": g.get("agent_type").cloned().unwrap_or(Value::Null), "arac": arac,
                "reddedilen": kotu, "kaynak": "pretool-altajan-okuma.sh"});
            let _ = ekle_satir(&o.repo.join("veri").join("bronz").join("altajan-okuma-olay.jsonl"), &py_dumps(&satir));
        }
        s.hata = format!("ALT-AJAN OKUMA KİLİDİ (İB-83): alt-ajan başka bağlam penceresini okuyamaz (transkript · kapsül/pano/defter/kutu · kütükler · Friday · dış projeler). Reddedilen: {}\n", kotu.join(", "));
        s.kod = 2;
    }
    s
}
