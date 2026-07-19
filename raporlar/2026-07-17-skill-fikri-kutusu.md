# Skill Fikri Kutusu — Rapor (TARTIŞMA; Fable/ana-sıra ile)

> **Mod:** rapor · KARAR YOK. **COMMIT: Salih 07-18 izin verdi** (branch'e, PC'den bulunabilirlik için); **merge→main/canon = Fable Cowork süzgeci** (m.41). m.41: bu CC/Opus yan-oturum → öneri/aday üretir, kanon KİLİTLEMEZ; Fable+Salih kanonlar. Kaynak talebi: Salih 07-17 ("tekrar tarif ettiğim bağlam-kümelerini skill fikri kutusuna topla" + "örnek olarak skill oluşturma tavsiyesi ver" + "rapora da ekle"). Repo dışı tutuluyor (commit atma); "işle" denince `raporlar/`e iner.

---

## 1. Önerilen sürekli kural (aday — Fable kanonlar)
**"Tekrarlayan-küme → skill adayı" tespiti:** Salih'in defalarca aynı kalıpla tarif ettiği **bağlam-kümeleri** yakalanır → bu kutuya aday düşer. Kutu = **K-016 besleme hattı** ("ihtiyaç listesi → üretim"). Skill değeri sezgisi: **değer ≈ tekrar-sıklığı × elle-yapma-maliyeti.**

## 2. Tespit edilen bağlam-kümeleri → skill adayları
| # | Bağlam-küme (Salih'in tekrar eden kalıbı) | Tetik | Skill ne yapar | Kanon | Örtüşme | Öncelik |
|---|---|---|---|---|---|---|
| **A** | **"karşıt gömülü 3 matematik-temelli model"** ←*Salih örneği* | "3-model / karar modeli" | 3 model (token×zaman×kalite×risk) + ≥1 karşıt-temel + öneri + defter bloğu | m.37+07-17/m.40a/m.39 | yok | **YÜKSEK** |
| **B** | "dışarıda çözülmüş mü tara / atlas koştur" | "araştır / atlas / dış tarama" | Alan-ailesi fan-out + V26 örneklem + Opus sentez, karardan ÖNCE | m.40b/V36/Atlas R1 | yok | **YÜKSEK** |
| **C** | "önceki kararla çelişki var mı" | (yeni karar anı) | Kanon-tarama → çelişki+artı/eksi+plan ÖNCE | m.16/m.31 | yok | ORTA |
| **D** | "talimatı lojiğe çevir" (loop/kural) | "loop/kural tanımı" | NL → önerme lojiği (∧∨¬→↔), X∧Y→Z | m.38/V46 | yok | ORTA |
| **E** | "kutu-damıtma / ingest / arşive indir" | "damıt / ingest" | Katmanlı damıtma + pointer koru + silme-yok arşiv | m.34/21/8/K-019 | yok | ORTA |
| **F** | "vardiya teslim / kapsül devri / iyi geceler" | "teslim / kapat" | Kapsül güncelle + teslim raporu + git-log disiplini | m.18/24/27 | kısmi (`hizalama`) | ORTA |

*Zaten kapsanan: `hizalama` (oturum-içi recap) · `dev-run-planner` (run/sprint) · `morning` (sabah brifingi).*

## 3. Örnek skill'ler — tam iskelet *(Salih'in "örnek göster" talebi)*

### Örnek 1 — `karar-modeli` (Salih'in literal örneği)
```
---
name: karar-modeli
description: Tetikleyiciler: "3 model sun", "karar modeli", "matematik-temelli
  seçenekler", "karşıt gömülü modeller". Ölçek-eşiği ÜSTÜ karar anında çalışır.
  Su-bardağı alt-karar / typo / tek-satır → çalıştırma, direkt yap.
---
1. (m.40b) Dışarıda çözülmüş mü? Gerekiyorsa Atlas koştur, saha örnekleriyle destekle.
2. 3 modeli sayısal karşılaştır: token × zaman × beklenen-kalite × RİSK.
3. (m.37 ek) ≥1 model KARŞIT-TEMEL: önerinin karar-varsayımına zıt
   (beklenen-değer ↔ minimax · Bayes ↔ frekans · keşif ↔ sömürü);
   aygıt gerçek + canlılık şartı.
4. Öneriyi ✅ işaretle + tek-satır gerekçe + triangülasyon (zıtlar nerede kesişti).
5. senaryo-defteri bloğu üret ("Karşıt-temel:" satırıyla).
6. Görünür sun, onay bekleme (m.37); m.41: yan-oturumsa kanon kilitleme, aday üret.
```

