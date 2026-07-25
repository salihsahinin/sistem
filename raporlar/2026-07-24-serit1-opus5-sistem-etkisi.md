# Şerit 1 — Claude Opus 5'in JARVIS'e Etkisi (Atlas Raporu, 2026-07-24)

> **Mod:** yan-oturum (m.41) — öneri üretir, kanon KİLİTLEMEZ. `core/` · `CLAUDE.md` · `.claude/` yazılmadı.
> **Şerit:** çift-atlas (tez ∧ ¬tez) · aile sayısı: 3 · tez 3/3, antitez 3/3 → **tam diyalektik**
> **Kime:** Salih + ana-sıra (nihai karar orada)
> **Kaynak dosyalar:** `scratchpad/T1-A{1,2,3}-serit{A,B}.md`

## 0. Kanıt kısıtı (dürüstlük beyanı — raporun tamamını etkiler)

Bu oturumun egress politikası `anthropic.com/news`, `claude.com/blog`, `support.claude.com` dahil çoğu hostu 403'ledi. Geçen alanlar: `platform.claude.com`, `code.claude.com`, `raw.githubusercontent.com`, paket kayıtları.

Bunun iki sonucu var ve ikisi de raporun okunma biçimini değiştirir:

1. **Bu şeridin [D] etiketleri gerçek ama tek-kaynaklıdır.** Hem tez hem antitez ajanı aynı kaynak evrenine (Anthropic'in kendi dokümanları) inmek zorunda kaldı. Antitez ajanı bunu kendisi beyan etti: *"Hiçbir iddiayı tam çürütemedim ve bunu süslemeyeceğim… bağımsız kanıt evreni 403 duvarının arkasında."* Dolayısıyla aşağıdaki "hayatta kalan çekirdek", **adversarial-hayatta-kalma** değil **tek-kaynağa-bağımlı hayatta-kalma**dır. Anthropic kendi ürünü hakkında yanılıyorsa bu raporda yakalanmaz.
2. **Benchmark ve plan-kotası rakamları [K]'da kaldı** — duyuru sayfalarına inilemedi.

## 1. Aile başına bulgular

### Aile 1 — Modelin kendisi
- **Tez:** 12 iddia, hepsi [D] (Anthropic dokümanları).
- **Antitez:** 0 çürütme, **8 daraltma**, 1 çözülemeyen çelişki.

### Aile 2 — Harness / Claude Code katmanı
- **Tez:** 12 iddia [D].
- **Antitez:** raporu diske yazdı, özet döndüremeden oturum limitine takıldı (`T1-A2-seritB.md`). Bu ailenin antitez hükümleri rapora **işlenmedi** — aşağıda ayrıca işaretli.

### Aile 3 — Prompt / bağlam mühendisliği deltası
- **Tez:** 12 iddia [D].
- **Antitez:** 5 daraltma, 7 çürütülemedi, **1 dürüst başarısızlık kaydı** (aşağıda §4).

## 2. Hayatta kalan çekirdek (JARVIS'e doğrudan dokunan)

### 2.1 ★ Doğrulama protokolümüz tehdit altında DEĞİL — gerilim çözüldü

Anthropic'in Opus 5 rehberi "doğrulama talimatlarını kaldırın" diyor. İlk okumada bu m.40b (tez→antitez→hakemlik) ve V26 (örneklem-denetimi) hattını söktürüyor gibi görünüyordu. **İki bağımsız antitez ajanı aynı ayrımı buldu:**

- Kaldırılması istenen şey modelin **kendi işini** tekrar tekrar doğrulaması ("do not use subagents to verify **your own** work").
- **Bağımsız/düşmanca çapraz denetim aynı sayfada öneriliyor** ve Anthropic'in kendi ürününde (`/deep-research` içinde "verifier agents") ürünleşmiş durumda.

**Hüküm:** m.40b'nin üretici≠doğrulayıcı ayrımı korunuyor. Kanonda değişiklik gerekmiyor. *Kaynak: T1-A1-seritB İ8, T1-A3-seritB İ2.*

### 2.2 ★ Kanon dosyasını kısaltma baskısı YOK — doğru okuma başka

Tez, resmi CLAUDE.md hedefinin <200 satır olduğunu ve uzun dosyaların talimat-uyumunu düşürdüğünü söyledi. Antitez bunu daralttı:

- Sert 200-satır kesmesi **CLAUDE.md'de değil, MEMORY.md'de**; CLAUDE.md kırpılmıyor.
- Resmî çare **kısaltmak değil, path-scoped rules'a taşımak**.
- "Uyum düşer" nedenselliği kaynakta kanıt referansı olmadan verilmiş — beyan olarak [D], altındaki ampirik önerme [K].
- HTML yorumları bağlama hiç girmiyor.

**Yerel ölçüm (bu oturumda yapıldı):** `CLAUDE.md` 27 satır / 6.085 bayt. Satır sayısı bizde yanıltıcı vekil ölçü — satırlar yoğun paragraflar. **KILAVUZ'daki KB+token rejimimiz resmî satır-eşiğinden daha iyi bir enstrüman.**

**Hüküm:** m.8 (otomatik silme yasağı) ile çatışma yok. Yeni borç açılmıyor. *Kaynak: T1-A3-seritB İ9.*

### 2.3 ★ Çelişki kapısına (m.16) dışarıdan gelen gerekçe

Resmî doküman: çelişen iki kural varsa **model birini keyfî seçebilir**; ve *"büyük veya karmaşık sistem promptları"* modeli daha sık düşündürüyor (gizli token+gecikme maliyeti).

**Yerel ölçüm:** `core/tuzuk-v0.md` 40 KB'yi **69 satırda** taşıyor (m.30 tek başına dev bir satır). Otomatik yüklenmiyor (m.20 pointer sistemi) — yani sürekli maliyet değil, ama okunduğu her seferde bu iki risk yürürlükte.

**Hüküm:** m.16'nın değeri dışarıdan doğrulandı. Tüzük içi çelişki taraması periyodik bakım kalemi olmayı hak ediyor. *Kaynak: T1-A3 İ9/İ11 + yerel ölçüm.*

### 2.4 ★ CLAUDE.md yaptırım değil, bağlamdır — yapısal kilit tercihimiz doğrulandı

Resmî doküman: CLAUDE.md sistem promptunun parçası değil; sistem promptundan **sonra kullanıcı mesajı** olarak veriliyor ve *"context, not enforced configuration"* sayılıyor. Kesin yaptırım için hook/permission gerekiyor.

**Hüküm:** m.41 Dilim-1 paketinin (settings-deny + PreToolUse teli) tercihi birincil kaynakla örtüşüyor. Antitez bunu çürütecek hiçbir şey bulamadı. *Kaynak: T1-A3-seritB İ10 (ÇÜRÜTÜLEMEDİ).*

### 2.5 Model ve efor: `cc/` görev emri ritüeli güncellenmeli

| Bulgu | Hüküm | JARVIS etkisi |
|---|---|---|
| Opus 5 CC v2.1.219 ile geldi; **bu makinede doğrulandı** (`claude --version` = 2.1.219) | [D] + yerel gözlem | `cc/README.md` envanteri (2.1.209) **bayat** |
| `.claude/agents/research-agent.md` içindeki `model: opus` artık **Opus 5'e** çözülüyor | [D] | Atlas ajanları bugün fiilen Opus 5 koştu |
| Varsayılan Opus 5 **yalnız** Max / Team Premium / Enterprise-PAYG / API'de; **Pro ve Team Standard → Sonnet 5** | [D] daraltma | Görev emrindeki model satırı plana bağlı — hangi planda olduğumuz yazılı değil |
| Efor merdiveni tam (low→max), varsayılan `high`; kodlama/ajanik iş için `xhigh` öneriliyor | [D] | 07-22 kararı (`Opus → xhigh`) resmî tavsiyeyle uyumlu |
| Model **ve** efor cache anahtarının parçası; oturum ortasında efor değiştirmek yeniden işletiyor | [D] | "modeli ve eforu oturum başında seç, sabit tut" — `cc/` ritüeline eklenmeli |
| Model-başına efor **tutma** yok; önceki modelin eforu devralınıyor — ama **sessiz değil**, seviye oturum başlığında/altbilgide görünür | [D] daraltma | Erken uyarım fazla sertti; yine de görev emrinde efor teyidi istenmeli |
| Efor **yanıt uzunluğunu güvenilir biçimde kısaltmıyor** | [D] | Uzunluk açık promptlanmalı; uzun sistem promptunda sona yakın hatırlatıcı |
| Prompt cache minimumu 512 token (Opus 5 icadı değil, Fable 5 ile gelmiş) | [D] daraltma | Kararlı-prefix standardımız (Model C) daha küçük dosyalarda da kazanıyor |

### 2.6 ★ Alt-ajan katmanı: iki iddia bu oturumda GÖZLEMLE doğrulandı

Bunlar artık "arama-özeti" değil, **yerinde gözlem** — kanıt hiyerarşisinde en üst basamak:

1. **Eşzamanlı 20 alt-ajan tavanı.** 12 ajan açtım, 13'üncü *"Concurrent subagent limit reached. You can run 20 subagents at once"* ile reddedildi. Tez iddiası birebir tuttu.
2. **İç içe alt-ajan canlı.** Benim açtığım 12 ajan 20 tavanını doldurdu → aradaki farkı ajanların kendi çocukları açıklıyor. Bu, CHANGELOG ("varsayılan derinlik 3") ile dokümanların ("varsayılan 1, alt-ajan alt-ajan açamaz") **çelişkisinde CHANGELOG lehine güçlü karine**. Kesin kanıt değil; çelişki resmî tarafta açık kaldı.

**Operasyonel sonuç:** bugünkü koşumun gerçek ajan sayısı ve token maliyeti benim açtığım 12'nin üzerinde ve **ne kadar üzerinde olduğunu bilmiyorum**. Atlas tanımında delegasyon kotası yok; Opus 5 rehberi tam bu davranış için "deterministic cap" öneriyor.

### 2.7 Güvenlik sınıfı — PortRisk hattına dokunan tek bulgu

Claude Code'da siber-işaretli istekler Opus 4.8'e düşürülüyor, biyoloji-işaretli istekler reddediliyor; tetikleyici ilk isteğe giren **CLAUDE.md içeriği ve git durumu** olabilir. Antitez bunu daralttı ama kırmadı — ve önemli bir ek getirdi: **alt-ajan/headless koşumlarında düşürme yok, doğrudan ret var.**

**JARVIS etkisi:** PortRisk (finans/risk) hattı ve güvenlik konulu atlas koşumları için gerçek arıza sınıfı. Teşhis yolu: `claude --safe-mode`.

## 3. Daraltılan / düşen iddialar

| İddia | Ne oldu |
|---|---|
| "Opus 5 tüm hesap tiplerinde varsayılan" | **DARALTILDI** — Pro/Team Standard'da Sonnet 5 |
| "Maks çıktı 128k" | **DARALTILDI** — Batch'te ayrı beta ile 300k |
| "Efor sessizce devralınıyor" | **DARALTILDI** — devralma var, sessizlik yok |
| "512 token eşiği Opus 5 ile geldi" | **DARALTILDI** — Fable 5 ile gelmiş |
| "Ayrı rate-limit kovası" | **DARALTILDI** — API'ye özgü; abonelik tarafı farklı ve Pro/Max için kanıtsız [X] |
| "Prompt corpus'u model-özel yeniden ayarlanmalı" | **DARALTILDI** — resmî tavsiye corpus-geneli tarama değil, **beş dar kategori** taraması |
| "Lafzî talimat-uyumu bir risktir" | **DARALTILDI** — doküman bunu esas olarak **artı** sayıyor |
| "1M tutarlılık ↔ context rot çelişkisi" | **DARALTILDI — gerilim sahte:** tutarlılık iddiası *talimat-uyumu/araç-çağırma/akıl yürütme* için, bozulma *doğruluk/geri-çağırma* için. Ayrık değişken kümeleri. |
| "Yalnız `ultrathink` anahtar kelime" | **DARALTILDI** — `ultracode` da tanınıyor; ayrıca "think hard" sıradan metin olsa da resmî olarak **etkili** steering ifadesi sayılıyor |

**Yerel tarama:** kanonda `think hard` / `ultrathink` kalıbı **bulunamadı** (tek eşleşme fikir havuzunda, kural metninde değil). Ölü prompt kalıbı borcumuz yok.

## 4. Antitez ajanının dürüst başarısızlık kaydı (protokol açısından değerli)

¬T1-A3, İ8'i (efor değişimi cache'i bozar) çürütmek için `Build an orchestration mode` referans uygulamasının kodunu okudu; efor'un `xhigh` sabitinde tutulduğunu, alt-ajanların bile devraldığını, mod değişiminin cache'i bozmayan mid-conversation system message ile yapıldığını buldu. **Karşı-tez düştü, iddia güçlendi.** Bu, süs-antitez olmadığının kanıtı.

