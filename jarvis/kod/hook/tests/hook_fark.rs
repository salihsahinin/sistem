//! Fark testleri: her hook için eski betik (bash/python) ile `jarvis-hook` ikilisi aynı girdide
//! stdout · stderr · çıkış kodu · kütük/durum satırları (ts hariç) bakımından eşit olmalı. Python/bash yoksa test başarısız olur (atlanmaz):
//! fark testi Python'sız anlamsızdır.
mod ortak;
use ortak::*;
use serde_json::{Value, json};

fn bash_girdi(cmd: &str) -> String {
    json!({"tool_name": "Bash", "tool_input": {"command": cmd}}).to_string()
}

// ------------------------------------------------------------------ pretool-core-tel
#[test]
fn core_tel() {
    let komutlar = [
        "echo x > core/a.md", "cat foo >> CLAUDE.md", "echo hi >\"./core/z\"", "printf a >.claude/settings.json", "mv a.txt core/b.txt",
        "cp x .claude/settings.json", "rm -rf core/x", "touch core/yeni.md", "truncate -s 0 CLAUDE.md", "echo a | tee core/pano.md",
        "dd if=/dev/zero of=core/x", "install -m 644 a .claude/hooks/x", "sed -i s/a/b/ core/tuzuk-v0.md", "sed -pi s/a/b/ CLAUDE.md",
        "perl -pi -e 's/a/b/' CLAUDE.md", "perl -i.bak -e 1 core/x", "git checkout -- core/x", "git restore .claude/settings.json",
        "git reset HEAD core/", "git clean -fd core/", "git rm core/x", "git mv core/a core/b", "ls\necho x > core/a.md", "ls\n\ncat y >> CLAUDE.md\nls",
        // izinli
        "sed -n 1,5p core/pano.md | grep -i core/", "cat core/pano.md", "ls .claude", "git status", "echo \"core/ bir dizin\"", "grep -rn core/ .",
        "git log -- core/", "rm tmp.txt", "cp a b", "sed -i s/a/b/ dosya.txt", "ls | sed -i x; cat core/pano.md", "echo ok", "", "git diff core/",
        "cat > cc/rapor/x.md", "echo çğış > notlar.md", "rm çmv core/x", "echo >core/", "echo > core", "XCORE/",
    ];
    let mut adimlar: Vec<Adim> = komutlar.iter().map(|c| adim(&bash_girdi(c))).collect();
    // Bash dışı / bozuk / boş girdiler
    adimlar.push(adim(&json!({"tool_name": "Read", "tool_input": {"file_path": "core/pano.md"}}).to_string()));
    adimlar.push(adim(&json!({"tool_name": "Write", "tool_input": {"file_path": ".claude/x", "content": "a"}}).to_string()));
    adimlar.push(adim("{bozuk json > core/a.md"));
    adimlar.push(adim("düz metin echo a > CLAUDE.md"));
    adimlar.push(adim(""));
    adimlar.push(adim("[]"));
    adimlar.push(adim(&json!({"tool_name": "Bash", "tool_input": "x > core/a"}).to_string()));
    adimlar.push(adim(&json!({"tool_name": "Bash"}).to_string()));
    adimlar.push(adim(&format!("{}\n", bash_girdi("echo x > core/a.md"))));
    fark(H::CoreTel, "core-tel", &bos, adimlar);
}

// ------------------------------------------------------------------ pretool-ajan-fren
fn agent(sid: &str, tool: &str) -> String {
    json!({"session_id": sid, "tool_name": tool, "tool_input": {"description": "test ajanı"}}).to_string()
}

