# Rapor — İB-77 atlası, aile C (İÇ-ENVANTER): `gorsellestir` skill adayı için iç kısıt + yeniden-kullanım envanteri

## 0. Künye
- Görev: cc/gorev... (İB-77, aile C, WEB YOK) — karar vermez, yalnız envanterler.
- Tarih: 2026-09-03. Araç çağrısı: 4 (bütçe 15).
- Kaynak taraması: `core/skill-uretim-semasi.md`, `core/skill-tetikleme-semasi.md`, `.claude/skills/skill-kapisi/SKILL.md`, `.claude/skills/karar-modeli/SKILL.md`, `~/.claude/skills/`, `~/.agents/skills/lavish/SKILL.md`, `graf/README.md`, `tools/*.py`, `~/staj başlangıç/.claude/skills/`, `kuyruk/senaryo-defteri.md`.

## 1. Kısıt listesi
1. **K0 GEREK** (`core/skill-uretim-semasi.md:31`): `¬kapsanmış(a,H) ∧ (Y1∨Y2∨Y3)` — önce hazine taraması (`ls .claude/skills/`); mevcut skill'lerden (lavish, dataviz, artifact-design/diagramming, hizalama) TAM kapsanıyorsa RET-0; KISMİ kapsama varsa yaprak = EVRİM değil YENİ ama "kapsam farkı" gövdede yazılmalı.
2. **K1 DEĞER** (`skill-kapisi/SKILL.md:12`): k_W ≥ 3 (90 gün, GÖREV birimi) ∨ Salih emri (Z2); "görselleştir" komutu Katman-1 emriyle geliyorsa Z2 yeter, sayaç şartı atlanır ama K2/K3 ATLANMAZ.
3. **İNŞA eval-önce** (`core/skill-uretim-semasi.md:46,66`): ≥3 eval + should_trigger≥5 + should_not_trigger≥5 yazılmadan gövde yazılamaz.
4. **K2 TOPRAKLAMA** (`core/skill-uretim-semasi.md:48-53`): R (referans-varlığı script `kapi-denetim.py`) + İ (bağımsız doğrulayıcı, n_val örneklem) + ¬P (kapı "dikkatli ol" talimatı OLAMAZ — CDN allowlist / dosya-boyutu gibi yapısal kontrol gerekir).
5. **K3 F1 description bütçesi** (`core/skill-uretim-semasi.md:64`): description ≤1024 char (kanon) ∧ ≤1536 (platform kesme) ∧ **Σ_H ≤ 7.380 char (hazine toplamı)** — bkz. §4.
6. **K3 F2/F3/F4/F6**: gövde <500 satır, referans ≤1 seviye derin; F6 kritik-talimat ilk ~5k token'da (`tools/kural-sayaci.py` ile denetlenir; byte>~20k ∨ kural-birimi>40 → bölme adayı).
7. **K3 şekil (T-R/T-O/T-Y/T-Ü)**: "görselleştir" komutu muhtemelen **T-Ü ÜRETİCİ** (rapor/HTML üretir, kanon/core/.claude yazmaz) — bu durumda `disable-model-invocation` ZORUNLU DEĞİL, ama "commit yapmaz" beyanı gövdeye girer (`core/skill-uretim-semasi.md:75`). Eğer görselleştirme çıktı olarak `raporlar/` veya `graf/`'a otomatik yazıyorsa (yan-etki) T-Y'ye kayar → flag zorunlu olur; bu ayrım netleşmeli.
8. **9-alanlı çağrı sözleşmesi** (`core/skill-tetikleme-semasi.md:23-34`): skill·tetik_kosulu·cagri_kipi·girdi·baglam·yan_etki_damgasi·done_yuklemi·hata_yolu·sira — emirde bu 9 alan doldurulmadan skill çağrılamaz.
9. **Teslim usulü (CLAUDE.md §5)**: tam mutlak yol + `open -R` + doğrudan açılan tür (HTML/PDF/MD) + arama-anahtarıyla-başlayan ad + kendini açıklayan ilk ekran + mobil uyum — `gorsellestir` çıktısı bu 5 şartı karşılamalı.
10. **Md açma yüzeyi = VS Code (Karar 80)** (`core/durum-kapsulu.md:10`) — üretilen çıktı `.md` ise VS Code'ta açılacağı varsayılmalı; HTML ise tarayıcıda.
11. **Deterministik tasarım + Karar 65 (`kuyruk/senaryo-defteri.md:156`)**: determinizmle çatışan seçenek (rastgele-tohum yok, LLM-rerank/router yok) her zaman kaybeder — görselleştirme ADIMLARI (veri çekme, layout, renk ataması) mümkün olduğunca **B4 (koda inen script)** olmalı; LLM yalnız "hangi grafik türü" gibi yorumlayıcı kararlarda kalmalı.
12. **KB-50 bağlam bütçesi** (Beyan 12, `kuyruk/senaryo-defteri.md:149`) — araç çıktısı (özellikle bir HTML dosyasının tam içeriği) sohbete DÖKÜLMEMELİ; skill dosya yoluna pointer vermeli.

