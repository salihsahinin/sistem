# Pano

*Şirketin nabzı tek bakışta. Kart = işin adresi, kendisi değil. "Ekrana gel" satırı dikkat filtresidir.*
*Şablon v2 (K-012 adım 4, 2026-07-12, deneysel m.29): +Açılış/Yaş (#22) +Bağımlı +Yetki (Beads bulgusu + Salih yetki-kartı fikri; yetki alanı ajan döneminde anlam kazanır — şimdilik tümü Carvis). Kural: DONE alanı boş kart açılamaz (KILAVUZ).*

**Güncelleme:** 2026-07-12 build oturumu (Carvis yazdı)

## AKTİF
| Kart | İş | DONE | Açılış | Bağımlı | Yetki | Ekrana gel |
|---|---|---|---|---|---|---|
| K-002 | PortRisk Sprint 1 (yfinance + getiriler) — şirketin ilk görev döngüsü + İLK HASAT-ETİKETLİ GÖREV (ölçüm-öncelikli strateji) | pytest yeşil + push (commit Salih'in) | 07-10 | — | Carvis | TEK AKTIF IS (Salih 07-11 karari) |

## BEKLEYEN
| Kart | İş | DONE | Açılış | Bağımlı | Yetki | Ekrana gel |
|---|---|---|---|---|---|---|
| K-003 | PortRisk Sprint 2 (SQLite veri katmanı) | şema + örnek sorgu README'de + ≥1 SQL testi | 07-10 | K-002 | Carvis | — |
| K-004 | İngilizce paket (CV + LinkedIn + GitHub profil) | 1 sayfa ATS-uyumlu CV + canlı LinkedIn + profil README | 07-10 | — | Carvis | Kasım başı |
| K-005 | IMC Prosperity (ya da eşdeğer) kaydı | leaderboard'da takım adı | 07-10 | — | Carvis | tur duyurusu |
| K-007 | GPA/transkript netleştirme | değer kapsüle işlendi | 07-10 | — | Carvis | CV çalışması başlarken |
| K-011 | Claude sistemini OneDrive-dışı köke taşıma (git `7a11abd`) | yeni kök çalışır + mount + scheduled görevler + eski yol arşiv | 07-11 | — | Salih+Carvis | Salih gün seçince (tam yedekle başlar) |

## BLOKE
| Kart | İş | Ön-koşul | Açılış | Yetki |
|---|---|---|---|---|
| K-008 | vault-index reposu (Faz 0 "Kanıt Dilimi") | PortRisk canlı-link DONE | 07-10 | Carvis |
| K-009 | Otomasyon (gecelik senkron Routine, uyucam/günaydın kancaları) — açılış gündemi: Karpathy-loop yöntemleri (Salih 07-12) + ajan-dönemi defteri (`kuyruk/build-tartisma-notlari.md`) | loop-eng Faz 2 + Faz 4 | 07-10 | Salih+Carvis |
| K-010 | İlk canlı ajan | K-009 + temel katman 2 hafta sorunsuz | 07-10 | Salih+Carvis |

## SON BİTEN
**K-012 KAPANDI (07-12): JARVIS kurulumu — tüzük v1 + seçim turu + 5 build adımı (CLAUDE.md v1 · KILAVUZ v1 · wiki standardı+2 sayfa+hasat+test-kuyruğu · pano v2 · köken-izi #1) tamamı commit ve push ile.** · **K-013+V25 (07-12):** ekosistem araştırması + rakip analizi → `raporlar/2026-07-12-K013-ekosistem-arastirmasi.md` + `kuyruk/build-tartisma-notlari.md`; 5 build-bulgusu adımlara dağıtıldı. **07-11:** TÜZÜK v1 İMZALANDI · K-006 kapandı · fikir kutusu kuruldu · scheduled temizlik · git onarımı.
