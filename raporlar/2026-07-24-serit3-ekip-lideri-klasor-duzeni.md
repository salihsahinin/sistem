# Şerit 3 — Ekip Liderleri: Ayrı Klasör mü, JARVIS İçine Gömülü mü? (Atlas Raporu, 2026-07-24)

> **Mod:** yan-oturum (m.41) — öneri üretir, kanon KİLİTLEMEZ. `core/` · `CLAUDE.md` · `.claude/` yazılmadı.
> **Soru (Salih, 07-24):** "İlerde tasarlayacağımız ekip liderleri için PC'de JARVIS gibi klasör mü oluşturacağız, yoksa JARVIS klasörünün içine gömülü mü olacaklar?"
> **Şerit:** çift-atlas · aile 3 · tez 3/3, antitez 1/3 (¬T3-A1 — belirleyici olan buydu)
> **Referans sürüm:** Claude Code 2.1.219 (bu makinede doğrulandı)
> **Kaynak dosyalar:** `scratchpad/T3-A{1,2,3}-seritA.md`, `T3-A1-seritB.md`

## 0. BLUF — cevap

**Gömülü düzen kazanıyor.** Ama başlangıçta sandığımız gerekçelerle değil, ve "gömülü" sözcüğünün doğru okunması şart:

> Liderler `.claude/agents/<lider>/` altına gömülür — `liderler/<ad>/` gibi sıradan bir alt klasöre **değil**. Bu ayrım her şeyi belirliyor: birincisi kökten açılan oturumda tam yükleniyor, ikincisi görünmüyor.

