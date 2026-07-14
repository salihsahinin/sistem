> **TAŞINDI (2026-07-15, Salih icra emri):** Homebase'ten JARVIS'e — köken: `Cowork Homebase/[C] Loop Engineering — Yol Haritası.md`; tespit raporu: `raporlar/homebase-tasima-tespiti-2026-07-15.md`. Orijinal Homebase'te arşiv-pointer'la durur (m.8).

---
author: claude
type: plan
date: 2026-07-07
---

# Loop Engineering — Öğrenme + Uygulama Yol Haritası

> **Kaynak:** Claude Code ekibinin resmi yazısı "Getting started with loops" (claude.com/blog, 30 Haziran 2026; @ClaudeDevs X duyurusu 7 Temmuz). Bu dosya öğrenme→uygulama sırasını tutar. Backlog AYRI: `[C] Loop Engineering — Sonrası.md` — kuralı değişmedi (3 aktif madde bitmeden hiçbir backlog maddesi açılmaz).
> **Statü:** Salih'in kararıyla İLK ÖNCELİK (2026-07-07). 07-02'deki 3 aktif madde bu haritanın Faz 1/2/4'üne gömülü — ayrı liste yok, tek sıra bu.

## 0 · Tek cümlelik öz

Loop engineering, promptu her seferinde senin yazman yerine **işin hangi parçasını sisteme devrettiğini** tasarlamaktır. Merdiven dört basamak: önce **kontrolü** devredersin (skill), sonra **durma koşulunu** (/goal), sonra **tetikleyiciyi** (/loop, /schedule), en sonda **promptun kendisini** (proaktif rutinler). Resmi tanım: *loop = ajan, bir durma koşulu sağlanana dek iş çevrimini tekrarlar.*

## 1 · Kavram haritası (resmi kaynaktan)

| Tip | Tetikleyen | Durduran | Sen neyi devredersin | Araç |
|---|---|---|---|---|
| Turn-based | Senin promptun | Claude "bitti" der | Kontrol adımını | Doğrulama skill'i |
| Goal-based | Sen (canlı) | Hedef sağlandı VEYA tur limiti | "Bitti"nin tanımını | `/goal` |
| Time-based | Zaman aralığı | Sen iptal edersin / iş biter | Tetikleyiciyi | `/loop` (lokal), `/schedule` (bulut) |
| Proactive | Olay/takvim, insansız | Görev hedefte biter; rutin sen kapatana dek | Promptu | Hepsi + auto mode + dynamic workflows |

**Turn-based:** Her normal prompt zaten bir döngüdür — bağlam topla → yap → kontrol et → gerekirse tekrarla → cevapla. Zayıf halka kontrol adımı; kendi manuel kontrollerini bir SKILL.md'ye gömersen Claude kendi işini uçtan uca doğrular. Kural: kontrol ne kadar sayısal, öz-doğrulama o kadar kolay. *Örnek: "UI değişikliğine bitti deme — sayfayı tarayıcıda aç, butona tıkla, konsolda sıfır hata gör, öyle raporla."*

**Goal-based (`/goal`):** "Bitti neye benziyor"u sen tanımlarsın; Claude durmayı her denediğinde ayrı bir değerlendirici model (evaluator — koşulun sağlanıp sağlanmadığına bakan küçük hakem) kontrol eder, sağlanmadıysa işe geri yollar. Tur limiti şart ("5 denemede dur") — yoksa açık çek yazmış olursun. Deterministik (yoruma yer bırakmayan) kriter en iyisi: geçen test sayısı, skor eşiği. *Örnek: `/goal ana sayfanın Lighthouse skorunu 90+ yap, 5 denemede dur.`*
> **Düzeltme (07-07):** CLAUDE.md'deki eski betim "verifier her turda kontrol eder" diyordu — resmi kaynağa göre evaluator her turda değil, **Claude durmayı denediğinde** devreye girer. Wiki sayfasına doğrusu yazılacak.

**Time-based (`/loop`, `/schedule`):** Tekrarlayan ya da dış sisteme bakan işler için tetikleyiciyi zamana bağlarsın. `/loop` kendi makinende koşar, kapatınca durur (*örnek: `/loop 5m PR'ımı kontrol et, review yorumlarını işle, CI'ı düzelt`*); `/schedule` aynı işi buluta taşır (Routine — makine kapalıyken de koşar; research preview). Token kuralı: aralığı, izlediğin şeyin gerçek değişim hızına eşle.

**Proactive:** Kompozisyon katmanı — `/schedule` (ne zaman) + `/goal` (bitti tanımı) + skill (nasıl doğrulanır) + auto mode (izin sorularını insansız yöneten mod) + dynamic workflows (çok-ajanlı orkestrasyon; research preview). *Örnek: "Her saat feedback kanalını tara; bulunan her rapor triage edilip cevaplanana dek durma; düzeltmede 3 çözümü paralel dene, hakem ajan seçsin."*

## 2 · Kalite + token ilkeleri (özet)

