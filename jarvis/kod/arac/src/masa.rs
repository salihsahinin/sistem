//! `.claude/skills/karar-masasi/scripts/masa-uret.py` karşılığı: deterministik karar masası HTML üreticisi (İB-88 P1, Karar 96).
//! Çıkış: 0 üretildi · 2 spec hatası · 3 masa no çakışması. Şablon `<kök>/jarvis/.claude/skills/karar-masasi/sablon.html` (kök: `alan_ajani::kok_coz`).
//! Python'da yakalanmamış istisna (eksik alan, tür uyumsuzluğu, geçersiz JSON) olan durumlar `py::coker` ile stderr + çıkış 1.
use crate::alan_ajani::{kok_coz, metin_yaz};
use jarvis_rituel::argparse::{Ayrisan, Secenek};
use jarvis_rituel::py;
use regex::Regex;
use serde_json::Value;
use std::fs;
use std::path::Path;

type Hata = String;

fn py_str(v: &Value) -> Result<String, Hata> {
    match v {
        Value::String(s) => Ok(s.clone()),
        Value::Number(n) => Ok(n.to_string()),
        Value::Bool(true) => Ok("True".into()),
        Value::Bool(false) => Ok("False".into()),
        Value::Null => Ok("None".into()),
        _ => Err("kapsayıcı değer metne çevrilemedi".into()),
    }
}

/// Python doğruluk değeri (`bool(v)`).
fn dogru(v: Option<&Value>) -> bool {
    match v {
        None | Some(Value::Null) => false,
        Some(Value::Bool(b)) => *b,
        Some(Value::Number(n)) => n.as_f64().is_some_and(|f| f != 0.0),
        Some(Value::String(s)) => !s.is_empty(),
        Some(Value::Array(a)) => !a.is_empty(),
        Some(Value::Object(o)) => !o.is_empty(),
    }
}

/// `html.escape(s, quote=True)`.
fn html_kacis(s: &str) -> String {
    let mut r = String::with_capacity(s.len());
    for c in s.chars() {
        match c {
            '&' => r.push_str("&amp;"),
            '<' => r.push_str("&lt;"),
            '>' => r.push_str("&gt;"),
            '"' => r.push_str("&quot;"),
            '\'' => r.push_str("&#x27;"),
            _ => r.push(c),
        }
    }
    r
}

/// `e(s)`: güvenli etiket (`strong|code|em|br`) varsa aynen, yoksa kaçışlı. `s or ""` kuralı Python gibi.
fn e(etiket: &Regex, v: Option<&Value>) -> Result<String, Hata> {
    let s = match v {
        None => "",
        Some(Value::String(s)) => s.as_str(),
        Some(d) if !dogru(Some(d)) => "",
        Some(_) => return Err("TypeError: re.search metin bekler".into()),
    };
    Ok(if etiket.is_match(s) { s.to_string() } else { html_kacis(s) })
}

fn al<'a>(v: &'a Value, k: &str) -> Result<&'a Value, Hata> {
    v.get(k).ok_or_else(|| format!("KeyError: {}", py::repr(k)))
}

fn al_metin(v: &Value, k: &str) -> Result<String, Hata> {
    match al(v, k)? {
        Value::String(s) => Ok(s.clone()),
        _ => Err(format!("{k}: metin bekleniyordu")),
    }
}

/// `x.get(k, varsayilan)`: anahtar yoksa varsayılan, var ise (null dahil) değer.
fn al_varsayilan<'a>(v: &'a Value, k: &str, varsayilan: &'a Value) -> &'a Value {
    v.get(k).unwrap_or(varsayilan)
}

fn nesne_mi(v: &Value) -> Result<(), Hata> {
    if v.is_object() { Ok(()) } else { Err("AttributeError: sözlük bekleniyordu".into()) }
}

fn liste_al<'a>(v: &'a Value, k: &str) -> Result<&'a [Value], Hata> {
    match v.get(k) {
        None => Ok(&[]),
        Some(Value::Array(a)) => Ok(a),
        Some(_) => Err(format!("{k}: liste bekleniyordu")),
    }
}

