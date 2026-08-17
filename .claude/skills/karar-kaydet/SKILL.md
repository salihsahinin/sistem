---
name: karar-kaydet
disable-model-invocation: true
description: Verilmiş bir kararı senaryo-defterine standart blokla yazar ve ayrı commit atar (S-J; karar-hatti tamamlayıcısı). YALNIZ elle tetik; Salih ya da seans akışı "kararı kaydet / deftere işle" dediğinde. KULLANILMAZ; karar ÜRETMEK için (karar-modeli/karar-hatti işi), rutin seans-ingest'inde (seans-kapanis kendi yazar) ve model kendi inisiyatifiyle (yan-etki freni — elle tetik esastır).
---

# Karar kaydet (S-J, v1 — 2026-08-14; yan-etki ayrıştırması: yazım+commit tek yerde)

Kural kaynağı: m.37 kayıt şartı + m.10/V5 commit disiplini + ingest şeması (zarf + bi-temporal) + LangMem episodik format (durum+akıl-yürütme+sonuç).

## Adımlar
1. **Blok yaz** (`kuyruk/senaryo-defteri.md` sonuna, tarih-başlıklı):
   - `[tip: karar | kaynak: <yüzey+hat> | tarih: | hedef: defter | sema: v2]` zarfı
   - **Durum** (hangi bağlamda doğdu) · **Akıl-yürütme** (seçenekler + gerekçe; m.37 ölçek-eşiği üstündeyse model kıyası) · **Hüküm** (ne kararlaştırıldı) · **Yetki** (Katman-1 Salih-imzalı / Katman-2 Carvis, veto-açık) · **Geri-açma koşulu** · `gecerli-baslangic:`.
2. **Çelişki denetimi:** karar eski bir kaydı geçersiz kılıyorsa eskiye `gecerli-bitis: <bu kararın tarihi>` damgası (SİLME yok); Katman-1 sınıfı çelişkiyse önce m.16 raporu.
3. **Boyut kontrolü:** defter FLAG'deyse (48KB) kaydı yine yaz ama teslim raporuna "boyut-tetiği: defter" satırı düş.
4. **Commit:** karar başına AYRI commit, İngilizce mesaj, `[icra]`/`[damıtma]` etiketi. Push yetki durumuna tabidir (serbest beyanı yoksa sor).

**Karar-borcu bağı (KB-07, Salih 08-17):** kaydedilen karar `veri/karar-borcu.jsonl`'daki bir açık kalemi kapatıyorsa aynı adımda o satır `durum: kapandı` + `kapanis_kaniti` (defter pointer'ı) alır; `python3 tools/karar-borcu-tablo.py` kırık-pointer 0 vermeli. Yeni açık karar doğduysa listeye satır düşer (grain: 1 satır = 1 açık kalem).

## Gotchas
- **Sahte imza:** Katman-1 kararı Salih imzası olmadan "İMZALI" yazma — imzasızsa "ADAY/İMZASIZ" damgası.
- **Övgü yok:** hüküm bölümü çıplak veridir (m.7).
- **Toplu kayıt tuzağı:** iki karar tek blokta/tek commit'te birleştirilmez.
