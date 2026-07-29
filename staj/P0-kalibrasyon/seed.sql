-- P0 kalibrasyon şeması + veri (ikinci-el araç pazarı — Otonet bağlamına yakın)
-- Doğrulama: sqlite3 p0.db < seed.sql  → sonra sorguları tek tek koş
CREATE TABLE musteri (id INTEGER PRIMARY KEY, ad TEXT, sehir TEXT);
CREATE TABLE arac (id INTEGER PRIMARY KEY, marka TEXT, yil INTEGER, fiyat INTEGER, sahip_id INTEGER);
CREATE TABLE satis (id INTEGER PRIMARY KEY, arac_id INTEGER, alici_id INTEGER, tarih TEXT, tutar INTEGER);
CREATE TABLE servis (id INTEGER PRIMARY KEY, arac_id INTEGER, tarih TEXT, maliyet INTEGER);

INSERT INTO musteri VALUES
 (1,'Ali','Ankara'),(2,'Ayse','Istanbul'),(3,'Mehmet',NULL),(4,'Zeynep','Izmir'),(5,'Can','Ankara');
INSERT INTO arac VALUES
 (1,'Toyota',2018,850000,1),
 (2,'Honda',2020,NULL,2),        -- fiyat NULL (pazarlik)
 (3,'Ford',2015,450000,3),
 (4,'Renault',2019,600000,NULL), -- sahip NULL (sirket stogu)
 (5,'Toyota',2021,1200000,4),
 (6,'Fiat',2017,380000,1);
INSERT INTO satis VALUES
 (1,1,2,'2026-06-15',830000),
 (2,3,5,'2026-06-30',445000),
 (3,6,4,'2026-07-01',375000),
 (4,5,2,'2026-07-10',1150000);
INSERT INTO servis VALUES
 (1,1,'2026-05-01',5000),
 (2,1,'2026-06-01',3000),
 (3,3,'2026-05-20',8000),
 (4,4,'2026-07-05',2500);