### Örnek 2 — `karar-hatti` (bileşik; 07-17 oturumunda elle koşulan boru hattı)
```
---
name: karar-hatti
description: Tetikleyiciler: "tam karar hattı", "araştır ve model sun", büyük/
  geri-alınamaz karar anı. Küçük/geri-alınabilir iş → direkt yap.
---
Zincir (3 skill'i sırayla çağırır):
1. (m.16) celiski-kapisi → önceki kanonla çelişki tara; varsa artı/eksi+plan ÖNCE.
2. (m.40b) atlas-kosum   → dış tarama, saha örnekleri.
3. (m.37) karar-modeli   → 3 model + karşıt-temel + öneri.
4. senaryo-defteri kaydı + (m.41) yan-oturumsa devir dosyası.
```

### Örnek 3 — `atlas-kosum` (07-17 "serbest koştur" izni; oturumda 6 kez yapıldı)
```
---
name: atlas-kosum
description: Tetikleyiciler: "araştır", "atlas koştur", "dış tarama", "saha örneği
  bul". Basit bilinen-cevap → koşturma, direkt söyle.
---
1. Soruyu alan-ailelerine böl (dik araştırma hatları).
2. Her aileye 1 Atlas ajanı (paralel), V26 örneklem-denetim + Opus sentez.
3. Bulguları etiketle (D/K/X) + URL + olgunluk + lisans; uydurma-yasağı, "bulunamadı" dürüstlüğü.
4. Öneri-öncesi ise m.40b: karardan ÖNCE koş.
```

## 4. Anlamlı skill KOMBİNASYONLARI (canon'dan)
- **★ Karar hattı** = C → B → A → defter (m.16→m.40b→m.37→m.39). *07-17'de sana elle koşulan tam boru hattı;* en değerli bileşik. → Örnek 2.
- **Loop-üretim hattı** = D(lojik) → loop tanımı → PreToolUse guardrail (m.38→loop-eng→G4). K-009 motoru.
- **Vardiya hattı** = kapsül-aç → iş → E(damıtma) → F(teslim). Oturum yaşam-döngüsü (m.18 üç-yüz).

## 5. Değer sıralaması (deneysel, m.39)
En sık + en pahalı-elle = tavan: **`karar-modeli`** (07-17'de 2×) · **`atlas-kosum`** (07-17'de 6×). Öncelik bu ikisinde.

## 6. Açık sorular (Salih cevabı bekleniyor — KARAR ALINMADI; Salih 07-17 kuralı gereği rapora eklendi)
1. Skill fikri kutusunun evi: ayrı `kuyruk/skill-fikir-kutusu.md` mi, `fikir-kutusu.md` içinde bölüm mü?
2. İlk üretilecek: `karar-modeli` mi, bileşik `karar-hatti` mi?
3. Örneklerden hangileri üretim-adayı, hangileri "henüz değil"?
4. "Tekrarlayan-küme → skill" sürekli kuralı kanona (V-kaydı/K-016 alt-süreç) girsin mi?

