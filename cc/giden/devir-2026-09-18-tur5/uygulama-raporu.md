# C4 — Uygulama raporu (Friday, AS-OF 2026-09-18; devir-2026-09-18-tur5, Karar 100 M1/M3/M4)

İkinci uygulama turu. Üç değişiklik, hepsi testli ve iki canlı kanıtlı. Doğrulama `ÖLÇEN` alanına göre Jarvis'te.

## 1. Diff özeti

| Çıktı | Dosya | Değişim |
|---|---|---|
| C1 | `.claude/hooks/okuma-izin.sh` | +112 / −36 bloğu — v0.3 → v0.4 |
| C2 | `.claude/hooks/okuma-izin-test.sh` | +10 — 22 vaka → 30 vaka |
| C3 | `CLAUDE.md` | +11 / −8 satır bloğu — 4.195 B → **4.090 B** (bütçe 4.096) |
| — | toplam | `3 files changed, 97 insertions(+), 36 deletions(-)` (C3'ün son iki kısaltması hariç) |

## 2. C1 — ayrıştırıcı v0.4 (Karar 100 M1, tur-4 §4d seçeneği (c))

**Ne değişti.** Bash dalında yol adayları artık komutun tamamından değil, **dosya açan komutların argümanlarından** toplanıyor. Hook başında tek küme: `cat sed head tail less more cp mv ln rm python3 python bash sh source . jq sqlite3 wc sort uniq diff open code ls find awk grep rg egrep fgrep tee touch mkdir stat file md5 shasum nl cut`. Emrin saydığı liste asgariydi ("en az bunlar"); `ls`, `find`, `grep` ailesi ve birkaç okuma komutu eklendi — `ls ~/jarvis/cc` gibi mevcut vakalar aksi hâlde kapsam dışı kalırdı.

**Desen argümanı ayrımı.** `grep rg egrep fgrep sed awk jq find` için ilk sözcük-argüman desen ya da betiktir, yol sayılmaz. `-e -f --regexp --file --include --exclude -name -iname -path` bayraklarının değeri de atlanır. Böylece tur-4'te çağrımı durduran `grep '<yasak yol>' dosya` biçimi geçiyor, ama `grep -r m.8 <yasak dizin>` hâlâ kesiliyor — desen ile argüman ayrıldı.

**Tırnak ve değişken.** Argümanlar tırnaktan soyuluyor, yani tırnaklı açık yol yakalanmaya devam ediyor (D2 tetiklenmedi). Değişken içeren belirteçte `$`'tan önceki sabit önek denetleniyor: `~/$J/kuyruk` yakalanıyor, yolun tamamı değişkense (Z3b) görünmüyor — Karar 100 M5 gereği bu turda açık bırakıldı.

**Yönlendirme ve `cd`.** `>`, `>>`, `<` hedefleri komut kümesinden bağımsız olarak aday; `cd` takibi (v0.3) korundu.

## 3. C1 — alt-ajan dalına `cc/gelen/**` (Karar 100 M3)

`agent_id` varsa yasak listesi: kapsül · pano · defter · fikir kutusu · `veri/bronz/**` · **`cc/gelen/**`** · `~/.claude/projects/**`; muaf: `~/.claude/projects/**/tool-results/**`. Dal yalnız `agent_id` doluyken çalıştığı için liderin kendi emrini okuması etkilenmiyor — D3 iki yolla doğrulandı: test vakası (`lider (agent_id yok) kendi emrini okur → exit 0`) ve bu koşumun kendisi (tur-5 emri `cc/gelen/` altından okundu, kilit tetiklenmedi).

## 4. C2 — test çıktısı (aynen, 30 vaka)

```
-- v0.1 vakaları (ana-sıra) --
PASS  heredoc gövdesinde ~/jarvis dizesi → exit 0 (beklenen 0)
PASS  $HOME/jarvis/kuyruk okuma → exit 2 (beklenen 2)
PASS  kanon/../kuyruk bağ-üstü çıkış → exit 2 (beklenen 2)
PASS  kanon/tuzuk-v0.md okuma → exit 0 (beklenen 0)
PASS  ~/jarvis/core listeleme → exit 0 (beklenen 0)
PASS  ~/jarvis/cc listeleme → exit 2 (beklenen 2)
PASS  Read jarvis/kuyruk/pano.md → exit 2 (beklenen 2)
PASS  Read friday kendi dosyası → exit 0 (beklenen 0)
PASS  Grep jarvis/core (kanon hedefi) → exit 0 (beklenen 0)
-- v0.3 onarımları (tur-3 C2: Z1-Z2) --
PASS  Z1 Bash ile repo dışı ev yolu (staj) → exit 2 (beklenen 2)
PASS  Z1b Bash ile sistem yolu serbest → exit 0 (beklenen 0)
PASS  Z1c Bash ile harness araç çıktısı serbest → exit 0 (beklenen 0)
PASS  Z2 cd ev + göreli jarvis yolu → exit 2 (beklenen 2)
PASS  Z2b cd repo alt dizini + göreli yol → exit 0 (beklenen 0)
   NOT: Z3 iki alt vakaya ayrıldı — ev kökü metinde görünürse kapanıyor, yol tamamen değişkende kurulursa kapanmıyor (K).
PASS  Z3a dize kurgusu, ev kökü metinde → exit 2 (beklenen 2)
PASS  Z3b yolun tamamı değişkende (bilinen sınır) → exit 0 (beklenen 0)
-- v0.3 alt-ajan dalı (Karar 99 M2) --
PASS  agent_id + kapsül okuma → RED → exit 2 (beklenen 2)
PASS  agent_id + wiki/serbest dosya → geçer → exit 0 (beklenen 0)
PASS  agent_id + kendi tool-results → geçer → exit 0 (beklenen 0)
PASS  agent_id + defter (Bash) → RED → exit 2 (beklenen 2)
PASS  agent_id + bronz kütük → RED → exit 2 (beklenen 2)
PASS  ana-sıra + kapsül okuma → geçer (değişmedi) → exit 0 (beklenen 0)
-- v0.4 ayrıştırıcı (Karar 100 M1) ve cc/gelen yasağı (M3) --
PASS  grep DESENİNDE yasak yol → geçer → exit 0 (beklenen 0)
PASS  cat ile tırnaklı açık yasak yol → RED → exit 2 (beklenen 2)
PASS  grep ARGÜMANINDA yasak dizin → RED → exit 2 (beklenen 2)
PASS  sed betiği desen, dosya serbest → geçer → exit 0 (beklenen 0)
PASS  değişkenli yol (Z3b sınırı) → geçer → exit 0 (beklenen 0)
PASS  alt-ajan cc/gelen okur → RED → exit 2 (beklenen 2)
PASS  lider (agent_id yok) kendi emrini okur → exit 0 (beklenen 0)
PASS  alt-ajan kendi tool-results (Bash) → geçer → exit 0 (beklenen 0)
--------
PASS 30 · FAIL 0
```

Mevcut 22 vakanın hiçbiri bozulmadı → **D1 tetiklenmedi**. Koşum sonrası `veri/bronz/` yalnız `hareket-olay.jsonl` taşıyor: test bronz kütüğe yazmadı. Bayrak yalnız kütük yazımını kapatıyor, `exit 2` kararını değil (tur-4'te devralınan örnekten ayrıldığım nokta korundu).

## 5. Canlı kanıtlar

**(i) Desen içindeki yasak yol artık geçiyor — D.** Tur-4'te aynı biçimdeki komut kilide takılmıştı. Bu turda `grep -c "<yasak yol deseni>" core/pano.md` koştu ve sonucunu döndürdü (eşleşme yok, çıkış kodu 1); kilit devreye girmedi.

**(ii) Aynı yolu `cat` ile açan komut kesiliyor — D.** Tırnaklı, açık yazılmış Jarvis defter yolunu `cat` ile okumayı denedim; kilit kesti:

> "OKUMA-İZİN KİLİDİ (Karar 91): … Reddedilen yol: /Users/HasanSalihSahin/jarvis/kuyruk/senaryo-defteri.md"

İkisi birlikte, ayrıştırıcının artık desen ile argümanı ayırdığını gösteriyor: aynı dize, birinde metin, öbüründe yol.

## 6. Komut listesinin eksik kalabileceği durumlar (desen 20 kontrol listesi riski)

Bu tasarım bir inkâr listesinden bir tanıma listesine geçti, ama liste yine sonlu: kümede olmayan bir okuma yolu taranmadan geçer. Bugün bilinen boşluklar: `git show`/`git cat-file` ile depo içeriğini basmak, `docker`/`ssh`/`scp` gibi uzak çalıştırıcılar, `perl -ne`/`ruby -e` gibi satır-içi yorumlayıcılar (`python` kümede, ama `-c` ile gelen kod metni taranmıyor), `xxd`/`od`/`strings`, ve bir kabuk betiğinin içinden yapılan okumalar (`bash betik.sh` çağrısında betiğin **kendisi** denetleniyor, içeriği değil). Ayrıca kümedeki bir komutun beklenmedik bayrak biçimi (`--file=<yol>` gibi `=` ile birleşik değer) bugün ayrı bir belirteç sayılmıyor. Kural: yeni bir okuma komutu ya da yeni bir bayrak biçimi görüldüğünde küme tazelenir; tazelemeyi yapan taraf, listeyi gören taraftır (desen 20). Bu bir yetenek tarifidir, bir güvence değil.

## 7. C3 — `CLAUDE.md` Edit usulü satırı (Karar 100 M4)

§5'e tek satır eklendi: `.claude/**` ve `core/**` yazımı yalnız Edit aracıyla; Bash ile yazım sınıflandırıcıya takılır. Dosya emirden önce zaten bütçe üstündeydi (4.195 B / 4.096 B). "Bir satır girer, bir satır çıkar" kuralı gereği dört yer kısaltıldı (§0 girişi, §1 görev alanı, §3 kapsül maddesi, §4 ritüel satırı, §6 pointer) ve dosya **4.090 B**'ye indi. Hiçbir kural kaldırılmadı; yalnız tekrar ve vurgu biçimi budandı. Bu turda `.claude/**` ve `CLAUDE.md` yazımlarının tamamı düzenleme araçlarıyla yapıldı, Bash ile yazım denenmedi.
