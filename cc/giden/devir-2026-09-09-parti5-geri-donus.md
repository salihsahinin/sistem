# Geri-dönüş — devir-2026-09-09-parti5 (Friday, 2026-09-09; şema `core/sablonlar/geri-donus-v0.md`)

## 1. biten
| iş | kanıt_yolu |
|---|---|
| KILAVUZ "Nerede ne var" bölüm taslağı (8 satırlık soru→dosya tablosu, 1.185 B ≤ 1,5 KB) | `cc/giden/devir-2026-09-09-parti5/kilavuz-nerede-ne-var.md` |
| 9 ay-dizini README metni (cc/gorev × 3 · cc/rapor × 3 · raporlar × 3), her biri 6 satır (başlık + 4 içerik + AS-OF) | `cc/giden/devir-2026-09-09-parti5/readme/<dizin>/README.md` |
| Çelişki/tekrar denetim listesi (amaç md.3), 8 kontrol noktası | `cc/giden/devir-2026-09-09-parti5/denetim-listesi.md` |
| Jarvis'e yazım = 0 (yalnız `cc/giden/**` + kapsül + pano + defter yazıldı) | `veri/bronz/hareket-olay.jsonl` |

## 2. kalan
| iş | neden_kaldı |
|---|---|
| README metinlerinin Jarvis'e yerleştirilmesi | Karar 91: yerleştirme Fable'ın; Friday Jarvis'e yazamaz. |
| Mevcut 25 README ile fiilî çelişki denetimi | Friday o dosyaları okuyamaz (hook); yerine kontrol listesi üretildi (D1 uyarınca iddia üretilmedi). |
| `cc/gorev/*` ve `cc/rapor/*` gerçek dosya-adı deseninin doğrulanması | Envanterde bu iki dizin için örnek ad YOK; kök README'nin `gorev-*` / `rapor-*` ifadesi tek dayanak → D1: iddia yerine açık soru. |

## 3. acik_sorular_salih (HÜKÜM YOK)
1. `cc/gorev/YYYY-MM` ve `cc/rapor/YYYY-MM` içindeki gerçek dosya-adı deseni nedir — kök README'nin `gorev-*` / `rapor-*` ifadesi bugün de geçerli mi?
2. `raporlar/` için ad cascade'i (`vardiya-teslim-*` → `seans-teslim-*`) hangi tarihte hangi biçimde durdu; ay README'lerinde tek desen mi göstereyim?
3. Ay-dizini README'sinde "3-6 satır" sayımı başlık satırını içeriyor mu (ben içerir varsaydım: başlık + 4 içerik + AS-OF = 6)?
4. Denetim listesi (amaç md.3) `done_yuklemi`de sayılmıyordu; ayrı dosya olarak üretmem doğru muydu, yoksa geri-dönüş notunun içinde mi kalmalıydı?

## 4. sonraki_ilk_is
Fable, `cc/giden/devir-2026-09-09-parti5/` altındaki 10 dosyayı denetim listesindeki 8 kontrolle karşılaştırıp Jarvis'e yerleştirir; Friday'in sıradaki işi tasarım diyaloğu tur 1 cevabını beklemektir.

## 5. diskteki_dosyalar
| yol | commit_dışı |
|---|---|
| `cc/giden/devir-2026-09-09-parti5/kilavuz-nerede-ne-var.md` | hayır |
| `cc/giden/devir-2026-09-09-parti5/denetim-listesi.md` | hayır |
| `cc/giden/devir-2026-09-09-parti5/readme/{cc/gorev,cc/rapor,raporlar}/{2026-07,2026-08,2026-09}/README.md` (9 dosya) | hayır |
| `cc/giden/devir-2026-09-09-parti5-geri-donus.md` | hayır |
| `core/durum-kapsulu.md` · `core/pano.md` · `kuyruk/senaryo-defteri.md` | hayır |
| `veri/bronz/hareket-olay.jsonl` (hook yazar) | hayır |

## 6. sayac
{ ajan_çağrısı: 0, araç_çağrısı: ~14 (tavan 40), işçi_sayısı: 0, alt_ajan_token: 0 }

## 7. sapmalar
| emir_maddesi | ne_yapıldı | neden |
|---|---|---|
| `done_yuklemi` (10 dosya sayıyor) | 11 dosya yazıldı: `denetim-listesi.md` eklendi | `amac` md.3 "çelişki/tekrar denetim listesi" istiyordu ama `done_yuklemi` onu saymıyor — iki alan çelişik. Yazma izni glob'u (`cc/giden/devir-2026-09-09-parti5/**`) içinde kalındı; iddia değil kontrol listesi üretildi (D1). |
| — | Başka sapma yok: işçi açılmadı, Jarvis'e yazılmadı, push edilmedi, `git add -A` kullanılmadı. | — |

## 8. tohum_desen_kullanimi
| desen_no | kullanıldı | neden |
|---|---|---|
| 1 (işçi SENKRON) | hayır | İşçi açılmadı (bütçe notu: tek lider yeter). |
| 4 (yapan ≠ ölçen) | hayır | Bu devirde ölçüm/hakem adımı yok; denetim işi Fable'a devredildi. |
| 5 (≥2 birincil kaynak) | hayır | Araştırma devri değil; dış kaynak açılmadı. |
| 10 (pathspec-only git) | evet | Yalnız `git add <yol>`; push yok. |
| m.20 pointer ilkesi | evet | KILAVUZ bölümü "ne var"ı README'ye pointer'ladı (D2/D3). |
| m.39 rakam disiplini | evet | Tüm dosya sayıları envanterden; doğrulanmamış her nokta AÇIK SORU'ya düştü, kestirim yazılmadı. |

## 9. ledger_onerisi (ÖNERİ)
| ib_no | önerilen_durum |
|---|---|
| İB-82 (parti-5 devri) | teslim edildi — Friday tarafı kapandı; Jarvis'e yerleştirme Fable'da açık |
| Katman-1 adayı | `done_yuklemi` ↔ `amac` çelişkisi (bkz. §7): devir-birimi v0 şemasına "amaçtaki her çıktı done_yükleminde sayılır" kuralı adayı — kararı Salih verir |

## 10. durma_nedeni
tamamlandı (parti-5 tarafında fren tetiklenmedi; Jarvis yolu hiç denenmedi). Not: okuma-izin kilidi koşumun İş-2 kısmında bir kez YANLIŞ-POZİTİF verdi — yazılacak dosyanın METNİNDE Jarvis kökünün tilde biçimi geçtiği için Bash çağrısı reddedildi; dosya Write aracıyla yazıldı. Ayrıntı: `cc/giden/tasarim-2026-09-09-tur1.md` A5.

## + kapsul_eklenen
- İlk canlı devir kapandı: parti-5 navigasyon paketi 11 dosya olarak `cc/giden/devir-2026-09-09-parti5/` + geri-dönüş notu; Jarvis'e yazım 0.
- Açık: `cc/gorev|rapor` ad deseni ve `raporlar/` ad cascade'i doğrulanmadı (envanterde örnek ad yok) → Fable/Salih cevabı bekleniyor.

## + cekirdek_adayi (Salih "kabul" derse `core/desenler.md`)
- "Okuyamadığın dosya hakkında iddia değil KONTROL LİSTESİ üret": kapalı-göz devirlerinde çıktı, hedef dosyayı gören tarafın (Fable) yürüteceği kontrol maddelerine dönüşür.
- "Devir birimini almadan önce `amac` ile `done_yuklemi`'i karşılaştır; fark varsa koşum başında sapma olarak beyan et, sonunda değil."
