# C5 — Uygulama raporu (Friday, AS-OF 2026-09-18; devir-2026-09-18-tur4, Karar 99 M2/M3/M4)

Bu bir uygulama turudur: üç değişiklik yapıldı, her biri koşumla kanıtlandı. `ÖLÇEN` alanı gereği testleri ve canlı denemeyi Jarvis yeniden koşar.

## 1. Diff özeti

| Çıktı | Dosya | Değişim |
|---|---|---|
| C1 | `.claude/hooks/okuma-izin.sh` | +96 / −23 civarı (git: 96 eklenen satır bloğu) — v0.2 → v0.3 |
| C2 | `.claude/hooks/okuma-izin-test.sh` | +35 — 9 vaka → 22 vaka |
| C3 | `.claude/settings.json` | +17 — deny 5 satır → 20 satır |
| C4 | `core/desenler.md` | +1 — desen 21 eklendi, toplam 21 madde |

`git diff --stat` çıktısı: `4 files changed, 126 insertions(+), 23 deletions(-)`.

## 2. C1 — hook v0.3: ne değişti

1. **Alt-ajan dalı (Karar 99 M2).** Girdide `agent_id` varsa ek yasak liste uygulanır: `core/durum-kapsulu.md` · `core/pano.md` · `kuyruk/senaryo-defteri.md` · `kuyruk/fikir-kutusu.md` · `veri/bronz/**` · `~/.claude/projects/**`. Muafiyet: `~/.claude/projects/**/tool-results/**` — alt-ajanın kendi araç çıktısı. Ana-sıra çağrısı (`agent_id` yok) bu daldan geçmez; davranışı değişmedi (test vakası var).
2. **Z1 onarımı.** Bash dalı artık izin listesi: ev dizini altındaki her yol belirteci izinli köklere göre denetleniyor. Ev dizini dışındaki sistem yolları (`/usr`, `/bin`, `/opt` …) serbest bırakıldı; kilidin konusu kullanıcı verisi. Böylece `~/staj …` gibi repo dışı ev yolları Bash'ten de kapandı ve Read ile Bash arasındaki asimetri kalktı.
3. **Z2 onarımı.** Aynı komuttaki `cd` izleniyor; göreli yollar repo köküne değil o anki dizine çözülüyor. `cd ~ && cat jarvis/...` artık yakalanıyor.
4. **Z3 kısmen (K).** Yol dizesi çalışma anında kuruluyorsa metin taraması göremiyor. İki alt vakaya ayrıldı: ev kökü metinde görünüyorsa (`~/$J/...`) kapanıyor; yolun tamamı bir değişkende kuruluyorsa kapanmıyor. Bu, metin tabanlı taramanın belgelenmiş sınırı — permissions belgesi aynı sınıfı `Bash(...)` kuralları için "isn't a security boundary around the program" diye anlatıyor. D3 gereği bir deneme yapıldı, tam kapanmadı → **K**, neden: kapatmak için işletim sistemi düzeyinde sandbox ya da komut çalıştıktan sonra denetim gerekir; ikisi de bu emrin dışında (kural adayı).
5. **Örnek koddan bilerek ayrıldığım nokta.** `cc/gelen/ornek-jarvis-pretool-altajan-okuma.sh:48`'de `exit 2` bloğu test bayrağının içinde: bayrak export edilince kilit yalnız kütüğe yazmıyor değil, **kesmiyor** da. Friday v0.3'te bayrak yalnız kütük yazımını kapatıyor, `exit 2` kararı bayraktan etkilenmiyor. Bu, o dosyanın Jarvis'teki aslını da ilgilendirir (geri-dönüşte kural adayı).

