# Ders: depo dosya mimarisi nasıl kurulur (düzeltme üzerinde öğretim) — hazırlık brifi, 2026-10-31

Üretici: Jarvis seansı `2026-10-31-jarvis`; 3 paralel tarama (dış kaynak atlas · öğretim yöntemi atlas · depo kusur envanteri). Fork oturumu bu dosyayı okuyup `ogren` akışıyla başlar. Her sayı tarama çıktısından; `[?]` kestirim; AS-OF 2026-10-31.

## 0. Varsayım ve kapsam
- "Filesystem file mimarisi" = deponun klasör ve dosya düzeni (repo mimarisi). İşletim sistemi dosya sistemi iç yapısı (inode, ext4) kapsam dışı; istenirse ayrı ders.
- Ders nesnesi = `C:\sistem\sistem` deposundaki gerçek kusurlar; her kutu bir kusuru düzeltir, düzeltmeyi Salih'in eli yapar (pratik = Salih'in eli).
- Süre 60-90 dk, 8 kutu; "6-8 kutu" tasarım seçimidir, literatür doğrulaması yok (öğretim taraması §D).

## 1. Öğretim yöntemi (kanıt özeti; öğretim taraması)
| İlke | Kanıt | Derse uygulama |
|---|---|---|
| Faded worked example | Renkl; Wikipedia ikincil, AS-OF 10-31 | Kutu 1-2 tam gösterilir, 3-5 bir adım boş, 6-8 Salih tek başına |
| Expertise reversal | HW Üniv. laboratuvar çalışması | **Probe** yüksekse fading erkene alınır |
| Subgoal labels | Morrison-Margulieux-Guzdial 2015 | Her düzeltme 3 adlı adım: sorumluluğu belirle · yeri seç · pointer/bağımlılığı güncelle |
| Self-explanation | meta-analiz g=0,55 (BPS özeti) | Kutu sonu sorusu: "bu düzeltme neden işe yarar, hangi yanlış kavram tuzak?" |
| Contrasting cases | Schwartz-Bransford, Stanford HSTAR | Önce/sonra ağaç çifti; ilk soru "fark ne?" |
| Canlı kodlama izletme etkisiz | ICER 2023, SIGCSE 2025 | Refactor izletilmez, Salih yazar |
| Çok dosyalı refactor zor | JSERD OSS çalışması | Kutu başına ≤3 dosya hareketi + doğrulama adımı |
| Mini-ADR | etkisi kanıtsız, deneysel | Kutu sonunda 4 satır: bağlam · karar · alternatif · sonuç |

