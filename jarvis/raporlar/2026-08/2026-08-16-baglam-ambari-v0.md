# Bağlam Veri Ambarı v0 — kuruldu (deneysel m.29; 58c078f; 2026-08-16 seans-7)

*Tanım: `wiki/baglam-veri-ambari.md` · kanıt `cc/rapor-2026-08-16-3.md` · üretici `tools/ambar-tablo.py` (hat: `tools/katman-hatti.py` adım 4). Ayrım fiziksel değil ERİŞİM-TASARIMI: aynı `veri/baglam.sqlite` içinde `amb_*` şeması — materyalize olgu tabloları + iki zaman sütunu (system_time = üretim/commit anı · valid_time = olgunun gerçek anı) + SCD-2 boyut görünümü + olay↔nesne köprüsü (factless + qualifier) + martlar. Operasyonel V-1'e dokunulmaz; ambar bronz kütüklerden deterministik türer (kod SHA + girdi SHA). Katman-1 (Salih'te): bus-matrix'e `prompt`/`kosum` süreç satırları + "ambar" teriminin kanona girişi.*

## İçerik (sayılar gerçek)
| Nesne | Grain | Satır | Kaynak (bronz) |
|---|---|---|---|
| `amb_olgu_kosum` | 1 satır = 1 işçi-ajan koşumu (workflow/alt-ajan; token in/out/cache, süre, araç çağrısı, model, aile/rol) | 240 (17 workflow) | `veri/bronz/kosum-olay.jsonl` ← `~/.claude/projects/<jarvis>/**/subagents/**/agent-*.jsonl` |
| `amb_olgu_prompt` | 1 satır = 1 Salih prompt'u (valid_time = ts; system_time = yükleme) | 102 | `veri/bronz/prompt-olay.jsonl` |
| `amb_olgu_karar_borcu` | 1 satır = 1 açık karar kalemi snapshot'ı (valid_from = kayıt tarihi; kapanınca hüküm satırına akar) | 52 | `veri/karar-borcu.jsonl` |
| `amb_boyut_anahtar` (görünüm) | SCD-2: gecerli_bas · gecerli_bitis · guncel_mi (Kimball asgari 3) | 321 | V-1 `anahtar` |
| `amb_kopru_olay_nesne` (görünüm) | factless + qualifier (OCEL event_object): olay=kayıt bloğu ↔ nesne=referans hedefi | 49927 | V-1 `referans` |
| `amb_boyut_vardiya` (görünüm) | 1 satır = 1 vardiya-teslim dosyası | 47 | V-1 `dosya` (tur=teslim) |
| Martlar (gold) | `v_amb_kosum_maliyet` (workflow başına) · `v_amb_acilis_brifi` (as-of tek satır) → `veri/gorunum/v_amb_*.csv` | — | ambar tabloları |

## Mart 1 — açılış-brifi (as-of; "seans başı"nda okunacak tek satır)
| kod_sha | acik_salih_karari | acik_icra_borcu | son_prompt | son_prompt_zamani | bugun_prompt | son_teslim | son_kosum | guncel_anahtar | kopru_satiri |
|---|---|---|---|---|---|---|---|---|---|
| 58c078f | 39 | 12 | devam et | 2026-08-16T06:57:49.724Z | 5 | raporlar/vardiya-teslim-2026-08-16-seans6-stokastik.md | wf_89527235-dbf · 8 ajan · 130429 out-token | 321 | 49927 |

## Mart 2 — koşum-maliyeti (workflow başına; ham usage: output token + cache-read; ajan-dakika toplamı)
| wf_id | ajan | modeller | dk | output_tokens | cache_read | arac_cagrisi |
|---|---|---|---|---|---|---|
| wf_89527235-dbf | 8 | claude-fable-5,claude-opus-5 | 36.1 | 130429 | 5142398 | 111 |
| wf_7e3aa1d0-008 | 8 | claude-opus-5,claude-fable-5 | 38.9 | 131179 | 6166722 | 112 |
| wf_a08eccb1-262 | 12 | claude-opus-5,claude-fable-5 | 47.6 | 166366 | 6068685 | 136 |
| wf_1ca8d045-cb9 | 8 | claude-opus-5,claude-fable-5 | 41.0 | 194216 | 5097038 | 102 |
| wf_7c885c15-09a | 8 | claude-opus-5,claude-fable-5 | 40.2 | 163089 | 4427286 | 90 |
| wf_f0b8ec8a-e40 | 12 | claude-opus-5,claude-fable-5 | 64.6 | 279951 | 7275617 | 116 |
| wf_4c664aa0-e9f | 4 | claude-opus-5 | 22.0 | 76291 | 3891468 | 90 |
| wf_5cd68941-2b0 | 20 | claude-fable-5,claude-opus-5 | 77.6 | 229754 | 11577373 | 228 |
| wf_2682fbbe-590 | 3 | claude-opus-5 | 22.4 | 52663 | 8604632 | 111 |
| wf_5b25bf13-8dc | 4 | claude-opus-5 | 32.2 | 169387 | 9469662 | 143 |

