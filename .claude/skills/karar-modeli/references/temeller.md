# Matematiksel Tabanlar Kataloğu (karar-modeli kat-3 referansı)

*Her koşumda 3 FARKLI taban seçilir; ≥1'i önerinin varsayımına zıt kutuptan (karşıt-temel garantisi). Zıt-çiftler tabloda eşleşik verilmiştir.*

| Taban | Tek-satır özü | Zıt kutbu |
|---|---|---|
| Beklenen-değer (EV) | olasılık×getiri toplamını maksimize et | Minimax |
| Minimax / en-kötü-durum | en kötü senaryonun zararını minimize et | Beklenen-değer |
| Bayesçi güncelleme | önsel + veri → sonsal; belirsizlik dağılımla taşınır | Frekansçı eşik |
| Frekansçı eşik/test | karar sabit hata-oranı eşiğiyle verilir | Bayesçi |
| Keşif (exploration) | bilgi değeri için varyansa yatır (bandit/TS) | Sömürü |
| Sömürü (exploitation) | bilinen en iyi kola yatır | Keşif |
| Birikimli-delta | küçük geri-alınabilir adımlar, her adım ölçülür | Topyekûn-optimizasyon |
| Topyekûn-optimizasyon / MDL | global yeniden-tasarım, sıkıştırma optimumu | Birikimli-delta |
| Reel-opsiyon | beklemenin opsiyon değeri var; erken kilitlenme maliyet | Şimdi-kilitle (commitment) |
| Şimdi-kilitle | erken taahhüt koordinasyon/odak getirisi sağlar | Reel-opsiyon |
| Kuyruk/darboğaz (queueing) | sistemin hızını darboğaz belirler; oraya yatır | Yerel-verim |
| Pareto/çok-amaç | eksenler indirgenmez; baskın olmayan küme sunulur | Tek-amaç skalarlaştırma |

Kullanım: taban adını modele yaz ("Model B — minimax zemini: ..."); katalog dışı taban serbest ama tek-satır tanımla.
