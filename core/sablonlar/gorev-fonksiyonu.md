# Görev-Fonksiyonu Şablonu v1 (2026-08-14, deneysel m.29)

*Her ajan görev-emri bu iskeletle yazılır (S-K temeli). Kural kaynağı: `core/ajan-metodolojisi.md`. İlke: alan adı talimattır — adları görevin kendi dilinden seç. Blok SIRASI sabittir (cache): statik önce, dinamik en sonda.*

```
## KİMLİK (statik — değişmez blok)
gorev_adi:        <tek isim>
rol:              lider | işçi | scout (rapor) | ship (değişiklik)
cagri_kosulu:     <tek cümle: bu görev NE ZAMAN çağrılır — lider yalnız bunu okur>
rejim:            kalite-öncelikli | maliyet-öncelikli
model:            <liderden pahalı OLAMAZ>

## GİRDİLER (tipli; "alan adı talimattır")
<girdi_adi>: <tip>        # ör. arastirma_sorusu: metin · hedef_dosya: yol

## BAĞLAM-MANİFESTİ (hafıza-as-import)
eager:            <her zaman yüklü — KÜÇÜK tut>
lazy:             <ad + ne-zaman-okunur künyesi; gövde yalnız tetiklenince>
butce:            ~<token tavanı>

## SINIRLAR (delegasyon dörtlüsünün 4.'sü — ZORUNLU)
kapsamda:         <ne yapılacak>
kapsam_disi:      <sana ait OLMAYAN — iş-tekrarı/boşluk freni>
araclar:          <pozitif liste + kaynak kılavuzu>
degismezler:      <koşum boyunca ihlal edilemeyecekler>

## DALLAR (numaralı; m.38 bağlaçları; dal+koşul toplamı ≤5 — aşarsa BÖL)
D1: eğer <koşul> → <eylem>
D2: aksi → <eylem>
D-KATMAN1: <Salih kararı gerektiren durum> → DUR + sor

## ÇIKTI SÖZLEŞMESİ
halusinasyon_derecesi: <H = Σ wᵢ·vᵢ (core/halusinasyon-paketi.md §2; scripts/derece.py) · aktif v'ler · eşik 7 (4 pahalı-geri-alma) · H ≥ eşik ∨ atıf-türü ⇒ SKILL TETİKLERİ'ne halusinasyon-engelleyici eklenir>
cikti_bicimi:     <dosya/rapor/karar-bloğu; işçi dönüşü ≈1-2k token özet>
done_yuklemi:     <boolean değerlendirilebilir; derece ifadesi YASAK>
done_olcumu:      DRFR — emirdeki her koşul tek tek karşılandı/karşılanmadı
yeniden_deneme:   3

## SKILL TETİKLERİ (tetiklenme şeması v1 — `core/skill-tetikleme-semasi.md`; emirde skill çağrılıyorsa ZORUNLU, çağrı başına bir blok; yoksa "yok")
- skill:              <hazinede VAR ∧ kapı-ağacından geçmiş ad>
  tetik_kosulu:       <m.38 boolean; iç içe ≤2; negatif de: "Z ise ÇAĞIRMA">
  cagri_kipi:         literal | ortuk | yasak      # T-Y (yan-etkili) → yalnız literal ∧ ana-sıra; alt-ajandan YASAK
  girdi:              <tipli argümanlar — TAM; eksikle başlatma yasak>
  baglam:             <hedef · çıktı-formatı+bütçe · araç/kaynak · sınırlar; iddia≠gerekçe; fork ise geçmişsiz>
  yan_etki_damgasi:   salt-okur | eklemeli | yıkıcı  × idempotent:e/h × dış-dünya:e/h   # kayıt alanı, yetki değil
  done_yuklemi:       <boolean; çıktı-şeması varsa çağıran doğrular>
  hata_yolu:          sözleşme-ihlali → çağıran düzeltir · yürütme → telafi · retry ≤3 · FAIL-LOUD
  sira:               <n/N · handoff kontratı (dosya/format) · paralel↔seri gerekçesi>
  kayit:              execute_tool · tool.name=<skill> · agent · error.type · model+sürüm · tarih → skill sayacı

## DİNAMİK EK (EN SONDA — cache'i kırmasın)
tarih / SHA / tetikleyen mesaj / koşuma özel veri
```

**Kullanım notları:** (1) Büyük iş = küçük fonksiyonların ZİNCİRİ; tek dev fonksiyon yazma. (2) Paralel dağıtımdan önce zorunlu soru: alt-görevler bağımsız bilgi mi topluyor, ortak çıktı mı üretiyor? Ortak-üretim → tek şerit ya da paylaşılan karar-manifesti. (3) Teslim, ingest şeması zarfıyla döner (`core/ingest-semasi.md`).
