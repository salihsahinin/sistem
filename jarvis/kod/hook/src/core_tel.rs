//! `pretool-core-tel.sh` karşılığı: Bash ile core/ · CLAUDE.md · .claude/ yazımı tökezleme-teli (çıkış 2 = engel).
//! grep -E satır başına çalışır ve bu makinede C yerelinde (ASCII `\b`, `[[:alpha:]]`, bayt `.`) davranır; bu yüzden
//! bayt düzeyinde ASCII regex kullanılır.
use crate::ortak::{Ortam, Sonuc, py_str, sondaki_nl_sil};
use regex::bytes::Regex;
use serde_json::Value;

const PROT: &str = r"(core/|CLAUDE\.md|\.claude/)";

fn desenler() -> Vec<Regex> {
    let r = |s: String| Regex::new(&format!("(?-u){s}")).expect("regex");
    vec![
        // göreli (`core/`, `./core/`) ya da mutlak önekli (`/c/.../core/`, `C:/.../core/`, `C:\...\core\`, `~/...`) hedef
        r(r#">{1,2}[[:space:]]*"?(?:\.?/?|(?:[A-Za-z]:|~|\$\{?HOME\}?)?[/\\](?:[^[:space:]"'|;&<>]*[/\\])?)(core[/\\]|CLAUDE\.md|\.claude[/\\])"#.to_string()),
        // yazan komut adı yalnız komut konumunda (kalem A6): satır başı ya da `;` `&&` `||` `|` `&` `$(` backtick `(`,
        // `then/do/else`, `xargs`, `-exec` sonrası; önünde `sudo [-o arg]`, `env`, `X=Y` önekleri ve `/bin/` gibi yol olabilir.
        // `grep -n tee core/x.md` gibi salt-okur komutun argümanındaki ad artık eşleşmez.
        r(format!(
            r"(?:^|;|&|\||\$\(|`|\(|\b(?:then|do|else|xargs)\b|-exec)[[:space:]]*(?:(?:(?:sudo|env|nice|nohup|time|command|exec)(?:[[:space:]]+-[^[:space:]]*(?:[[:space:]]+[^-[:space:]][^[:space:]]*)?)*|[A-Za-z_][A-Za-z0-9_]*=[^[:space:]]*)[[:space:]]+)*(?:[^[:space:];|&]*/)?(mv|cp|rm|touch|truncate|tee|dd|install)\b.*{PROT}"
        )),
        r(format!(r"\b(sed|perl)\b[^|;&]*[[:space:]]-[[:alpha:]]*i[^|;&]*{PROT}")),
        r(format!(r"\bgit[[:space:]]+(checkout|restore|reset|clean|rm|mv)\b.*{PROT}")),
    ]
}

fn komut_cikar(girdi: &str) -> String {
    let v: Option<Value> = serde_json::from_str(girdi).ok();
    let cmd = v
        .as_ref()
        .and_then(|v| v.as_object())
        .and_then(|d| match d.get("tool_input") {
            None => Some(None),
            Some(Value::Object(ti)) => Some(ti.get("command")),
            Some(_) => None, // .get çağrısı patlar -> boş
        })
        .map(|c| match c {
            None => String::new(),
            Some(c) => py_str(c),
        })
        .unwrap_or_default();
    sondaki_nl_sil(&cmd).to_string()
}

pub fn kos(o: &Ortam) -> Sonuc {
    let girdi = o.stdin_metin();
    let girdi = sondaki_nl_sil(&girdi).to_string();
    let mut cmd = komut_cikar(&girdi);
    if cmd.is_empty() {
        cmd = girdi;
    }
    let desen = desenler();
    let engel = cmd.split('\n').any(|satir| desen.iter().any(|d| d.is_match(satir.as_bytes())));
    let mut s = Sonuc::bos();
    if engel {
        s.hata = format!(
            "TEL (m.41 kilit): Bash ile core/ · CLAUDE.md · .claude/ yazımı bu yüzeyde engellidir. Bu bir tökezleme-telidir; iş meşruysa ana-sıra(Cowork/Fable) ya da Salih eliyle yapılır. Komut: {cmd}\n"
        );
        s.kod = 2;
    }
    s
}

#[cfg(test)]
mod testler {
    use super::*;

    fn engel_mi(cmd: &str) -> bool {
        let d = desenler();
        cmd.split('\n').any(|satir| d.iter().any(|r| r.is_match(satir.as_bytes())))
    }

    #[test]
    fn mutlak_yonlendirme_kesilir() {
        assert!(engel_mi("echo x > /c/sistem/sistem/jarvis/core/deneme.md"));
        assert!(engel_mi("echo x >> C:/sistem/sistem/jarvis/core/deneme.md"));
        assert!(engel_mi(r"echo x > C:\sistem\sistem\jarvis\core\deneme.md"));
        assert!(engel_mi("echo x > \"/c/sistem/sistem/jarvis/CLAUDE.md\""));
        assert!(engel_mi("echo x > ~/sistem/jarvis/.claude/settings.json"));
    }

    #[test]
    fn goreli_yonlendirme_hala_kesilir() {
        assert!(engel_mi("echo x > core/deneme.md"));
        assert!(engel_mi("echo x >> ./core/deneme.md"));
        assert!(engel_mi("echo x > CLAUDE.md"));
    }

    #[test]
    fn izinli_durumlar_bozulmaz() {
        assert!(!engel_mi("cat core/durum.md"));
        assert!(!engel_mi("echo x > raporlar/a.md"));
        assert!(!engel_mi("echo x > /c/sistem/sistem/jarvis/raporlar/score/a.md"));
        assert!(!engel_mi("echo x > alt/core/a.md"));
        assert!(!engel_mi("ls core/ 2> /dev/null"));
    }

    #[test]
    fn salt_okur_argumandaki_ad_kesilmez() {
        assert!(!engel_mi("grep -n tee core/x.md"));
        assert!(!engel_mi("rg cp core/a.md"));
        assert!(!engel_mi("git log --grep install -- core/x.md"));
    }

    #[test]
    fn komut_konumundaki_yazma_kesilir() {
        for c in ["tee core/x.md", "echo x | tee -a core/x.md", "sudo cp a core/x", "ls && rm core/x", "ls || touch core/x",
            "env A=1 mv a core/b", "echo $(rm core/x)", "echo `rm core/x`", "A=1 cp a core/b", "sudo -u root env A=1 install a core/b",
            "(rm core/x)", "if true; then rm core/x; fi", "xargs rm core/x", "find . -exec rm core/x ;", "/bin/rm core/x"] {
            assert!(engel_mi(c), "{c}");
        }
    }
}
