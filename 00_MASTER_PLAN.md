# 00 — MASTER PLAN: 6 Aylık Proof-of-Work Portföyü

**Karar kaynağı:** Salih, 2026-07-10 — "BUILD VAR" + "proof of work ile ilerleyeceğiz" + "6 ay şimdilik" + hedef "bomba gibi CV" (staj bulunamadı → 2027 yaz penceresi). **Statü:** aktif plan; tek-flagship stratejisi red-team kanıtına dayalı Katman-2 varsayılanıdır (veto = revert). **Revizyon kuralı:** bu dosya ay sonunda tek satır gerçekleşme kaydıyla güncellenir — daha sık değil (plan-spiral koruması).

## 1. Hedef tanımı

6 ay sonunda (≈ 2027 Ocak, ilk başvuru pencereleri açılırken): **başvuruya hazır İngilizce CV + onu taşıyan kanıt seti.**

**Proof of work tanımı:** herkesin doğrulayabileceği eser — public repo, düzenli commit tarihçesi, geçen testler, canlı demo linki, ölçülmüş sonuç. Plan, niyet ve markdown KANIT DEĞİLDİR. (Bu reponun kendisi de kanıt sayılmaz — komuta merkezidir.)

**Kayıtlı duvar (red-team, 07-10):** son 2 günde plan reposuna 53 commit, CV artefaktına 0. Bu planın tek gerçek riski budur; bütün tasarım bu duvara karşı kurulmuştur.

## 2. Artefakt sınıflandırması (red-team sonrası)

| Artefakt | Rol | Statü |
|---|---|---|
| **PortRisk** (`github.com/salihsahinin/portrisk`) | TEK FLAGSHIP — finans-domenli data/ML kanıtı | AKTİF; canlı demoya kadar başka artefakt açılmaz |
| **vault-index** (bilgi-index CLI) | Dondurulmuş aday — repo #2 | DONDU; geri-açma tetiği: PortRisk canlı-link DONE. Blueprint hazır: `02_KNOWLEDGE_INDEX_PLAN.md` |
| **JARVIS node** (bu repo) | Komuta merkezi + mülakat anlatısı kaynağı | PRIVATE kalır; CV'ye repo olarak GİRMEZ (red-team: noise/red-flag). Taşıyıcısı: mülakat anlatısı + PortRisk README'de "AI-assisted workflow" bölümü |
| **Yarışma satırı** (IMC Prosperity ya da eşdeğer) | GPA'dan bağımsız ölçülebilir sinyal | Tur açılınca kayıt (pano K-005) |

## 3. PortRisk hattı — flagship'in DONE merdiveni

Her basamağın DONE'u yazılı; basamak atlanmaz. (Loop-eng dersi: done yazamıyorsan iş tanımlamamışsındır.)

1. **Sprint 1 — veri + getiriler.** yfinance ile fiyat çek, getiri serileri hesapla. DONE: pytest yeşil + push.
2. **Sprint 2 — SQL katmanı.** Fiyat verisi SQLite'a yazılır/sorgulanır (screener'ların değişmez maddesi; strateji Faz-2'den öne çekildi). DONE: veri katmanı SQLite üzerinden; README'de şema + örnek sorgu; ≥1 test SQL'i kapsar.
3. **Sprint 3 — risk metrikleri.** Volatilite, Sharpe, Sortino, max drawdown. DONE: her metrik test + MİDAS v7 15-enstrüman portföyüyle örnek çıktı.
4. **Sprint 4 — VaR.** Tarihsel + parametrik VaR; varsayımların yazılı savunusu. DONE: iki yöntem test'li + metodoloji notu (İngilizce).
5. **Sprint 5 — backtest çekirdeği.** Ağırlıklı portföy vs benchmark. DONE: tek komutla koşan backtest + grafik çıktısı.
6. **Sprint 6 — DEPLOY.** Streamlit dashboard, canlı URL (Streamlit Community Cloud — ücretsiz). DONE: README'nin ilk ekranında tıklanabilir canlı link + demo GIF.
7. **Sprint 7 — cila.** İngilizce README (hook 1 cümle + demo + mimari diyagram + metodoloji + "AI-assisted workflow: neyi AI yaptı, neyi elle doğruladım" bölümü — 2026 slop-ayrıştırıcısı). DONE: dış okuyucu 2 dakikada ne olduğunu anlıyor.

