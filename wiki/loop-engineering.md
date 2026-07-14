> **TAŞINDI (2026-07-15, Salih icra emri):** Homebase'ten JARVIS'e — köken: `Cowork Homebase/[C] Loop Engineering.md`; tespit raporu: `raporlar/homebase-tasima-tespiti-2026-07-15.md`. Orijinal Homebase'te arşiv-pointer'la durur (m.8).

---
author: claude
type: wiki
date: 2026-07-10
---

# Loop Engineering — Wiki

> **Tek cümle:** Loop engineering, promptu her seferinde senin yazman yerine, işin hangi parçasını sisteme devrettiğini tasarlamaktır. Resmi tanım: *loop = bir durma koşulu sağlanana dek iş çevrimini tekrarlayan ajan.*
> **Kaynak:** Claude Code ekibi, "Getting started with loops" (claude.com/blog, 30.06.2026) — TR transkript: `[C] Looplara Baslangic — Blog Transkripti (TR).md`. Faz 0 kapanışı: 2026-07-10 (`[C] Loop Engineering — Yol Haritası.md`).

## 1 · Dört tip — mekanizmayla

| Tip | Tetikleyen | Durduran | Devrettiğin | Araç |
|---|---|---|---|---|
| **Tur-tabanlı** | SEN (her prompt) | Claude'un "bitti" kanaati | Yalnız kontrol adımı | Doğrulama skill'i |
| **Hedef-tabanlı** | SEN (canlı prompt) | Senin yazdığın koşul (evaluator bakar) VEYA tur limiti | Durma koşulunu | `/goal` |
| **Zaman-tabanlı** | Zaman aralığı (kural) | Sen iptal edersin / iş biter | Tetikleyiciyi | `/loop` (lokal) · `/schedule` (bulut) |
| **Proaktif** | Olay/takvim, insansız | Görev hedefte biter; rutin sen kapatana dek | Promptun kendisini | Hepsi + auto mode + workflows |

Merdiven yukarı çıktıkça döngünün bir parçası daha senden koda geçer: kontrol → durma koşulu → tetikleyici → prompt.

**Kritik ayrım (Faz 0 düzeltmesi):** "Her tipte tetikleyici kuraldır" YANLIŞ — tur ve hedef tabanlıda tetikleyici hâlâ sensin; kurala bağlanan şey hedef-tabanlıda bitiş, zaman-tabanlıda başlangıç, proaktifte ikisi birden.

**Evaluator ilkesi (düzeltilmiş, 07-07):** `/goal`'daki değerlendirici model koşulu her turda DEĞİL, yalnız **Claude durmayı denediğinde** kontrol eder — sağlanmadıysa işe geri yollar. Tur limiti şart ("5 denemede dur"), yoksa açık çek.

## 2 · Karar kuralları (Salih formülasyonları, Faz 0)

- **Sıfırıncı kural: çoğu iş loop istemez.** Tek promptluk işe /goal kurmak token israfı, /schedule kurmak absürt. Örnek: "CSV'de 15 ağırlığın toplamını 1.00 yap" → tur-tabanlı, ucuz model, tek atım.
- **B-koşulu (Salih, 07-10): iterasyon gerekli + done yazılabilir = /goal.** İkisi birden şart: zor ama done'ı yazılamayan iş ("tezi daha ikna edici yap") /goal'a giremez — evaluator neye bakacak? O iş tur-tabanlı kalır, hakem sensin.
- **Done ne kadar nicel, öz-doğrulama o kadar kolay:** geçen test sayısı, skor eşiği, script PASS/FAIL. "pytest yeşil" = nesnel bitti-sinyali.
- **Zaman-tabanlıda aralık = izlenen şeyin gerçek değişim hızı.** Daha sık koşturmak sadece token yakar.
- **Model boyutu:** rutine küçük/hızlı model, yargı gerektiren karara en yetenekli model (resmi tavsiye). Jarvis bağlantısı: havuz #14 routing · #24 loop-model rasyosu · #25 gece vardiyasının teknik zemini = /schedule + auto mode.

## 3 · Kalite + token (özet)

Tek hatayı düzeltme, o hatayı yakalayacak kuralı skill'e göm (sonraki bütün turlar kazanır). Review'u taze bağlamlı ikinci ajana yaptır. Büyük koşudan önce küçük dilimde pilot. Deterministik iş için script (her seferinde akıl yürütmekten ucuz). İzleme: `/usage`, argümansız `/goal`, `/workflows`.

## 4 · Salih'in eşleştirmeleri (Faz 0)

- **Transkript hattı** (kontrol→indir→transkribe→RAG→özet) → **proaktif**: takvimle gelir, done deterministik, prompt sabit-girdiler değişken. (Faz 4'ün hedefi.)
- **CSV ağırlık düzeltme** → **tur-tabanlı**: tek promptluk iş, loop kurmaya değmez.
- Sıradaki gerçek koşu (Faz 2 adayı): PortRisk Sprint 1 — `/goal pytest yeşil, 10 turda dur` (ön-koşul: `python --version`).

## 5 · Kaynaklar + backlog

- Resmi yazı: https://claude.com/blog/getting-started-with-loops
- Resmi docs: https://code.claude.com/docs/en/goal · /routines · /workflows · /agents
- İsmin kökeni: Addy Osmani, "Loop Engineering" (06.2026) — https://addyosmani.com/blog/loop-engineering/ · The New Stack (Boris Cherny): https://thenewstack.io/loop-engineering/
- **Backlog:** `[C] Loop Engineering — Sonrası.md` — 8 bekleyen madde (auto mode, skill-as-verifier, ikinci-ajan review, ultraplan, dispatch, bağlam hijyeni, paralel çalışma, Jarvis desenleri); 3 aktif madde (Faz 1/2/4) kapanmadan hiçbiri açılmaz, hatırlatma yalnız tetikleyici bağlamda.
