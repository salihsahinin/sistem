# Masa Gündemi — EK-6 DARALTILMIŞ (2026-08-20)


**MASA KAPANDI 2026-08-29 (4. Lavish masası, Karar 78 — 10/10 hüküm):** F1 vaka-tetikli beklet · F2 birim=GÖREV + m.43 N=3 (Salih notu aynen defterde) · F3 düzeltme+aynı-sayaç N=3 · F4 → İB-60 loop-dedektör · F5 süpersede-kapat (1,73× → İB-54) · F6 m.25 V47 şerhi İMZA · F7 DE-GOLD tek kaynak · F8 → İB-61 teyit turu · T1/T2 süpersede-kapat. ⑨ DONDUR baki (açma tetiği Salih beyanında).
*Künye: EK-6 külliyatının (~106 K1 kalemi / 9 küme, 08-01 gece ingest'i) triyaj-sonrası CANLI kalanları. Triyaj: `raporlar/2026-08-20-ek6-triyaj-supersede.md` (hükümler §4: S1 süpersede kapanışları · S2 ⑨ DONDUR-tetikli · S3 optimize dağıtım — Salih 08-20, defter Karar 41). Külliyat şerhi baki: F2 denetimi 3/34 TUTMADI + 1 icat-rakam — kalemler denetimli okunur. Bu masa ayrı oturumda açılır; kalem başına açıklama-bloklu sunum.*

## Kalemler (9)

1. **g22-B1 bellek kapısı** — RAM/Commit izleme kuralının kanonlaşması (kaynak: `kuyruk/masa-gundemi-2026-07-30.md:549-552`).
2. **g22-B2..B5 paketi** — GB ekseni · izleme rutini · donanım eşiği · kalibrasyon (aynı kaynak; B1'le tek blokta sunulabilir).
3. **g23-açık-1: tekrar-BİRİMİ tanımı** — loop sayacının nesnesi ne (adım kümesi ↔ görev ↔ oturum); 08-15 şeması kapsamadı (`:553-557`).
4. **g23-açık-2: m.43'e TETİK ayağı** — skill-doğum kuralına loop-kaynaklı tetik eklenir mi (m.43 eşiği artık N=5 — 08-20 Karar 30 sonrası yeniden çerçevelenmeli).
5. **g23-açık-3: m.40b-loop kaydı** — loop-TESPİT mekanizması (çağrı sözleşmesi değil dedektör; şema kapsamı dışı).
6. **g24 CC-oran çekirdeği** — CC-oran matrisi/hedef-metni 4 seçenek + gerekçe-disiplini (K1-24-b) + `kosum-maliyeti.py` 1,73× şişiklik kalibrasyon bulgusu (`:558-564`). Rejim-etiketi parçası KAPANDI (m.46(d), Karar 39); K1-24-l "K-009'dan önce oku" notu K-009 açılış gündemine pointer.
7. **⑧ m.25 eşiği V47 formu** — "pipeline sınıfı için m.25 eşiğinin V47 formunda yazılması (K1-K6+kalibrasyon protokolü)"; halefi yok, K0-Y3 yakın ama aynı değil (#8/#105).
8. **⑤ ölçüm-bankı tekleştirme** — `kuyruk/olcum-banki.md` ↔ DE-katmanı GOLD "ölçüm-bankı satırları" (`core/veri-muhendisligi-katmani.md:17`) çakışıyor; tek kaynak kararı.
9. **① pipeline/loop kanonu belirsizleri** — ~4 kalem (dar-ajan zinciri, "özetle DENMEZ" yasağı; rapor-13:313-315, rapor-20 K1-c, EK-F K1-l/K1-o): ajan-metodolojisi + ingest-şeması kısmen absorbe etmiş görünüyor, kalem-kalem bakış gerekir.

## DONDURULMUŞ (S2 hükmü)

- **⑨ "diğer" ~95 tekil kalem** — tarih-damgalı DONDUR (08-20). **Açma tetiği (Salih, aynen): "mevcut önemli karar borçları bitince."** Kaynak kod-listesi: `raporlar/2026-08-01-ingest-grafhatti.md` §2.3; hiçbir şey silinmedi (m.8).

## KAPANANLAR (S1 hükmü — arşiv damgası)

- K2-d (halef: `core/skill-tetikleme-semasi.md:27` tetik_kosulu) · ③ bütçe-fren (halef: `core/ajan-metodolojisi.md:19,35` + m.46(d)) · ④ çağrı-kapısı (halef: tetikleme şeması bütünü) · ⑥ m.40b-desen (halef: 12-koşum serisi, K2-l) · ⑦ K-019 (halef: `core/world-model-tasarimi.md:51,68` + ingest v2). Düşük-öncelik borç: yanlış-kapanış kontrolü (ilerde).

## Çapraz-okuma sonucu — İB-14 (KB-24 teyidi; 2026-08-22 seans-14, Carvis; kaynak: `core/skill-tetikleme-semasi.md` v1 ↔ g23 K1-a..l / K2-d)
*Teyit notu, karar değil; kalemlerin masadaki yeri Salih'te. ABSORBE = şema/hat aynı işlevi bugün karşılıyor (kanıt pointer'lı); AÇIK = kapsam dışı, kalem kalır.*
- **K2-d tetik(D8) alanı → ABSORBE:** şema alan 2 `tetik_kosulu` (m.38 boolean, negatif de yazılır, derece ifadesi YASAK) + Kapı-Ö (`¬(tetik kaynağı = araç/skill ÇIKTISI)`) D8'in tamamını karşılar.
- **g23 "asgari log: cc/defter'e case_id+activity" → ABSORBE:** Kapı-K OTel satırı (operation/tool.name/agent.name/model/tarih) + silver `hareket` (1 satır = 1 araç çağrısı; Skill çağrıları dahil) + `v_skill_kosum` / `tools/skill-esik.py` (Karar 51) — log katmanı KOŞUYOR; defter sütunu gereksiz.
- **Kalem 4 (g23-açık-2 m.43'e TETİK ayağı) → KISMEN ABSORBE + ÇELİŞKİ ADAYI (m.16):** skill-üretim şeması K0 künyesinde "köken aşağıdan: m.43 sayaç k_W" = tetik ayağının kendisi (loop/tekrar-kaynaklı doğum). **Bulgu:** Karar 30 (08-20) m.43 eşiğini N=3→5 yaptı; `skill-kapisi` SKILL.md K1 metni "k_W ≥ 3 (τ=0,8)" yazıyordu → 08-22 **5**'e çekildi (Katman-2 skill gövdesi, Karar 30 icrası); `core/skill-uretim-semasi.md` Z1 formülü sembolik (`k_W ≥ k_τ`) ama τ=0,8 sabiti k_τ=3 üretir → **Katman-1 metin düzeltmesi Salih'te:** τ≈0,86 ∨ "k_τ=5 (Karar 30)" şerhi. Kalan soru (AÇIK): loop-kaynaklı tetik skill-ÖNCESİ sayaca nasıl girer (tekrar birimi aşağıda).
- **Kalem 3 (g23-açık-1 tekrar-BİRİMİ) → AÇIK (kısmî tanım var):** şema yalnız VAR OLAN skill çağrısını sayar (Kapı-K → k_W; birim = çağrı); skill-üretim şeması K1 k_W'yi "özdeş↔varyant ayrı, W=90 gün" görev-tekrarı olarak sayar. Skill-ÖNCESİ loop için birim (adım kümesi ↔ görev ↔ oturum) hâlâ tanımsız → kalem kalır.
- **Kalem 5 (g23-açık-3 m.40b-loop kaydı / loop-DEDEKTÖRÜ) → AÇIK:** şema çağrı sözleşmesidir, desen-tespit yapmaz (EK-6 notu doğru). Veri hazır (silver `hareket` + `v_skill_kosum` + `baglam_olay`), dedektör yok → kalem kalır; kural-tabanlı dedektör = icra adayı (karar sonrası).
- **Kalem 6 (g24 CC-oran çekirdeği) → AÇIK:** şema §5 sayısal alanlar (pass^k, model damgası) CC-oran matrisini kapsamaz; rejim-etiketi parçası zaten KAPANDI (Karar 39) — kalem kalır (K1-24-b gerekçe-disiplini + 1,73× kalibrasyon).
**Özet:** 9 kalemden 2'si (K2-d, g23 log) ABSORBE — kapatılabilir; 1'i (kalem 4) kısmen + m.16 çelişki adayı (3↔5; Katman-1 metin); 3'ü AÇIK kalır. Ledger İB-14 KAPANDI (teyit yapıldı); kapanış hükümleri Salih'te.