*Örnek olgu satırları (wf_89527235 = bağlam-ambarı atlası; 8 ajan; roller ilk prompt'tan çıkarıldı):*
| kosum_id | aile | rol | modeller | dk | output_tokens | arac_cagrisi |
|---|---|---|---|---|---|---|
| wf_89527235-dbf:aa96c743474ae986f | AB | Atlas TEZ araştırmacısı | claude-opus-5 | 5.8 | 16166 | 26 |
| wf_89527235-dbf:a385c4e52fb8ef643 | CD | Atlas TEZ araştırmacısı | claude-opus-5 | 4.6 | 14362 | 19 |
| wf_89527235-dbf:a578f812e43459dc3 | CD | Atlas ANTİTEZ ajanı (açık De | claude-opus-5 | 9.3 | 35085 | 24 |
| wf_89527235-dbf:a6756d61e1ea698f0 | AB | Atlas ANTİTEZ ajanı (açık De | claude-opus-5 | 9.0 | 33446 | 21 |
| wf_89527235-dbf:a0a54536794d38cb2 | CD | V26 örneklem-denetçisi (aile | claude-fable-5 | 0.5 | 1514 | 7 |
| wf_89527235-dbf:a8730b358ea1ed4ae | CD | MASKELİ HAKEM | claude-fable-5 | 3.1 | 12237 | 4 |
| wf_89527235-dbf:aebba2cae4d97d33c | AB | V26 örneklem-denetçisi (aile | claude-fable-5 | 0.3 | 1098 | 5 |
| wf_89527235-dbf:add6ad4b8df8e434c | AB | MASKELİ HAKEM | claude-fable-5 | 3.4 | 16521 | 5 |

## Boyut örneği — `amb_boyut_anahtar` (SCD-2 görünüm; en çok referanslı 5)
| anahtar_id | tur | gecerli_bas | gecerli_bitis | guncel_mi | referans_sayisi |
|---|---|---|---|---|---|
| anahtar_terim:skill | anahtar_terim | 2026-07-10T18:14:36+03:00 | — | 1 | 4315 |
| anahtar_terim:antitez | anahtar_terim | 2026-07-18T04:27:50Z | — | 1 | 2290 |
| anahtar_terim:sema | anahtar_terim | 2026-07-10T18:14:36+03:00 | — | 1 | 2268 |
| anahtar_terim:hakem | anahtar_terim | 2026-07-11T16:02:55+03:00 | — | 1 | 1786 |
| anahtar_terim:atlas | anahtar_terim | 2026-07-15T01:50:02+03:00 | — | 1 | 1359 |

## Köprü örneği — `amb_kopru_olay_nesne` qualifier dağılımı
| qualifier | n | hedef_var |
|---|---|---|
| anahtar_terim | 23459 | — |
| tuzuk_madde | 7129 | — |
| etiket | 5199 | — |
| dosya_pointer | 4548 | 3796 |
| url | 2595 | — |
| v_no | 2536 | — |
| kart | 1946 | — |
| tarih | 1128 | — |

## `amb_olgu_karar_borcu` özet (küme × sahip × durum)
| kume | karar_sahibi | durum | n | en_eski |
|---|---|---|---|---|
| I-icra | Carvis | icra-sırada | 11 | 2026-07-30 |
| I-icra | Salih+Carvis | icra-sırada | 2 | 2026-07-30 |
| I-icra | Carvis | belirsiz | 1 | 2026-08-02 |
| KP-kapandi | Salih | kapandı | 1 | 2026-07-25 |
| S1-sistem-tasarim | Salih | Salih'te | 3 | 2026-08-16 |
| S1-sistem-tasarim | Salih | İMZASIZ | 3 | 2026-08-16 |
| S1-sistem-tasarim | Salih | masaya | 1 | 2026-08-16 |
| S2-yon-entegrasyon | Salih | Salih'te | 7 | 2026-07-23 |
| S3-oturum-disiplini | Salih | Salih'te | 3 | 2026-07-23 |
| S3-oturum-disiplini | Salih | İMZASIZ | 2 | 2026-08-12 |
| S3-oturum-disiplini | Salih | masaya | 1 | 2026-08-12 |
| S4-kanon-serh | Salih | İMZASIZ | 2 | 2026-08-14 |

## Sınırlar / kör (dürüstlük)
- Görünümler (`amb_boyut_*`, `amb_kopru_*`) SANAL — Stonebraker ölçütüyle tam "ambar" için materyalize edilmeleri gerekir; v0'da yalnız üç olgu tablosu materyalize (kosum · prompt · karar_borcu). Bitemporal sütunlar var ama `valid_to` çoğu satırda boş (henüz kapanış olayı yok).
- Koşum token'ları HAM usage'dır (`gen_ai.usage.*` eşleme sözlüğü); harness'in "subagent_tokens" sayısıyla birebir aynı değildir (o farklı topluyor) — iki sayı da m.39 damgalıdır, karıştırılmaz.
- Rol/aile ilk prompt'tan regex ile çıkarıldı (deneysel); Explore/atlas ajanlarında rol boş kalabilir.
- Ambar-üretimi brifin kalitesi ÖLÇÜLMEDİ (kör: A/B yok) — açılış-brifi martı ilk kez bir sonraki "seans başı"nda okunur ve elle brifle kıyaslanır.