## 5. V26 örneklem-denetimi

| Ajan | Denetlenen iddia | Yöntem | Sonuç |
|---|---|---|---|
| T1-A1 | CC sürümü 2.1.219 | `claude --version` | **TUTTU** (yerinde gözlem) |
| T1-A2 | Eşzamanlı 20 ajan tavanı | 13. ajanı açma denemesi | **TUTTU** (yerinde gözlem) |
| T1-A2 | İç içe alt-ajan derinliği >1 | tavan aritmetiği | **Güçlü karine**, kesin değil |
| T1-A2 | `tools:` listesinde çözülemeyen giriş varsa ajan başlamaz | 9 atlas ajanının fiilen başlaması | **YANLIŞLANDI** — ajanlar `Task` girişiyle başladı |
| T1-A2 | PreToolUse `exit 2` sertleşmesi | telin kodu okundu | Telimiz JSON üretmiyor → **etkilenmiyor** |
| T1-A3 | CLAUDE.md 200 satır eşiği | `wc -l` | 27 satır — **eşik altında**, ama ölçü vekil |

> **Denetim sınıfı uyarısı:** Bu tablodaki "TUTTU"lar yerel gözlemdir. Dış kaynak iddialarında kaynağa inemediğim için denetimim *kaynak doğrulama* değil, ajanlar-arası tutarlılık kontrolüdür. İkisini karıştırmayın.

