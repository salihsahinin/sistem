# Cowork/CC Tartışma Oturumu — INDEX (2026-07-17→18)

> **"Dün konuştuklarımı bul" giriş-noktası.** Salih'in CC (Opus yan-oturum) tarafında açtığı tartışma serisinin toplu haritası. **Mod:** hepsi TARTIŞMA/aday · KARAR YOK · **commit branch'e (Salih 07-18 izni, PC'den bulunabilirlik)** · **merge→main/canon = Fable Cowork süzgeci (m.41).** Kanon dosyalarına (core/, pano, kapsül, senaryo-defteri, fikir-kutusu) DOKUNULMADI.

## Nasıl bulunur (PC/Cowork'ten)
`git log --oneline` → bu commit · ya da `raporlar/2026-07-17-*` dosyaları. Scratchpad = uzak-oturum geçici klasörü, PC'den erişilemez (o yüzden commit'lendi).

## Raporlar
1. **`2026-07-17-otomasyon-vizyon-mimarisi-3model.md`** — Nihai hedef (sesle/telefondan geliştirme). Atlas 4-şerit dış-tarama (ses/mobil/otonomi/guardrail) + m.37 **3-model (A kaldıraç / B ölçüm-önce ✅ / C worst-case karşıt-temel)** + triangülasyon + **§9 Kararlar Kısmı** (sesli/mobil karar konsolu, m.18 üç-yüz).
2. **`2026-07-17-skill-fikri-kutusu.md`** — Tekrarlayan-küme→skill tespiti + örnek skill'ler (`karar-modeli`/`karar-hatti`/`atlas-kosum`) + değer sıralaması + Atlas rafine (eval + m.31 freni).
3. **`2026-07-17-cc-okuma-sirasi.md`** — CC'nin Cowork gibi davranması: **yetkinlik özdeş / yetki ayrı** · Cowork≠CC (ortak CLAUDE.md) · 3 opsiyon (pointer / **SessionStart hook** / snapshot) · PreToolUse yetki-kilidi.
4. **`2026-07-17-skill-nasil-olusturulur.md`** — Skill üretim metodolojisi: frontmatter (otoriter) · description zanaatı · script-vs-LLM + `disable-model-invocation` freni · **kompozisyon (`karar-hatti` = context:fork orkestratör)** · skill-creator eval · tuzaklar.
5. **`2026-07-18-yakinsayan-formul-kategorizasyon.md`** — m.35 matematiksel omurgası: skill-kombinasyon aramasını RASTGELE'den YAKINSAYAN'a çevirme. **4-facet kategorizasyon** (işlev×nesne×yetki×tekrar) + **Contextual Thompson Sampling/BOHB** + **desirability 4-tuple ödül** + pişmanlık-eğrisi ölçümü. Açık risk: durağan-olmama.
6. **`2026-07-18-geri-alinabilirlik-plan-optimizasyonu.md`** — kararlara **geri-alınabilirlik notu** + önem-sıralı plan opt. **m.37 3-model** (A skaler-etiket+son-sorumlu-an ✅ / B reel-opsiyon / C worst-case karşıt-temel). **★ Geri-alınabilirlik AMAÇ-FONKSİYONUNU seçer** (iki-yönlü→A/WSJF, tek-yönlü→C/minimax). senaryo-defterine `Geri-alınabilirlik:` alanı (07-15 RİSK-sütununu formalleştirir) + KAPI/SIRA/EÖ formülleri (Φ zamanlama-kapısı). Uyarı: cost-of-change eğrisi kanıt değil.
7. **`2026-07-18-planlanmis-optimizasyon-fikirleri.md`** — **fikir-kutusu adayı blok:** oturumun 14 ertelenmiş optimizasyonu (O1-O14) tek tetiklenebilir kayıtta. **★ İki maliyet-sınıfı:** taşıyan-borç (C_carry>0, erken-tetik) vs saf-opsiyon (C_carry≈0, beklet+çoğu budanır). İki-katmanlı tetik: KAPI `P·V>erteleme` + reel-opsiyon (a∨b∨c); SIRA WSJF/RICE. m.37-yakınsama = budama motoru. m.5/A7 bağı.
8. **`2026-07-18-skill-desenleri-veriden-madenleme.md`** — öğrenme-şeridi GİBİ ama iç korpustan (git-log/senaryo-defteri/raporlar/cc) skill-deseni madenleme. **Üç grain** (episodik/semantik/**prosedürel=boşluk**); öğrenme-şeridini aynalayan 5+1 döngü (+ACE bakım halkası); `skill olur ⟺ destek≥minsup ∧ MDL>0 ∧ LGG az-slot`; 7-aşama boru hattı (AWM/anti-unification/MDL). **★ Kanon riski: m.34 context-collapse** (monolitik yeniden-özüt → ACE delta'ya çevir). Keşif-tarafı; rapor 5 = seçim-tarafı.
12. **`2026-07-18-gece-arastirma-sistemi-kullanim.md`** — Salih fikri: **gece-araştırma sistemi** (sonsuz-araştırma → öncelik-partisyon + **[S]/[O]/[T] derinlik-haritası** = rapor 11 pointer-grafı → derin-kaynak eskalasyonu → **Salih-diline İNDİRGEME** "karar için açıklama, ustalık için değil" = V55+m.17) + m.37 saturation durma-kuralı. + **JARVIS'i gece kullanma** playbook (şirket/kişisel/öğrenme/bakım). m.27 uyku/günaydın · K-009 kapısı. *(§2-yöntem/§3-playbook: Atlas rafine.)*

---

11. **`2026-07-18-pointer-sistemi-iletisim-kategorizasyon.md`** — m.20 pointer ölçek: pointerlar-arası iletişim + tür kategorizasyonu. **m.37 3-model:** A tipli-bağ-grafı✅ / B gömük-erişim / C holist-emergent (**karşıt-temel = rapor 9 atomizm↔holizm DEVAMI**). **★ spreading-activation** = iletişim mekanizması; **A-MEM/GraphRAG/MOC**; yakınsak-çekirdek 5 bağ-türü (SKOS/CiTO/RST); **Grindrod uzlaşması** (benzerlik≠özdeşlik); **tipli-bağ = m.34 delta aracı** (supersedes silmeden-geçersizkılar, context-collapse panzehiri). Katmanlı-hibrit (m.20/22/34 izomorfik).

---

10. **`2026-07-18-jarvis-arayuz-cok-sayfa-mod.md`** — kararlar-kısmını tam **JARVIS arayüzü**ne genişletme: **3 kategori** (A paylaşılan/gözlemlenebilirlik · B Salih-özel · C mod-sayfaları), tek git-omurgası → çok yüz (m.18). **★ Gözlemlenebilirlik:** Claude Code OTel `effort`+`agent.name`+`cost.usage` ZATEN yayınlıyor → event-sourcing JSONL log → tablo projeksiyonu (koşan=Start-var-Stop-yok; çift-sayım: total_cost_usd partisyonu). **★ "Konuşarak İnşa Modu 1":** oyun ikinci-ekran companion, bağlam-adaptif tetik, yalnız Tier-1(m.31) sesli keser, earcon+glanceable. G4/m.18/m.28/m.31 bağı.

---

9. **`2026-07-18-tractatus-temel-onerme-kesisim.md`** — felsefi zemin: Tractatus **5.5262** (temel önermeler→dünya Spielraum'u) + Russell zıt (genel-olgular var / holizm). **★ DÖRT-YOLLU EŞLEME** — Tractatus'u çökeren 2 probleme tüzük yapısal cevap: atomist-form=**m.38** · bağımsızlık-yok/renk-dışlama(6.3751)=**m.16** · kapanış/genellik(Russell genel-olgu)=**m.41** · tek-temel-riski=**m.37**. Not: Salih'in okuduğu çeviri parantez-yanılsaması içeriyordu (gerçek gerilim=renk-dışlama). Öz: *formda Tractatus, yönetimde Russell/Quine, anti-monist sigortalı.*

## Açık sorular — TOPLU (Salih cevabı bekleniyor; karar ALINMADI, 07-17 kuralı)
**Skill:** kutu evi (ayrı dosya/bölüm)? · ilk skill (`karar-modeli`/`karar-hatti`)? · hangileri üretim-adayı? · "tekrarlayan-küme→skill" kuralı kanona girsin mi?
**CC:** CC hep yan mı / Fable+beyanla ana-sıra olabilir mi? · hook mu pointer mı? · yetki yapısal-kilit mi talimat mı? · banner metni?
**Otomasyon:** "canlı ajan" çizgisi hangi basamak? · ses PoC'una şimdi mi? · guardrail ilk dilimle mi?
**Kararlar kısmı:** ayrı UI mı (A pano/B push/C ses) yoksa mevcut-yüzey skill/view mi? · hangi kararlar konsola? · sesli-onay doğrulama-derinliği? · `karar-modeli` skill'inin çıktı-hedefi mi?

## Standing direktif (aday — Fable kanonlar)
- Salih 07-17: "atlası her istediğin için koştur" (serbest atlas).
- Salih 07-17: cevaplanmamış soruda karar alma → rapora ekle.
- Salih 07-17: tekrarlayan-küme→skill fikri kutusu.
- Salih 07-18: bu raporlar branch'e commit'lenebilir (bulunabilirlik); merge/canon Fable'da.
- Salih 07-18: skill-geliştirme RASTGELE değil YAKINSAYAN formül olmalı; kaldıraç = talimatları doğru kategorize (rapor #5).
- Bütünlük denetimi 07-18: geç-commit eksiklik bırakmadı (scratchpad↔repo 3/3 özdeş, push tam).

## Not
Rapor #4 §9 (Atlas skill-metodolojisi: EVAL-ÖNCE akış · description zanaatı · 15 tuzak · kompozisyon gerçeği + `karar-hatti` dersleri) DONE — tüm dış-tarama tamamlandı. Bu oturumun bütün araştırma şeritleri kapandı.
