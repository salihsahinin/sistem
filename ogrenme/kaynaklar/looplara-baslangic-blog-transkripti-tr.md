> **TAŞINDI (2026-07-15, Salih icra emri):** Homebase'ten JARVIS'e — köken: `Cowork Homebase/[C] Looplara Baslangic — Blog Transkripti (TR).md`; tespit raporu: `raporlar/homebase-tasima-tespiti-2026-07-15.md`. Orijinal Homebase'te arşiv-pointer'la durur (m.8).

# Loop'lara Başlangıç

**Kaynak:** @ClaudeDevs — 6 Temmuz 2026 (yazan: @delba_oliveira)

Şu sıralar coding agent'ına prompt yazmak yerine "loop tasarlamak" üzerine çok konuşuluyor. X'te bir loop'un tam olarak ne olduğunu anlamaya çalışırsanız birden fazla farklı cevapla karşılaşırsınız.

Claude Code ekibi olarak biz **loop'ları, bir durma koşulu sağlanana kadar iş döngülerini tekrarlayan agent'lar** olarak tanımlıyoruz. Birkaç farklı loop türünü şu kriterlere göre kategorize ediyoruz:

- Nasıl tetiklendikleri
- Nasıl durdurdukları
- Hangi Claude Code primitifinin (temel yapı taşı) kullanıldığı
- Her birinin hangi görev türüne en uygun olduğu

Ana loop türlerini, her birinin ne zaman kullanılacağını ve token kullanımını yönetirken kod kalitesini nasıl koruyacağınızı ele alacağız. Her görev karmaşık loop'lar gerektirmez; en basit çözümle başlayın ve bu desenleri seçici kullanın.

## Tur-tabanlı loop'lar (Turn-based)

- **Tetikleyici:** Kullanıcı prompt'u.
- **Durma kriteri:** Claude görevi tamamladığına ya da ek bağlama ihtiyacı olduğuna karar verir.
- **En iyi kullanım:** Düzenli bir sürecin ya da programın parçası olmayan kısa görevler.
- **Kullanım yönetimi:** Spesifik prompt'lar yazın ve tur sayısını azaltmak için skill'lerle doğrulamayı iyileştirin.

Gönderdiğiniz her prompt, her turu sizin yönlendirdiğiniz manuel bir loop başlatır. Claude bağlam toplar, aksiyon alır, işini kontrol eder, gerekirse tekrarlar ve yanıt verir. Buna agentic loop diyoruz.

Örneğin Claude'dan bir beğeni butonu oluşturmasını isteyin. Kodunuzu okur, düzenlemeyi yapar, testleri çalıştırır ve çalıştığına inandığı bir şeyi size teslim eder. Sonra işi manuel olarak kontrol eder ve bir sonraki prompt'u yazarsınız.

Manuel adımlarınızı bir SKILL.md olarak kodlayarak doğrulama adımını iyileştirebilirsiniz; böylece Claude kendi işinin daha fazlasını uçtan uca kontrol edebilir. Bu, Claude'un sonucu görmesini, ölçmesini veya sonuçla etkileşmesini sağlayacak araçları veya connector'ları içermelidir. Kontroller ne kadar nicel olursa, Claude'un kendi kendini doğrulaması o kadar kolaylaşır.

Örneğin SKILL.md dosyanızda şunu belirtebilirsiniz:

```markdown
---
name: verify-frontend-change
description: Herhangi bir UI değişikliğini tamamlandı ilan etmeden önce uçtan uca doğrula.
---

# Frontend değişikliklerini doğrulama
Bir UI değişikliğini yalnızca başarılı bir edit'e dayanarak asla tamamlandı diye raporlama. İnsan bir reviewer'ın yapacağı gibi doğrula:

1. Dev sunucusunu başlat ve düzenlenen sayfayı tarayıcıda aç.

2. Değişiklikle doğrudan etkileş. Yeni bir kontrol (buton, input, toggle) için: tıkla, beklenen durum değişimini doğrula ve öncesi/sonrası ekran görüntüsü al.

3. Tarayıcı konsolunu kontrol et: sıfır yeni hata veya uyarı.

4. Chrome Devtools MCP'yi kullanarak bir performans trace'i çalıştır ve Core Web Vitals denetimi yap.

Herhangi bir adım başarısız olursa sorunu düzelt ve 1. adımdan itibaren yeniden çalıştır — kısmen doğrulanmış işi teslim etme.
```