## 6. Öneriler (karar Salih/ana-sırada — burada karar alınmadı)

**Sıcak (bugün anlam taşıyan):**
1. `cc/README.md` envanterini tazele: CC **2.1.219**, Opus 5 varsayılan, `/effort` hâlâ ayrı komut değil.
2. `cc/` görev emri şablonuna iki satır ekle: (a) modeli **ve** eforu oturum başında sabitle, ortada değiştirme (cache); (b) koşum öncesi efor seviyesini oturum başlığından **teyit et** (model-başına tutma yok).
3. Atlas ajan tanımına **delegasyon kotası** yaz (Opus 5 rehberinin doğrudan tavsiyesi + bugünkü 20-tavan gözlemi). Şerit-4'ün ilk maddesi.
4. Hangi Claude planında olduğumuzu kanona yaz — model varsayılanı buna bağlı.

**Ilık:**
5. Tüzük içi çelişki taramasını periyodik bakım kalemi yap (m.16'nın makine tarafı).
6. PortRisk hattı açıldığında `--safe-mode` teşhisini not düş; alt-ajan koşumlarında siber-işaretli istek **reddedilir**, düşürülmez.

**Yapılmayacak (bilerek):**
7. m.40b/V26 doğrulama zincirine dokunma — kaldırılması istenen şey o değil.
8. Kanon dosyalarını "resmî eşik" gerekçesiyle kısaltma — eşik bize uygulanmıyor, rejimimiz zaten daha iyi.

## 7. Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. İç içe alt-ajan derinliği fiilen kaç? CHANGELOG 3, doküman 1 diyor; bizim gözlemimiz >1. **Ölçülmeli** (bir atlas koşumunda çocuk sayısını raporlatarak).
2. Bugünkü koşumun gerçek token maliyeti ne oldu? Görünmeyen çocuk ajanlar yüzünden bilinmiyor. `/usage` ölçümü alınmalı.
3. Hangi Claude planındayız — Opus 5 mi Sonnet 5 mi varsayılan?
4. Aile 2'nin (harness) antitez hükümleri bu rapora işlenmedi (`T1-A2-seritB.md` diskte, özet dönmedi). Ana-sıra okumalı.
5. `raw.githubusercontent.com`'un açık olması bir politika tercihi mi, gözden kaçan bir açıklık mı? Araştırma kapasitemizin şu anki tavanı buna bağlı.

---

*Yan-oturum çıktısı. Kanon kilitlenmedi, `core/` yazılmadı. Karar ana-sırada (m.41).*
