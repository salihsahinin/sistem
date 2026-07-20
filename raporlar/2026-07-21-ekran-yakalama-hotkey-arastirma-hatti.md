# Ekran-Yakalama + Hotkey → Oto-Araştırma Hattı — Araştırma Raporu (yan-oturum)

> **Yüzey (m.41):** **Yan-oturum** (CC, Opus — Fable değil / "ana sıra" beyanı yok) çıktısı. Kanona DOKUNMAZ; imza masasına/ana-sıraya **aday**. Salih talebi ("ilerde bi klavye kısayolu… nasıl yapacağımı araştırıp rapor yaz"), 2026-07-21. Bu **fikir aşaması** — şimdi inşa YOK. Etiketler: **D**=birincil kaynak · **K**=arama/ikincil · **X**=doğrulanamadı.
>
> **Koşum:** 2 net-ayrık araştırma ajanı — Claude-tarafı (claude-code-guide) + Windows-tarafı (general-purpose, sonnet); toplam ~278k token / 63 araç-koşumu. Ajanlar bilerek örtüşmedi: Windows-tarafı `claude` CLI'yi kara-kutu saydı, Claude-tarafı yakalama araçlarını kapsam-dışı bıraktı. Bu rapor ikisini **diker**.

---

## 1. Carvis sentezi — uçtan uca önerilen hat

**Vizyon (Salih):** spesifik bir ekran görüntüsü al → kısayola bas → not-kutusu açılır → bağlamı yaz → Carvis o bağlamda araştırıp rapor üretir.

**Önerilen yığın:** **ShareX** (hotkey + bölge-yakalama + otomatik PNG kaydı + ardından program çalıştırma) **+ AutoHotkey v2** (not-kutusu + `claude` çağrısı + raporu açma) **+ headless `claude -p`** (görseli Read, WebSearch ile araştır, raporu Write ile yaz).

**Uçtan uca akış:**
```
[Ctrl+Shift+J]  →  ShareX bölge-yakala  →  PNG'yi C:\shots\...png'ye kaydet
                                          →  "Perform actions": AHK script'i "$input"(=PNG yolu) ile çağır
        AHK: InputBox not-kutusu  →  Salih bağlamı yazar
                                  →  claude --bare -p "<PNG'yi oku> + <not> → araştır → raporu yaz"
                                        --allowedTools "Read,WebSearch,WebFetch,Write" --permission-mode dontAsk
                                  →  Claude raporu C:\JARVIS\raporlar\yakala-<stamp>.md'ye Write eder
        AHK: Run(reportPath)  →  rapor açılır
```

