# Bulut-vardiya raporu: skill mimarisi + Dispatch + ana-oturum tanımı (2026-07-23)

> 1 satır: Bulut Cowork oturumunun teslimi — skill katmanları netleşti, Dispatch araştırıldı, ana-oturumun yüzeyden bağımsız tanımı karar-adayı olarak sunuluyor. DAMGA: HAM FİKİR / PC'de ingest edilecek.
> Kaynak oturum: bulut Cowork, JARVIS köprüyle bağlı (CLAUDE.md otomatik okundu; proje-skilleri pasifti).

## 1. Skill katmanları — tespit (bulgu, karar değil)

İki ayrı katman var ve karışıyordu:

- **Proje-skilleri** (`C:\JARVIS\.claude\skills\`): atlas-kosum · celiski-kapisi · karar-hatti · karar-modeli. Yalnız PC'den JARVIS klasöründen açılan oturumlarda otomatik yüklenir. Bulut oturumları bunları YÜKLEMEZ (dosya olarak okunabilir, tetik çalışmaz).
- **Hesap-skilleri** (app'e kurulu, her yüzeyde gelir): hizalama · dev-run-planner · morning · grill-me (+ Anthropic format skilleri + cowork-starter-pack plugin'i).

Yapısal kısıt: Carvis hesaba skill KURAMAZ — yalnız `.skill` paketi hazırlar, kurulum tıkı Salih'te. Proje-skillerine ise köprüden/PC'den tam yazım yetkisi var.

Önerilen mimari (Salih'e sunuldu, itiraz gelmedi; teyit ana oturumda): varsayılan yerleşim `.claude/skills` (tam otomasyon, Carvis yetkisinde) · yalnız mobil/bulutta da gereken skiller hesaba terfi eder (Salih tıkıyla).

## 2. Dispatch — araştırma özeti (dış kaynak: code.claude.com + support.claude.com)

- Dispatch = Cowork sekmesinde yaşayan, telefon+masaüstünden erişilen TEK sürekli sohbet. Görev mesajlanır; Dispatch işi PC'de koşturur — geliştirme işine Claude Code oturumu, bilgi işine Cowork oturumu açar; sonuç bildirimle döner. Şart: masaüstü uygulaması açık/uyanık + Pro-Max plan.
- JARVIS hattındaki yeri: vizyon sıralamasında (dosya zemini → kuyruk → canlı ajan) **kuyruk katmanının hazır-gelen hali**. Telefondan atılan görev JARVIS zemininde, proje-skilleriyle, tam dosya erişimiyle koşar → bulut oturumlarının "skill yüklenmiyor" boşluğunu kapatır.
- Telefondan üç yol farkı: bulut CC (Anthropic sunucusu, PC kapaliyken sürer, yerel erişim yok) · Remote Control (PC'de açık CC oturumunu telefondan sürme) · Dispatch (görev mesajla, iş PC'de, yönlendirme Dispatch'te).
- **Çelişki-kapısı notu (m.16):** Dispatch'in zamanlanmış/tekrarlayan görev özelliği K-009/K-010 blokajıyla (otomasyon yok) çelişir. Öneri: o özellik blokaj kalkana dek KAPALI. Salih-tetiklemeli görevler blokaja girmez. Karar Salih'in — henüz alınmadı.
- Kurulum Salih'in elinde (Carvis yapamaz): iki uygulamayı güncelle → Cowork → Dispatch → Get started → izinler → Finish setup. Kurulum bu rapor yazılırken henüz yapılmamıştı.
- Önerilen ilk test promptu (okuma-yalnız, üçlü test: dosya erişimi + yönlendirme + CLAUDE.md zemini):
  "Çalışma zeminim C:\JARVIS klasörü; oradaki CLAUDE.md oturum kurallarını içerir. İlk görev: C:\JARVIS\core\durum-kapsulu.md dosyasını oku ve bana tek satır insan-yüzü durum özeti gönder. Hiçbir dosyaya yazma."
  İkinci test (kademeli, m.40): küçük yazma görevi — kuyruk'a tek satır.

## 3. KARAR-ADAYI (Katman 1 — Salih imzası gerekir): ana-oturumun yetenek-listeli tanımı

m.41'deki CC-Fable deseninin genelleştirilmesi. Taslak madde:

> Bir oturum ana oturumdur ↔ (kanon okunuyor: CLAUDE.md ∧ kapsül ∧ pano) ∧ (kanon-yazım kanalı var) ∧ (Salih "ana sıra" beyanı).

Yüzey-başına durum: PC Cowork = doğal ana · CC = koşullu-ana (m.41, mevcut) · bulut Cowork (köprü açıkken) = iki koşul sağlanıyor, eksikler: açılışta kapsül+pano okuması (manuel yapılabilir) + commit'in PC'ye devri · Dispatch = işi PC'de koşturduğundan doğal ana zemin · köprüsüz mobil = snapshot, ana olamaz.

Artı: süreklilik yüzeyden kopar, vardiya her yerden devralınır. Eksi: yazım-kanalı zayıf yüzeylerde proof-of-work (m.9) commit'siz kalır — devir protokolü şart. İmza + tüzüğe işleme ana oturumda.

## 4. Oturumda yapılan yazımlar (Katman 2, geri-alınabilir)

- `kuyruk/2026-07-23-skill-kurulum-notu.md` — skill terfi süzgeci + kurulumlar SONRAYA (Salih emri). 4 proje-skill'in hesap-terfi değerlendirmesi bekliyor.
- Bu rapor: `raporlar/2026-07-23-bulut-vardiya-dispatch-skill-raporu.md`.
- Commit atılmadı (bulut yüzeyi, git'e dokunulmadı) — ana vardiya commit'ler.

## 5. Ana oturum için iş sırası önerisi

1. Bu raporu ingest et; §3 karar-adayını imzala/reddet/revize et.
2. Dispatch kurulumu (Salih) + ilk test promptu koşumu; sonuç senaryo-defterine.
3. Zamanlanmış-görev özelliği kararı (§2 çelişki notu).
4. Skill terfi süzgeci (kuyruk notu) + gerekirse .skill paketleri.
5. "Günaydın" açılış davranışı: PC'de açılış işini CLAUDE.md okuma-sırası yapıyor, skill yok — vardiya-açılış skill'i istenirse ayrı karar.
