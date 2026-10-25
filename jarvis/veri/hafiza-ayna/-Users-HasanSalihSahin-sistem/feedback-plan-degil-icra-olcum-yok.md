---
name: feedback-plan-degil-icra-olcum-yok
description: "Salih 10-25 (Karar 123): söylenen değişiklik plan taslağı, pilot ya da \"N seans ölçüm\" kapısı beklemeden sisteme uygulanır; hata sonradan ayıklanır"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8899f41a-eb35-41bf-9949-0d3afed800f9
  modified: 2026-10-25T18:09:58.082Z
---

Salih 2026-10-25, aynen: "sana plan taslak yapmanı söylemedim direk söylediğimi sisteme implement etmeni istedim … plan yapma alışkanlığını icraya çevirme alışkanlığına çeviriyoruz … bundan sonra bir değişiklik için önce ölçüm yapılmayacak". Kayıt: kök `AGENTS.md` md.13 + `jarvis/kuyruk/senaryo-defteri.md` Karar 123.

**Why:** ölçüm/pilot kapısı işi geciktiriyor; model hatayı sonradan görüp ayıklayabilir (Karar 115 önce-test kaldırmasıyla aynı aile).

**How to apply:** "geri-açma: N seansta ölçülür", "pilot sonra genelleştir", "önce dene" türü şartlar yazılmaz; planlanmış revizyon listesi bekletilmez, aynı seansta icraya alınır; sapma çıkarsa `[ariza]` commit'iyle düzeltilir. İlgili: [[feedback-icra-listesi-onaysiz-devam]].