#[test]
fn ajan_fren() {
    let es = |a: Adim| a.env("JARVIS_FREN_UYARI", "3").env("JARVIS_FREN_DURDUR", "5");
    let mut adimlar = vec![];
    for _ in 0..7 {
        adimlar.push(es(adim(&agent("s1", "Agent"))));
    }
    adimlar.push(es(adim(&agent("s2", "Task"))));
    adimlar.push(es(adim(&agent("s1", "Bash"))));
    for _ in 0..4 {
        adimlar.push(es(adim(&agent("a", "Agent"))));
    }
    adimlar.push(es(adim(&agent("a", "Agent")).env("JARVIS_FREN_KAPALI", "1")));
    adimlar.push(es(adim(&agent("a", "Agent")).env("JARVIS_FREN_KAPALI", "0")));
    adimlar.push(es(adim("{bozuk")));
    adimlar.push(es(adim("")));
    adimlar.push(es(adim(&json!({"tool_name": "Agent"}).to_string())));
    adimlar.push(es(adim(&json!({"tool_name": "Agent", "session_id": "", "tool_input": {"description": "ç".repeat(100)}}).to_string())));
    adimlar.push(es(adim(&json!({"tool_name": "Agent", "session_id": "u".repeat(60), "tool_input": {}}).to_string())));
    adimlar.push(es(adim(&json!({"tool_name": "Agent", "session_id": "tt"}).to_string())).env("JARVIS_FREN_UYARI", "x").atla());
    // varsayılan eşikler (72/144): tek çağrı sessiz
    adimlar.push(adim(&agent("vars", "Agent")));
    fark(H::AjanFren, "ajan-fren", &bos, adimlar);
}

// ------------------------------------------------------------------ pretool-altajan-okuma
fn alt(arac: &str, ti: Value) -> String {
    json!({"agent_id": "a1", "agent_type": "Explore", "session_id": "ses-1", "tool_name": arac, "tool_input": ti}).to_string()
}

#[test]
fn altajan_okuma() {
    let r = |p: &str| alt("Read", json!({"file_path": p}));
    let b = |c: &str| alt("Bash", json!({"command": c}));
    let mut adimlar = vec![
        adim(&json!({"tool_name": "Read", "tool_input": {"file_path": "{R}/core/durum-kapsulu.md"}}).to_string()),
        adim(&r("{R}/core/durum-kapsulu.md")),
        adim(&r("{R}/core/tuzuk-v0.md")),
        adim(&r("{R}/core/pano.md")),
        adim(&r("core/pano.md")),
        adim(&r("{EV}/.claude/projects/x/y.jsonl")),
        adim(&r("{EV}/.claude/projects/-Users-x-sistem-jarvis/58141fb3/tool-results/toolu_x.txt")),
        adim(&r("{EV}/.claude/projects/-Users-x-sistem-jarvis/58141fb3.jsonl")),
        adim(&r("{R}/cc/devir/friday-2026-09-18-tur4/gorev.md")),
        adim(&r("{R}/cc/gelen")),
        adim(&r("{R}/cc/rapor/x.md")),
        adim(&r("{R}/veri/bronz/hareket-olay.jsonl")),
        adim(&r("{R}/veri/bronz/altajan-okuma-olay.jsonl")),
        adim(&r("{R}/../friday/cc/x.md")),
        adim(&r("{K}/friday")),
        adim(&r("/c/sistem/x")),
        adim(&r("")),
        adim(&alt("Grep", json!({"pattern": "m.8", "path": "{R}/wiki"}))),
        adim(&alt("Grep", json!({"pattern": "m.8", "path": "{R}/kuyruk/senaryo-defteri.md"}))),
        adim(&alt("Glob", json!({"pattern": "*.md", "path": "{R}/core"}))),
        adim(&alt("Glob", json!({"pattern": "*.md", "path": "{R}/cc/devir"}))),
        adim(&alt("Edit", json!({"file_path": "{R}/core/pano.md"}))),
        adim(&b("cat kuyruk/senaryo-defteri.md | head")),
        adim(&b("ls {K}/friday/cc")),
        adim(&b("ls cc/rapor/2026-09")),
        adim(&b("ls cc/gelen/")),
        adim(&b("cat > cc/rapor/x.md <<'EOF'\nbkz core/durum-kapsulu.md\nEOF")),
        adim(&b("cat <<-\"EOF\"\n  core/pano.md\nEOF\ncat core/pano.md")),
        adim(&b("cat <<EOF\nbkz core/pano.md\n")),
        adim(&b("cat ~/.claude/projects/x/y.jsonl")),
        adim(&b("cat $HOME/.claude/projects/x && cat ${HOME}/.claude/projects/y")),
        adim(&b("ls C:/Users/zz/staj başlangıç/x")),
        adim(&b("cat {R}/core/pano.md {R}/fikir-kutusu.md")),
        adim(&b("echo user@host:core/pano.md x=core/pano.md")),
        adim(&b("grep -rn m.8 core/ kuyruk/")),
        adim(&b("")),
        adim(&alt("Bash", json!({}))),
        adim(&alt("Read", json!({}))),
        adim("{bozuk"),
        adim(""),
        adim(&json!({"agent_id": "", "tool_name": "Read", "tool_input": {"file_path": "{R}/core/pano.md"}}).to_string()),
    ];
    // JARVIS_HOOK_TEST bayrağı yalnız kütüğü kapatır; kilit yine keser
    adimlar.push(adim(&r("{R}/core/pano.md")).env("JARVIS_HOOK_TEST", "1"));
    adimlar.push(adim(&b("cat core/pano.md")).env("JARVIS_HOOK_TEST", "1"));
    // gerçek cc/devir dizini olsun diye var olan yollar da denensin
    let hazirla = |k: &Kum| {
        std::fs::create_dir_all(k.jarvis.join("cc").join("devir").join("x")).unwrap();
        std::fs::create_dir_all(k.jarvis.join("cc").join("rapor")).unwrap();
        std::fs::write(k.jarvis.join("cc").join("devir").join("x").join("g.md"), "a").unwrap();
    };
    adimlar.push(adim(&r("{R}/cc/devir/x/g.md")));
    adimlar.push(adim(&b("cat cc/devir/x/g.md")));
    fark(H::Altajan, "altajan", &hazirla, adimlar);
}

