# R1 + R2 — kaynaklı cevap (Friday, 2026-09-10; devir-2026-09-10-tur2)

**Etiketler:** D = birincil kaynakta doğrulandı · K = kısmen (kaynak konuyu anıyor ama soruyu tam kapatmıyor) · X = bulunamadı / erişilemedi.
**Kural (D4, desen 2026-09-09 P/Q):** aşağısı belgenin NE BELGELEDİĞİNİ söyler; "yeterlidir" normu kurulmaz.

## 0. Açılan adresler — AS-OF 2026-09-10

| # | Emirdeki URL | Ne oldu | Fiilen okunan |
|---|---|---|---|
| R1 | `https://docs.claude.com/en/docs/claude-code/hooks` | **301 Moved Permanently** → `https://code.claude.com/docs/en/hooks` | yönlendirme hedefi |
| R2 | `https://docs.claude.com/en/docs/claude-code/settings` | aynı biçimde → `https://code.claude.com/docs/en/settings` | yönlendirme hedefi |

Not (D1 kapsamı): 301'i sunucunun `Location` başlığı verdi; **alternatif adres aramadım**, arama motoru kullanmadım. Emirdeki iki adres artık bu iki adrese taşınmış görünüyor — kalıcı yeni adresler olarak kabul edilmeleri hüküm gerektirir (soru 1).
İkinci not: R2'nin `permissions` sözdizimini anlatan asıl sayfa `/docs/en/permissions`'a *bağlantı veriyor*; o sayfa emrin R-listesinde olmadığı için **AÇMADIM** (soru 2). S2 cevabının K etiketi bundandır.

---

## S1 — PostToolUse girdisi Bash için okunan/yazılan yolu veren resmî alan taşıyor mu?

**Etiket: X — böyle bir alan belgelenmemiş.**

Kaynak: `https://code.claude.com/docs/en/hooks`. Belgelenen ortak girdi alanları: `session_id` · `prompt_id` · `transcript_path` · `cwd` · `scratchpad_dir` · `permission_mode` · `effort` · `hook_event_name`; olaya özgü olanlar: `tool_name` · `tool_input` · `tool_use_id`. Belge bunu şöyle sınırlıyor:

> "The `tool_name`, `tool_input`, and `tool_use_id` fields are event-specific."

Bash için verilen örnek girdide `tool_input` yalnız şunları taşıyor: `command`, `description`, `timeout`, `run_in_background`. Yani **komut metninden başka bir yol kaynağı belgelenmiyor**; `file_path` alanı yalnız dosya araçlarının `tool_input`'unda bulunur.

**Sonuç (D2 gereği, öneri — kendim değiştirmedim):** `hareket-kutuk.sh` v0.2'nin komut-metni ayrıştırması, belgelenen girdi yüzeyi bakımından şu an tek hook-anı yoludur; v0.2'nin hiçbir satırı bu bulgu yüzünden gereksizleşmiyor.

**Ama tek yol o değil:** belge `transcript_path`'i ortak alan olarak belgeliyor ve onun için bir uyarı taşıyor —

> "written asynchronously and may lag the in-memory conversation"

Yani Jarvis'in transkript-türevi yöntemi (`tools/hareket-tablo.py`, tur-1 cevabı (c)6) Friday'de de **belgelenmiş bir girdiyle** kurulabilir; bedeli gecikme, kazancı komut ayrıştırmasının kırılganlığından kurtulmak. Hangisinin seçileceği hüküm (soru 3).

---

## S2 — `permissions.deny` Read/Bash için yol-bazlı kısıt verebiliyor mu?

**Etiket: Read için D · Bash için X (bu sayfada belgelenmemiş) · bütün olarak K.**

Kaynak: `https://code.claude.com/docs/en/settings`. Sayfanın kendi örneği yol-bazlı bir Read reddi gösteriyor:

```json
{
  "permissions": {
    "allow": ["Bash(npm run lint)", "Bash(npm run test *)"],
    "deny":  ["Read(./.env)", "Read(./.env.*)"]
  }
}
```

Alıntı: > "a rule that names a tool and what it may do"

Yol semantiği için sayfanın uyarısı (bizim için kritik, çünkü `kanon/` bir symlink ve Jarvis kökü repo dışında):

> "a permission rule that starts with `/` … anchors at the session's primary working directory"

Zamanlama için:

> "`deny` and `ask` rules apply right away"

(yani `allow` kurallarının beklediği klasör-güveni beklemezler).

**Bash tarafı:** bu sayfada `Bash(...)` yalnız komut kalıbıyla örneklenmiş (`npm run lint`); Bash'i **yol** ile kısıtlayan bir örnek ya da cümle bu sayfada yok. Sözdiziminin tamamı `/docs/en/permissions` sayfasında ve orayı açmadım → X.