Kutu şablonu: **Kavram** (İngilizce sektör başlığı, tek cümle) → **Kusur** (depodan önce/sonra) → **Düzeltme** (fading'e göre) → **Doğrulama** (komut) → **Geri-anlatım** → **Mini-ADR**.

## 2. Plan DAG (8 kutu; başlık = sektör başlığı, dış kaynak taraması §başlıklar)
1. **Root Signals and Screaming Architecture** — kök dizin neyi söyler (Uncle Bob 2011; Turborepo kökte az dosya). Kusur: kök `AGENTS.md`'de adı geçmeyen `veri/`, `target/`, `Cargo.toml`, `arsiv/`, `KURULUM.md`; `jarvis/` kökünde fazla `.DS_Store`, `kuyruk/arsiv/` boş dizin. Düzeltme: `.DS_Store` ×3 ve boş dizin silinir (Salih eli, m.8 sınırı: boş klasör kayıt değildir) + kök `README.md`'ye Rust workspace pointer satırı. Soru: "kökte duran dosya hangi soruya cevap vermeli?"
2. **Tracked, Untracked, Ignored: Three States of a File** — git durum üçlüsü. Kusur: `friday/.DS_Store` izleniyor (gitignore izleneni kapsamaz); `calc/veri`, `span/veri` takipsiz, diğer 5 ajanda `.gitkeep` izli; 3 `hareket-olay.jsonl` takipsiz. Düzeltme: `git rm --cached friday/.DS_Store`; `git add calc/veri/bronz/.gitkeep span/veri/bronz/.gitkeep deci/veri/bronz/hareket-olay.jsonl sage/... vega/...`. Doğrulama: `git status --short | wc -l`. Yanlış kavram: "ignore edilen dosya izlenmez" (tersi: izlenen dosya ignore edilmez).
3. **Derived Artifacts and Foreign Clones Stay Out** — türev ve yabancı kod depoya girmez. Kusur: `projects/portal-parkur/.godot` (28 KB), `test_cikti` (11 MB), `referans/` (154 MB, içinde 8 `.git/`). Düzeltme: üç satır `.gitignore`. Soru: "ürün ayrı repo kuralıyla bu dizinin ilişkisi ne?"
4. **Pointer Discipline: Every Name Must Resolve** — pointer ilkesi (md.7; Zettelkasten sabit kimlik). Kusur: 4 kırık pointer, hepsi Karar 118 M2 sonrası Python adı: `jarvis/CLAUDE.md` §2-3'te `hareket-tablo.py`, `hafiza-ayna.py`, `acilis-kapilari.py`; kök `AGENTS.md` md.1/14'te `alan-ajani-dogur.py`. Düzeltme: Rust adına çevir (Katman-1, Salih imzası; fork oturumu Jarvis'e devir dosyası bırakır ya da Salih bu oturumda imzalar). Doğrulama: `ls target/release/ | grep -c ...`. Fading başlar: Salih bir dosyayı kendisi düzeltir.
5. **Archive, Never Delete** — ADR yalnız-eklemeli, PARA Archives, md.8. Kusur: `jarvis/cc/` kökünde 2 `.py` + 2 `.md` gevşek dosya (plan parti 3 artığı); kökte ikinci arşiv çatısı `arsiv/kod/` kanonda yazılı değil. Düzeltme: `git mv` ile `arsiv/kod/python/` ve `cc/rapor/2026-08/`; kök `AGENTS.md` md.17'ye "kod arşivi → `arsiv/kod/`" (Katman-1). Soru: "silme ile arşive indirme git tarihçesinde nasıl ayrışır?"
6. **Hidden Directories Need a Visible Gate** — gizli klasör yok ilkesi (jarvis/CLAUDE.md §2). Kusur: kapısız nokta-dizinler `jarvis/lean/.lake`, `jarvis/kuyruk/ders-gbm/.venv` (canlı defterde 3. parti kod), `jarvis/mods/*/.claude-plugin`, kök `.obsidian`; `kaynak-kodu/no-mistakes` depo dışı mutlak symlink. Düzeltme: `kaynak-kodu/README.md`'ye satırlar; `.venv` için `kuyruk` dışına taşıma kararı Salih'in. Salih tek başına yapar.
7. **Worktree Lifetime Ends at Merge** — paralel oturum birimi (md.14; Karar 95 EK). Kusur: 22 worktree, 22/22 main'e merge edilmiş, 62-151 commit geride; biri depo içinde (`jarvis/.claude/worktrees/py-arsiv-...`). Düzeltme: `git worktree remove` ×22 + `git branch -d` ×21 (hepsi merged, `-d` güvenli); Salih beyanı ister (son seans kaydındaki açık karar). Doğrulama: `acilis-kapilari` K1 `TEMİZ`.
8. **Agent Context Files and Their Budget** — AGENTS.md konvansiyonu (agents.md), CLAUDE.md ≤200 satır (code.claude.com/docs/en/memory), bağlam dosyası maliyeti (Gloaguen ve ark., arXiv 2602.11988: başarı artmıyor, maliyet >%20). Kusur: `jarvis/CLAUDE.md` §7'de `kod/ lean/ mods/ graf/ paylasim/` yok; README eksik dizinler `core tools kod lean paylasim` + kök `bin sablonlar projects gunluk arsiv`; `jarvis/CLAUDE.md` symlink'i jarvis kökünde görünmüyor `[?]`. Düzeltme: §7'ye tek satır (≤80 satır bütçesi), 5 satırlık README'ler. Kapanış transferi: Salih görmediği bir dizinde (`friday/`, `ogrenme/` yok) kusuru kendi bulur.

Bağımlılık: 2 → 3 (git durumları önce) · 4 → 5 (pointer önce taşıma) · 1,6,8 bağımsız · 7 en sona (Salih beyanı).

## 3. Çerçeve bilgisi (dış kaynak taraması; doğrulanmış)
- Feature vs layer: Fowler PresentationDomainDataLayering; Nx dört kütüphane türü (feature/ui/data-access/util) + `enforce-module-boundaries`; Turborepo `apps/`+`packages/`, iç içe paket hata; Cargo workspace tek `Cargo.lock`/`target`, üyeler düz `crates/*`; Python src-layout.
- Docs-as-code: ADR yalnız-ekle + superseded (Microsoft WAF, sayfa 2026-04-10); MADR `docs/decisions/NNNN-baslik.md` v4.0.0; Diátaxis 4 form.
- Bilgi deposu: PARA (Archives üst kova), Johnny.Decimal (AC.ID; 10×10 doğrulanmadı), Zettelkasten (atomik, sabit kimlik, klasör yerine bağ).
- Veri: medallion bronze/silver/gold (Databricks); dizin adlarına eşleme Jarvis çıkarımı.
- Denetim araçları: ls-lint (ad kuralları, MIT); alint (derinlik, dosya sayısı; doğrulanmadı); Repolinter arşivlendi iddiası ikincil.
- Depodaki karşılıklar: `veri/bronz|baglam.sqlite|gorunum` = medallion; `kuyruk/senaryo-defteri.md` = ADR defteri; `arsiv/` = PARA Archives; `kaynak-kodu/` = gizli dizin kapısı.

## 4. Zayıf kanıt (derste "çıkarım" diye sunulur)
Koku listesinin tek kanonik kaynağı yok · kutu sayısı/süre · mini-ADR etkisi · treemap/ağaç diff görselinin ölçülmüş etkisi yok (yalnız CodeCity/graf ailesi ölçülü, ICSE 2011) · Johnny.Decimal 10×10 · Bazel WORKSPACE kaldırılma sürümü.

## 5. Fork oturumuna devir
- Başlangıç: "seans başı, dosya-mimarisi" → `ogren` skill'i; **probe** ≤12 soru bu dosyanın §2 kavramlarından; sonra DAG görseli (yalnız istekle), sonra kutu 1.
- Katman-1 düzeltmeler (kutu 4, 5, 8'in kanon satırları) fork'ta yazılmaz; Salih imzasıyla bu ana oturumda ya da devir dosyasıyla Jarvis'e gelir. Kutu 7 Salih beyanı ister.
- Commit: `git add <yol>` (paralel oturum canlı), karar başına ayrı commit, önek `[icra]`.
- Kaynak URL listesi tarama çıktılarında; ders kaydına taşınacak olanlar bu dosyadaki adlarla aranır.
