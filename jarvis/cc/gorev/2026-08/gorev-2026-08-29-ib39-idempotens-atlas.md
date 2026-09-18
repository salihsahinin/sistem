# Görev Emri — İB-39: İdempotens sistematik entegrasyonu atlası (Salih 08-20 KB-18 eki)

*Derleyen: Carvis ana-sıra (Fable), 2026-08-29 icra devam oturumu. Tetik: ledger İB-39 (icra-sırada; "araştırma emri"). Koşum-önü kapı: bu emir HAZIRLANDI, atlas KOŞULMADI — paralel oturumda İB-63 atlası SAHADA (08-29 19:xx), ardışık koşum kuralı (vaka-3 çift-koşum dersi). Koşum tetiği: Salih ∨ İB-63 kapanışı.*

- **Görev / hedef:** Jarvis'te "yeniden koşum güvenliği" = idempotens (f(f(x))=f(x)) için (1) dış literatür/pratik emsalleri, (2) araç emsalleri, (3) iç envanterin (C ailesi, HAZIR: `raporlar/2026-08-29-ib39-ic-envanter.md`) boşluklarını çıkarıp ENTEGRASYON TASARIMI önermek: hangi script/skill/ritüel yeniden koşulduğunda ne olur, hangi mekanizma (tekil anahtar · idempotency-key · temp→rename · rebuild) standart olur (AXI-STANDARDI A4 satırı buna bağlanır).
- **Kavram ayrımı (emre gömülü):** Salih'in KB-18 tanımı (aynı girdi→aynı çıktı) = DETERMİNİZM (Karar 65); idempotens = tekrar-uygulama sonucu değiştirmez. İkisi kardeş hedef ("deterministik ve idempotent sistem", Salih 08-20). Kısmi ön-iz: 07-26 U10/L17 (Temporal), hüküm yok — sıfırdan değil üstüne (hazırı temel al).
- **Aileler (dik):** **A — formal/protokol:** HTTP Idempotency-Key (IETF draft — 07-26 C7'de ARANAMADI; canlı çek, AS-OF damgalı), exactly-once ↔ at-least-once + dedup, idempotent consumer deseni, veri hattı idempotensi (dbt incremental/merge, Airflow idempotent task, "rebuild from bronze" ilkesi). **B — araç emsalleri:** Temporal (activity idempotency, workflow determinism constraint), Stripe idempotency keys, Kafka EOS, Make/Bazel/Nix content-addressed yeniden-üretim, Claude Code Workflow resume cache (`resumeFromRunId`: aynı (prompt, opts) → önbellek). **C — iç envanter (web gerekmez):** hazır tablo + 4 soru (envanter raporu "Okuma") → ajan her scripti sınıflandırır: idempotent-by-rebuild · append+tekil-anahtar · append-çoğalan (bilinçli koşum kütüğü mü?) · atomik-olmayan yazım.
- **İzinli aksiyonlar:** WebFetch/WebSearch (A/B), Read/Grep (C), rapor yazımı. **Yasaklar:** kod değiştirme · kanon yazımı · LLM ile "idempotent mi" hükmü (C'de kanıt = kod satırı pointer'ı).
- **Okunacak dosyalar:** `raporlar/2026-08-29-ib39-ic-envanter.md` · `tools/AXI-STANDARDI.md` (A4) · `veri/README.md` (kayit_id_kume_sha, append-only sözleşmeleri) · `tools/katman-hatti.py` docstring · `cc/rapor-2026-07-26-SOZEL-ajan-durma.md:173` (Temporal ön-izi) · `core/skill-tetikleme-semasi.md` (yan-etki damgası: idempotent alanı).
- **Yazılabilir yüzeyler:** `cc/rapor-2026-08-29-ib39-*.md` (tez/antitez/V26/hakem) · sentez `raporlar/2026-08-29-ib39-idempotens-atlas.md`.
- **Durma koşulu (done-yüklemi):** sentez yazıldı ∧ A+B'de ≥8 birincil kaynak (AS-OF damgalı) ∧ C'de {len(rows)} script sınıflandırıldı ∧ entegrasyon tasarımı 3 seçenek (biri karşıt-temelli, m.37) ∧ karar-masası kalemi taslağı.
- **Teslim formatı:** m.40b: tez ×3 → CoVe-Factored antitez (A/B) + C için ayak-izi doğrulama → V26 kural-tabanlı örneklem → maskeli hakem → sentez D/K/X + URL; `tools/atlas-derle.py` mekanik derleme.
- **Koşucu sınıfı (#24):** işçi Sonnet 5 (bütçe 10-15, effort düşük-orta, aile 3 — Salih 08-15 −%30); hakem Opus 5; sentez Carvis.
- **Zaman bütçesi:** tek Workflow koşumu; 3 aile × (tez+antitez+V26+hakem) ≤ 12 ajan (fren UYARI 36 altı).
- **Emir konumu + erişim:** `cc/gorev-2026-08-29-ib39-idempotens-atlas.md` · main · HEAD 9c1bffe.

## SPEC / PLAN / TASKS
- **SPEC:** problem = yeniden-koşum (retry, çift oturum, bağlam-dolu kesinti sonrası devam) güvenliği yazılı standart değil; kullanıcı = Carvis + işçi ajanlar; done = yukarıdaki yüklem; kapsam dışı = kod değişikliği (ayrı İB).
- **PLAN:** A/B web + C repo; risk: A'da IETF taslağı sürüm kayması (AS-OF zorunlu) · B'de vendor-blog SEO gürültüsü (V26 birincil kaynak); ölçüm P6 dörtlüsü.
- **TASKS:** T1 tez-A · T2 tez-B · T3 tez-C (envanter sınıflandırma) · T4-T5 antitez A/B · T6 C ayak-izi doğrulama · T7-T9 V26 · T10-T12 hakem · T13 sentez (Carvis).