**D3 gereği ÖNERİ (settings.json'a DOKUNMADIM; metin aynen, sözdizimi DOĞRULANMADI `[?]`):**

```json
"deny": [
  "Read(/Users/HasanSalihSahin/jarvis/**)",
  "Read(./kanon/../**)"
]
```

Bu bir öneridir, hüküm değil; üç çekincesi var ve üçü de `okuma-izin.sh`'in **yerine** değil **yanına** konmasını gerektirir:
1. Kuralın kök-anchor davranışı (yukarıdaki alıntı) `kanon/` symlink'inin gerçek hedefiyle (`~/jarvis/core`) nasıl etkileşiyor — belgede karşılığını bulamadım; yanlış yazılırsa `kanon/` okumasını da keser, o zaman Friday kanonsuz kalır.
2. Deny yalnız **Read**'i kapatır; Bash `cat`/`sed` yolu bu sayfada belgelenmiş biçimde kapanmıyor — kilidin Bash dalı yerini korumalı.
3. Glob'un `**` semantiği bu sayfada tanımlı değil.

---

## S3 — Hook girdisi çağrının bir ALT-AJANDAN geldiğini ayırt eden resmî alan taşıyor mu? (Jarvis İB-83)

**Etiket: D (alan adları) · K (örnek JSON).**

Kaynak: `https://code.claude.com/docs/en/hooks`. İki alan belgeleniyor:

| Alan | Belgedeki tanım (alıntı) |
|---|---|
| `agent_id` | > "Unique identifier for the subagent. Present only when the hook fires inside a subagent call." |
| `agent_type` | > "Agent name (for example, `\"Explore\"` or `\"security-reviewer\"`)." |

Belge kapsamı şöyle veriyor:

> "When running with `--agent` or inside a subagent, two additional fields are included"

`agent_id` için kullanım amacı da açıkça yazılı:

> "Use this to distinguish subagent hook calls from main-thread calls."

**Ayrıca iki hook OLAYI belgeleniyor:** `SubagentStart` ("When a subagent is spawned") ve `SubagentStop` ("When a subagent finishes"); ikisinin de matcher'ı **agent type**'tır (`general-purpose`, `Explore`, `Plan`, özel ajan adları, ya da `^my-plugin:reviewer$` gibi eklenti-kapsamlı adlar).

**Örnek JSON — K:** sayfanın verdiği tam örnek girdi bir **ana-sıra** `PreToolUse` çağrısıdır ve içinde `agent_id`/`agent_type` yoktur (zaten "present only … inside a subagent"):

```json
{
  "session_id": "abc123",
  "prompt_id": "550e8400-e29b-41d4-a716-446655440000",
  "transcript_path": "/home/user/.claude/projects/.../transcript.jsonl",
  "cwd": "/home/user/my-project",
  "scratchpad_dir": "/tmp/claude-1000/-home-user-my-project/abc123/scratchpad",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": { "command": "npm test", "description": "Run test suite", "timeout": 120000, "run_in_background": false },
  "tool_use_id": "toolu_01ABC123..."
}
```

Alt-ajan hâlinin **birebir örnek JSON'unu belgede bulamadım**; alan adları ve varlık koşulu belgeli, örnek gövde değil. İB-83 için pratik karşılık: `agent_id` alanının VARLIĞI ana-sıra/alt-ajan ayrımı için belgelenmiş göstergedir, `agent_type` ise hangi ajan olduğunu verir — ikisi de `hareket-kutuk.sh`'e tek satırla eklenebilir (öneri, kendim eklemedim; İB-83 Jarvis'in işi).

Yan bulgu (sorulmadı, İB-83'ü ilgilendirir): belge `effort` alanını da ortak girdi sayıyor ve "`PreToolUse`, `PostToolUse`, `Stop`, `SubagentStop`" gibi olaylarda bulunduğunu söylüyor — yani "işçi senden pahalı model kullanamaz" değişmezinin (`core/rol.md` md.4) **efor** ayağı hook düzeyinde gözlemlenebilir; model adı için belgede karşılık bulamadım.

---

## Özet tablo

| Soru | Etiket | Tek cümle |
|---|---|---|
| S1 Bash yol alanı | **X** | Belge Bash `tool_input`'unda `command`/`description`/`timeout`/`run_in_background` dışında yol alanı belgelemiyor; `transcript_path` belgeli ama gecikmeli. |
| S2 deny yol-bazlı | **K** | Read için yol-bazlı deny belgeli (`Read(./.env)`) ve deny hemen yürürlükte; Bash'in yolla kısıtlanması bu sayfada belgelenmemiş. |
| S3 alt-ajan ayrımı | **D** | `agent_id` + `agent_type` belgeli ("Present only when the hook fires inside a subagent call"), `SubagentStart`/`SubagentStop` olayları da var; alt-ajan örnek JSON'u yok. |

**R3/R4/R5 AÇILMADI.** Bu koşumda açılan adres: yalnız yukarıdaki iki yönlendirme hedefi.