fn dogrula(spec: &Value) -> Result<Vec<String>, Hata> {
    nesne_mi(spec)?;
    let mut hatalar = vec![];
    for z in ["no", "tarih", "baslik", "tetik", "kalemler"] {
        if spec.get(z).is_none() {
            hatalar.push(format!("zorunlu alan eksik: {z}"));
        }
    }
    let kalemler = liste_al(spec, "kalemler")?;
    let mut idler: Vec<Option<&Value>> = vec![];
    for k in kalemler {
        nesne_mi(k)?;
        let id = k.get("id");
        if matches!(id, Some(Value::Array(_) | Value::Object(_))) {
            return Err("TypeError: unhashable type".into());
        }
        idler.push(id);
    }
    let mut tekil: Vec<Option<&Value>> = vec![];
    for i in &idler {
        if !tekil.contains(i) {
            tekil.push(*i);
        }
    }
    if idler.len() != tekil.len() {
        hatalar.push("kalem id çift".into());
    }
    for k in kalemler {
        let id = match k.get("id") {
            Some(v) => py_str(v)?,
            None => "None".into(),
        };
        let sec: &[Value] = match k.get("secenekler") {
            None => &[],
            Some(Value::Array(a)) => a,
            Some(_) => return Err("secenekler: liste bekleniyordu".into()),
        };
        if sec.is_empty() {
            hatalar.push(format!("{id}: seçenek yok"));
        }
        let mut oneri = vec![];
        for (i, s) in sec.iter().enumerate() {
            nesne_mi(s)?;
            if dogru(s.get("oneri")) {
                oneri.push(i);
            }
        }
        if !oneri.is_empty() && oneri[0] != 0 {
            hatalar.push(format!("{id}: önerilen seçenek ilk sırada değil (m.40 eki)"));
        }
        for s in sec {
            if !dogru(s.get("value")) {
                hatalar.push(format!("{id}: value boş"));
            }
        }
    }
    Ok(hatalar)
}

fn kalem_html(etiket: &Regex, k: &Value) -> Result<String, Hata> {
    let bos = Value::String(String::new());
    let coklu = dogru(k.get("coklu"));
    let fn_ad = if coklu { "kuyruklaCoklu" } else { "kuyrukla" };
    let tip = if coklu { "checkbox" } else { "radio" };
    let id = py_str(al(k, "id")?)?;
    let mut sec = vec![];
    for s in liste_al(k, "secenekler")? {
        let cls = if dogru(s.get("oneri")) { "opt oneri" } else { "opt" };
        sec.push(format!(
            "        <label class=\"{cls} block p-3 rounded bg-base-200 cursor-pointer\"><input type=\"{tip}\" name=\"secim\" value=\"{}\"> <strong>{}</strong>\n          <div class=\"text-sm opacity-80 mt-1\">{}</div></label>",
            html_kacis(&al_metin(s, "value")?),
            e(etiket, Some(al(s, "etiket")?))?,
            e(etiket, Some(al_varsayilan(s, "aciklama", &bos)))?
        ));
    }
    let buton = if coklu { "Seçimi kuyruğa yaz" } else { "Beyanı kuyruğa yaz" };
    let baslik = al_metin(k, "baslik")?;
    let kisa = serde_json::to_string(&py::ilk(&baslik, 40)).map_err(|x| x.to_string())?;
    Ok(format!(
        "\n  <!-- {id} -->\n  <section class=\"card bg-base-100 shadow-md\" data-lavish-question=\"{id}\">\n    <div class=\"card-body\">\n      <h2 class=\"card-title\">{id} · {} <span class=\"badge badge-outline\">{}</span></h2>\n      <p class=\"text-sm opacity-80\"><strong>Ne demek:</strong> {}</p>\n      <form onsubmit=\"event.preventDefault(); {fn_ad}(this,'{id}',{});\">\n      <div class=\"space-y-2\">\n{}\n      </div>\n      <button type=\"submit\" class=\"btn btn-primary btn-sm mt-3\">{buton}</button> <span class=\"text-xs opacity-60 durum\"></span>\n      </form>\n    </div>\n  </section>",
        e(etiket, Some(&Value::String(baslik)))?,
        e(etiket, Some(al_varsayilan(k, "rozet", &bos)))?,
        e(etiket, Some(al_varsayilan(k, "ne_demek", &bos)))?,
        html_kacis(&kisa),
        sec.join("\n")
    ))
}