## 2. Yeniden-kullanım tablosu
| Parça | Ne üretir | Yüzey | Nasıl çağrılır | Pointer |
|---|---|---|---|---|
| `tools/pointer-graf.py` | D2 graf + SVG (5 pano, determinist, sha256 loglu) | dosya (`graf/*.svg`) | CLI: `python3 tools/pointer-graf.py --d2 ... --render 5` | `graf/README.md` |
| lavish (`~/.agents/skills/lavish/SKILL.md`, jarvis'e symlink `~/.claude/skills/lavish`) | tek-dosya HTML artifact + `npx lavish-axi` ile insan-yorumlu review döngüsü | HTML dosya, tarayıcı | `/lavish` ya da örtük tetik | `~/.agents/skills/lavish/SKILL.md` |
| `dataviz` (anthropic-skills, sistem-skill listesinde var ama **dosya sisteminde bulunamadı** — plugin/harness-gömülü, jarvis/`~/.claude` altında ayrı dosyası yok) | grafik/dashboard tasarım kuralları (form heuristiği, renk formülü) | herhangi bir HTML/SVG çıktısı | Skill tool `dataviz` | KAYNAKTA YOK (dosya yolu yok; yalnız isimle mevcut) |
| `artifact-design` / `artifact-diagramming` (aynı durum) | Artifact tasarım/diyagram kuralları | Artifact (HTML) | Skill tool | KAYNAKTA YOK (dosya yolu yok) |
| `hizalama` (anthropic-skills) | oturum-içi kronoloji + Vinland temalı tek-dosya HTML | HTML artifact | tetik cümleleri ("hizala") | KAYNAKTA YOK (dosya yolu bulunamadı; grep `~/.claude` boş sonuç verdi) |
| `tools/kod-envanter.py`, `tools/sunum-son50.py`, `tools/sunum-proof-of-work.py` | HTML üreten mevcut jarvis script'leri (grep `'html'` eşleşmesi) | dosya | CLI | `tools/SCRIPTLER.md` (içerik teyit edilmedi, isim listesi çıkarıldı) |
| `.claude/skills/skill-kapisi/scripts/kapi-denetim.py` | K2-R referans denetimi (deterministik) | stdout | skill-kapisi adım 5 | aynı dizin |
| `tools/kural-sayaci.py` | F6 kritik-talimat/byte sayacı | stdout | `--skill <ad>` | skill-kapisi adım 6 |

## 3. Yan-oturum erişim bulgusu (kanıtlı)
`~/.claude/skills/` KULLANICI-seviyesi dizindir (proje-bağımsız); içinde `lavish`, `gh-axi`, `chrome-devtools-axi` symlink, `no-mistakes` gerçek dizin var. `~/staj başlangıç/.claude/skills/` PROJE-seviyesi ayrı dizindir, yalnız `staj-acilis`/`staj-kapanis` gerçek klasörleri içerir — jarvis'ten symlink YOK, ama kullanıcı-seviyesindeki `lavish` gibi bir symlink staj oturumunda da GÖRÜNÜR olurdu (Claude Code kullanıcı-skill dizinini her projede okur). Sonuç: `gorsellestir` jarvis içinde üretilip `~/.claude/skills/gorsellestir` olarak symlink'lenirse, staj klasöründen açılan oturum da bunu görür — CLAUDE.md §2 "gizli klasör yok" ilkesiyle uyumlu ama staj'ın kendi CLAUDE.md'si yerine jarvis kuralına tabi bir skill sızdırmış olur; ayrım net değilse karışıklık riski var (açık soru §5).

## 4. Description bütçesi bulgusu (sayısal, kaynaklı)
`core/skill-uretim-semasi.md:64,103`: F1 kuralı description ≤1024 char (kanon 07-17) ∧ platform kesme 1536 char ∧ **Σ_H(description) ≤ 0,9 × liste-bütçesi = 7.380 char** (çevrim 4,1 char/token, Salih `/context` ölçümü 08-20, KB-19/Karar 33). 08-20'de 16 skill = 8.220 char → 840 char aşım; 08-21 kısaltma turuyla 7.379 char'a indirildi (Karar 43, GEÇTİ). **`tools/*.py` içinde bu bütçeyi SAYAN ayrı bir araç bulunamadı** — grep `"7.380\|description"` yalnız `argparse description=` kullanımlarını ve SQL `.description` (cursor) alanlarını buldu, özel bir "description bütçe hesaplayıcı" script'i YOK; ölçüm Salih'in elle `/context` çıktısından yapılmış (KAYNAKTA YOK: otomatik sayaç). Yeni `gorsellestir` skill'i eklenirse mevcut 7.379 char + yeni description ≤ 7.380 olmalı — pratikte **1 char'lık pay var**, yani description'lar mevcut hazineden kısaltılmadan yeni skill EKLENEMEZ.

## 5. Açık sorular
1. `gorsellestir` T-Ü mü T-Y mi (çıktıyı otomatik `graf/`/`raporlar/`'a mı yazacak, yoksa yalnız gösterip mi bırakacak) — şekil kararı flag zorunluluğunu değiştirir.
2. dataviz/artifact-design/hizalama skill'lerinin gerçek dosya konumu bulunamadı; bunlar plugin-gömülü ise `gorsellestir` onlara "çağırarak" mı yoksa "ilkelerini kopyalayarak" mı yeniden kullanacak — pointer mı kopya mı?
3. Description bütçesi 1 char paya düştüğüne göre yeni skill eklenirken hangi mevcut description(lar) kısaltılacak (Salih kararı, Katman-1)?
4. `tools/SCRIPTLER.md` içeriği bu koşumda okunmadı — HTML üreten 3 script'in (kod-envanter, sunum-son50, sunum-proof-of-work) tam olarak neürettiği teyit edilmedi, yalnız grep eşleşmesiyle listelendi.
5. Yan-oturum sızma riski (§3) için ayrı bir kanon kuralı mı gerekiyor, yoksa mevcut "gizli klasör yok" ilkesi yeterli mi?