## 3. C2 — test çıktısı (aynen, `bash .claude/hooks/okuma-izin-test.sh`)

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
--------
PASS 22 · FAIL 0
```

İlk koşumda Z3 vakası `FAIL` verdi: beklenen 0 yazmıştım, kilit 2 döndürdü. Sebep bir hata değil, beklentimin dar olmasıydı — `~/$J/...` biçiminde ev kökü metinde görünüyor ve izin listesi onu zaten kesiyor. Vaka gerçeğe göre ikiye ayrıldı; kodda düzeltme yapılmadı.

**Test bronz kütüğe yazmıyor:** koşumdan sonra `veri/bronz/` içeriği yalnız `hareket-olay.jsonl`; `altajan-okuma-olay.jsonl` oluşmadı.

## 4. C5 canlı denemeler

**(a) Yasak yolu `Read` ile deneme — D.** `Read /Users/HasanSalihSahin/jarvis/kuyruk/senaryo-defteri.md` çağrısı reddedildi. Dönen hata:

> "File is in a directory that is denied by your permission settings."

Bu, hook'un stderr metni değil; reddin kaynağı **izin ayarı**. İki şeyi gösteriyor: deny bloğu bu oturumda yeniden başlatma olmadan etkin, ve `Read` için yol denetimi PreToolUse hook'undan önce uygulanıyor. (Aynı yolu hook da keserdi; hangisinin önce davrandığını ancak mesaj metni ayırt ettiriyor.)

**(b) `kanon/` hâlâ okunuyor — D, D2 tetiklenmedi.** Deny bloğu eklendikten sonra `Read kanon/tuzuk-v0.md` çalıştı (dosyanın ilk satırları geldi), `sed` ile Bash okuması da çalıştı. Beklendiği gibi: deny listesinde `core/` satırı yok ve tek satırlık kök reddi kullanılmadı. D2 dalı gerekmedi, geri alma yapılmadı.

**(c) Alt-ajan `RED` olayı kütüğe düşüyor — D.** Gerçek kütüğü kirletmemek için geçici bir repo kökü (`CLAUDE_PROJECT_DIR=/private/tmp/friday-hook-kanit`) ile, bayraksız koşuldu:

```
ALT-AJAN OKUMA KİLİDİ (Karar 99 M2): işçi, liderin bağlam penceresini okuyamaz (…). Reddedilen: /private/tmp/friday-hook-kanit/core/durum-kapsulu.md
exit=2
{"ts": "2026-09-18T11:24:03+03:00", "oturum": "s1", "agent_id": "a9", "agent_type": "general-purpose", "arac": "Read", "reddedilen": ["/private/tmp/friday-hook-kanit/core/durum-kapsulu.md"], "kaynak": "okuma-izin.sh v0.3"}
```

Gerçek `veri/bronz/` bu koşumdan etkilenmedi.

**(d) Beklenmedik yan etki — v0.3'ün yanlış-pozitif maliyeti.** Koşum sırasında kendi komutlarımdan biri kilide takıldı: komutun sonunda bir `grep` **deseni** olarak Jarvis kökü geçiyordu. v0.2'de bu yalnız kütüğe yol gibi düşüyordu (tur-3 F6); v0.3'te izin listesi olduğu için çağrı **durdu**. Yani ayrıştırıcının desen dizesini yoldan ayırt edememesi artık bir maliyet doğuruyor. Üç seçenek — hüküm Salih'in:
- *Bırak:* güvenli yönde hata; bedeli, yasak yolu metninde anan komutun yeniden yazılması.
- *Tırnak içi `grep`/`sed` desenlerini atla:* yanlış-pozitif düşer, ama `cat "$dosya"` gibi tırnaklı gerçek yollar da atlanır — yanlış-negatif riski.
- *Yalnız dosya komutlarının argümanlarını tara:* daha isabetli, ayrıştırıcı karmaşıklığı artar.

## 5. Ne yapılmadı

- `permissions.additionalDirectories` / `blockReadsOutsideWorkingDirectories` (tur-3 C1 §3c) — emrin dışında, dokunulmadı.
- `settings.json`'da emir dışı hiçbir anahtar değişmedi: mevcut 5 deny satırı ve iki hook kaydı yerinde, yalnız 15 satır eklendi.
- Z3b (yolun tamamı değişkende) kapatılmadı — K, gerekçesi §2.4.