fn uret(sablon_yolu: &str, spec: &Value) -> Result<String, Hata> {
    let etiket = Regex::new(r"</?(strong|code|em|br)\b").expect("regex");
    let bos = Value::String(String::new());
    let mut kanit = String::new();
    match spec.get("kanit") {
        None => {}
        Some(Value::Array(satirlar)) => {
            for r in satirlar {
                nesne_mi(r)?;
                kanit.push_str(&format!(
                    "          <tr><td>{}</td><td>{}</td><td>{} · <strong>{}</strong></td></tr>\n",
                    e(&etiket, Some(al(r, "bulgu")?))?,
                    e(&etiket, Some(al(r, "deger")?))?,
                    e(&etiket, Some(al_varsayilan(r, "kaynak", &bos)))?,
                    e(&etiket, Some(al_varsayilan(r, "etiket", &bos)))?
                ));
            }
        }
        Some(_) => return Err("kanit: liste bekleniyordu".into()),
    }
    let hakem = if dogru(spec.get("hakem")) {
        format!(
            "\n  <section class=\"card bg-base-100 shadow-md hakem\"><div class=\"card-body\"><h2 class=\"card-title text-lg\">Hakem / kanıt notu</h2><p class=\"text-sm opacity-80\">{}</p></div></section>",
            e(&etiket, Some(al(spec, "hakem")?))?
        )
    } else {
        String::new()
    };
    let kalemler_v = liste_al(spec, "kalemler")?;
    let mut kalemler = String::new();
    for k in kalemler_v {
        kalemler.push_str(&kalem_html(&etiket, k)?);
    }
    let n = kalemler_v.len();
    let sablon = match py::oku_kati(Path::new(sablon_yolu)) {
        Ok(t) => t,
        Err(py::OkuHata::Io(x)) => return Err(format!("{sablon_yolu}: {x}")),
        Err(py::OkuHata::Kod) => return Err(format!("{sablon_yolu}: UnicodeDecodeError")),
    };
    let no = py_str(al(spec, "no")?)?;
    let tarih = al_metin(spec, "tarih")?;
    let varsayilan_karar = Value::String("sonraki Karar".into());
    let varsayilan_once = Value::String("—".into());
    Ok(sablon
        .replace("{{NO}}", &no)
        .replace("{{TARIH}}", &tarih)
        .replace("{{BASLIK}}", &e(&etiket, Some(al(spec, "baslik")?))?)
        .replace("{{N}}", &n.to_string())
        .replace("{{GIRIS}}", &e(&etiket, Some(al_varsayilan(spec, "giris", &bos)))?)
        .replace("{{TETIK}}", &e(&etiket, Some(al(spec, "tetik")?))?)
        .replace("{{ONCE}}", &e(&etiket, Some(al_varsayilan(spec, "once_yapildi", &varsayilan_once)))?)
        .replace("{{ASOF}}", &e(&etiket, Some(al_varsayilan(spec, "asof", &bos)))?)
        .replace("{{KANIT}}", &kanit)
        .replace("{{HAKEM}}", &hakem)
        .replace("{{KALEMLER}}", &kalemler)
        .replace("{{KARAR_NO}}", &e(&etiket, Some(al_varsayilan(spec, "karar_no", &varsayilan_karar)))?)
        .replace("{{KAYNAK_HTML}}", &format!("kaynak-kodu/lavish/masa-{no}-{tarih}.html"))
        .replace("{{KALICI}}", &format!("raporlar/masa/masa-{no}-karar-yuzeyi-{tarih}.html")))
}

/// `str(pathlib.Path(p))`: yinelenen ayraçlar ve `.` bileşenleri atılır, Windows'ta `/` -> `\`.
fn pathlib_str(p: &str) -> String {
    let (surucu, kuyruk) = py::splitdrive(p);
    let kuyruk = if cfg!(windows) { kuyruk.replace('/', "\\") } else { kuyruk };
    let kok = kuyruk.starts_with(py::SEP);
    let parcalar: Vec<&str> = kuyruk.split(py::SEP).filter(|c| !c.is_empty() && *c != ".").collect();
    let s = format!("{surucu}{}{}", if kok { py::SEP.to_string() } else { String::new() }, parcalar.join(&py::SEP.to_string()));
    if s.is_empty() { ".".into() } else { s }
}

/// `Path / bilesen`.
fn yol_ekle(taban: &str, bilesen: &str) -> String {
    let b = pathlib_str(bilesen);
    if taban == "." {
        return b;
    }
    if taban.ends_with(py::SEP) || (cfg!(windows) && taban.ends_with(':')) {
        format!("{taban}{b}")
    } else {
        format!("{taban}{}{b}", py::SEP)
    }
}

