# İB-51 (1)+(2) — Kural envanteri ve deterministik kümeleme; (3) yükleme-mekanizması adayları (atlas girdisi)

**AS-OF 2026-08-29 · yan icra oturumu (Fable) · HEAD a6eaa5f · Karar 74 M-7 (Salih: İB-51 tetiklendi — "önce deterministik envanter+kümeleme, atlas sonra") · KB-66 Salih notu: "sisteme eklenmiş kuralları kümeleyip görev sınıfına uygun alt-kümeyi bağlama çağıran düzen" · üretici [tools/kural-envanter.py](../tools/kural-envanter.py) (stdlib, LLM yok; birim tanımı `kural-sayaci.py` ile TEK) · gold `veri/gorunum/v_kural_envanter.csv` (1 satır = 1 birim) + `v_kural_envanter_ozet.csv`**

*Ne bu:* Jarvis'te yazılı kuralların NEREDE yaşadığı, hangi ANDA bağlama girdiği ve hangi GÖREV SINIFINA ait olduğunun ölçülü envanteri; sonunda "görev sınıfı → hangi taşıyıcılar yüklenmeli" eşleme şeması ve mekanizma adayları. Karar VERMEZ; atlas koşumunun (Fable-dışı işçiler, −%30 rejimi) sorusunu keskinleştirir. Sayılar satır-grain KESTİRİMDİR (kural-sayaci docstring'indeki iki yönlü yanlılık; m.29).

## 1. Envanter — taşıyıcı sınıfı (yükleme anı)

| Taşıyıcı | Ne zaman bağlama girer | Dosya | Kural birimi | Byte |
|---|---|---|---|---|
| **T0 her-oturum** | otomatik (CLAUDE.md) | 1 | **19** | 6.033 |
| **T1 ritüel-skill** | her seansta tetik ("seans başı/bitimi") | 2 | **52** | 15.731 |
| T2 çağrı-skill | yalnız çağrılınca (14 skill) | 14 | 203 (ort. 14,5/skill) | 54.297 |
| T3 kanon-pointer | pointer'la okununca (tüzük 46 madde + core kural dosyaları + KILAVUZ) | 12 | 416 | 168.424 |
| T4 wiki | başvuru (SOP/Gotchas) | 20 | 327 | 94.657 |
| **Toplam** | | **49** | **1.017** | 339.142 |

**Okuma:** bir seansın taban yükü T0+T1 = **71 birim / 21,8 KB** (kural-sayaci bugün yalnız CLAUDE.md'yi sayıyor: 19 → ritüel skill'ler eklenince 71). KB-50 (a) eşiği ≤100: ortalama **2 çağrı-skill** tetiklenince (71 + 2×14,5 = 100) eşik doludur — yani bugünkü düzende eşik "normal bir seans"ta aşılır; kural-sayaci'nın `--skill` ile ölçmesi gerekir (bugün varsayılan ölçüm 19, gerçek ≥71).

## 2. Kümeleme — görev sınıfı (deterministik anahtar-kelime kuralı, çok-etiketli; birimlerin %53'ü ≥2 sınıfta)

| Sınıf | Birim | Dosya | CLAUDE.md'de | En yoğun taşıyıcılar |
|---|---|---|---|---|
| karar | 323 | 48 | 10 | tüzük 38 · anahtar-kaydı 23 · KILAVUZ 21 · skill-uretim-semasi 16 |
| ajan-koşum | 356 | 47 | 8 | tüzük 27 · skill-uretim-semasi 24 · ajan-metodolojisi 22 · KILAVUZ 16 |
| kanon-bakım | 279 | 40 | 7 | tüzük 26 · anahtar-kaydı 25 · wiki/kokenler 21 · KILAVUZ 15 |
| zaman | 257 | 46 | 5 | wiki/anakronizm-freni 24 · tüzük 21 · anahtar-kaydı 21 · seans-acilis 11 |
| veri-hattı | 224 | 39 | 4 | veri-muhendisligi 20 · world-model 20 · sema-sikistirma 14 · wiki/kolon-katmani 13 |
| teslim | 196 | 47 | 5 | tüzük 17 · KILAVUZ 15 · anahtar-kaydı 9 · seans-kapanis 8 |
| ritüel | 153 | 38 | 3 | seans-acilis 16 · anahtar-kaydı 16 · tüzük 14 · seans-kapanis 13 |
| git | 115 | 38 | 6 | tüzük 14 · KILAVUZ 9 · seans-kapanis 8 · anahtar-kaydı 8 |
| üslup-yasak | 80 | 28 | 4 | tüzük 13 · anahtar-kaydı 8 · skill-tetikleme 6 · seans-acilis 5 |
| genel (eşleşmeyen) | 178 | 42 | 0 | skill-uretim-semasi 17 · wiki/dil-secimi 13 · gorsel-artefakt 10 |

