# Pano

*Şirketin nabzı tek bakışta. Kart = işin adresi, kendisi değil. "Ekrana gel" satırı dikkat filtresidir.*
*Şablon v2 (K-012 adım 4, 2026-07-12, deneysel m.29): +Açılış/Yaş (#22) +Bağımlı +Yetki (Beads bulgusu + Salih yetki-kartı fikri; yetki alanı ajan döneminde anlam kazanır — şimdilik tümü Carvis). Kural: DONE alanı boş kart açılamaz (KILAVUZ).*

**Güncelleme:** 2026-07-12 build oturumu (Carvis yazdı)

## AKTİF
| Kart | İş | DONE | Açılış | Bağımlı | Yetki | Ekrana gel |
|---|---|---|---|---|---|---|
| K-015 | JARVIS ilk prototip — tasarım şeması (m.36 REVİZE: artık kapı değil, K-002 ile PARALEL şerit). YAŞAYAN LİSTE: (1) ~~ingest/katman şeması v1~~ DONE 07-12 (İMZALI: kuyruk/oneri-ingest-sema-v1.md) · (2) ~~TETİKLİ/UFUK başlangıç modeli~~ DONE 07-12 (Q3-A: gömülü etiket + günaydın taraması) · (3) loop-eng Faz 2 (/goal) + Faz 4 (Routine) + Karpathy loop yöntemi öğrenimi/revizyonu — Salih öğrenimi · (4) ~~tartışma kuyruğu kapanışı~~ DONE 07-12 · (+Salih ekler/çıkarır, her değişiklik commit) | listedeki tüm maddeler kapandı | 07-12 | — | Salih+Carvis | K-002 ile paralel (Salih 07-12 sabah: kapı kaldırıldı) |
| K-002 | PortRisk Sprint 1 (yfinance + getiriler) — şirketin ilk görev döngüsü + İLK HASAT-ETİKETLİ GÖREV | pytest yeşil + push (commit Salih'in) | 07-10 | ~~K-015~~ düştü (m.36 revizyonu 07-12) | Carvis | ŞİMDİ — K-015 ile paralel şerit |

## BEKLEYEN
| Kart | İş | DONE | Açılış | Bağımlı | Yetki | Ekrana gel |
|---|---|---|---|---|---|---|
| K-003 | PortRisk Sprint 2 (SQLite veri katmanı) | şema + örnek sorgu README'de + ≥1 SQL testi | 07-10 | K-002 (AKTİF'e taşındı 07-12) | Carvis | — |
| K-004 | İngilizce paket (CV + LinkedIn + GitHub profil) | 1 sayfa ATS-uyumlu CV + canlı LinkedIn + profil README | 07-10 | — | Carvis | Kasım başı |
| K-005 | IMC Prosperity (ya da eşdeğer) kaydı | leaderboard'da takım adı | 07-10 | — | Carvis | tur duyurusu |
| K-007 | GPA/transkript netleştirme | değer kapsüle işlendi | 07-10 | — | Carvis | CV çalışması başlarken |
| K-014 | Claude chat instructions güncellemesi — Jarvis bağlamına göre yeniden yazım (Salih 07-12) | yeni instructions Salih ayarlarına yapıştırıldı | 07-12 | ~~tartışma kuyruğu~~ TETİK GELDİ 07-12 | Salih+Carvis | ŞİMDİ (kuyruk kapandı) |
| K-016 | İlk JARVIS-yapımı skill turu — ihtiyaç listesi → üretim (KILAVUZ skill standardı + eval kuralı + skill-creator; ilham taraması gerektiğinde tazelenir; V25 altın kural: kurulum yok, yeniden yazım) | ≥1 kendi skill'imiz eval setiyle canlı | 07-12 | K-015 | Salih+Carvis | K-015 DONE olunca |
| K-011 | Claude sistemini OneDrive-dışı köke taşıma (git `7a11abd`) | yeni kök çalışır + mount + scheduled görevler + eski yol arşiv | 07-11 | — | Salih+Carvis | Salih gün seçince (tam yedekle başlar) |

## BLOKE
| Kart | İş | Ön-koşul | Aç