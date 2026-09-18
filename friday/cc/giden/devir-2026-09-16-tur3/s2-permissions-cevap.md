# C1 — S2 kapanışı: `permissions.deny` Read/Bash için yol-bazlı kısıt verebiliyor mu? (Friday, AS-OF 2026-09-16)

**Etiketler:** D = birincil kaynakta doğrulandı · K = kısmen · X = bulunamadı/erişilemedi. Belge bir yeteneği **belgeler**; aşağıda "yeterlidir" cümlesi yok (D4).

## 0. Açılan sayfalar (B5: 1-derinlik kuralı)

| # | Adres | Derinlik | Sonuç |
|---|---|---|---|
| 1 | `https://docs.claude.com/en/docs/claude-code/permissions` | 0 (emir) | **301 → yönlendirildi:** `https://code.claude.com/docs/en/permissions` (tur-2 B4 kuralı) |
| 2 | `https://code.claude.com/docs/en/permissions` | 0 (hedef) | açıldı, tamamı okundu (704 satır) |
| 3 | `https://code.claude.com/docs/en/settings-reference` | 1 (sayfa 2'nin `blockReadsOutsideWorkingDirectories` bağlantısı) | açıldı, **kırpılmış döndü**: yalnız dizin satırı geldi, madde gövdesi gelmedi → K |

Daha derine inmedim: sayfa 3'ün önerdiği `llms.txt` 2. derinliktir ve alternatif adres sayılır (D1). Sayfa 2'nin bağlantı verdiği `sandboxing`, `hooks-guide`, `sub-agents` sayfalarını S2 için gerekmediği için açmadım.

---

## 1. Sonuç

| Yarı | Etiket | Belgenin söylediği |
|---|---|---|
| **Read** | **D** | Yol-bazlı `Read` deny belgeli; dört desen türü, gitignore sözdizimi, symlink davranışı tanımlı. |
| **Bash** | **D (sınırlı kapsamla)** | İki ayrı mekanizma belgeli: (i) `Bash(...)` kuralları **komut metnini** eşler, yolu değil — belge bunun güvenlik sınırı olmadığını açıkça yazıyor; (ii) **`Read` deny kuralları** Bash'te tanınan dosya komutlarına (`cat`, `head`, `tail`, `sed`, `tee`) ve yönlendirme hedeflerine uygulanıyor — ama dosyayı adıyla anmayan komutlara ve alt süreçlere uygulanmıyor. |
| **S2 bütün** | **D** | Tur-2'deki K kapanıyor: iki yarı da belgeli. D2 dalı (Read var ∧ Bash yok → K) tetiklenmedi, çünkü Bash yarısı da belgelenmiş — sınırlarıyla birlikte. |

---

## 2. Kanıt (alıntılar ≤15 kelime, kaynak: `https://code.claude.com/docs/en/permissions`)

**Read yol-bazlı deny:**
> "add a `Read` deny rule for its path, such as `Read(./.env)`"

Desen türleri (belgedeki tablo, özet):

| Desen | Anlamı | Belgedeki örnek |
|---|---|---|
| `//path` | dosya sistemi kökünden mutlak | `Read(//Users/alice/secrets/**)` |
| `~/path` | ev dizininden | `Read(~/Documents/*.pdf)` |
| `/path` | ayar kaynağına göre | `Edit(/src/**/*.ts)` |
| `path` / `./path` | geçerli dizine göre | `Read(*.env)` |

Tuzak (tur-2'de sezdiğim anchor belirsizliği burada kapanıyor):
> "A pattern like `/Users/alice/file` isn't an absolute path."

**Bash'te Read deny'nin kapsamı:**
> "file commands Claude Code recognizes in Bash, such as `cat`, `head`, `tail`"

Kapsam dışı:
> "a Python or Node script that opens files itself"

ve `grep -r pattern .` gibi dosyayı adıyla anmayan komutlar.

**`Bash(...)` kurallarının niteliği:**
> "isn't a security boundary around the program"

Belgenin önerdiği iki alternatif: işletim sistemi düzeyinde sandbox ve metni kendi mantığıyla denetleyen PreToolUse hook'u:
> "To inspect the full command text with your own logic … use a PreToolUse hook"

**Hook ile deny'nin ilişkisi (okuma-izin.sh için belirleyici):**
> "A hook that exits with code 2 stops the tool call before permission rules"

ve ters yönde:
> "Hook decisions don't bypass permission rules."

Yani ikisi **yan yana** çalışabilir: hook exit 2 önce keser; hook geçirirse deny kuralları yine uygulanır.

**Symlink — `kanon/` için belirleyici:**
> "Deny rules: apply when either the symlink path or its target matches."

**`!` istisnasının sınırları:**
> "the pattern can't reach a rule anchored with one of those prefixes"

(`/`, `~/`, `//` ile başlayan kurallar için) ve
> "A carve-out can't reopen a file inside a directory that a rule blocks"

**`blockReadsOutsideWorkingDirectories` (K — yalnız dizin satırı okunabildi, `settings-reference`):**
> "Make the file tools refuse reads outside the working directories"

Bash'i kapsayıp kapsamadığı, `additionalDirectories` ile nasıl birleştiği ve symlink davranışı madde gövdesinde — o gövde gelmedi.

---

## 3. Deny kuralı metni — **öneri** (`settings.json`'a dokunmadım; D-KATMAN1 → kural adayı)

### 3a. Belgeye göre **işlemeyen** biçim — tek satır

```json
"deny": ["Read(~/jarvis/**)"]
```

Bu kural `kanon/`'u da keser. Nedeni: `kanon` bir symlink, hedefi `~/jarvis/core`; belge, deny kuralının "symlink yolu **ya da** hedefi" eşleşince uygulandığını söylüyor. `Read(!~/jarvis/core/**)` ile istisna da kurulamıyor: belge, `!` deseninin `~/` ile başlayan bir kurala ulaşamayacağını ve engellenmiş bir dizinin içini yeniden açamayacağını söylüyor. Sonuç: Friday kanonsuz kalır.

### 3b. Belgeye göre **işleyen** biçim — alt dizinleri tek tek sayan liste

Jarvis üst düzeyindeki girdiler için kaynak, kapalı-göz özeti: kök README klasör haritası (`cc/gelen/devir-2026-09-09-parti5-envanter.md`, AS-OF 2026-09-09). `core/` listede **yok**:

```json
"deny": [
  "Read(~/jarvis/CLAUDE.md)",
  "Read(~/jarvis/KILAVUZ.md)",
  "Read(~/jarvis/README.md)",
  "Read(~/jarvis/fikir-kutusu.md)",
  "Read(~/jarvis/kuyruk/**)",
  "Read(~/jarvis/raporlar/**)",
  "Read(~/jarvis/cc/**)",
  "Read(~/jarvis/wiki/**)",
  "Read(~/jarvis/veri/**)",
  "Read(~/jarvis/tools/**)",
  "Read(~/jarvis/.claude/**)",
  "Read(~/jarvis/kaynak-kodu/**)",
  "Read(~/jarvis/ogrenme/**)",
  "Read(~/jarvis/arsiv/**)",
  "Read(~/jarvis/graf/**)"
]
```

Belgelenen kazanç: `cat`/`head`/`tail`/`sed`/`tee` ve `< dosya` yönlendirmeleri de kapsanıyor; deny kuralları klasör-güvenini beklemiyor (tur-2 R2); hook geçirse bile deny uygulanıyor.

Belgelenen ve belgelenmeyen sınırlar — üçü de hook'un **yerine değil yanına** konmasını gerektiriyor:
1. **Liste bir inkâr listesi.** Jarvis'e yeni bir üst düzey dizin eklendiğinde kapsam dışı kalır. Hook ise bir izin listesi — kök dışı her şeyi keser. Bu fark belgede değil, liste mantığında (desen 20: listeyi hedefi gören taraf tazeler).
2. **`python`, `grep -r` ve dosyayı adıyla anmayan komutlar** kapsam dışı (belgeli). Hook'un Bash dalı bunları metin taramasıyla yakalıyor.
3. **`kanon/../kuyruk` gibi bağ-üstü göreli yollar:** belge symlink hedefini denetlediğini söylüyor, ama `..` çözümünün hangi sırada yapıldığını söylemiyor → `[?]`. Hook v0.2 bunu `realpath` ile çözüyor (satır 28).

### 3c. İzin listesi biçimi — belge adını veriyor, gövdesi okunamadı (K)

```json
"permissions": {
  "additionalDirectories": ["~/jarvis/core"],
  "blockReadsOutsideWorkingDirectories": true
}
```

Bu, hook'un mantığıyla (izinli kökler dışını kes) aynı biçimde bir **izin listesi** olurdu. Ama üç şey okunamadı: Bash'i kapsayıp kapsamadığı ("file tools" deniyor), `kanon/` symlink'inin hedefinin `additionalDirectories` içinde sayılıp sayılmadığı, ve `~/.claude/projects/...` (araç çıktılarının düştüğü yer) gibi Friday'in zaten okuduğu yolları kesip kesmediği. Gövde okunmadan öneri olarak bile güçsüz; bir sonraki turda `settings-reference` maddesi ayrıca açılabilir (açık soru).

---

## 4. Özet

- Tur-2'de K kalan **S2 artık D:** Read için yol-bazlı deny belgeli; Bash'te Read deny tanınan dosya komutlarını ve yönlendirmeleri kapsıyor, `Bash(...)` kuralları ise belgeye göre güvenlik sınırı değil.
- Tek satırlık kök reddi (`Read(~/jarvis/**)`) belgeye göre `kanon/`'u da keser; işleyebilen biçim alt dizin listesidir (3b) ve bir inkâr listesidir.
- Belgenin kendisi, hook ile deny kuralının **yan yana** çalıştığını tarif ediyor. `okuma-izin.sh` kalır; 3b onun arkasında ikinci katman olabilir — karar Salih'in (kural adayı).
