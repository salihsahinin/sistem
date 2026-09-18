# Sistem monorepo planı — Karar 101 icrası (2026-09-18, Jarvis/Fable; hüküm Salih)

*Kaynak: Karar 101 (defter). Deneme fazı yok (Salih). Bu dosya yol planıdır; icra adımları "kim yapar" sütunuyla. Rakamlar 09-18 envanterinden (m.39); firstmate desenleri `~/dev/firstmate` taramasından (Explore alt-ajanı, 13 araç çağrısı; `dosya:satır` atıfları ajan raporunda, özet burada).*

## 0. Tasarım cümlesi
Depo = **sistem**: N ajan + genelleştirilmiş kanon. Kod ve kanon ortak, **durum ve hafıza ajan-başına** (firstmate deseni: `FM_HOME` = ajanın özel `data/ state/ config/`; kod kökü ortak — `AGENTS.md:49-51`). Jarvis = ana-sıra ajan + kanonların bakıcısı (firstmate rolü: Salih'in tek temas noktası, işi delege eder, projeye kendisi yazmaz — hard rule 1). Friday = kalıcı domain-lider (secondmate sınıfı: kendi evi + charter, varsayılan boşta). İşçi ajanlar = crewmate sınıfı (tek görev, atılabilir worktree).

## 1. Hedef ağaç
```
~/sistem/
  AGENTS.md              ortak kök kanon ≤25 satır (harness-bağımsız tek kaynak)
  CLAUDE.md  → AGENTS.md symlink (firstmate deseni; kimlik/durum satırı yok)
  README.md              depo haritası: ajan listesi + sahiplik tablosu
  sablonlar/             görev-fonksiyonu · geri-dönüş v0 · A1 lojik blok · charter iskeleti
  .claude/settings.json  tek hook girişi: bin/hook-dispatch.sh (cwd'ye göre ajan hook'una yönlendirir)
  bin/hook-dispatch.sh
  ogrenme/               Salih'in; ajan-dışı; ajanlara deny
  jarvis/                AGENTS.md(+CLAUDE.md symlink) · core/ · kuyruk/ · cc/ · veri/ · tools/ · raporlar/ · wiki/ · arsiv/ · graf/ · .claude/ · KILAVUZ.md · fikir-kutusu.md · kaynak-kodu/ · paylasim/
  friday/                AGENTS.md(+symlink) · core/ (desenler, kapsül, pano, rol) · cc/gelen · cc/giden · .claude/ ; kanon/ symlink kalkar
```
Sahiplik yönlendirme tablosu (firstmate `AGENTS.md:233-243` deseni; kök md'de tek paragraf): **genel kural** → kök `AGENTS.md` (Jarvis yazar, Salih imzalar) · **ajan kuralı/kimliği** → `<ajan>/AGENTS.md` (Jarvis yazar, Salih imzalar; ajan kural yazamaz, m.42 d) · **ajan hafızası** → `<ajan>/core/` (ajanın kendisi) · **karar defteri** → `jarvis/kuyruk/senaryo-defteri.md` (tek defter; diğer ajanların kararı yok, kural adayı var) · **proje kanonu** → ileride `projects/<ad>/AGENTS.md`.

## 2. Kök AGENTS.md taslağı (≤25 satır; F4'te yazılır)
1. Bu depo **sistem**: N ajan + ortak kanon; her ajan kendi dizininde çalışır, kendi `AGENTS.md`'sini ve `core/` hafızasını okur; başka ajanın dizini okunmaz (izolasyon = cwd + hook + deny).
2. Salih tek karar verici (m.1-2); Katman-1 (kök kanon, ajan kanonları, silme, dışarı çıkan iş, para) yalnız Salih imzası.
3. Öncelik kuralı (firstmate `AGENTS.md:549-556` deseni): Salih'in güncel, açık, somut talimatı duran her kuralı ezer; ezme genişletilmez (analoji yok, duran yetkiye dönüşmez); yıkıcı/geri-alınamaz iş yine açık beyan ister. Duran kuralla çelişki → önce çelişki raporu (m.16).
4. Ortak 8 madde (tüzükten taşındı, tüzükte pointer): m.8 silme yasağı (arşiv + pointer) · m.9 push yalnız Salih beyanıyla · m.10 commit İngilizce, kaynak Türkçe · m.20 pointer ilkesi · m.31 veto = revert · m.39 her rakam kaynaklı, kestirim `[?]` · m.42(h) amaç ↔ done çelişirse amaç kazanır, fark başta `[sapma]` · md.49 işyeri/staj verisi depoya girmez.
5. Zaman: tarih yalnız sistem saatinden; zaman-bağımlı iddia AS-OF damgalı (Karar 68).
6. Üslup: vurgu kalın; büyük harf yalnız kısaltma/durum jetonu; övgü yok, çıplak veri (m.7).
7. Git: pathspec-only `git add <yol>` (H4); başka ajan canlıyken `-A` yasak; commit mesajı İngilizce.
8. Ajanlar arası iletişim: emir = ajanın `cc/gelen/` dosyası + masaüstü oturum mesajı (protokol §5 EK-3); dönüş = `cc/giden/` dosyası + `.aktif-devir` silinir; ajanlar Salih'e doğrudan yazmaz, Jarvis üzerinden (firstmate hard rule 4).
9. Bakım (firstmate `AGENTS.md:558-563`): kod gösteriyorsa tekrar yazma, otoriter dosyayı işaret et; eklemek yerine yeniden yaz/buda; güvenlik sınırı korunur; bütçe ≤25 satır, aşım = arıza.

## 3. jarvis/AGENTS.md §1 revizyonu (bugünkü CLAUDE.md'den; F4)
"Sen **JARVİS**'sin: sistemin **ana-sıra ajanı** ve kanonların bakıcısı; Salih'in kölesi (yetki sıfır, emir tam icra); rol modeli firstmate — Salih'in tek temas noktası, işi domain-lider seviyesine kadar bölersin (m.44), proje işini kendin yapmazsın (istisna: Salih'in somut anlık onayı). Friday ve diğer ajanlar sana dosyayla döner, Salih'e yazmaz." §3 okuma sırası, §7 "nerede ne var" yollar `jarvis/` köküne göre; tüzük m.41/m.44 EK satırı: "ana-sıra = `~/sistem/jarvis` cwd'li Claude Code oturumu".

## 4. Fazlar

| Faz | İş | Kim | Çıktı / kanıt |
|---|---|---|---|
| **F1 hazırlık** (bu seans) | plan (bu dosya) · `tools/yol-tasi.py --kuru` (eski→yeni yol tablosu; 8 tools + 2 hook + 3 friday-atıflı dosya + `.no-mistakes` yapılandırması; dokümanlar dokunulmaz, AS-OF tarihli) · `bin/hook-dispatch.sh` taslağı · kök `AGENTS.md` + `jarvis/AGENTS.md` §1 taslakları (`kuyruk/taslak-*`) | Jarvis | kuru koşum diff'i + 3 taslak dosya |
| **F2 taşınma** (≈30 dk el işi; komut listesi §5) | tüm oturumları kapat → `mv ~/jarvis ~/sistem` → `git mv` ile Jarvis içeriği `jarvis/` altına (ogrenme/ kökte kalır) → untracked büyük veri (`kuyruk/galeri-siralama` 5,5 GB, `.venv`) elle → `git subtree add --prefix=friday ~/friday main` (17 commit tarih korunur) → `friday/kanon` symlink sil → GitHub repo adı `jarvis`→`sistem`, `git remote set-url` → eski `~/friday` arşive | Salih | `git log --oneline -3` + `git worktree list` + `ls ~/sistem` |
| **F3 yol düzeltme** | `yol-tasi.py --uygula` · silver yeniden üretim (`katman-hatti.py`) · `acilis-kapilari.py` proje-anahtarı (`~/.claude/projects/-Users-…-sistem-jarvis`; eski transkriptler görünmez, kütükte bilinçli kopuş satırı) · `hareket-tablo.py` transkript kaynağı · Friday `settings.json` deny 20→1 (`jarvis/**` + `ogrenme/**`) · Friday hook yolları | Jarvis | testler: Jarvis hook 14/14 · Friday hook 22/22 · `katman-olcum.py` PASS |
| **F4 kanon revizyonu** | kök `AGENTS.md` yaz · `CLAUDE.md` symlink'leri · `jarvis/AGENTS.md` §1/§3/§7 · tüzük: 8 madde pointer + m.41/m.44 EK · defter: Karar 91 D `gecerli-bitis` · Karar 99 M1 yeniden · protokol §5 EK-2 tablo (Friday = `friday/` cwd oturumu, worktree **kapalı**; ~/sistem/jarvis yan oturumlar worktree **açık**) · Friday `AGENTS.md` (kanon yolu kök; `.claude/**` Edit-usulü satırı) · K1 kapısı `friday/` commit'lerini tanır · `README.md` harita | Jarvis yazar, Salih imzalar (masa-15 tek kalem "kanon paketi") | `kural-sayaci.py` ≤100 · kök md ≤25 satır · `ad-esitligi-denetim.py` PASS |
| **F5 kanıt** | `~/sistem/jarvis` ve `~/sistem/friday` oturumları açılır; `talimat-yukleme-olay.jsonl`: Friday oturumunda jarvis satırı **0** (geri-açma koşulu) · hook echo ile hangi `settings.json`'ın yüklendiği görülür (bilinmeyen tek nokta: alt-dizin cwd'si kendi `.claude/`'ını mı, git kökünü mü yükler; dispatcher iki durumda da çalışır) · Friday tur-6 emri `send_message` ile · A2 kilit testi iki dizinde | Salih açar, Jarvis ölçer | kanıt tablosu `raporlar/2026-09/sistem-monorepo-kanit-2026-09-18.md` |

Sıra: F1 → F2 → F3 → F4 → F5; F2 gününde iki ajan da durur (Friday tur-5 bitmiş olmalı). Onarım kuralı: F3 testleri kırmızıysa F4'e geçilmez; F5 jarvis satırı > 0 ise izolasyon yeniden (Karar 101 geri-açma).

## 5. F2 komut listesi (Salih eli; her satır tek Run)
```bash
# 0) tüm Claude Code oturumları kapalı; guvenlik-2 worktree'si: cd ~/jarvis && git worktree remove --force .claude/worktrees/2026-09-15-guvenlik-2-4bfcd1 && git worktree prune
```
```bash
cd ~ && mv jarvis sistem && cd sistem && mkdir jarvis
```
```bash
# tracked içerik → jarvis/ (ogrenme ve .gitignore kökte kalır; liste F1 kuru koşumundan üretilir, buraya yapıştırılır)
git mv CLAUDE.md KILAVUZ.md README.md fikir-kutusu.md core kuyruk cc veri tools raporlar wiki arsiv graf kaynak-kodu paylasim .claude .mcp.json jarvis/ 2>&1 | tail -3
```
```bash
# untracked büyük veri ve yerel dizinler
mv .venv .lavish .obsidian jarvis/ 2>/dev/null; ls jarvis/kuyruk/galeri-siralama | head -2
```
```bash
git commit -m "[icra] Move Jarvis agent tree under jarvis/ (Decision 101 monorepo 'sistem')"
```
```bash
git subtree add --prefix=friday ~/friday main -m "[icra] Import Friday agent tree with history (Decision 101)"
```
```bash
rm friday/kanon && git add friday && git commit -m "[icra] Retire friday/kanon symlink (canon read from repo root, Decision 101)"
```
GitHub: Settings → Rename → `sistem`; sonra `git remote set-url origin https://github.com/salihsahinin/sistem.git`. Eski `~/friday` → `mv ~/friday ~/arsiv-friday-2026-09-18` (F5 kanıtından sonra silinebilir, m.8: arşiv). Masaüstü uygulamada iki proje: `~/sistem/jarvis` (worktree kapalı) ve `~/sistem/friday` (worktree kapalı).

## 6. Firstmate'ten alınan / alınmayan
Alınan: (1) `CLAUDE.md → AGENTS.md` symlink, tek kaynak · (2) sahiplik yönlendirme tablosu · (3) emirde makine-okur sözleşme satırı (A1 `GİT_İZNİ/PUSH/KARAR_YETKİSİ` zaten var; spawn-önü uyuşmazlık reddi `devir-md2json --dogrula`) · (4) tek-satır durum kanalı `cc/giden/<devir_id>.status` (`working · needs-decision · blocked · done · failed`, keyed açık/kapalı) — İB adayı, F5 sonrası · (5) öncelik + "asla genişletme" paragrafı. Alınmayan: şekil-temelli delegasyon reddi (Jarvis'in kendi alt-ajanlarını kilitler) · watcher `state/` yüzeyi (çoklu-backend gözetimi için) · 65 KB kök dosya (bizde ≤25 satır + bölüm-başına dosya).

## 7. Riskler (ölçülü)
- Alt-dizin `settings.json` yükleme davranışı `[?]` → dispatcher hook iki durumda da çalışır; deny listesi hook'ta zorlanır, `permissions.deny` yedek.
- Proje anahtarı değişince eski transkriptler K1 kapısından düşer; hareket kütüğü bronzu zaten repoda (kayıp yok).
- İki ajan aynı `main`'de: pathspec disiplini (H4) tek fren; çakışma yalnız aynı dosyada, dizinler ayrık.
- `git mv` + `subtree` geri alınabilir (tek commit revert); GitHub yeniden adlandırma yönlendirme bırakır.

## 8. Genişleme notu (Salih 09-18, Karar 101 EK) + F1 sonuçları
- **Harness ve backend sayısı artacak; öğrenme borcu Salih'in.** Tasarım kapıları açık: kök kanon `AGENTS.md` (Karar 47 08-21 doğrulaması: Claude Code `AGENTS.md` okumaz, yalnız `CLAUDE.md`; symlink `CLAUDE.md → AGENTS.md` tam bu yüzden — Claude `CLAUDE.md`'yi, Codex/başka harness `AGENTS.md`'yi okur, tek metin) · dispatcher yalnız cwd + stdin + dosya kullanır · dönüş kanalı dosya (her backend yazabilir) · firstmate 1./2. deseni **ertelendi**, tetik = ikinci harness/backend fiilen kurulunca; o gün ders şeridi adayı (`ogrenme/`).
- **F1 çıktıları (09-18):** `tools/yol-tasi.py` (kuru koşum: 31 dosya · 83 satır; 8 tools + 2 Jarvis hook + 4 skill dosyası + Friday hook/test/ayar/CLAUDE.md; diff `raporlar/2026-09/yol-tasi-kuru-2026-09-18.diff`; Friday deny 15 satırı **bayraklı**, F3'te Edit ile tek `jarvis/**`) · `kuyruk/taslak-f1/hook-dispatch.sh` (mini hook-koşucu: ajanın kendi `settings.json` hooks kayıtlarını matcher'la koşturur; Jarvis 7 kayıt · Friday 2 kayıt değişmeden çalışır) · `kuyruk/taslak-f1/settings.kok.json` (kök: 5 olay + `InstructionsLoaded` → dispatcher; `permissions.deny` kökte yok) · kök `AGENTS.md` taslağı §2 · `jarvis/AGENTS.md` §1 taslağı §3. Mevcut `AGENTS.md` (Karar 47 statik levha, 2,1 KB) → `jarvis/AGENTS.md` olarak kalır ve F4'te canlı kanona döner (Karar 47'nin "ilk Claude-dışı ajan aracı" tetiği Salih'in çok-harness beyanıyla çekildi sayılır).