Ayrı repo yalnız **tek** koşulda haklı çıkar: bir liderin dışarı açılması (public) ya da sert bir güven sınırı gerekmesi. Bu bugün geçerli değil (m.14: bu repo CV'ye girmez, private).

**Ve karar ucuz:** gömülü→ayrı göç gerçek repomuzda ölçüldü — `subtree split` **0,483 sn**, ters yön **0,109 sn**, tarihçe korunuyor, çift yönlü. m.31'in "pahalı geri-alma" eşiği **tetiklenmiyor**. Yani bu bir Katman-1 ağırlığında kilitlenme değil; yanlış çıkarsa dönülür.

## 1. Süreç notu — bu şerit fikrini değiştirdi

Üç tez ajanının üçü de "ayrı klasör üstündür" tezini savunmakla görevlendirildi. İkisi **kendi tezini kısmen yıktı**, antitez kalanı yıktı. Bu, protokolün çalıştığının kanıtı ve raporun okunma biçimini belirliyor: aşağıdaki sonuç, aranan sonucun tersi.

- **T3-A3** kendi tezinin iki ayağını "TEZ ALEYHİNE" diye etiketledi.
- **T3-A2** dürüst sonucunu kendisi yazdı: *"ayrışma kazancı repo sınırında değil, üç ortogonal eksende elde ediliyor — üçü de tek repo içinde sağlanabilir."*
- **¬T3-A1** belkemiğini kırdı: *"İddiaların mekaniği neredeyse tamamen doğru; kırılan şey çıkarım."*

## 2. Düşen argümanlar (ayrı klasör lehine sanılan, ölçümde çöken)

| Argüman | Ne oldu | Kanıt |
|---|---|---|
| "Gömülü liderler görünmez" | **ÇÖKTÜ** — `.claude/agents/` **özyinelemeli** taranıyor; `.claude/agents/<lider>/` kökten açılan oturumda tam yükleniyor | ¬T3-A1 İ4 [D] |
| "Ayrı klasör bağlam izolasyonu verir" | **ÇÖKTÜ** — bağlam izolasyonu **çalışma-zamanı** özelliği, dosya-sistemi özelliği değil; alt-ajan aynı dizinde de temiz bağlamla başlar | T3-A2 İ1 [D] |
| "Lider-başına hook ayrı kök ister" | **ÇÖKTÜ** — hook'ların dört kaynağı var, biri ajan frontmatter'ı | ¬T3-A1 İ3 [D] |
| "Çok kök arama kaybı yaratır" | **ÇÖKTÜ** — ölçüldü: 10 ayrı kök 59 ms ≤ tek kök 69 ms; belirleyen kök sayısı değil içerik hacmi | T3-A3 İ10 [X] |
| "Boyut ayrışmayı gerektirir" | **ÇÖKTÜ** — depo 1,3 MB / 169 dosya; GitHub eşikleri 10 GB / dizin başına 3.000 girdi | T3-A3 İ12 [D] |
| "Kilit ancak ayrı kökte yapısal olur" | **ÇÖKTÜ** — proje kapsamında `/path` proje köküne çıpalanır (göreli, git'e girer); ayrıca `.claude/settings.local.json` 2.1.211'den beri **git repo köküne** çözülüp "herhangi bir alt dizin veya worktree" oturumunu kapsar | ¬T3-A1 İ1/İ11 [D] |

Son satır argümanı **tersine çeviriyor**: repo-geneli kilit mirası **yalnız tek repo içinde** var. Ayrı repolara bölersek bu mekanizmayı kaybederiz.

## 3. Ayakta kalan gerçek maliyetler

### 3.1 Ayrı klasörün bedeli
- **Kanon mirası kaybı.** `--add-dir` ile bağlanan dizinin CLAUDE.md, kuralları ve becerileri **yüklenmez** — liderler birbirinin ve merkezin kanonunu göremez. *(T3-A2 İ7 [D])*
- **Yönetişim taşınmaz.** `--add-dir` ajan+skill yükler ama hook / deny / CLAUDE.md taşımaz; üstelik fırlatma-anı bayrağı ister, git'e işlenemez. *(¬T3-A1 İ5 [D])*
- **Hafıza parçalanır.** Ajan-başına kalıcı hafızanın satıcı tasarımı zaten repo içi: `.claude/agent-memory/<ajan>/`, önerilen kapsam `project` (sürüm kontrolüyle paylaşılabilir). Ayrı repo bunu böler. *(T3-A2 İ5, ¬T3-A1 İ9 [D])*
- **Wiki grafı bölünür.** `[[wiki-link]]` vault sınırını geçmez. Azaltma önerisi (vault kökünü liderlerin üstüne koymak) **test edilmedi** [çıkarım]. *(T3-A3 İ11 [D])*
- **Resmî ekip primitifi tek kök varsayıyor.** Takım üyeleri "the same project context as a regular session" yüklüyor. *(¬T3-A1 İ12 [D])*

### 3.2 Gömülü düzenin bedeli — ve çözümü
Üç ajanın bağımsız olarak yakınsadığı tek gerçek açık:

> **`.claude/settings.json` ata dizinden miras alınmaz.** Bir alt dizinden açılan oturum kökteki `Edit(core/**)` deny'ini ve `pretool-core-tel.sh` hook'unu **hiç yüklemez**. *(T3-A1 İ1, T3-A2 İ4, T3-A3 İ6 — üç bağımsız [D])*

Bu ciddi bir açık ama **ayrı repo argümanı değil**, çünkü ¬T3-A1 üç ayrı kapatma yolu buldu: (a) her alt dizine işlenen `.claude/settings.json` (proje kapsamlı, göreli, git'e girer — rehberin kendi reçetesi); (b) repo köküne çözülen `.claude/settings.local.json`; (c) ajan frontmatter'ındaki `disallowedTools` / `permissionMode`.

**Not:** (b) yolunun `--setting-sources` ile düşürülebilirliği ve `settings.local.json`'ın git'e girip girmeyeceği ayrı bir tasarım kararı — burada çözülmedi.

## 4. Ayrı klasörün ayakta kalan tek meşru gerekçesi

**Görünürlük repo-atomiktir.** Alt-dizin görünürlüğü yoktur; private bir repo public yapıldığında içindeki her şey görünür olur ve sızma geri alınamaz. *(T3-A3 İ8 [D])*

m.13 (tek-flagship), m.14 (bu repo private, CV'ye girmez) ve MASTER_PLAN karar 4 ile birlikte okununca: **bir lider ilerde dışarı açılacaksa o lider ayrı repoda doğmalı.** Bugün böyle bir lider yok.

## 5. Kanıt asimetrisi (dürüstlük şerhi)

T3-A2 önemli bir uyarı koydu: **repo-yerleşimi düzeyinde çok-repo'yu ölçen çalışma bulunamadı** [X]; tek-repo tarafında büyük şirket sayıları ve hakemli çalışmalar var. Yani "ayrı repo daha iyi" iddiası literatürde ölçülmemiş bir iddia; "tek repo çalışır" ise ölçülmüş.

Buna karşılık bellek-izolasyonu lehine ölçümler de var ([K], 403 nedeniyle birincile inilemedi): izolasyon bulaşmayı ajanların <%18'iyle sınırlarken paylaşımlı senkronizasyonda %61'e çıkıyor. **Ama** karşı-kanıt da var: paylaşılan çalışma alanı + yazma-anı çatışma tespiti, worktree-başına-ajan izolasyonunu bir kodlama ölçütünde +18,7 puan geçiyor.

**Bu çatışma çözülmedi.** İkisi de [K]. Ortalama almıyorum — bayrak olarak duruyor.

## 6. Öneri (karar Salih/ana-sırada)

**Önerilen düzen — "tek repo, üç eksende ayrışma":**

```
C:\JARVIS\
├─ core/                         ← kanon (kilitli)
├─ .claude/
│  ├─ settings.json              ← kök kilit
│  ├─ agents/
│  │   ├─ atlas.md
│  │   └─ <lider>/               ← özyinelemeli taranır, kökten görünür
│  │       └─ <lider>.md
│  └─ agent-memory/<lider>/      ← lider-başına hafıza, git'te, partisyonlu
└─ liderler/<lider>/             ← liderin ÇALIŞMA çıktıları (kanon değil)
```

Ayrışma üç eksende sağlanır, üçü de tek repo içinde: **bağlam** (alt-ajan zaten temiz pencereyle başlar) · **çalışma dizini** (gerekirse `isolation: worktree`) · **hafıza namespace'i** (`agent-memory/<lider>/`).

**Bölme tetiği (şimdi karar verme, koşul yaz):** bir lider (a) dışarı açılacaksa, ya da (b) sert güven sınırı gerektiriyorsa → o lider ayrı repoya çıkar. Göç 0,5 saniye ve tarihçe korunuyor.

**Kapatılacak açık:** alt-dizin oturumlarında `core/` kilidinin yüklenmesi. Üç yol var; hangisi seçilecek ana-sıra kararı.

## 7. Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. `.claude/settings.local.json` git'e girmeli mi? Repo-geneli kilidi veriyor ama yerel-ayar dosyası olarak tasarlanmış.
2. `--setting-sources` ile kilidin düşürülebilirliği kabul edilebilir bir risk mi, yoksa yalnız hook mu güvenilir sayılmalı?
3. Wiki vault kökünü liderlerin üstüne koyma önerisi test edilmedi — Obsidian'da fiilen çalışıyor mu?
4. ¬T3-A2 ve ¬T3-A3 antitezleri koşamadı (oturum limiti). Gömülü-düzen lehine bu sonuç **tek antitezle** kuruldu; ana-sıra bunu zayıflık olarak değerlendirmeli.
5. A5 (ekip-lideri hattı) bu bulguyla yeniden yazılmalı mı? Mevcut A5 metni "ayrı klasör" varsayımı taşımıyor ama tasarım paketi bu rapordan sonra kurulmalı.

---

*Yan-oturum çıktısı. Kanon kilitlenmedi. Karar ana-sırada (m.41).*