## 7. Açık borç
- ~~Atlas "skill tasarım desenleri" şeridi koşuyor~~ **DONE (§8'e işlendi).**
- Atlas "yüzeyler-arası tutarlılık" şeridi koşuyor → CC okuma-sırası raporunu tamamlayacak.

---

## 8. Atlas skill-desenleri bulguları (rafine — DONE)

**Kanıt kısıtı (dürüstlük):** WebFetch bu oturumda 403 (birincil doküman tam-metni yok, arama-özeti); GitHub API kapalı (yıldız/lisans DOĞRULANMADI). Aşağısı orta-yüksek güven, primary-source değil.

### 8.1 SKILL.md anatomisi (kanon-eşleşmeli)
- Skill = **klasör + `SKILL.md`** (YAML frontmatter + markdown gövde) + ops. `scripts/` `references/` `assets/`.
- Zorunlu: `name` (küçük-tire, ≤64, klasör adıyla eş) · `description` (≤1024, **NE yapar + NE ZAMAN**; "undertrigger"a karşı hafif iddialı yaz).
- CC uzantı alanları: `disable-model-invocation` · `user-invocable` · `argument-hint` · `arguments` · `allowed-tools`.
- **Progressive disclosure 3 kat** (name+desc ~100 tok → gövde <5k → linkli referans talep-üzerine) = **m.20 pointer + m.22 katmanlı-yerleşimin BİREBİR eşleniği.** (JARVIS önden.)

### 8.2 ★ KRİTİK tasarım içgörüsü (senin "commit atma" hattıyla birebir)
**Yan-etkili adımı (kayıt/commit) ayrı `disable-model-invocation: true` skill'e ayır.** Deterministik-script > markdown talimat (belirsizliği sıfırlar): "3 model üret" = LLM adımı; "senaryo-defterine yaz + commit" = script + SADECE elle-tetik. Böylece otonom pipeline kanona kazara yazamaz — m.31 freni + m.9 proof-of-work + m.25 otonomi-sınırı koda gömülür. → **`karar-hatti` bileşiğinin Aşama-4'ü (kayıt) `/karar-kaydet` diye AYRI skill olmalı.**

### 8.3 Rafine iskelet — `karsit-uc-model` (Örnek 1'in olgun hali)
```yaml
---
name: karsit-uc-model
description: Bir karar/tasarım sorusu için her biri FARKLI matematiksel temele
  dayanan, içine karşıt-görüş (steelman) GÖMÜLÜ 3 karar modeli + trade-off matrisi
  üretir. Kullan: ölçek-eşiği üstü karar, "3 model / karar modeli / karşıt gömülü
  model". Tek-satırlık karar → KULLANMA.
argument-hint: "<karar sorusu>"
arguments: [soru]
user-invocable: true
disable-model-invocation: false
metadata: { owner: carvis, version: "0.1.0-deneysel" }
---
1. Ontolojik çerçeveleme (LLM).
2. 3 model — her biri: matematiksel temel (references/temeller.md'den FARKLI taban) +
   önerme + GÖMÜLÜ karşıt-fikir (steelman) + artı/eksi + kısıt-duyarlılığı.
3. Trade-off matrisi + triangülasyon.
4. Dürüstlük bloğu (bilinen/inanılan/spekülatif + güven).
```
- `references/temeller.md` (kat-3): karar teorisi · minimax · Bayes/frekans · Pareto · reel-opsiyon… → her koşumda 3 farklı taban + karşıt-temel GARANTİ.

### 8.4 Eval (K-016 eval-kuralının somut hali)
- **skill-creator v2 Executor/Grader:** with-skill vs without-skill A/B; `evals.json` (prompt+assertion) · `grading.json` (alanlar TAM: `text`/`passed`/`evidence`) · `timing.json`/`metrics.json`. İki subagent paralel (biri skill'li biri skill'siz — bağlam kirlenmesi önlenir).
- **Description optimizasyonu:** 20 sorgu (10 tetiklemeli + 10 tetiklememeli) × 3 koşum, 60/40 train/validation, overfit'ten kaçın. → her yeni skill yayına girmeden ZORUNLU adım.

### 8.5 İlham repoları (yıldız/lisans DOĞRULANMADI — GitHub API kapalı)
| Repo | Öğrettiği | Not |
|---|---|---|
| anthropics/skills | skill-creator + Executor/Grader eval | resmi referans (~44k beyan) |
| obra/superpowers | workflow zinciri (brainstorm→design→plan→subagent) | karar-hattı ilhamı (yıldız çelişkili) |
| kepano/obsidian-skills | format disiplini, wiki'ye en yakın | Steph Ango |
| VoltAgent/awesome-agent-skills · karanb192/awesome-claude-skills | küratörlü indeks | genişlik/doğrulanmış liste |

### 8.6 Rafine sıradaki adımlar (öneri; karar Salih'in)
1. `karsit-uc-model`'i deneysel-damgalı (m.29) yaz; `references/temeller.md` wiki'den türet.
2. Kaydı `/karar-kaydet` (`disable-model-invocation:true`) AYRI skill yap (§8.2 freni).
3. 20-sorgu description eval'i (§8.4) — yayına girmeden.
4. GitHub-erişimli oturumda anthropics/skills'in gerçek `evals.json`/`grader.md` şablonu birebir çekilsin (bu oturumda API kapalıydı).
