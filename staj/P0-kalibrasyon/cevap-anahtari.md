# P0 — Cevap Anahtarı (TAHMİNLERİNİ YAZMADAN AÇMA)

*Tüm sonuçlar 2026-07-25 vardiyasında fiilen koşturulup doğrulandı (SQLite + pandas 2.3.3). sqlite3 CLI yoksa doğrulama: `python3 -c "import sqlite3;con=sqlite3.connect(':memory:');con.executescript(open('seed.sql').read());print(con.execute('SORGU').fetchall())"`*

## SQL

| # | Sonuç | Hata sınıfı |
|---|---|---|
| S1 | **2 satır:** (Ayse,1), (Zeynep,1) | **LEFT JOIN + WHERE** — sağ tablonun kolonuna WHERE koyunca dış birleştirme sessizce INNER'a döner; "tüm müşteriler + 0'lar" beklentisi çöker. Doğrusu: koşulu ON'a taşımak |
| S2 | **0 satır** | **NOT IN + NULL** — `sahip_id` içinde NULL var → sonuç HER ZAMAN boş. Naif cevap "Can"dı. Doğru form S8'de |
| S3 | 6 · 5 · 5 | COUNT(*) ≠ COUNT(kolon): COUNT(fiyat) NULL'u (Honda) saymaz; DISTINCT marka=5 (Toyota çift) |
| S4 | Ford 450.000 · Renault 600.000 · **Toyota 1.700.000** | **Fan-out** — arac 1'in 2 servis kaydı fiyatı iki kez topladı (gerçek: 850.000, arac 5 hiç yok). Birden-çoğa join + SUM = şişkin rakam, hata yok |
| S5 | **5** (6 değil) | NULL üç değerli mantık — `NULL<x OR NULL>=x` = unknown; Honda iki daldan da elenir. "Tümü" görünümlü koşul tümü değildir |
| S6 | 1 satır: (2, 1.980.000) | TEMİZ — tuzak yok. Her soruda tuzak arama refleksi de kalibrasyon hatasıdır |
| S7 | 2 | Tarih sınırı — string DATE'te BETWEEN uç günü kapsar; kolon timestamp olsaydı '2026-06-30 14:00' sessizce dışarıda kalırdı. Güvenli kalıp: `>= başlangıç AND < ertesi-gün` |
| S8 | Can | TEMİZ — doğru anti-join (`LEFT JOIN … IS NULL`), S2'nin NULL-güvenli hali. `NOT EXISTS` de güvenli |
| S9 | satir=4 · tekil=3 | Fan-out teşhis tekniği — COUNT vs COUNT(DISTINCT) farkı çoğaltmayı ele verir (arac 1 iki kez) |
| S10 | **2 satır:** Ayse, Zeynep | NULL + NOT — Mehmet'in şehri NULL → `NOT(unknown)=unknown`, elenir. "Ankara olmayan herkes" Mehmet'i İÇERMEZ |

**Sessiz-katil sınıfı sorular (P1 sınavının 6/6 kuralına denk gelenler): S1, S2, S4, S5, S7, S10.**

## Python

| # | Sonuç | Hata sınıfı |
|---|---|---|
| PY1 | **4** | Merge fan-out — inner merge; arac 1 iki servis satırıyla çoğalır, arac 2/5/6 düşer. Refleks: merge sonrası `len` + `validate=` |
| PY2 | Ankara 3 · Istanbul 1 · Izmir 1 → **toplam 5 ≠ 6** | groupby NaN anahtarı sessizce düşürür (`dropna=True` varsayılan). Satır kaybı hatasız |
| PY3 | **380000 (değişmedi)** | Zincirli atama — `df[maske][kolon]=0` kopyaya yazar; orijinal aynen. Doğrusu: `df.loc[maske,"fiyat"]=0` |
| PY4 | `[1]` sonra `[1, 2]` | Mutable default argümanı — liste çağrılar arası yaşar |
| PY5 | **`[]`** | `except: pass` — `fiyatt` yazım hatası KeyError'ı yutuldu; boş sonuç "hiç araç yok"muş gibi raporlanır. En tehlikeli ajan-kod deseni |
| PY6 | `False` · `2.67` | Float ikili temsil — 0.1+0.2≠0.3; round banker's değil temsil sorunu (2.675 tam tutulamıyor) |
| PY7 | **4** | NaN karşılaştırması her zaman False — Honda filtreden sessizce düşer (S5'in pandas ikizi) |
| PY8 | 3 | Aliasing — `b=a` kopya değil, aynı liste |
| PY9 | `{'Toyota':6,'Honda':5,'Ford':4,'Renault':7,'Fiat':4}` | **Sessiz mantık hatası** — `len(m)` marka ADININ harf sayısı, adet değil. Kod çalışır, çıktı "sayım" gibi görünür, tamamen yanlış. Aradığın şey `value_counts()` |
| PY10 | **1 (değişmedi)** | `fillna` yeni Series döndürür; atanmadı → NaN duruyor. "Temizledim" sanılan veri kirli |

**Sessiz-katil sınıfı: PY1, PY2, PY3, PY5, PY7, PY9, PY10.**

## Kalibrasyon yönergesi
1. Baseline = doğru tahmin / 20 → `P0-tahminlerim.md` sonuna yaz (SQL ve Python ayrı ayrı).
2. Yanlışları hata SINIFINA göre grupla; aynı sınıftan 2+ yanlış → o başlık P1/P2'de öncelik. Toplam puana bakma.
3. Her yanlış için farkı 1 cümleyle açıkla (çevrim adım 3) ve 27-28 Tem tekrar kuyruğuna at (adım 4).
