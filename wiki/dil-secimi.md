# Dil seçimi — hangi iş sınıfı hangi dilde (Jarvis sistemi + "Jarvis gibi ürün" ekosistemi)

**Tanım:** Jarvis'te ve Jarvis-benzeri ürünlerde yazılacak kodun dili tek bir "en iyi dil" sorusu değil, **iş-sınıfı × kısıt** eşlemesidir: her iş sınıfının (hook · CLI/veri hattı · ajan döngüsü · MCP sunucusu · dağıtılabilir ikili · konfig/şema · politika · sandbox) kendi belirleyici kısıtı vardır (gecikme, SDK varlığı, tekrar-üretilebilir derleme, LLM'in o dildeki doğruluğu, okunabilirlik). Kural seti ÖNERİ damgalıdır (Katman-2 sayfa; kanon statüsü KB-64 masasında).
**Durum:** GÜNCEL · **son teyit:** 2026-08-26 (seans-16) · **kaynaklar:** `cc/rapor/2026-08/rapor-2026-08-26-1.md` (m.40b çift-atlas wf_d8cf4f3a-1a8, 3 aile × 12 işçi; hayatta-kalma 8/22/0/0; V26 37/4/4) · `cc/rapor/2026-07/rapor-2026-07-30-10.md` (07-30 icra-katmanı; VERİLİ zemin) · `veri/kod-envanter.jsonl` (yerel ölçüm, `tools/kod-envanter.py`) · **güven:** orta — A ailesi D (V26 temiz), B/C yapı-taşları D ama tez/antitez tarafları K'ya düştü; kişisel-ölçek sayısal eşikler literatürde YOK (kör nokta); sentez tek-şerit, antitez görmedi.

## Çekirdek