**Dikişin kilit noktası:** Windows-tarafı ajanı glue script'inde `claude` çağrısını "TODO/placeholder" bıraktı (kara-kutu olduğu için). Claude-tarafı ajanı tam o komutu verdi. Birleşince (bölüm 5'teki iskelet):
- **Görsel girişi:** ekran görüntüsünün **yolunu prompt metnine** yaz + `Read` aracını allow-list'e ekle → Claude Read'i çağırıp görseli görsel-içerik olarak modele verir; base64'ü Claude Code kendi yapar, sen yapmazsın. (D — headless'ta drag/paste **interaktif-only**; güvenilir tek yol budur.)
- **Araştırma:** `WebSearch`/`WebFetch` allow-list'te → gömülü, ekstra API-key/tool kurulumu gerekmez.
- **Rapor:** prompt'ta "raporu şu dosyaya Write et" de → Claude'un kendisi dosyayı yazar (stdout parse'a gerek yok).
- **Gözetimsiz güven:** `--permission-mode dontAsk` → oturum asla girdi beklemez, allow-list dışı her şey **sessizce reddedilir** (takılmaz da). `bypassPermissions`'tan güvenli.

**Auth çatalı (karar gerektirir):** `--bare` script'ler için önerilen mod AMA OAuth/keychain okumaz → **`ANTHROPIC_API_KEY` şart** (per-token faturalandırma). Abonelik (Pro/Max) kotasını kullanmak istersen `--bare` KULLANMA + `claude setup-token` (uzun-ömürlü OAuth token). Yani: hız/determinizm → `--bare`+API key; abonelik kotası → bare'siz+setup-token. (D)

---

## 2. JARVIS yerleşimi — governance (m.30 / m.42 / K-009 / K-010)

Bu hat teknik olarak fizibıl; asıl mesele **hangi otomasyon sınıfına** girdiği. Üç bağ:

**(a) m.30 çizgisi — yarı vs tam otomatik.** m.30 ek fıkrası: *"otomasyon = tetik devrine kadar / canlı ajan = prompt+kimlik devri; PreToolUse ön-koşulu."*
- **Yarı-otomatik** (hotkey PNG'yi yakalar + not-kutusu açar; Salih notu girer, koşumu görür/onaylar) = **m.30 otomasyonu, ŞİMDİ serbest.** İnsan halkada.
- **Tam-otomatik** (hotkey → `dontAsk` ile habersiz araştırma, insan yok) = Salih'in kimliği/auth'u altında özerk davranan araştırma ajanı = **"prompt+kimlik devri"ne yaklaşır → K-010/canlı-ajan kapısı** (K-010 sicil sayacı bu gece başlıyor, ön-koşul 2 hafta sorunsuz temel). Yani tam-otomatik sürüm K-010 olgunlaşana kadar beklemeli.

**(b) PreToolUse yakınsaması (dikkat çekici).** Claude-tarafı ajanı bağımsızca buldu: *"`PermissionRequest` hooks don't fire in `-p` mode; use `PreToolUse` hooks for automated permission decisions"* (D). Bu, m.30'un yazdığı **"PreToolUse ön-koşulu"** ile birebir örtüşüyor — JARVIS kanonunun seçtiği mekanizma, Claude Code'un gerçekliğinin dayattığı mekanizmayla aynı çıktı. m.30 ön-koşulu isabetliymiş.

**(c) m.42 zarfı.** `dontAsk` + **dar allow-list** (`Read,WebSearch,WebFetch,Write` — **Bash YOK**) tam olarak m.42: *pozitif yetki listesi* + *katı-başlangıç* + *Özgürlük(a) ≤ Toparlanabilirlik(hata(a))*. Araştır+yaz düşük-hasar/geri-alınabilir; Bash saldırı yüzeyini ve geri-alma maliyetini büyütür → dışarıda kalır. Ayrıca hat **güvenilmeyen web içeriği** yutacak (prompt-injection vektörü) → dar allow-list bu yüzden güvenlik zarfı, süs değil. `.git`/`.claude` "protected paths" `bypassPermissions` dışı her modda otomatik korunuyor (ek katman).

**Kardeş/arka-uç bağları:**
- **SES-POC kardeşi:** bu, çalışan sesli-PoC'un (pasif toplama) **görsel** kardeşi — ikisi de "an + bağlam → Carvis" yakalama hattı. Ortak altyapı/felsefe paylaşabilir.
- **atlas-kosum arka-ucu:** `claude -p "…araştır…"` adımı, prompt'a `/atlas-kosum` (ya da bugün konuştuğumuz multi-hop diyalektik) koyarak doğrudan araştırma-makinesini çağırabilir. Bu hat = **ön-uç tetik**, atlas-kosum = **arka-uç motor**.

---

## 3. Windows-tarafı bulgular (tesisat)

**Global hotkey:**
- **AutoHotkey v2 = en sağlam** (D): keyfi kombinasyon (`^`Ctrl `!`Alt `+`Shift `#`Win) `::` ile bağlanır, gövdede `Run()`/`RunWait()`. Klasör kısıtı yok, 2-3 satır.
- PowerToys Keyboard Manager (D): GUI-only, kod yok — ama **"Start App" sadece `.exe`** hedefliyor; `.ps1`/`.py` için `powershell.exe -File …` host'la sarmala (K, GitHub issue #32046).
- Native `.lnk` "Shortcut key" (K): yalnız Desktop / Start Menu klasöründeyse çalışır — **önerilmez**.
- PowerToys Advanced Paste / Run: bu iş için değil (elendi).

**Bölge ekran-görüntüsü:**
- **ShareX = tek başına iki şartı da karşılıyor** (D): (a) otomatik PNG kaydı **ve** (b) sonrasında komut tetikleme. Kurulum: Hotkey → Task `Capture → Region`; Task settings → **Actions → Add** → `File path`=host exe, `Arguments`=`"$input"` (placeholder **`$input`/`$output`**, `%input%` DEĞİL), **Hidden window** işaretli; ana pencerede **After capture → Save image to file + Perform actions** ikisi de açık. Komut satırı: `ShareX.exe -workflow "…"`. **Domain uyarısı (X):** yalnız **getsharex.com** + **github.com/ShareX/ShareX** resmi; `.org`/`.net` klon/ayna, güvenilmesin.
- Win+Shift+S (Snipping Tool): native ama davranış sürüme bağlı — **"Automatically save original screenshots" ayarı elle açılmalı** (yoksa sadece panoya kopyalar). **X: kurulumdan önce Settings'te doğrula.** Ayrıca "en yeni PNG"yi izleme yöntemi kırılgan (hangi PNG "bu" belirsiz).
- nircmd `savescreenshot`: **interaktif drag-select YOK** (sabit x,y,w,h) → senaryoya uymuyor.
- PowerShell `CopyFromScreen`: koordinat ister → interaktif seçim için kendi şeffaf overlay Form'unu yazman gerekir (çok kod).

**Quick-input "not-kutusu":**
- **AHK `InputBox()` = 1 satır** (D): `.Value` + `.Result` döner.
- PowerShell WinForms (D): ~20 satır ama **sıfır ek kurulum** (Windows'ta yerleşik; Microsoft'un resmi örneği). Native-only fallback için ideal.
- Python `tkinter.simpledialog.askstring` (D): ~3 satır ama Python kurulu olmalı.
- Electron: tek metin kutusu için ~115MB → aşırı, elendi.

**Glue gotcha'ları:**
- AHK `Run`/`RunWait` **stdout'u doğrudan yakalamaz** → `%ComSpec% /c … > dosya` yönlendirmesi gerekir (ama Claude dosyayı kendi Write ettiği için bize gerekmez).
- Çok-satırlı/tırnak-özel-karakterli not → komut argümanına gömmek riskli; **geçici `.txt`'ye yaz**, yolu geçir.
- .NET `SendKeys` **Windows tuşunu güvenilir gönderemez**; AHK `Send("#+s")` gönderebilir — bu yüzden native-fallback'te Win+Shift+S'i **Salih'in kendisi** bassın (iki-tuşlu akış).

---

## 4. Claude-tarafı bulgular (entegrasyon)

**Headless `claude -p`** (D, kaynak: code.claude.com/docs/en/headless + cli-reference):
- `--bare` = script/SDK için **önerilen** mod (hook/skill/MCP/CLAUDE.md keşfini atlar, deterministik; "gelecekte `-p` varsayılanı olacak"). **Gotcha:** OAuth/keychain okumaz → `ANTHROPIC_API_KEY` şart.
- `--output-format` = `text` | `json` (result, session_id, `total_cost_usd`) | `stream-json` (+`--verbose`).
- `--allowedTools "Read,WebSearch,WebFetch,Write"` (prefix-pattern destekli, ör. `Bash(git diff *)`); `--permission-mode` (aşağıda); `--continue`/`-c`, `--resume`/`-r <id>`, `--session-id`, `--fork-session`; `--model` (`sonnet`/`opus`/`haiku`/`fable` alias ya da tam ad); `--add-dir` (ek dizin — **genel `--cwd` bayrağı YOK**; çalışma dizini için OS `Set-Location` ya da SDK `cwd`); `--max-turns`, `--max-budget-usd`, `--append-system-prompt`.
- **Sonuç yakalama:** iki kanal — stdout (`--output-format`) **ya da** Claude'un `Write` aracıyla diske yazdığı gerçek dosya (**pipeline için önerilen**).

**Görsel/ekran-görüntüsü girişi** (D):
- Üç doküman-yöntemi: drag-drop (**interaktif-only**), Ctrl+V paste (**interaktif-only**), **görsel yolunu metinde belirtmek** (`"Analyze this image: C:\...\x.png"`) — sadece bu üçüncüsü headless prompt string'ine taşınır.
- **Neden çalışır:** `Read` aracı PNG/JPG'yi "visual content" olarak modele verir (ham bayt değil); Claude Code büyük görseli otomatik resize/recompress eder. Base64'ü **sen yapmazsın**.
- `@path` mention görsel için **güvenilir değil** (K/X) — yöntem 3'e güven.
- Ham API limiti (fallback için): görsel ≤10MB / 8000×8000px, büyük ekran-görüntüsü otomatik downscale.

**Claude Agent SDK** (D): TS `npm i @anthropic-ai/claude-agent-sdk` (native binary bundled), Python `pip install claude-agent-sdk` (≥3.10). Giriş: Python `query(prompt, options)` / `ClaudeSDKClient`; TS `query({prompt, options})`. Built-in araçlar harness ile aynı: **Read, Write** (WriteFile DEĞİL), Edit, Bash, WebSearch, WebFetch, … `ClaudeAgentOptions(allowed_tools=[...], permission_mode="dontAsk", cwd=...)`. Görsel için SDK'da özel parametre **dokümante bulunamadı** (K) → aynı "yol + Read" deseni güvenli. Prod otomasyon/uygulama gömme için CLI yerine SDK öneriliyor. **Auth kısıtı:** SDK'da Anthropic üçüncü-tarafa claude.ai-login/rate-limit'i onaysız vermiyor → **API key** beklenen yol.

**Messages API fallback** (D): `image` content-block (base64 / url / file_id — file_id tekrar-referans için önerilir), görsel-önce-metin-sonra daha iyi. **Ham API'de yerleşik web taraması YOK** → server-side **web search tool** eklenir (`web_search_20260318` en yeni; `$10/1000 arama` + token; `max_uses`/`allowed_domains`/`user_location`; `pause_turn` için minik retry). **Raporu diske SEN yazarsın** (API stateless).

**Hooks/Triggers** (D):
- Hook'lar **zaten açık** bir session'ın lifecycle olaylarıdır. `FileChanged` bile **soğuk-başlangıç tetikleyicisi DEĞİL** (session açık + dizini izliyor olmalı). Yani "klasöre PNG düşünce sıfırdan claude başlat" için hook **yanlış araç**.
- **Tetikleyici = yakalama script'inin kendisi** (PNG+not'u kaydettikten sonra son adımda `claude -p` çağırır) — bu düz process-orkestrasyonu, "hook" değil.
- Yararlı ikincil rol: tetiklenen session İÇİNDE `Stop` hook'u ile "rapor yazıldı mı" kalite-kapısı.
- **Kritik:** `PermissionRequest` hook'ları `-p`'de **çalışmaz** → otomatik izin kararı için **`PreToolUse`** (bkz. §2b).

**Auth & güvenlik** (D):
- Üç yol: abonelik OAuth (`claude auth login` → Pro/Max kotası) · `ANTHROPIC_API_KEY` (per-token, expiration seçilebilir) · `claude setup-token` (CI/script için uzun-ömürlü OAuth token). **`--bare` ⇒ OAuth çalışmaz, API key şart.**
- **Permission mode tablosu:** `default`/`manual` (her şey onay bekler → script **tıkanır**) · `acceptEdits` (dosya düzenleme oto) · `auto` (classifier denetler, "güvenlik garantisi değil") · **`dontAsk`** (yalnız `permissions.allow` eşleşenler, **asla beklemez** → gözetimsiz için resmi öneri) · `bypassPermissions` (*"prompt injection'a karşı koruma YOK"* → yalnız izole/internetsiz VM).
- **Somut öneri:** `dontAsk` + dar `Read,WebSearch,WebFetch,Write` (Bash yok). `WebSearch` varsayılan izin ister → allow-list'e mutlaka ekle.

---

## 5. Somut iskelet (dikilmiş)

### A) Önerilen: ShareX + AutoHotkey v2

**ShareX (GUI):** Hotkey `Ctrl+Shift+J` → `Capture → Region`; Actions → Add: `File path`=`…\AutoHotkeyU64.exe`, `Arguments`=`"C:\Scripts\yakala.ahk" "$input"`, Hidden window ✔; After capture → Save image to file ✔ + Perform actions ✔.

```autohotkey
#Requires AutoHotkey v2.0
#SingleInstance Force

; ShareX bu script'i "$input" = yakalanan PNG yolu ile çağırır
imagePath := A_Args[1]

ib := InputBox("Ekran görüntüsü için bağlam / not:", "JARVIS - Not", "w520 h160")
if (ib.Result != "OK") || (Trim(ib.Value) = "")
    ExitApp()
noteText := ib.Value

stamp := FormatTime(, "yyyyMMdd-HHmmss")
reportPath := "C:\JARVIS\raporlar\yakala-" stamp ".md"

; Claude-tarafı önerisi (§4): --bare + Read(görsel) + WebSearch + Write + dontAsk
; NOT: --bare => ortamda ANTHROPIC_API_KEY tanımlı olmalı (abonelik istersen --bare'siz + setup-token)
prompt := "Read the screenshot at " imagePath ". User context: '" noteText "'. "
        . "Research it with WebSearch/WebFetch, verify the key claims, then write a full "
        . "cited report to " reportPath " using the Write tool. Label findings D/K/X."
cmd := 'claude --bare -p "' StrReplace(prompt, '"', '""') '" '
     . '--allowedTools "Read,WebSearch,WebFetch,Write" --permission-mode dontAsk'
RunWait(A_ComSpec ' /c ' cmd, , "Hide")

if FileExist(reportPath)
    Run(reportPath)
else
    MsgBox("Rapor üretilemedi: " reportPath)
```

### B) Hafif fallback: Win+Shift+S + PowerToys + PowerShell

Bir kerelik: Settings → Snipping Tool → "Automatically save original screenshots" **AÇ**. PowerToys KM: `Ctrl+Alt+J` → Start App → `powershell.exe`, Args `-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "C:\Scripts\yakala.ps1"`. (Salih önce Win+Shift+S ile yakalar, sonra Ctrl+Alt+J.)

```powershell
Add-Type -AssemblyName System.Windows.Forms

# (a) En yeni PNG (kullanıcı bu script'ten ÖNCE Win+Shift+S basmış olmalı)
$shots = "$env:USERPROFILE\Pictures\Screenshots"
$imagePath = Get-ChildItem $shots -Filter *.png -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1 -ExpandProperty FullName
if (-not $imagePath) { [System.Windows.Forms.MessageBox]::Show("PNG yok. Önce Win+Shift+S."); exit }

# (b) Not kutusu (kısaltılmış WinForms — tam örnek: MS Learn creating-a-custom-input-box)
$note = [Microsoft.VisualBasic.Interaction]::InputBox("Bağlam / not:", "JARVIS - Not", "")
if ([string]::IsNullOrWhiteSpace($note)) { exit }

# (c) claude çağrısı (§4 önerisi; --bare => ANTHROPIC_API_KEY gerekli)
$stamp = Get-Date -Format yyyyMMdd-HHmmss
$reportPath = "C:\JARVIS\raporlar\yakala-$stamp.md"
$prompt = "Read the screenshot at $imagePath. User context: '$note'. Research with WebSearch, " +
          "verify, then Write a full cited report to $reportPath. Label findings D/K/X."
& claude --bare -p $prompt --allowedTools "Read,WebSearch,WebFetch,Write" --permission-mode dontAsk

# (d) Raporu aç
if (Test-Path $reportPath) { Invoke-Item $reportPath }
```
*(Not: `Microsoft.VisualBasic.Interaction.InputBox` için `Add-Type -AssemblyName Microsoft.VisualBasic` gerekebilir; ya da §3'teki tam WinForms formu kullanılır.)*

---

## 6. Açık kararlar / borçlar (m.41 — kilitlenmedi, imza masasına)

1. **Otomasyon sınıfı (Salih/ana-sıra kararı):** yarı-otomatik (şimdi serbest, m.30) mi, tam-otomatik (K-010 kapısı) mı? Öneri: **yarı-otomatikle başla** (Salih notu girer + koşumu görür), K-010 olgunlaşınca tam-otomatik değerlendir.
2. **Auth çatalı:** `--bare`+`ANTHROPIC_API_KEY` (per-token) vs bare'siz+`setup-token` (abonelik kotası). Maliyet + gözetimsiz-güvenlik dengesi.
3. **Doğrulanacak (X):** (a) headless'ta görsel-yol+Read zincirinin gerçekten çalıştığı **tek küçük testle** teyit edilmeli — Claude-tarafı bunu K/D-karışık işaretledi; (b) Snipping Tool "auto-save" varsayılanı sürüme bağlı, kurulumdan önce kontrol.
4. **Skill bağı:** araştırma adımı `/atlas-kosum` (ya da yeni multi-hop diyalektik) çağırsın mı — ön-uç/arka-uç dikişi.
5. **İnşa freni (m.13/m.41):** bu rapor öneridir; hat kurulacaksa `.claude/`/settings yazımı ana-sıra/Salih işi, bu yan-oturum kilitleyemez.

---

## 7. Kaynaklar

**Claude-tarafı (resmi doküman, D):**
- https://code.claude.com/docs/en/headless · https://code.claude.com/docs/en/cli-reference · https://code.claude.com/docs/en/permission-modes · https://code.claude.com/docs/en/common-workflows · https://code.claude.com/docs/en/tools-reference · https://code.claude.com/docs/en/hooks-guide
- https://code.claude.com/docs/en/agent-sdk/overview · /agent-sdk/python · /agent-sdk/typescript
- https://platform.claude.com/docs/en/build-with-claude/vision · https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool · https://platform.claude.com/docs/en/manage-claude/authentication

**Windows-tarafı:**
- ShareX (D): https://getsharex.com/actions · https://getsharex.com/docs/region-capture · https://getsharex.com/docs/command-line-arguments · https://github.com/ShareX/ShareX
- AutoHotkey v2 (D, autohotkey.com doğrudan 403 → r.jina.ai proxy): /docs/v2/lib/Hotkey.htm · Run.htm · InputBox.htm · Send.htm
- PowerToys (D): https://learn.microsoft.com/en-us/windows/powertoys/keyboard-manager · /advanced-paste · /run · GitHub issue #32046
- Snipping Tool (D/K): https://support.microsoft.com/en-us/windows/use-snipping-tool-... · https://www.elevenforum.com/t/forcing-win-shift-s-to-actually-save-screenshots.33523/
- nircmd (D): https://nircmd.nirsoft.net/savescreenshot.html
- PowerShell (D): https://learn.microsoft.com/en-us/dotnet/api/system.drawing.graphics.copyfromscreen · https://learn.microsoft.com/en-us/powershell/scripting/samples/creating-a-custom-input-box · SendKeys API sayfası
- Python tkinter (D): https://docs.python.org/3/library/dialog.html

**Erişim engelleri:** autohotkey.com → 403 (proxy ile aşıldı) · getsharex `.org`/`.net` → klon, güvenilmedi (X).
