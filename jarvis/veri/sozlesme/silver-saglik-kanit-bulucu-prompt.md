# silver-sağlık T-A — LLM KANIT-BULUCU prompt şablonu (KB-41 (a); Karar 58, 2026-08-21)

*Bu şablon `tools/silver-saglik.py`'nin ürettiği `silver_karantina_aday` çiftleri için kullanılır. Koşucu = alt model (KB-03 hiyerarşisi), çağrıyı script YAPMAZ (deterministik tasarım; LLM maliyeti Salih tetiğinde). LLM HÜKÜM VERMEZ — yalnız çelişen cümle çiftini GÖSTERİR (ContraDoc: ikili yargı %50-54 ≈ rastlantı; kanıt-bulma %70-93). Çıktı `silver_karantina` kuyruğuna (tespit damgalı) → Salih triyajı. İlk 10 koşum insan-etiketli kalibrasyon (precision ölçülmemiş — A hakem kör).*

## Çağrı (çift başına; girdi = iki silver kaydı, metin + künye)

```
GÖREV: Aşağıdaki iki kayıt aynı anahtar terime ({anahtar_terim}) değinir ve Jarvis kanonunun SICAK katmanındadır.
Yalnız ŞUNU yap: iki metinde BİRBİRİYLE BAĞDAŞMAYAN (aynı şey hakkında farklı değer/kural/tarih söyleyen) cümle çifti varsa,
o cümleleri AYNEN alıntıla. Yorum yapma, hangisinin doğru olduğuna karar verme, özetleme.
Bağdaşmayan çift bulamıyorsan tek satır yaz: YOK.

KAYIT A — {dosya_a}:{satir_bas_a}-{satir_son_a} (kayit_id {kayit_id_a}, son commit {son_commit_a})
<<<
{metin_a}
>>>

KAYIT B — {dosya_b}:{satir_bas_b}-{satir_son_b} (kayit_id {kayit_id_b}, son commit {son_commit_b})
<<<
{metin_b}
>>>

ÇIKTI BİÇİMİ (başka hiçbir şey yazma):
A: "<A'dan aynen cümle>"
B: "<B'den aynen cümle>"
KONU: <tek kelime/öbek — hangi değer/kural çatışıyor>
```

## Sonucun kuyruğa yazımı (script dışı; koşucu)
`veri/silver-kuyruk.jsonl`'e olay: `{"olay":"ACILDI","tip":"T-A-KANIT","hedef_tur":"kayit_cifti","hedef_id":"<kayit_id_a>|<kayit_id_b>","neden":"<KONU>","kanit_a":"…","kanit_b":"…","model":"<alt model>","ts":…}` — LLM'in YOK dediği çiftler yazılmaz (yalnızca sayılır: koşum kütüğüne `T-A-KANIT yok=n`). Triyaj hükmü Salih'in; kapanış olayı `KAPANDI` + gerekçe.

## Kalibrasyon kütüğü (ilk 10 koşum)
Her koşumda: çift sayısı · LLM "kanıt var" sayısı · Salih'in "gerçek çelişki" dediği sayı → precision = gerçek / kanıt-var. 10 koşum sonra ön-eleme sinyal regex'i ve `min_uzunluk` eşiği bu sayıyla kalibre edilir (`veri/sozlesme/silver-saglik-kurallar.json` `on_eleme`).