Tek hatayı düzeltmekle kalma — o hatayı yakalayacak kuralı skill'e göm ki sonraki bütün turlar kazansın. Review'u taze bağlamlı ikinci ajana yaptır (ana ajanın kendi gerekçesinden etkilenmez; backlog #3 ile aynı fikir). Token tarafı: işe göre en küçük primitive+model · net done tanımı · büyük koşudan önce küçük dilimde pilot · deterministik iş için script (her seferinde yeniden akıl yürütmekten ucuz) · `/usage` ve argümansız `/goal` ile tüketimi izle.

## 3 · Fazlar — önce öğren, sonra uygula

Her fazın kendi DONE tanımı var. Bu bilinçli: konunun özü zaten "done tanımı yazamıyorsan loop kuramazsın, dilek kurarsın."

### FAZ 0 — Oku + kendi cümlelerinle anlat (öğrenme · ~45 dk) — **DONE (2026-07-10)**
> Kapanış kaydı: TR transkript üzerinden koşuldu (`[C] Looplara Baslangic — Blog Transkripti (TR).md`). 4 tip mekanizmalarıyla oturdu (2 sert düzeltme: "her tipte tetikleyici kural değildir" + "done yazılamıyorsa /goal kurulamaz"); eşleştirmeler: transkript hattı→proaktif (Claude, örnek) + CSV düzeltme→tur-tabanlı (Salih, "1 promptluk iş" gerekçesiyle); B-koşulu Salih'ten: iterasyon gerekli + done yazılabilir = /goal. Öğrenme modeli bu koşuda güncellendi (Salih talimatı): tekrar-ettirme yerine uygularken — ilk örnek Claude'dan gerekçeli, ikincisi Salih'ten; düzeltme sertliği hatanın proje+anlayış etkisiyle orantılı.
**İş:** Resmi blog yazısını baştan sona oku → sonra Cowork'e yaz: 4 tip nedir, her birinde neyi devrediyorsun, senin işlerinden hangi ikisine hangi tip uyar. Claude yanlışı sertçe düzeltir (PortRisk anlama-kapısının mini versiyonu — orada çalıştı).
**DONE:** 4/4 tip doğru anlatıldı + kendi işlerinden 2 eşleştirme önerdin.

### FAZ 1 — Wiki sayfası (= aktif madde 1) — **DONE (2026-07-10)**
> Kapanış: `[C] Loop Engineering.md` açıldı, kaynaklar linkli, backlog işaretli (commit `07135ae`). Rol revizyonu (Salih talimatı, 07-10): dolgu Claude'dan — "ben söylüyorum, sen yapıyorsun" (Jarvis çekirdek modu); Salih'in öğrenme payı Faz 0'da konuşarak ödendi, formülasyonları sayfada isimli.
**İş:** `[C] Loop Engineering.md` sayfasını aç: goal/loop/routine ayrımı + evaluator ilkesi (düzeltilmiş haliyle) + devretme merdiveni + kaynak linkleri + backlog linki ve 1 satır özet (backlog dosyasındaki kural gereği). İskelet Cowork'ten, dolgu senden — sayfayı ben yazarsam öğrenme bende kalır.
**DONE (07-02 tanımı):** Sayfa açıldı, kaynaklar linkli.

### FAZ 2 — İlk `/goal` koşusu (= aktif madde 2 · CC tarafı, sende)
**İş:** Gerçek, küçük bir görevde `/goal` + tur limiti. Aday — dayatma değil, tercih (5) hâlâ senin: PortRisk Sprint 1'in ilk dilimi, *"/goal: yfinance ile 15 enstrümanın kapanış fiyatlarını çeken fonksiyon yazılsın, pytest yeşil; 10 turda dur"* (ön-koşul: `python --version` — hâlâ hiç koşulmadı). Deterministik kriter hazır: test. Alternatif istersen PortRisk-dışı küçük bir görev de olur.
**DONE (07-02 tanımı):** Koşu tamamlandı + 3-5 cümle öğrenim wiki sayfasına işlendi.

### FAZ 3 — `/loop` tanışması (opsiyonel · 10 dk)
**İş:** Oturumdayken kısa aralıklı bir `/loop` başlat, davranışı gör, iptal et. Amaç sadece hissetmek; kalıcı bir şey kurmak değil.
**DONE:** Bir `/loop` başlatıldı + iptal edildi + 1 cümle not.

### FAZ 4 — İlk Routine (= aktif madde 3)
**İş:** Transkript pipeline sabah koşusu: yeni içerik kontrolü → indir → transkribe → RAG'e ekle → Homebase'e özet; `/schedule` ile buluta.
**DONE (07-02 tanımı):** Routine oluşturuldu + ilk otomatik koşu doğrulandı.

### FAZ 5 — Kapanış + backlog kapısı
**İş:** 3 aktif madde kapandı → görev biter; wiki sayfasına kapanış satırı. Backlog maddeleri (auto mode, skill-as-verifier, ikinci-ajan review…) yalnız tetikleyicileri gerçekleşince ya da sen açıkça çekince açılır — kural değişmedi.
**DONE:** Wiki'de kapanış satırı + backlog işaret edildi.

## 4 · Roller

Salih: CC tarafındaki tüm koşular (`/goal`, `/loop`, `/schedule`) + wiki dolgusu + Faz 0 anlatımı. Cowork: plan/iskelet, kaynak doğrulama, anlama kontrolü, bu dosyanın bakımı. (07-02 rol tanımıyla aynı.)

## 5 · Kaynaklar

- Resmi yazı (ana kaynak): https://claude.com/blog/getting-started-with-loops
- X duyurusu: https://x.com/ClaudeDevs/status/2074208949205881033
- Resmi docs: https://code.claude.com/docs/en/goal · https://code.claude.com/docs/en/routines · https://code.claude.com/docs/en/workflows · https://code.claude.com/docs/en/agents
- Bağlam (ismin kökeni): Addy Osmani "Loop Engineering" (Haziran 2026) — https://addyosmani.com/blog/loop-engineering/ · The New Stack, Boris Cherny röportajı — https://thenewstack.io/loop-engineering/