**Kanonik örnek (deseni yeniden üreten en küçük hâl):** PreToolUse teli. 07-30'da Windows'ta bash+python+5 grep = 241,5 ms ölçüldü ve "Go'ya geçelim mi?" soruldu; cevap dil değil mimari çıktı (6 süreç→1: kazancın %95'i). 08-26'da Mac'te aynı tel 30,7 ms, yerel-exe tabanı 1,6 ms → derlenmiş ikilinin tavan kazancı 14 ms/çağrı. Hook sözleşmesi dil-bağımsız (stdin JSON → exit 0/2). Sonuç: **dil kısıtı yok, gecikme kısıtı var; ölçüm kısıtı karşılıyorsa dil değişmez.** Aynı akıl her sınıfa uygulanır: önce sınıfın kısıtını ölç, sonra dil.

**İş-sınıfı × dil kural seti (ÖNERİ, 08-26):**

| İş sınıfı | Kural | Belirleyici kısıt (kanıt) |
|---|---|---|
| Sıcak hook | dil serbest; bugün bash/Python KALIR; yalnız `type=command` + EXEC biçimi (args, kabuksuz) | gecikme (Mac 30,7 ms; tavan kazanç 14 ms) · sözleşme dil-bağımsız (D) · `sh -c`/prompt-hook deterministik değil |
| CLI aracı / veri hattı | Python stdlib KALIR; yorumlayıcı SÜRÜM-PİNLİ (3.9.6 EOL 2025-10-31) | throughput kıyası ölçülmemiş → değiştirilmez (m.35) · LLM doğruluğu en yüksek sınıf · sahip okur |
| Ajan döngüsü / orkestrasyon | Python ∨ TypeScript | Agent SDK yalnız bu ikisi (Py v0.2.143 · TS v0.3.245, 2026-08); başka dil = `claude -p --output-format json` alt-süreç |
| MCP sunucusu (ürün arayüzü) | Tier-1: TS · Python · C# · Go (go-sdk v1.7.0) · Rust (rmcp v3.1.4); ilk Jarvis sunucusu Python | tier = özellik+bakım, performans değil · stdio: stdout yalnız protokol, stderr yalnız günlük |
| Dağıtılabilir ikili (dış makine) | Go'nun tetiği BURADA; gerekçe "çalışma-zamanı kurdurmayan tek dosya + bit-bit tekrar-üretilebilir derleme" (Go 1.21+ `CGO_ENABLED=0 -trimpath`), "küçük ikili" DEĞİL | ikili boyutu dile değil yüke bağlı (ripgrep 1,8 MB ↔ gh 13,9 ↔ Codex 88) · Go LLM doğruluğu düşük → nadir-dil kapısı |
| Messages-API istemcisi | 7 resmî SDK dili; Rust yok | Jarvis'te sınıf yok (Claude Code üzerinden) |
| Konfig / şema / doğrulama | JSON Schema 2020-12 + Python doğrulayıcı YETER; CUE eşiği: "çok-kaynaklı kısıtların sıra-bağımsız birleştirilmesi" gereksinimi belgelenince | CUE'nun Jarvis yükünü geçtiği belgeli durum yok (SAĞLAM) · Türkçe tanımlayıcı CUE'da OK (NFC) · CUE 1.0-öncesi, Dagger benimseme yüzünden bıraktı |
| Politika motoru (deny/allow) | regex/liste (m.30) KALIR; OPA/Cedar girmez | Cedar çözümlemesi dış SMT + zaman-aşımı (h) · Rego `http.send` yan-etkili, yalnız `--capabilities allow_net: []` pinli kapatılır |
| Kural/betik sandbox'ı (ufuk) | dil-düzeyi sonluluk beyanı olan dil: Starlark ∨ Dhall | Turing-tam olmayan spec · Datalog/Alloy ekseni taranmadı |

**Üç yatay kural:**
1. **Nadir-dil kapısı** — LLM'in yazacağı dil Python/TS/JSON dışındaysa: istemde spec/sözdizimi referansı + deterministik derleyici/vet/şema kapısı + parite testi. (CangjieBench: nadir dilde <%7 pass@1, referansla +22..+46 puan; Multi-SWE-bench dil kırılımı: Java 23,4 · Rust 15,9 · TS 11,6 · Go 7,5 · JS 5,1 — 2025-04, gösterge.)
2. **İki-yol parite testi** — dil geçişinin kabul ölçütü: eski/yeni yol aynı girdide bayt-birebir aynı çıktı + N saat hatasız (Turborepo 72 saat). Geçiş tetiği: dış-makine dağıtımı ∨ yerel ölçülmüş gecikme/hacim sınırı; tetik yoksa geçiş yok.
3. **Sürüm-pinli kanal + bakım-tazeliği kapısı** — derlenmiş ikili determinizm vermez, pin verir (DotSlash · Nix flake · npm pin · brew sha); pinsiz `curl|sh` / `go install @latest` girmez. Envantere giren her dil/araç için son release · son commit · 90-gün commit sayısı çekilir; release boşluğu >12 ay → sha-kilidi zorunlu.

## SOP — "yeni bir şey yazacağım, hangi dilde?"
1. `python3 tools/kod-envanter.py` koş → mevcut dil dağılımı + kurulu araç-zinciri + gecikme tabanı (bronz `veri/kod-envanter.jsonl`).
2. İşi yukarıdaki tabloda bir sınıfa oturt; sınıfın **belirleyici kısıtını** yerelde ölç (gecikme ms · SDK var/yok · dış makine var/yok · şema yükü).
3. Kısıt karşılanıyorsa mevcut dil (Python/bash/JS-dayatma) — **bitti.**
4. Karşılanmıyorsa: yeni dil = m.42 (+1 araç zinciri) + m.16 → **KB kalemi aç, Salih kararı**; karar gelirse nadir-dil kapısı + parite testi + sürüm-pinli kanal ile gir.
5. Konfig/şema için: JSON Schema + Python doğrulayıcı; "iki alanın DEĞERİNİ karşılaştırma" ya da "çok-kaynaklı kısıt birleştirme" gereksinimi belgelenince önce $vocabulary/eklenti, sonra CUE (eşik kaydı ledger'a).

## Gotchas
- **"Go mu Rust mı" tuzağı (07-30):** dil sorusuna iş yükü tanımlanmadan atlamak — cevap mimari çıktı. 08-26'da tekrar: cevap iş-sınıfı matrisi çıktı, tek dil değil.
- **"Derlenmiş = küçük/deterministik" yanılgısı:** ikili boyutu yüke bağlı; determinizm pin'den gelir, dilden değil (C-E3).
- **SDK tazeliği:** "Rust'ın SDK'sı yok" 07-30'da tam doğruydu, 08-26'da yalnız API istemcisi için doğru (MCP'de Tier-1). Dil-durum iddiaları v2-tazelik taşır; her koşumda yeniden çekilir.
- **Sistem Python'a yaslanma:** macOS 3.9.6 upstream EOL; Apple geri-yaması bilinmiyor → "stdlib-only olduğu için sorun yok" yeterli değil (KB-62).
- **CUE'yu LLM'e yazdırma:** LLM-doğruluk ölçümü YOK; Türkçe tanımlayıcı engel değil ama nadir-dil kapısı zorunlu.
- **Workflow script'leri JS** — seçim değil dayatma; envanterde "JS 2.054 satır" görüp "TS'ye geçmişiz" çıkarımı yapma.

## Süpersede zinciri
- 07-30 `cc/rapor/2026-07/rapor-2026-07-30-10.md` §4.6 "Rust hiçbir sınıfta" → **yerini aldı: [2026-08-26, "Rust: Messages-API istemcisinde yok (SAĞLAM); MCP sunucusu sınıfında Tier-1 resmî (rmcp v3.1.4)"]**.
- 07-30 §4.6 "Go'nun tek tetiği = başka makineye tek-ikili (küçük ikili)" → **gerekçe düzeltildi [2026-08-26]:** tetik aynı, gerekçe "çalışma-zamanı kurdurmayan + tekrar-üretilebilir derleme"; boyut argümanı DÜŞTÜ.
- 07-30 §4.1 "hook 241,5 ms → mimari" → **Mac'te [2026-08-26]:** 30,7 ms; sorun yok; hüküm (dil değil mimari) ayakta.

## Bağlantılar
[[tarama-yontemleri]] (ölçüm-önce seçim kuralı aynı desen) · [[silver-saglik]] · [[paralel-oturum-protokolu]] · [[no-mistakes]] · [[stokastik-dusunce]] (deterministik tasarım ilkesi, Karar 65) · [[ai2ai-rapor-formati]] · [[olcum-banki]] (yerel eşik kalibrasyonu) · [[pointer-sistemi]]

**Bağlantılar:** · [[anakronizm-freni]] (karşı-link 08-26)
