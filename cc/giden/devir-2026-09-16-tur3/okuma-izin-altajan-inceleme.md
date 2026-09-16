# C2 — `okuma-izin.sh` işçi/alt-ajan çağrılarında da geçerli mi? (Friday, AS-OF 2026-09-16)

Kapsam: `.claude/hooks/okuma-izin.sh` v0.2 (47 satır), `.claude/hooks/okuma-izin-test.sh` (9 vaka), `.claude/settings.json` matcher satırı. **Statik okuma**; hook'u çalıştırmadım, sentetik girdi de vermedim (tur-2 cevabı B3: "Friday sınamasın"). Hook'a dokunmadım; aşağıdaki her değişiklik **öneri** kipindedir.
Belge kaynağı: `https://code.claude.com/docs/en/hooks` (tur-2'de açıldı; bu turda yeniden açmadım) + `https://code.claude.com/docs/en/permissions` (bu turda açıldı, bkz. C1).

---

## 1. Hook `agent_id` / `agent_type` alanlarını ele alıyor mu?

**Hayır.** Dosyada `agent` dizesi hiç geçmiyor (`grep -n agent` → 0 eşleşme). Girdiden okunan alanlar yalnız şunlar:

| Satır | Okunan |
|---|---|
| `okuma-izin.sh:20` | `tool_name`, `tool_input` |
| `okuma-izin.sh:32` | `tool_input.file_path`, `tool_input.path` (Read/Grep/Glob) |
| `okuma-izin.sh:34` | `tool_input.command` (Bash) |

Karşılaştırma: aynı repodaki `hareket-kutuk.sh:42` `agent_id` ve `agent_type`'ı **kaydediyor**. Yani Friday'de alt-ajan çağrısı bugün **gözlemleniyor ama ayrıca denetlenmiyor**. D3 dalı tetiklendi.

## 2. İşçi açıldığında kilit geçerli kalır mı? — **D (yol denetimi için) · K (alt-ajana özgü kısıt için)**

**Kilidin çalışması — D.** Hooks belgesi `agent_id` alanını şöyle tanımlıyor:
> "Present only when the hook fires inside a subagent call."

Yani hook'lar alt-ajan çağrısında da **tetikleniyor**; belge bunu alan tanımının ön koşulu olarak veriyor. Hook'un karar mantığı (`okuma-izin.sh:30-45`) yalnız araç adına ve yola bakıyor, çağıranın kim olduğuna bakmıyor. Bundan çıkan sonuç: bir işçinin Jarvis kanon-dışı yolu okuma denemesi, ana-sıradakiyle **aynı** koşulda exit 2 alır. Belge hook'un exit 2'sinin izin kurallarından önce kestiğini de belgeliyor (C1 §2).

**Alt-ajana özgü kısıt — K.** Kilit işçiye ana-sıradan **daha dar** bir alan tanımıyor. Jarvis'in İB-83 eşleniği (`pretool-altajan-okuma.sh`, tur-2 cevabı §0) alt-ajana ek bir yasak liste uyguluyor: transkriptler, kapsül/pano/defter/kutu, kütükler. Friday'de işçi bugün şu dosyaları okuyabilir: `core/durum-kapsulu.md`, `core/pano.md`, `kuyruk/*`, `veri/bronz/hareket-olay.jsonl`, `cc/gelen/*` (başka devirlerin emirleri dahil). Rol metni işçiye "karar yetkisi yok" ve "8 alanlı case" diyor (`core/rol.md` md.4), okuma kapsamı ise yazılı değil. Bunun bir açık mı, yoksa istenen bir durum mu olduğu Salih'in hükmüne bağlı → açık soru.

## 3. İşçi hâlinde de geçerli olan, alt-ajana özgü olmayan üç zayıflık (statik, sınanmadı)

**Z1 — Bash dalı bir izin listesi değil, Jarvis için bir inkâr listesi.** Başlık yorumu (`:4`) "izinli kökler … dışı → exit 2" diyor. Bu yalnız Read/Grep/Glob için doğru: `:31-32` adayları `izinli_mi()`'ye veriyor. Bash dalı (`:33-41`) ise yalnız Jarvis kökünün yazılışlarını ve `../` / `kanon/../` göreli çıkışlarını aday yapıyor. Sonuç: Bash ile repo dışı, **Jarvis olmayan** her yol (örneğin `~/staj başlangıç`, md.49 alanı) kilitten geçiyor. Aynı yol Read aracıyla istenseydi reddedilirdi. Bir işçi araç seçimiyle bu asimetriyi kullanabilir. Somut örnek: bu oturumda harness'in araç çıktısını yazdığı `~/.claude/projects/.../tool-results/` dosyasını Bash ile okudum ve geçti. Read aracıyla okusaydım `izinli` listesinde olmadığı için reddedilirdi (`:23`).

**Z2 — `cd` + göreli yol.** `:9` "`cd` ile dizin değiştirme Jarvis köküne yasak" diyor. `cd ~/jarvis` gerçekten yakalanıyor (`:36-37`, `KOK` deseni), ama ev dizinine geçip Jarvis'i göreli yolla anan bir komut ne `KOK` desenine ne `../` desenine uyuyor. Ayrıca göreli yollar her zaman **repo köküne** göre çözülüyor (`:28`); aynı komutun içindeki `cd`'yi hesaba katmıyor. Permissions belgesi de aynı sınıfı kendi kuralları için ayrı bir durum olarak ele alıyor:
> "a relative path that follows a `cd` in the same command, needs your approval"

**Z3 — Dize kurgusu.** Tarama komut **metnine** bakıyor. Yol, bir kabuk değişkeni ya da birleştirmeyle çalışma anında kurulursa metinde görünmez. Belge `Bash(...)` kuralları için aynı sınıfı "security boundary" olmamakla anlatıyor (C1 §2). Hook da metin tabanlı olduğu için aynı sınırı taşıyor.

Test kapsamı: `okuma-izin-test.sh` 9 vaka taşıyor (`:8-16`). Hiçbiri `agent_id` içeren bir girdi, Z1 (Jarvis olmayan repo dışı yol, Bash), Z2 (`cd` + göreli) ya da Z3 değil.

---

## 4. Değişiklik önerileri (hook'a dokunmadım; D-KATMAN1 → kural adayı)

Her seçenek: ne demek · ne yaparım · artı · eksi. Önerilen ilk sırada.

**Ö1 (önerilen) — Test dosyasına 4 vaka ekle, kodu değiştirme.**
- *Ne demek:* Z1–Z3 ve alt-ajan hâli için sentetik girdiyle beklenen exit kodunu yaz. Örnek: `{"agent_id":"a1","agent_type":"general-purpose","tool_name":"Read","tool_input":{"file_path":"<Jarvis kuyruk yolu>"}}` → 2.
- *Ne yaparım:* Vaka metnini Jarvis'e öneri olarak veririm; koşumu Jarvis yapar (yapan ≠ ölçen, tur-2 B3).
- *Artı:* "işçi hâlinde de geçerli" iddiası ölçülmüş olur; Z1–Z3'ün gerçek olup olmadığı kod değişmeden görülür.
- *Eksi:* Açığı kapatmaz, yalnız görünür kılar.
- *Gerekçe:* Z1–Z3 benim statik okumam; önce ölçülmeleri gerekiyor.

**Ö2 — Bash dalını izin listesine çevir (Z1).**
- *Ne demek:* `:33-41`'de, `/` ya da `~` ile başlayan **her** yol belirtecini aday yap ve `izinli_mi()`'ye ver. Belirteç çıkarma için `hareket-kutuk.sh` v0.3'teki ayrıştırıcı zaten var.
- *Artı:* Read ile Bash arasındaki asimetri kapanır; staj alanı (md.49) da Bash yoluyla kapanır.
- *Eksi:* Yanlış-pozitif riski yüksek. `/usr/bin`, `/dev/null`, `~/.claude/projects` (harness araç çıktısı), `/opt/homebrew` gibi yollar izin listesine eklenmeli. Bu oturumda harness'in araç çıktısını okuma yolu kesilebilir. İzin listesi büyüdükçe denetimi zorlaşır.

**Ö3 — Alt-ajana ek yasak liste (İB-83 eşleniği).**
- *Ne demek:* `g.get("agent_id")` doluysa `izinli` listesinden şu yollar düşer: `core/durum-kapsulu.md`, `core/pano.md`, `kuyruk/`, `veri/bronz/`, `cc/gelen/` (işçinin kendi devir birimi hariç), `~/.claude/projects`.
- *Artı:* Jarvis ile simetrik olur; işçi, liderin hafızasını bağlamına çekemez.
- *Eksi:* İşçi case şablonu bugün işçiye hangi dosyaları okutacağını açıkça yazıyor, ama bu listenin hangi dosyaları meşru saydığı yazılı değil. Yanlış kurulursa işçi kendi girdisini okuyamaz. Friday bugün işçi açmıyor (Karar 89 öngörüyor), dolayısıyla canlı veri yok.

**Ö4 — `permissions.deny` alt dizin listesiyle ikinci katman (C1 §3b).**
- *Artı:* Tanınan Bash dosya komutlarını ve yönlendirmeleri de belgelenmiş biçimde kapsıyor. Ayar kaynağı alt-ajan için ayrı değil, dolayısıyla işçide de geçerli olması beklenir.
- *Eksi:* Belgede "izin kuralları alt-ajanlara uygulanır" diye açık bir cümle bulamadım `[?]` — permissions sayfasının Agent bölümü yalnız hangi alt-ajanın **açılabileceğini** düzenliyor (`Agent(Explore)`). Ayrıca bir inkâr listesi.

**Sıra önerisi:** Ö1 → (sonuca göre) Ö2 ∨ Ö4 → Ö3 (ilk işçi koşumundan önce).