## Hedef-tabanlı loop (/goal)

- **Tetikleyici:** Gerçek zamanlı manuel bir prompt.
- **Durma kriteri:** Hedefe ulaşıldı VEYA maksimum tur sayısına erişildi.
- **En iyi kullanım:** Doğrulanabilir çıkış kriterleri olan görevler.
- **Kullanım yönetimi:** Spesifik bir tamamlanma kriteri ve açık tur limitleri belirleyin: "5 denemeden sonra dur."

Bazen tek bir tur yeterli olmaz, özellikle daha karmaşık görevlerde. Agent'lar iterasyon yapabildiklerinde daha iyi performans gösterir. "Bitti"nin neye benzediğini /goal ile tanımlayarak Claude'un ne kadar süre iterasyona devam edeceğini uzatabilirsiniz.

Başarı kriterini siz tanımladığınızda, Claude neyin "yeterince iyi" olduğuna karar vermek ve loop'u erken bitirmek zorunda kalmaz. Claude her durmaya çalıştığında bir değerlendirici model koşulunuzu kontrol eder ve hedef karşılanana ya da tanımladığınız tur sayısına ulaşılana kadar onu işe geri gönderir.

Bu yüzden geçen test sayısı ya da belirli bir skor eşiğini aşmak gibi deterministik kriterler bu kadar etkilidir.

Örneğin:

```bash
/goal ana sayfanın Lighthouse skorunu 90 veya üzerine çıkar, 5 denemeden sonra dur.
```

## Zaman-tabanlı loop (/loop ve /schedule)

- **Tetikleyici:** Belirlenen bir zaman aralığı.
- **Durma kriteri:** Siz iptal edersiniz ya da iş tamamlanır (PR merge edilir, kuyruk boşalır).
- **En iyi kullanım:** Tekrarlayan işler ya da dış ortamlar/sistemlerle arayüz kurma.
- **Kullanım yönetimi:** Daha uzun aralıklar belirleyin ya da zamana değil olaylara göre tepki verin.

Bazı agentic işler tekrarlayıcıdır: görev aynı kalır, yalnızca girdiler değişir. Örneğin her sabah Slack mesajlarını özetlemek. Diğer işler dış sistemlere bağlıdır ve bunlarla arayüz kurmanın basit bir yolu, belirli aralıklarla kontrol edip değişene tepki vermektir. Örneğin kod review'ları alabilecek ya da CI'ı fail edebilecek bir PR.

Bunlar için Claude'un ne zaman çalışacağını, bir prompt'u belirli aralıklarla yeniden çalıştıran `/loop` ile tetikleyebilirsiniz. Örneğin:

```bash
/loop 5m PR'ımı kontrol et, review yorumlarını ele al ve fail eden CI'ı düzelt
```

`/loop` sizin bilgisayarınızda çalışır; kapatırsanız durur. `/schedule` ile bir routine (rutin — bulutta zamanlanmış görev) oluşturarak loop'u buluta taşıyabilirsiniz.

## Proaktif loop'lar

- **Tetikleyici:** Bir olay ya da program; gerçek zamanda insan olmadan.
- **Durma kriteri:** Her görev hedefine ulaşınca sonlanır. Routine'in kendisi siz kapatana kadar çalışır.
- **En iyi kullanım:** İyi tanımlanmış tekrarlayan iş akışları: bug raporları, issue triage, migration'lar, dependency yükseltmeleri vb.
- **Kullanım yönetimi:** Routine'leri daha küçük, daha hızlı modellere yönlendirin ve yargı gerektiren kararlar için en yetenekli modeli kullanın.

Yukarıdaki primitifler, **auto mode** ve **dynamic workflows** (araştırma önizlemesi) gibi diğer Claude Code özellikleriyle birlikte, uzun soluklu işler için bir loop halinde birleştirilebilir.

Örneğin gelen geri bildirimi ele almak için:

1. **`/schedule`** (araştırma önizlemesi) ile yeni raporları kontrol eden bir routine çalıştırın
2. **`/goal`** ile "bitti"nin neye benzediğini tanımlayın ve nasıl doğrulanacağını **skill'lerle** belgeleyin
3. **Dynamic workflows** ile her raporu triage eden, düzelten ve düzeltmeyi review eden agent'ları orkestre edin
4. **Auto mode** ile routine izin sormak için durmadan çalışsın

Hepsini bir araya getirince prompt şöyle görünebilir:

