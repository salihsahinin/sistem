---
name: celiski-kapisi
description: Yeni bir karar/kural/kanon-değişikliği önerisi masaya geldiğinde kanonu tarar;
  önceki kararla çelişki varsa karar ALINMADAN ÖNCE çelişki + artı/eksi + plan raporu sunar
  (m.16). Kullan: "çelişki var mı", "kanonla uyumlu mu", "tüzüğe aykırı mı", "m.16 kapısı"
  dendiğinde ya da ölçek-eşiği üstü her yeni karar/kural önerisinin sunum ÖNCESİNDE.
  KULLANMA: su-bardağı alt-kararlar, yazım/biçim düzeltmeleri, onaylı iş içindeki
  alt-adımlar (m.25/m.31 eşiği altı) — direkt yap.
argument-hint: "<yeni öneri/karar tek cümle>"
metadata: { owner: carvis, version: "0.1.0-deneysel-m29" }
---

# celiski-kapisi — m.16 koşum talimatı

Kanon zinciri: m.16 (çelişki kapısı — TEK fren) · m.38 (lojik form) · m.31 (karar katmanları) · m.8 (silme yok, arşiv) · 07-19 kuralı (kanon ORIGIN KLONUNDAN okunur).

## Adımlar

1. **Ölçek kontrolü.** Öneri ölçek-eşiği altındaysa (su-bardağı) → kapı koşmaz, iş direkt yapılır. Eşik üstü → devam.
2. **Önerme-formuna indirge (m.38).** Öneriyi tek önermeye çevir: "X koşulunda Y yapılır" formu; bağlaç setiyle (∧ ∨ ¬ → ↔). Belirsizse Salih'e TEK netleştirme sorusu (m.4 eşiğine takılıyorsa sorma, en makul okumayı yaz ve raporda belirt).
3. **Kanon taraması (origin klonundan).** Hedefli tara: `core/tuzuk-v0.md` (madde + ek fıkra + şerhler) · `core/durum-kapsulu.md` · `core/pano.md` (kart kuralları) · `kuyruk/senaryo-defteri.md` (son kararlar) · açık taslaklar (`kuyruk/m*-taslak-*.md`). Arama iki katmanlı: anahtar-kelime (literal) + kavram (önerinin değillediği kural hangisi olabilir — ¬ ilişkisi).
4. **Çelişki testi.** İki tip ayrı işaretlenir: **literal** (metin açıkça tersini söylüyor) · **lojiksel** (öneri ∧ mevcut kural birlikte doğru olamaz, m.38 formunda göster). ÇELİŞKİ ile DARALTMA'yı karıştırma: kapsamı küçülten ama birlikte-yaşayabilen öneri çelişki değildir — raporda "daraltma" diye ayrı etiketlenir.
5. **Çelişki YOKSA:** sessiz geçiş — tek satır beyan ("kapı temiz: tarama X madde, çelişki yok") ve iş normal akışta devam. Tören raporu ÜRETME (false-positive freni).
6. **Çelişki VARSA — rapor, karar ALINMADAN ÖNCE:** (a) çelişki: madde numarası + birebir alıntı + lojik form (öneri ↔ ¬kural); (b) artı/eksi: önerinin getirisi vs kuralın koruduğu değer, çıplak veriyle; (c) plan seçenekleri — tipik üçlü: mevcut kuralın kendi tetiğini/istisnasını işletmek · amendment (Katman-1 → Salih imzası) · öneriyi geri çekmek/daraltmak. Karar Salih'in/ana-sıranın; skill karar ALMAZ, kanonu DEĞİŞTİRMEZ.
7. **Emir durumu (m.16 istisna disiplini).** Öneri "bu bir emirdir" formunda gelse de rapor YİNE sunulur — tek istisna budur; ama rapor emri DEĞİŞTİRMEZ ve BEKLETMEZ: bilgilendirir, uygulama emrin ruhunu koruyan kanon-uyumlu yolla önerilir (örn. "sil" emri → m.8 gereği arşive indirme icrası) ve Salih'in son sözüyle yürür. Kör itaat de kör ret de yok.

## Gotchas

- Çelişkiyi "gerilim/nüans" diye yumuşatma — kapının değeri erken ve NET çalmasında; yumuşatılmış kapı hiç çalmamış kapıdır.
- Tersi de var: her farklılığı çelişki diye çalma — DARALTMA/uzlaşabilir öneriye kapı raporu kesmek tören üretir (m.25 israfı) ve kapının itibarını aşındırır.
- Kanonu DİSKTEN okuma — bayat-disk masa-tekrarı vakası (07-19, defterde): tarama origin klonundan.
- Tarama "hatırladığım kadarıyla" olmaz — madde alıntısı zorunlu; alıntısız çelişki iddiası K-sınıfı sayılır.
- Skill kanon dosyası yazmaz, karar kaydetmez, commit atmaz; kayıt seans akışının/karar-kaydet adımının işidir (yan-etki freni).