**Okuma:** (a) `core/tuzuk-v0.md` ve `core/baglam-anahtar-kaydi.md` her sınıfta ilk üçte — "genel kanon" taşıyıcıları; sınıf-özel yükleme onlardan MADDE seçerek yapılmalı, dosya bütünüyle değil (tüzük 53,8 KB). (b) `zaman` sınıfının gövdesi wiki'de (anakronizm-freni 24) — Karar 69 (a) "pointer CLAUDE.md'de, gövde wiki'de" deseni ölçülebilir biçimde çalışıyor. (c) `genel` 178 birim = anahtar-kelime kuralının kör noktası (%17,5); atlas/insan sınıflaması ya da kural genişletme adayı — otomatik etiketleme LLM'e verilmez (Karar 65), kural genişletilir.

## 3. Görev sınıfı → yükleme eşlemesi (deterministik şema; bugün fiilen NASIL yükleniyor ↔ ÖNERİLEN alt-küme)

| Görev sınıfı | Bugün | Önerilen alt-küme (pointer'lı; tam dosya değil) | Kestirilen yük |
|---|---|---|---|
| ritüel | T0+T1 otomatik | aynen | 21,8 KB |
| git | CLAUDE.md §4/§6 + seans-kapanis §7 | + tüzük m.9/m.10 + `wiki/paralel-oturum-protokolu.md` H4 | +~3 KB |
| karar | CLAUDE.md §4/§5 + karar-* skill'leri çağrılınca | tüzük m.16/m.37/m.40 maddeleri + `celiski-kapisi` | +~6 KB |
| ajan-koşum | CLAUDE.md §6 pointer satırı | `core/ajan-metodolojisi.md` + `skill-tetikleme-semasi` + atlas/pipeline skill | +~15 KB |
| veri-hattı | pointer | `core/veri-muhendisligi-katmani.md` §2/§8 + `veri/README.md` hat sırası + wiki silver/kolon | +~10 KB |
| kanon-bakım | pointer | tüzük m.8/m.20-22 + `baglam-anahtar-kaydi` §3 + damitma/wiki skill | +~8 KB |
| teslim | CLAUDE.md §5 | + KILAVUZ "Tasarım ilkeleri" + Obsidian-uyum satırı | +~3 KB |
| zaman | CLAUDE.md §6 tek satır | + `wiki/anakronizm-freni.md` M1-M7 + `bayat-cekim.py` SOP | +~4 KB |
| üslup-yasak | CLAUDE.md §6 | tüzük m.7/m.23/m.33 | +~1 KB |

Yük kestirimleri birim-byte toplamından (v_kural_envanter_ozet), m.29.

## 4. (3) Yükleme mekanizması adayları — atlas sorusu (karar Salih'in / masa)
- **(a) Deterministik sınıflayıcı hook:** kullanıcı istemi (ya da ilk araç çağrısı) aynı anahtar-kelime kuralıyla sınıflanır → bağlama tek satır pointer listesi enjekte edilir ("bu iş `veri-hattı`: oku core/veri-muhendisligi-katmani.md §2, veri/README.md hat sırası"). *Artı:* Karar 65 uyumlu, ≤300 B, mevcut hook altyapısı. *Eksi:* yanlış sınıf = yanlış pointer (kör nokta %17,5); pointer'ı okumak yine modelin işi.
- **(b) Sınıf-skill'leri:** 9 görev sınıfı için description'ı sınıf sözcükleriyle tetiklenen 9 ince skill (gövde = pointer listesi). *Artı:* mevcut mekanizma. *Eksi:* hazine 16→25, skill-listing bütçesi (%1, 2.000 tk) zorlanır; tetiklenme deterministik değil (model seçer).
- **(c) SessionStart brifine sınıf→pointer tablosu:** statik 9 satır (≤600 B) brif bütçesine (≤2 KB) girer. *Artı:* sıfır yeni mekanizma. *Eksi:* her seans yüklenir (istenmeyen "her kural her konuşmada" biçiminin küçük hali).
- **(d) Dış emsal (atlas doğrulasın, AS-OF ≤ kesim doğrulanmadı):** yol-kapsamlı kural dosyaları (Claude Code `.claude/rules/*` `paths:` frontmatter · Cursor rules `globs` · Copilot `applyTo`) — dosya-yolu tetikli deterministik yükleme; Jarvis'te görev sınıfı ≈ dokunulan dizin (veri/ → veri-hattı, wiki/ → kanon-bakım, cc/ → ajan-koşum).
- **Öneri (Carvis, karar değil):** atlas sorusu = "(d) yol-kapsamlı kural mekanizması Claude Code'da canlı mı; varsa (a)'nın yerine geçer mi; bağlam maliyeti ölçümü nasıl" — atlas işçileri Sonnet, bütçe 10-15, effort düşük (−%30 rejimi). Koşum Salih tetiğinde (M-7 tetikledi; bu rapor emrin girdisi).

## 5. Ne değişti / ne değişmedi
- Değişen: envanter + kümeleme aracı ve gold görünümleri; kural-sayaci'nın eksik saydığı gerçek seans yükü (19 → ≥71) ölçüldü; eşleme şeması + 4 mekanizma adayı yazıldı.
- Değişmeyen: hiçbir kural taşınmadı/silinmedi; CLAUDE.md dokunulmadı (Katman-1); atlas koşmadı.
- Yeniden açma: sınıf regex'i değişirse sayılar değişir (kural kimliği script'te); kural-sayaci `--skill seans-acilis seans-kapanis` varsayılanı Salih kararı (KB-50 a ölçüm tanımı).