**Ayrıştırıcı anlatı (jenerik VaR repo mezarlığından çıkış):** "Kendi gerçek 15-enstrümanlı portföyümün riskini ölçemiyordum; aracı kendim kurdum" — MİDAS v7 model portföyü (gerçek bakiye rakamları ASLA repoya girmez, yalnız model ağırlıkları).

## 4. 6 aylık takvim (ay sonu DONE'ları)

| Ay | İş | DONE |
|---|---|---|
| **Temmuz** (kalan 3 hafta) | Sprint 1 + Sprint 2 başlangıcı; commit çapası başlar | Sprint 1 DONE; ≥6 push'lu commit |
| **Ağustos** | Sprint 2-3 | SQL katmanı + risk metrikleri canlı; haftalık ≥3 commit temposu tutuyor |
| **Eylül** | Sprint 4-5 (90-gün değerlendirmesi 09-10'da Homebase kadansında — oraya bakılır) | VaR + backtest DONE |
| **Ekim** | Sprint 6-7: DEPLOY + cila | Canlı URL + İngilizce README yayında |
| **Kasım** | İngilizce paket (CV + LinkedIn + GitHub profil README — tek hafta sonu) + başvuru takvimi + dalga 1 | ATS-uyumlu 1 sayfa İngilizce CV hazır; hedef program listesi tarihli |
| **Aralık–Ocak** | Başvuru dalga 2 + IMC Prosperity (tur açılınca) + vault-index tripwire kontrolü | Başvurular atılmış; yarışma satırı CV'de (tur takvimine bağlı) |

**Başvuru pencereleri (red-team):** Garanti BBVA Talent Week Data MT ~27 Oca–19 Şub (2026 verisi; 2027 benzer beklenir) · İş Bankası MasterClass · Akbank Gençlik Akademisi · Optiver/IMC Amsterdam yaz stajları (elit eleme; yan bahis). **CV'nin gerçek deadline'ı Kasım değil, ilk programın açılış tarihi.**

## 5. Metrik ve ritim

- **TEK metrik: push'lanmış portrisk commit'i.** (Kayıtlı kural 06-10'dan beri: "gün ancak commit'le sayılır.")
- **Commit çapası:** 8 hafta boyunca haftada ≥3 anlamlı commit; mesajlar İngilizce, kendi cümlelerinle (commit şekli aynı zamanda AI-slop ayrıştırıcısı).
- **Ritim:** haftada ≥2 kod oturumu; her oturum ≥1 push ile kapanır. Sürdürülebilirlik > yoğunluk (sürtünmesizlik ilkesi, havuz #18).
- **Plan-spiral koruması:** bu repoya (JARVIS node) haftada ≤30 dk; kod:plan zaman oranı ≥ 3:1. Bu kural ihlal ediliyorsa duvar raporu §1 yeniden okunur.

## 6. Eksik-kapatma listesi (red-team §2.5'ten; takvime gömülü)

SQL → Sprint 2 · İngilizce CV/LinkedIn/profil → Kasım paketi · yarışma → Prosperity turu · canlı link → Sprint 6 · mülakat hazırlığı ("modelleme tercihini savun" + quant testleri) → Kasım'dan itibaren, başvuru dalgalarına paralel · GPA gerçeği → Salih netleştirir (banka programlarının ilk kapısı; kayıtlarda yok — açık değişken).

## 7. Karar kayıtları

1. **BUILD VAR (2026-07-10, Salih).** Kapsam: C:\JARVIS node reposu (planlar + temel katman dosyaları). Kapsam DIŞI: otomasyon, canlı ajan, Homebase kanonu. Geri-açma/onay: Salih'in ayık taraması; veto = revert. Şerh (çıplak kayıt): aynı günün daha erken kaydı "high'ım, build'e geçmek istemiyorum" (ingest #13) + BUILD YOK teyidi — çelişki taramada çözülür.
2. **Yöntem = proof of work; pist = 6 ay (2026-07-10, Salih; soru cevapları).**
3. **Tek-flagship stratejisi (2026-07-10, Carvis Katman-2 varsayılanı; kaynak: red-team raporu §2.4 + 53:0 kanıtı).** Geri-açma: Salih vetosu YA DA PortRisk canlı-link DONE (o gün vault-index çözülür).
4. **JARVIS node CV-repo'su değildir (Katman-2; kaynak: red-team §2.3).** Geri-açma: node'dan dar/çalışan/ölçülebilir bir araç çıkarsa o araç ayrı repo olarak değerlendirilir.