```bash
/schedule her saat: project-feedback kanalını bug raporları için kontrol et. /goal: bu çalıştırmada bulunan her rapor triage edilene, aksiyon alınana ve yanıtlanana kadar durma. Bir bug'ı düzeltirken, paralel worktree'lerde üç çözümü keşfetmek için bir workflow kullan ve bir judge'ın bunları adversarial (karşıt gözle) review etmesini sağla.
```

## Kod kalitesini korumak

Bir loop'un çıktısının kalitesi, etrafındaki sisteme bağlıdır. Sistemi tasarlarken:

- **Codebase'in kendisini temiz tutun:** Claude, codebase'inizde halihazırda var olan desenleri ve konvansiyonları takip eder.
- **Claude'a kendi işini doğrulamanın bir yolunu verin:** Sizin ve ekibiniz için "iyi"nin neye benzediğini skill'lerle kodlayın.
- **Dokümanlara ulaşmayı kolaylaştırın:** Framework ve kütüphane dokümanları güncel best practice'leri içerir.
- **Kod review'ları için ikinci bir agent kullanın:** Taze bağlama sahip bir reviewer daha az yanlıdır ve ana agent'ın akıl yürütmesinden etkilenmez. Yerleşik `/code-review` skill'ini ya da GitHub için Code Review'ı kullanabilirsiniz.

Tekil bir sonuç standardı karşılamadığında, sadece o sorunu düzeltmekle kalmayın; gelecekteki tüm iterasyonlar için sistemi iyileştirecek şekilde kodlamaya çalışın.

## Token kullanımını yönetmek

Token kullanımını yönetmek için loop'ların net sınırları olmalı:

- **İş için doğru primitifi ve modeli seçin:** Küçük görevler birden fazla agent ya da loop gerektirmez. Bazı görevler daha ucuz ve hızlı modelleri kullanabilir.
- **Net başarı ve durma kriterleri tanımlayın:** "Bitti"nin neye benzediği konusunda spesifik olun ki Claude çözüme daha erken varabilsin (ama fazla erken de değil).
- **Büyük bir çalıştırmadan önce pilot yapın:** Dynamic workflows yüzlerce agent doğurabilir. Önce işin küçük bir diliminde kullanımı ölçün.
- **Deterministik işler için script kullanın:** Bir script çalıştırmak, adımları akıl yürüterek geçmekten daha ucuzdur. Örneğin bir PDF skill'i, kodu her seferinde yeniden türetmek yerine Claude'un her defasında çalıştırdığı bir form-doldurma script'i içerebilir.
- **Routine'leri gereğinden sık çalıştırmayın:** Aralığı, izlediğiniz şeyin ne sıklıkla değiştiğiyle eşleştirin.
- **Kullanımı gözden geçirin:** `/usage` komutu son kullanımı skill, subagent ve MCP bazında döker; argümansız `/goal` şu ana kadarki tur sayısını ve token kullanımını gösterir; `/workflows` her agent'ın token kullanımını gösterir ve bir agent'ı istediğiniz an durdurabilirsiniz.

## Başlarken

Özetle:

| Loop | Devrettiğiniz şey | Ne zaman kullanmalı | Aracınız |
| --- | --- | --- | --- |
| Tur-tabanlı | Kontrol | Keşfediyor ya da karar veriyorsanız | Özel doğrulama skill'leri |
| Hedef-tabanlı | Durma koşulu | "Bitti"nin neye benzediğini biliyorsanız | /goal |
| Zaman-tabanlı | Tetikleyici | İş projenizin dışında, bir programa göre gerçekleşiyorsa | /loop, /schedule |
| Proaktif | Prompt'un kendisi | İş tekrarlayan ve iyi tanımlanmışsa | Yukarıdakilerin hepsi + dynamic workflows |

Loop'lara başlamak için halihazırda yaptığınız işlere bakın. Darboğazın siz olduğunuz bir görev seçin ve hangi parçayı devredebileceğinizi sorun: doğrulama kontrolünü yazabilir misiniz? Hedef yeterince net mi? İş bir programa göre mi geliyor?

Bir fikriniz olduğunda loop'u çalıştırın, nerede takıldığı ya da aşırıya kaçtığı gibi sonuçları gözlemleyin ve üzerinde iterasyon yapmaktan çekinmeyin.

Daha fazla bilgi için Claude Code dokümanlarındaki agent'ları paralel çalıştırma, loop, schedule, goal ve dynamic workflows sayfalarına bakın.
