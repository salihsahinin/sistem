---
name: emekli-anahtar-cascade
description: Bir ad/tetik/kavram değeri emekli olduğunda (ör. emekli "günaydın" → "seans başı", eski ad Carvis → Jarvis, emekli vardiya → seans) bağlam anahtar kaydına damgalı emekli satırını üretir ve yayılımı deterministik script'le yürütür; kalıntı taraması (sıcak/ılık/soğuk), diff önizleme → onay → yeniden yazım, README bağlama bloğu, denetim-sonra ve commit mesajı. Kullan; "X'i emekli et", "X yerine Y", "adı değiştir", "tetiği değiştir", "cascade koş", "kalıntı var mı" dendiğinde ya da her ad/tetik/kural değişiminde (core/baglam-anahtar-kaydi.md §3 zorunlu adımlar). Kullanma; tarihli kayıtları (raporlar/cc/arşiv) yeniden yazmak için, kanon dosyasını Salih imzasız değiştirmek için, salt sayım için (anahtar-denetim.py yeter), yazım/biçim düzeltmesi için.
argument-hint: "<anahtar_id> <eski> → <yeni> [tarih] [karar no]"
disable-model-invocation: true
metadata: { owner: jarvis, version: "0.1.0-deneysel-m29", kural: "core/baglam-anahtar-kaydi.md §1 ilke 5-9 · §3", ib: "İB-90 P1+P2", karar: "Karar 96 M2 A3 · Karar 93 EK deseni" }
---

# emekli-anahtar-cascade — emeklilik + yayılım (v0.1, 2026-09-15)

Tür: T-Y yan-etkili (kanon kaydına satır + sıcak/ılık dosyalarda yeniden yazım + commit). Frenler: kanon dosyası (`core/`) yalnız Edit aracıyla ve Katman-1 sınıfı değişimde Salih imzasıyla (m.31; §3.1); yeniden yazım "diff üret → onay" modelindedir (§1 ilke 9), soğuk katman (tarihçe) asla yazılmaz (Karar 68 EK). Script: `tools/anahtar-cascade.py` (üretir), denetim `tools/anahtar-denetim.py` (sayar); ad-eşitliği özel hâli `tools/ad-esitligi-denetim.py` (Karar 93 EK). Tekrar sayımı: 08-15 günaydın · 08-17 metafor paketi (5 anahtar) · 09-10 Carvis → Jarvis — 3 elle cascade.

## Adımlar (§3 sırası backward)
1. **Kayıt satırı üret:** `python3 tools/anahtar-cascade.py kaydet --anahtar <id> --eski "<eski>" --yeni "<yeni>" --tarih YYYY-MM-DD --gerekce "<karar no + neden>" [--tur …] [--varyant …] [--izinli <regex> …]` → JSON. Çevrim (eski = yeni) ve zincir derinliği >1 script'te reddedilir. Çıktıyı `core/baglam-anahtar-kaydi.md` §2 JSON bloğuna **Edit** ile ekle; `guncelleme` alanına tarih + karar no. Katman-1 sınıfıysa (ad, tetik, rol, kanon terimi) Salih imzası olmadan bu adım yapılmaz.
2. **Denetim-önce (baseline):** `python3 tools/anahtar-denetim.py --anahtar <id>` → sıcak/ılık/soğuk sayıları deftere/commit mesajına.
3. **Tarama + önizleme:** `python3 tools/anahtar-cascade.py tara --anahtar <id> --katman sicak` → her kalıntı satırı `-`/`+` çiftiyle. Anlamı bozacak satır (dizin adı, regex, tarihçe cümlesi) → izinli kalıba al (kayıt satırındaki `izinli_kaliplar`) ya da elle yaz; kod dosyaları (.py/.sh/.json/.html) script'çe yazılmaz, elle bakılır. Skill description'ları **önce** (tetik yüzeyi, §1 ilke 7).
4. **Uygula (onaylı):** `python3 tools/anahtar-cascade.py uygula --anahtar <id> --katman sicak --onay`; ılık için aynı komut `--katman ilik` (aynı seansta ya da bakım kartı). `.claude/` ve `core/` altındaki dosyalar için script yazımı da Edit ile eşdeğerdir; PreToolUse teli Bash metnini denetler, meşru cascade ana-sırada koşar.
5. **README bağlama (Karar 93 EK sınıfı):** `python3 tools/anahtar-cascade.py readme --anahtar <id>` → bağlanmamış kalıntı taşıyan dizinlerin README eşleniğinde "<eski> = <yeni> (eski değer)" satırı var mı. Salih "her kombinasyonda bilinsin" dediyse `--zorunlu` (ihlal), aksi hâlde `FLAG`.
6. **Tetik-eval:** tetik/skill-adı anahtarlarında ilgili skill'in `evals/evals.json` should_not_trigger listesine eski değer eklenir (§3.4).
7. **Denetim-sonra + commit:** `python3 tools/anahtar-denetim.py --anahtar <id>` sıcak ihlal 0 → `[icra]` commit `retire <id>: <eski>→<yeni>, cascade N dosya`; ≠0 → commit mesajına "`KISMİ`" + bakım kartı (**restrict**, §1 ilke 6). Kaldırma (kaydı arşive indirme) ≥3 seans sonra ayrı commit (§3.6).

## Gotchas
- **Kayıt dosyası kalıntı değildir:** script `core/baglam-anahtar-kaydi.md`'yi taramadan çıkarır; anahtar-denetim ile aynı sayım.
- **Varyant ≠ yazım hatası:** Türkçe/ASCII farkı (emekli değer günaydın/gunaydin) script'te otomatik; çekim ekleri (vardiyası, vardiyada) `--varyant` ile verilir, yoksa sayılmaz.
- **Dizin/dosya adları:** `raporlar/vardiya/` gibi emekli değer taşıyan yol parçaları yeniden yazılmaz (git mv ayrı karar, m.8); izinli kalıba al.
- **README bloğu her anahtar için zorunlu değil:** Carvis = Jarvis örneği Salih'in açık "her kombinasyon" kararıydı; emekli günaydın için 9 dizin `FLAG` çıkar, hüküm Salih'in.
- **Skill description = tetik yüzeyi:** emekli tetik description'dan çıkar, alias yalnız soğuk katmanda pointer (§1 ilke 7).