/// `len(repo.glob("raporlar/masa/masa-*-karar-yuzeyi-*.html"))`.
fn mevcut_say(repo: &str) -> usize {
    let dizin = yol_ekle(&yol_ekle(repo, "raporlar"), "masa");
    let re = Regex::new(if cfg!(windows) { r"(?is)^masa-.*-karar-yuzeyi-.*\.html$" } else { r"(?s)^masa-.*-karar-yuzeyi-.*\.html$" }).expect("regex");
    match fs::read_dir(dizin) {
        Ok(rd) => rd.filter_map(Result::ok).filter(|d| re.is_match(&d.file_name().to_string_lossy())).count(),
        Err(_) => 0,
    }
}

pub fn kos(argv: &[String]) -> i32 {
    let ap = Ayrisan::yeni(
        "masa-uret.py",
        None,
        vec![Secenek::deger(&["--repo"], "repo", None), Secenek::bayrak(&["--kuru"], "kuru", None)],
    )
    .konumsal("spec");
    let a = match ap.ayristir(argv) {
        Ok(a) => a,
        Err(k) => return k,
    };
    let repo = match a.metin("repo") {
        Some(r) => pathlib_str(r),
        None => yol_ekle(&yol_ekle(&pathlib_str(&py::expanduser("~")), "sistem"), "jarvis"),
    };
    let kuru = a.bayrak("kuru");
    let yol = a.konumsal().unwrap_or_default();
    let metin = match py::oku_kati(Path::new(yol)) {
        Ok(t) => t,
        Err(py::OkuHata::Io(x)) => return py::coker(&format!("{yol}: {x}")),
        Err(py::OkuHata::Kod) => return py::coker(&format!("{yol}: UnicodeDecodeError")),
    };
    let spec: Value = match serde_json::from_str(&metin) {
        Ok(v) => v,
        Err(x) => return py::coker(&format!("{yol}: JSONDecodeError: {x}")),
    };
    let hatalar = match dogrula(&spec) {
        Ok(h) => h,
        Err(m) => return py::coker(&m),
    };
    if !hatalar.is_empty() {
        py::print(&format!("SPEC HATASI: {}", hatalar.join(" · ")));
        return 2;
    }
    let (no, tarih) = match (py_str(&spec["no"]), py_str(&spec["tarih"])) {
        (Ok(n), Ok(t)) => (n, t),
        _ => return py::coker("no/tarih okunamadı"),
    };
    let kalici = yol_ekle(&yol_ekle(&yol_ekle(&repo, "raporlar"), "masa"), &format!("masa-{no}-karar-yuzeyi-{tarih}.html"));
    let calisma = yol_ekle(&yol_ekle(&yol_ekle(&repo, "kaynak-kodu"), "lavish"), &format!("masa-{no}-{tarih}.html"));
    let mevcut = mevcut_say(&repo);
    if !kuru && Path::new(&kalici).exists() && !dogru(spec.get("ustune_yaz")) {
        py::print(&format!("MASA NO ÇAKIŞMASI: {kalici} var (ustune_yaz: true ile geç)"));
        return 3;
    }
    let sablon = py::join(&py::join(&py::join(&py::join(&kok_coz(), "jarvis"), ".claude"), "skills"), "karar-masasi");
    let sablon = py::join(&sablon, "sablon.html");
    let html = match uret(&sablon, &spec) {
        Ok(h) => h,
        Err(m) => return py::coker(&m),
    };
    let form_n = html.matches("data-lavish-question=").count();
    let uzunluk = html.chars().count();
    let kalem = liste_al(&spec, "kalemler").map(<[Value]>::len).unwrap_or(0);
    if kuru {
        py::print(&format!("kuru: {uzunluk} B · kalem {kalem} · form {form_n} · mevcut masa {mevcut}"));
        return 0;
    }
    for yol in [&calisma, &kalici] {
        if let Some(p) = Path::new(yol).parent()
            && let Err(x) = fs::create_dir_all(p)
        {
            return py::coker(&format!("{}: {x}", p.display()));
        }
    }
    for yol in [&calisma, &kalici] {
        if let Err(m) = metin_yaz(yol, &html) {
            return py::coker(&m);
        }
    }
    py::print(&format!("üretildi: {calisma}\nkalıcı: {kalici}\nkalem {kalem} · form {form_n} · {uzunluk} B"));
    0
}
