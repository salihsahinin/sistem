# AI2AI Rapor Formatı (L2 Register)

**Üst blok:** Ajandan-ajana (işçi→lider→Jarvis) rapor ve emirlerin biçim standardını TEK yerde toplayan derleyici sayfa. Durum: **GÜNCEL** · yazım: 2026-08-21 (Karar 54e — Salih şartı: "elimizde ai2ai formatın nasıl olduğunu anlatan bir dökümantasyon bulunmalı"; kutu kalemi RET/kapandı çünkü kurallar zaten kanondaydı — bu sayfa YENİ KURAL KOYMAZ, dağınık kuralları adresler). Kaynaklar: tüzük m.38 ek fıkra (rapor-dili paketi md.19-25) · m.46 (koşum-emri bütünlük paketi) · `core/sablonlar/gorev-{emri,raporu,fonksiyonu}.md` · `core/ingest-semasi.md` §5 · [[uc-register]]. Güven: **yüksek** (tümü imzalı kanon; sayfa yalnız derler).

## Çekirdek
AI2AI = üç register'ın L2'si ([[uc-register]]): hedef okuyucu MODEL olduğundan biçim süsleme değil YAPI taşır — önerme-yapılı, m.38 bağlaç setiyle (∧ ∨ ¬ → ↔). Altı bileşen:

1. **Künye + bant-dışı doğrulama (m.46a):** her koşum promptu emrin kanonik adresini (dal · yol) + commit SHA'sını taşır; koşucunun İLK adımı emri okuyup künyeyi rapora yazmak — SHA uyuşmazsa DUR + arıza bildirimi. SHA aynı zamanda emrin SÜRÜM damgasıdır (dosya değişir → SHA değişir; Karar 54c bu yüzden ayrı sürüm alanını RET'ledi). Künye alanı şablonun SONUNDA durur (cache; m.46(a) konum şerhi 08-20).
2. **Notasyon (md.19):** niceleyici ayrımı zorunlu (her=∀ / bazı=∃) · `[ARANAMADI]` ≠ "bulunamadı" (arama hiç yapılamadı ↔ arandı-yok) · olumsuz uçta sayısal çapa karar ağırlığı taşımaz · kapsam AI2AI raporlarını da İÇERİR.
3. **Niteleyici-taşıma (md.20):** özet GÖVDEDEN türetilir, elle yazılmaz; kanıt-türü/örneklem/kapsam niteleyicilerini taşımayan özet EKSİK maddedir.
4. **Damga disiplini:** her iddia D/K/X + URL (m.39); künye yalnız arama-özetinden geldiyse `[K]` zorunlu, `[D-belge]` yalnız birincil metne inilmişse (m.46b); çıplak yüzde yasak — şans düzeltmesi/taban eklenir (md.25).
5. **Dönüş zarfı (ingest-şeması §5):** işçi dönüşü ≈1-2k token özet + pointer (5-alan zarf); aşamalar arası HAM KANIT geçer, türetilmiş yargı geçmez (m.40b hakemlik kuralı).
6. **done-yüklemi (K2-c):** boolean tamam-koşulu; derece ifadesi yasak; teslimde emirdeki her koşul tek tek işaretlenir (DRFR — metodoloji §1).

## SOP — ai2ai çıktı üretirken
1. Şablonu al: emir → `gorev-emri.md` · rapor → `gorev-raporu.md` · görev tanımı → `gorev-fonksiyonu.md` (hepsi `core/sablonlar/`).
2. Blok sırası SABİT: statik önek önde, tarih/SHA/tetikleyen-mesaj EN SONDA (cache — metodoloji §2 sıra kuralı).
3. Kenar makine-tüketicili ise şemalı biçim (JSON/JSONL); Salih okuyacaksa L1 kuralları ezer ([[uc-register]] kenar-başına-biçim ilkesi).

## Gotchas
- **Format-tax:** her şeyi şemaya çevirmek kazanç değil — kazanç YAPIDAN gelir; B2/B3 meşru duraklardır (metodoloji §3).
- Eski "ai2ai format standardı" kutu kalemleri md.38 paketiyle karşılandı (EK-6 küme ② kapanış gerekçesi; Karar 54e) — yeni format kuralı önermeden önce bu sayfa + tüzük okunur.
- Bu sayfa derleyicidir; çelişkide tüzük kazanır.

## Bağlantılar
[[uc-register]] · [[ingest-semasi]] · [[adversarial-hayatta-kalma]] · [[pointer-sistemi]]

**Bağlantılar:** · [[dil-secimi]] (karşı-link 08-26) · [[ajan-metodolojisi]] (karşı-link 09-03)
