# Sokrates ajanı: sentez ve teslim (2026-10-29, seans 2026-10-29-jarvis, hedef #49)

## Sonuç
Konuşulabilir Sokrates ajanı hazır. Persona v0.3, hakem kararı `GEÇTİ` (tur 3; her ölçüt MIN ≥4). Canlı uçtan uca test: `sokrates` ajan tipi Agent aracıyla çağrıldı, tanıtım + tek soru + "doğru inanç ≠ bilgi" karşı örneği döndü, araç çağrısı 0.

## Nasıl konuşulur (üç yol, kaynak tek)
| Yol | Adım | Not |
|---|---|---|
| **Desktop (önerilen)** | Claude desktop'ta `C:\sistem\sokrates` klasörünü aç, yaz | `.claude/settings.local.json` output style'ı `sokrates` seçer; mühendislik promptu kapalı (`keep-coding-instructions: false`). İlk açılışta `/output-style` ile doğrula. |
| Terminal | `C:\sistem\sokrates\sokrates.bat` | `claude --agent sokrates`; Sonnet, araç yalnız Read, maxTurns 40. |
| Herhangi oturum | `/sokrates <konu>` | Skill oturuma kişiliği yükler; jarvis'te de kopyası var (`.claude/skills/sokrates/`). |

Çıkış: "[jarvis]" yaz ya da "rol oyununu bitiriyorum" de. Samimi "yapay zekâ mısın" sorusuna `[Jarvis]` etiketiyle dürüst tek cümle gelir, sonra karakter sürer.

## Üretim zinciri (alt graf #49)
1. **Araştırma (#50):** 4 rapor: 01 depo içi (sinav-grill skill, hakem biçimi, kanon kuralları) · 02 birincil kaynaklar (Platon erken diyaloglar, Ksenophon, Vlastos elenchus, D/K/X 20 satır; "bildiğim tek şey" biçimi X) · 03 modern tasarımlar (saf "asla cevap verme" kırılgan; persona sapması 8+ turda; grilling deseni) · 04 Claude Code mekanizmaları (output style + agent + skill).
2. **Kişilik kanonu (#55):** `core/sokrates-ajani.md` (Opus işçisi v0.1; Jarvis v0.2, v0.3). §7 sistem promptu tek kaynak; üç yüzey ondan türetilir.
3. **Teknik yüzey (#62):** `C:\sistem\sokrates\` (README, CLAUDE.md, settings.local.json, output-styles, agents, skills, sokrates.bat, diyaloglar/) + jarvis kopyası.
4. **Test döngüsü (#66):** rubrik 5 ölçüt (05-test-plani.md); tur 1: 8 senaryo, `KALDI` (A4 3: samimi rol-bitirme isteğinde karakterde kalma) · tur 2: 6 senaryo, `KALDI` (A3 3: "Fransa" tırnakla) · tur 3: 4 senaryo, `GEÇTİ`. Hakem raporları `cc/rapor/2026-10/rapor-2026-10-29-sokrates-v0.{1,2,3}-hakem.md`. Toplam 18 simülasyon transkripti `C:\sistem\sokrates\diyaloglar\`.

## Jarvis hükümleri (Salih onayına açık)
- Ajan tarihsel karakter, tutor değil: görüş söyler, her görüşü soruya çevirir; "cevabı söyle" iki kademe + `[sokratik-sapma]` işareti.
- Kimlik dürüstlüğü: samimi oyun-dışı soruda inkâr yok, `[Jarvis]` tek cümle + açık kaynak dosya yolu; oyun içi meydan okuma karakterde.
- Yasak kelime tek okuma: MÖ 399 sonrası ad/kavram tırnakla bile tekrarlanmaz.
- Ruh hâli yorumu yok (m.23/m.33); övgü yok; em-dash yok.

## Borçlar (v0.4)
- Prompt 1308 kelime (bütçe 900); sıkıştırma.
- Hakem tur 3 önerileri: askıdaki soruya ≤2 turda dönüş; bıkma + "söylemeyecek misin" çakışmasında önce görüş; toparlama sonrası aynı soruyu yineleme.
- Simülasyon sabit kullanıcı mesajlı (tek çağrı); gerçek konuşma ölçümü Salih'in kullanımıyla.
- `sage/` (felsefe ajanı) dizini izolasyon gereği okunmadı; oradaki Stoa/felsefe bağlamı istenirse Jarvis devir dosyasıyla ister.

## Yan ürün
jarvis-oda v0.4 (`ajan` alanı: `.claude/agents/<ad>.md` rolüyle işçi; hakem odada görünür) ve v0.4.1 (yerel saat) yan oturumda yazıldı (7e78afb, 814d986); yeniden başlatmada etkin.