// ------------------------------------------------------------------ stop-buyuk-harf
fn tp_user() -> String {
    json!({"type": "user", "message": {"content": "soru"}}).to_string()
}
fn tp_text(t: &str) -> String {
    json!({"type": "assistant", "message": {"content": [{"type": "text", "text": t}]}}).to_string()
}
fn tp_arac(ad: &str, alan: &str, ic: &str) -> String {
    json!({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": ad, "input": {alan: ic}}, {"type": "text", "text": "Görsel yukarıda."}]}}).to_string()
}

fn stop_adim(satirlar: &[String], aktif: bool, ekstra: Option<(&str, &str)>) -> Adim {
    let mut g = json!({"transcript_path": "{R}/tp.jsonl", "stop_hook_active": aktif, "hook_event_name": "Stop"});
    if let Some((k, v)) = ekstra {
        g[k] = json!(v);
    }
    adim(&g.to_string()).dosya("tp.jsonl", &(satirlar.join("\n") + "\n"))
}

#[test]
fn stop_buyuk_harf() {
    let metinler = [
        "Bu kutu TEMELDE şunu anlatır: injection AYIRT edilemez.", "OWASP LLM01 listesi, promptfoo YAML dosyası, `DONE`.", "Bu SANA yazıldı, kanal VAR.",
        "İş DONE, pratik KALAN.", "Şöyle:\n```\nEXPORT ALL CAPS HERE\n```\nve `INLINE_CAPS` normal.", "Bu adım ZORUNLU ve İLGİSİ yok.",
        "WSL kurdum, CTE ile PATH değişkenini ekledim.", "WSL2 ve PATH_ADI ve C:/PATH yolu", "aynen: \"BU VURGU alıntıdır\" ve sonra normal.",
        "aynen: “TIRNAK İÇİ CAPS” bitti", "bkz https://example.com/PATH/WSL ve ardından düz metin", "AS-OF damgası, F1 skoru, BM25 sıralama, KB-08 kaydı, GSM8K.",
        "ALT-AJAN tekrar tekrar ALT-AJAN ve BRAVO CHARLIE DELTA ECHO FOXTROT GOLF HOTEL INDIA JULIET KILO LIMA MIKE NOVEMBER",
        "iki ZEBRA bir ELMA ve ÇİLEK ÖĞRETİM ŞEKER ÜZÜM", "ab ABC. XYZ, (QRS) -TUV- a.BCD EFG/HIJ KLM_NOP", "Tamamen küçük harfli düz cümle.", "", "   ",
        "SÖZCÜK\nSATIR İKİ CAPS", "kelime1ABC ABC1 aABC ABCd", "MCP ve DAG ve HITL ve NDCG ve JARVİS ve İB", "SQL’DE vurgu", "çıplak ÇÖZÜM",
    ];
    let mut adimlar = vec![];
    for m in metinler {
        adimlar.push(stop_adim(&[tp_user(), tp_text(m)], false, None));
    }
    adimlar.push(stop_adim(&[tp_user(), tp_text("TEMELDE yine caps var ama ikinci tur.")], true, None));
    // araç girdileri (v0.3)
    for (ad, alan, ic) in [
        ("mcp__visualize__show_widget", "widget_code", "<div class=\"x\"><style>.A{color:red}</style><script>addLog(\"iki AYRI sunucudan BİRLİKTE\");</script></div>"),
        ("mcp__visualize__show_widget", "widget_code", "<svg viewBox=\"0 0 10 10\"><text>MCP sunucusu · DAG</text></svg>"),
        ("mcp__visualize__show_widget", "widget_code", "<p>Fiyat &AMP; &nbsp;TEMEL &#12; ZORUNLU</p>"),
        ("Write", "content", "Bu ders TEMELDE şunu anlatır."),
        ("Edit", "new_string", "yeni METIN burada"),
        ("Write", "content", "   "),
        ("Read", "content", "BU ALAN TARANMAZ"),
    ] {
        adimlar.push(stop_adim(&[tp_user(), tp_arac(ad, alan, ic)], false, None));
    }
    // çok-asistanlı tur: ilk metin seçilir, user sıfırlar
    adimlar.push(stop_adim(&[tp_user(), tp_text("Önce normal metin."), tp_text("Sonra İKİNCİ vurgu.")], false, None));
    adimlar.push(stop_adim(&[tp_user(), tp_text("ESKİ TUR vurgusu."), tp_user(), tp_text("yeni tur temiz")], false, None));
    adimlar.push(stop_adim(&[tp_user(), tp_text("temiz"), tp_arac("Write", "content", "ZORUNLU")], false, None));
    adimlar.push(stop_adim(&["bozuk satır".into(), tp_user(), tp_text("KALDI")], false, None));
    // last_assistant_message alanı önceliği
    adimlar.push(stop_adim(&[tp_user(), tp_text("transkript VURGULU")], false, Some(("last_assistant_message", "alan METNİ temiz"))));
    adimlar.push(stop_adim(&[tp_user(), tp_text("temiz")], false, Some(("last_assistant_message", "alan VURGULU metin"))));
    adimlar.push(adim(&json!({"last_assistant_message": "yalnız ALAN vurgusu"}).to_string()));
    adimlar.push(adim(&json!({"last_assistant_message": "temiz alan"}).to_string()));
    adimlar.push(adim(&json!({"transcript_path": "{R}/yok.jsonl"}).to_string()));
    adimlar.push(adim(&json!({}).to_string()));
    adimlar.push(adim("{bozuk").atla());
    fark(H::Buyuk, "stop", &bos, adimlar);
}

// ------------------------------------------------------------------ instructions-loaded
#[test]
fn instructions_loaded() {
    let adimlar = vec![
        adim(&json!({"session_id": "s1", "hook_event_name": "InstructionsLoaded", "load_reason": "session_start", "file_path": "C:/x/CLAUDE.md", "cwd": "C:/x"}).to_string()),
        adim(&json!({"session_id": "s2", "reason": "nested_traversal", "path": "C:/x/y/CLAUDE.md"}).to_string()),
        adim(&json!({"session_id": "s3", "matcher": "compact", "file": "a.md", "ekstra": 1, "cwd": null}).to_string()),
        adim(&json!({"session_id": "s4", "load_reason": "", "reason": "include", "file_path": "", "path": "p.md"}).to_string()),
        adim(&json!({"hook_event_name": "Baska"}).to_string()),
        adim(&json!({}).to_string()),
        adim("{bozuk json"),
        adim(""),
        adim("[1,2]").atla(),
        adim("\"düz\"").atla(),
        adim(&json!({"session_id": 12, "load_reason": ["a"], "dosya": "ç ğ ş İ"}).to_string()),
        adim(&json!({"session_id": "ü", "file_path": "C:/ç/ş/CLAUDE.md"}).to_string()),
    ];
    fark(H::Talimat, "talimat", &bos, adimlar);
}

// ------------------------------------------------------------------ prompt-dosya + paket + userprompt
fn up(p: &str, sid: &str) -> String {
    json!({"prompt": p, "session_id": sid}).to_string()
}

const PROMPTLAR: &[&str] = &[
    "m.9 gereği push", "m.8 silme", "karar 88 nedir", "Karar 112", "karar 9999", "İB-79 durumu", "KB-50 nedir", "ib-79 küçük harf", "K-001 kartı", "masa kuralları",
    "sonraki iş ne", "SIRADAKİ NE", "öncelik nedir", "ÖNCELİK", "atlas araştır", "ARAŞTIR", "pipeline koş", "işçi lider", "damıt ve ingest et", "DAMIT", "INGEST",
    "push et", "galeri ya da staj", "STAJ", "merhaba hava güzel", "", "   ", "m.7 ve m.9 ve karar 88 ve karar 89 ve İB-79 ve push", "m.100", "m.8 m.8 m.8",
    "karar 1 karar 2 karar 3 karar 4 karar 5", "Salih: atlas pipeline araştır damıt", "ŞİMDİ SONRAKİ ÖNCELİK", "ıİiI", "karar 0088",
];

#[test]
fn prompt_dosya() {
    let mut adimlar: Vec<Adim> = PROMPTLAR.iter().map(|p| adim(&up(p, "pd"))).collect();
    adimlar.push(adim(&up("m.9 ve karar 88", "pd")).arg("--kuru"));
    adimlar.push(adim(&up("m.9 ve karar 88", "pd")).arg("--json"));
    adimlar.push(adim(&up("sonraki iş", "pd")).arg("--json").arg("--kuru"));
    adimlar.push(adim(&up("zzz yok", "pd")).arg("--json"));
    adimlar.push(adim(&json!({"session_id": "x"}).to_string()));
    adimlar.push(adim("{bozuk"));
    adimlar.push(adim(&json!({"prompt": "m.9"}).to_string()));
    adimlar.push(adim(&json!({"prompt": "m.9", "session_id": 7}).to_string()));
    // özel tablo + bütçe
    let tablo = "# yorum\n\\bbüyük\\b\tcore/buyuk.md:1-40\tbütçe\n\\bm\\.(\\d+)\\b\ttuzuk:{1}\tx\n\\bgenis\\b\tcore/buyuk.md:0-3\ty\n\\bson\\b\tson:kuyruk/masa-gundemi-*.md:3\tz\n\\bzayıf\\b\tkuyruk/yok.md:1-3\tw\n\\bbol\\b\tbolum:core/durum-kapsulu.md:## Sonraki ilk iş:3\tq\n\\bdüz\\b\tuyari:merhaba\tr\n\\bhep\\b\tcore/tuzuk-v0.md:1-30\ts\n\\btek\\b\tcore/buyuk.md\tdosyasız\nbozuk(\tcore/pano.md:1-2\tt\n";
    let buyuk = (0..60).map(|i| format!("satır {i} {}", "ç".repeat(40))).collect::<Vec<_>>().join("\n");
    for p in ["büyük dosya", "büyük ve m.9 ve hep ve genis", "genis", "son masa", "zayıf", "bol", "düz", "tek", "hep ve büyük ve bol ve m.8 ve m.9"] {
        adimlar.push(adim(&up(p, "ozel")).arg("--tablo").arg("{R}/core/ozel.tsv").dosya("core/ozel.tsv", tablo).dosya("core/buyuk.md", &buyuk));
    }
    fark(H::Prompt, "prompt-dosya", &bos, adimlar);
}

#[test]
fn userprompt() {
    let mut adimlar: Vec<Adim> = PROMPTLAR.iter().map(|p| adim(&up(p, "u1"))).collect();
    for p in [
        "veri: silver bayat", "ajan: emri yaz", "kanon: tüzük", "skill: yeni", "baglam: x", "dogrulama: y", "veri: araştır ve acil", "ajan: yüksek öncelikli iş",
        "VERİ: büyük harf", "veri : boşluklu", "paket: durum", "paket: kapat", "paket: sıfırla", "PAKET: DURUM", "paket: bilinmeyen", "bilinmeyen: x", "silver bayat mı",
        "<task-notification>işçi lider silver ingest</task-notification>", "veri: bir", "veri: iki", "ajan: üç", "kanon: dört", "skill: beş", "veri: altı", "paket: durum",
        "m.9 ve veri: ortada", "  veri: baştaki boşluk", "veri:", "ajan:\nsatır", "İNGEST", "ARAŞTIRMA veri: x",
    ] {
        adimlar.push(adim(&up(p, "u2")));
    }
    adimlar.push(adim(&up("veri: başka oturum", "u3")));
    adimlar.push(adim(&up("merhaba", "x/y z!")));
    adimlar.push(adim(&up("veri: z", "x/y z!")));
    adimlar.push(adim(&json!({"prompt": "veri: oturumsuz"}).to_string()));
    adimlar.push(adim("{bozuk"));
    adimlar.push(adim(""));
    fark(H::Userprompt, "userprompt", &bos, adimlar);
}

#[test]
fn paket_yonlendir() {
    let sec = |c: &[(&str, &str)], ek: &[&str]| {
        let mut a = adim("").arg("--sec");
        for (n, p) in c {
            a = a.arg("--niyet").arg(n).arg("--paket").arg(p);
        }
        for e in ek {
            a = a.arg(e);
        }
        a
    };
    let adimlar = vec![
        adim(&up("ajan: başla", "p1")),
        sec(&[("silver bayat", "veri"), ("işçi emri", "ajan"), ("hava güzel", "yok")], &["--oturum", "p1"]),
        sec(&[("silver bayat", "ajan")], &["--oturum", "p1", "--duzeltme"]),
        sec(&[("selam", "yok")], &["--oturum", "p1"]),
        sec(&[("a", "veri"), ("b", "ajan"), ("c", "kanon")], &["--oturum", "p1"]),
        sec(&[("a", "kanon")], &["--oturum", "p1"]),
        sec(&[("a", "olmayan")], &["--oturum", "p1"]).atla(),
        sec(&[("x", "veri")], &["--oturum", "p1", "--kuru"]),
        sec(&[("x", "veri"), ("y", "veri")], &["--oturum", "p1", "--json"]),
        sec(&[("x", "skill")], &["--json", "--kuru"]),
        sec(&[("bunu araştır acil", "veri")], &["--oturum", "p2"]),
        sec(&[("n".repeat(200).as_str(), "veri")], &["--oturum", "p3"]),
        adim("").arg("--sec").arg("--niyet").arg("x"),
        adim("").arg("--sec"),
        adim(&up("merhaba", "son1")),
        sec(&[("silver", "veri")], &[]),
        adim("").arg("--denetle"),
        adim("").arg("--denetle").arg("--json"),
        adim("").arg("--denetle").arg("--manifest").arg("{R}/yok.json"),
        adim(&up("veri: bir", "p4")).arg("--json"),
        adim(&up("veri: iki", "p4")).arg("--json"),
        adim(&up("paket: durum", "p4")).arg("--json"),
        adim(&up("paket: kapat", "p4")).arg("--json"),
        adim(&up("hava güzel", "p4")).arg("--json"),
        adim(&up("veri: kuru", "p5")).arg("--kuru"),
        adim(&up("ajan: x", "p5")).arg("--durum-dizin").arg("{R}/baska-durum"),
    ];
    fark(H::Paket, "paket", &bos, adimlar);

    // sahte manifest: denetim ihlalleri ve özel sabitler
    let man = json!({"esik_gecis": 2, "butce_bayt": 500, "kapsul_dizin": "core/paket-kapsul",
        "kademeler": {"sonnet": "Sonnet 5.5", "opus": "Opus 5.5", "fable": "Fable 5.1"},
        "agir_is": "\\b(araştır\\w*)", "oncelik": "\\b(yüksek öncelik\\w*|acil)\\b",
        "paketler": [
            {"id": "veri", "ad": "Veri", "kademe": "sonnet", "tetik": ["\\bsilver\\b"], "cekirdek": ["core/veri.md"], "pointer": ["core/uzun.md"], "skill": ["damitma"]},
            {"id": "ajan", "ad": "Ajan", "kademe": "opus", "tetik": ["\\bişçi\\w*"], "cekirdek": ["core/ajan.md:1-2"], "pointer": [], "skill": []}]});
    let bozuk = json!({"esik_gecis": 2, "butce_bayt": 500, "kademeler": {"sonnet": "S"},
        "agir_is": "ok", "oncelik": "ok",
        "paketler": [
            {"id": "Veri", "kademe": "sonnet", "tetik": ["\\bLider", "\\bok"], "cekirdek": ["core/yok.md", "core/uzun.md"], "pointer": ["core/yok2.md"]},
            {"id": "paket", "kademe": "haiku", "tetik": []},
            {"id": "durum", "kademe": "sonnet"},
            {"id": "veri", "kademe": "sonnet"}, {"id": "veri", "kademe": "sonnet"}]});
    let kur = |k: &Kum| {
        let c = k.jarvis.join("core");
        std::fs::create_dir_all(c.join("paket-kapsul")).unwrap();
        std::fs::write(c.join("veri.md"), "# veri\nkural\n").unwrap();
        std::fs::write(c.join("ajan.md"), "# ajan\nbir\niki\n").unwrap();
        std::fs::write(c.join("uzun.md"), "x".repeat(900)).unwrap();
        std::fs::write(c.join("sahte.json"), serde_json::to_string(&man).unwrap()).unwrap();
        std::fs::write(c.join("bozuk.json"), serde_json::to_string(&bozuk).unwrap()).unwrap();
        std::fs::write(c.join("kirik.json"), "{bozuk").unwrap();
        let mut rx = man.clone();
        rx["agir_is"] = json!("(");
        std::fs::write(c.join("regex.json"), serde_json::to_string(&rx).unwrap()).unwrap();
    };
    let m = |dosya: &str| ["--manifest".to_string(), format!("{{R}}/core/{dosya}")];
    let mut a2 = vec![];
    for p in ["ajan: emri nasıl yazarız", "veri: silver", "ajan: iki", "veri: üç", "paket: durum", "paket: kapat", "paket: sıfırla", "veri: yüksek öncelikli, silver bozuk", "veri: araştır", "hava", "SILVER bayat mı"] {
        let mut a = adim(&up(p, "sh"));
        if p == "veri: üç" {
            a = a.dosya("core/paket-kapsul/veri.md", "kaldığımız yer
");
        }
        a.args.extend(m("sahte.json"));
        a2.push(a);
    }
    a2.push(adim("").arg("--denetle").arg("--manifest").arg("{R}/core/sahte.json"));
    a2.push(adim("").arg("--denetle").arg("--manifest").arg("{R}/core/bozuk.json").atla());
    a2.push(adim("").arg("--denetle").arg("--manifest").arg("{R}/core/bozuk.json").arg("--json").atla());
    a2.push(adim("").arg("--denetle").arg("--manifest").arg("{R}/core/kirik.json").atla());
    a2.push(adim("").arg("--denetle").arg("--manifest").arg("{R}/core/regex.json").tam_atla());
    let mut a = adim(&up("veri: kırık manifest", "sh"));
    a.args.extend(m("kirik.json"));
    a2.push(a);
    let mut a = adim("").arg("--sec").arg("--niyet").arg("a").arg("--paket").arg("veri").arg("--oturum").arg("sh");
    a.args.extend(m("sahte.json"));
    a2.push(a);
    let mut a = adim("").arg("--sec").arg("--niyet").arg("a").arg("--paket").arg("veri").arg("--niyet").arg("b").arg("--paket").arg("ajan").arg("--oturum").arg("sh");
    a.args.extend(m("sahte.json"));
    a2.push(a);
    fark(H::Paket, "paket-sahte", &kur, a2);
}

#[test]
fn zz_vaka_sayisi() {
    // Bilgi amaçlı: diğer testlerle paralel koşar; kesin sayı `cargo test -- --nocapture --test-threads=1` ile görülür.
    eprintln!("FARK vaka sayacı (bu süreçte): {} {:?}", SAYAC.load(std::sync::atomic::Ordering::SeqCst), HOOK_SAYAC.lock().unwrap());
}
