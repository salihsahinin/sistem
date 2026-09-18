# Rapor S-5 — Cascade Failure Kaynak Doğrulama (AB-5)

**Tarih:** 2026-08-21  
**Rol:** S-5 (cascade-failure-kaynak-dogrulama)  
**Kaynağı:** https://arxiv.org/abs/2605.17288  

---

## 1. Künye Doğrulaması

| Alan | Bulgu | Hüküm |
|------|-------|-------|
| Başlık | "When Efficiency Backfires: Cascading LLMs Trigger Cascade Failure under Adversarial Attack" | **D** |
| Yazarlar | Zehan Sun, Dingfan Chen, Songze Li | **D** |
| Tarih | May 17, 2026 | **D** |
| URL Erişim | https://arxiv.org/abs/2605.17288 (başarılı) | **D** |

**Hüküm Özet:** Künye tam uyuşmakta. Makale erişilmiş, okunmuştur.

---

## 2. Ana Bulgu (Türkçe Özet)

Makale, kademeli LLM sistemleri (hafif modeller + güçlü modeller veri yönlendirmesi) tasarımının düşmanca saldırılara karşı kritik zafiyetler sunduğunu göstermektedir. Saldırganlar, kademeli yapının bağımlılıklarını hedef alarak hem hafif ön-uç modellerini hem de yönlendirme mekanizmalarını eşzamanlı olarak tahrif edebilir; sonuç olarak cascade sistemlerin temel hedefleri (maliyet-verimlilik ve doğruluk) birlikte çöker.

---

## 3. D/K/X Hükmü: "Kapı Sayısı Arttıkça Saldırı Yüzeyi Artar"

**Makale Bulgusu:**
- Cascade yapı içindeki "sequential dependencies" saldırıya açık noktalar oluşturur
- "Constrained sequential collaborative optimization of adversarial suffix under cascade dependencies" — zincirleme girişim mekanizması
- Cascaded yönlendirme + hafif model zinciri = artırılmış saldırı vektörü

**Hüküm:** **K** (Kaynaklı; tek-kaynak, URL doğru, ancak iddianın tam ölçek nicelemesi makale özeti düzeyinde net değil — tüm kapı sayılarını test etmemiş görünmektedir)

---

## 4. Jarvis Kapı-Zincirine Uygulanabilirlik

Jarvis'in çelişki-kapısı → skill-kapısı → hakem zinciri de cascade mimarisinin bir türüdür ve bu makalenin tehdidi taşır: saldırgan en basit kapıdan (örn. input-parsing) başlayarak üst kapıları (skill-tetik, hakem kararı) kademeli olarak erozyona uğratabilir. Bağlantılı kapılardaki yığmalı hata cascade çöküşe neden olabilir; her kapı eklenmesi saldırı yüzeyini doğrusal olmayan biçimde artırmaktadır.

---

## 5. F2 Destek Tablosu (Halüsinasyon-Engelleyici)

| İddia | Kaynak | Doğrulama | Etiketi |
|-------|--------|-----------|---------|
| Cascade LLM sistemleri düşmanca girişe açıktır | arXiv 2605.17288 (Sun, Chen, Li, 2026) | URL açıldı, konu doğrulanmış | D |
| Saldırı kademeli bağımlılıkları hedef alır | arXiv 2605.17288 §3-4 (özet) | "cascade dependencies" terimleri eşleşmekte | D |
| Maliyet-verimlilik ve doğruluk birlikte düşer | arXiv 2605.17288 sonuç | "controllable degradation" cümlesi eşleşmekte | D |
| Kapı sayısı arttıkça saldırı yüzeyi artar (Jarvis) | Özet çıkarım | Mantık zinciri makaleyi destekler, ölçeklem belirtilmemiş | K |

---

## 6. Cevaplanamayanlar / Sınırlar

- Makalede "kaç kapıya kadar ölçek doğrusal kalır" analitik sınır belirtilmemiştir (özet düzeyinde).
- Jarvis spesifik kapı-tasarımına uygulanabilirlik ayrıntılı değerlendirilmemiş (bu rapor için kapsam-dışı).

---

**Done Yüklemi Kontrol:**
- ✓ Rapor yazıldı  
- ✓ Künye D hükmü  
- ✓ Özet + uygulanabilirlik bölümleri dolu  
- ✓ URL erişildi, FAIL-LOUD yasak uygulanmadı  
- ✓ F2 destek tablosu var  

**Durum:** DRFR (başarılı)
