# GELEN — Paralel-oturum çift-koşum, VAKA 3 (2026-08-16 00:12-00:29, S-8 downstream ×2)

> **HAM / ingest edilecek.** Zarf: [tip: ders | kaynak: seans-3-fork terminal 08-16 | tarih: 2026-08-16 | hedef: KILAVUZ paralel-vardiya + seans-acilis canlı-oturum kapısı | sema: v2]. Bağ: vaka-1 (08-12 port çakışması) · vaka-2 (08-15 emir-dosyası üstyazımı).

## Olay (çıplak veri)
- 23:59 seans-3-fork manifest'e "TEK KOŞUCU: SEANS-3" damgası bastı (`f03b63c`) — o anki bilgiyle doğru: seans-4'ün devamı ölmüştü (journal boş).
- 00:04 SEANS-5 (masaüstü; Salih beyanı "transkriptlerin devamı burası" = ÜSTÜN yetki) W-1'i devraldı; kendi eko-devamını kurdu.
- 00:12-00:15 hesap kapısı (bu oturum): OtoDev'de koşum reddedildi; kişisel hesap doğrulanınca `wf_5cd68941-2b0` başlatıldı — **manifest'in 00:0x seans-5 satırı okunmadan** (fork "devam" emrini kendi kaldığı-yer bilgisiyle icra etti).
- 00:24-00:26 seans-5/6: `wf_f0b8ec8a` (12 işçi ~743k) bitti → rapor-8 derlendi; 00:29 bu oturumun `wf_5cd68941-2b0` (12 işçi ~549k) bitti → ÇİFT-İŞ. Hasar: ~549k token (gün içi 3. çakışma).

## Bulgu
1. Manifest-damgası tek başına fren DEĞİL: damga atmak yetmiyor, koşum BAŞLATMADAN ÖNCE manifest'in SON hâli okunmalı (git log + ilgili hat satırı). Vaka-2 kuralının simetriği: "SAHADA gördüğünü koşma" + **"koşmadan önce SAHADA var mı diye BAK".**
2. Salih beyanı ("devamı burası") oturum-damgasını geçersiz kılar — fork bunu göremezdi; tek çare koşum-önü manifest okuması.
3. Çift-koşumun yan ürünü değerli: bu oturumun hakem seti TAM-kapsam antitezle koştu (eko-rejimdeki "yalnız yapı-taşı adaylarına" kısıtı yok) — G-W1 için EK kaynak (aşağıda pointer).

## Kural adayı (seans-acilis canlı-oturum kapısına ek fıkra; deneysel m.29)
> **Koşum-önü manifest kapısı:** herhangi bir Workflow/ajan başlatmadan ÖNCE ilgili manifest hattının durumu + son 30 dk git log okunur; hat başka oturumda SAHADA/DONE ise koşum başlatılmaz, fark manifest'e yazılır.

## G-W1'e ek-kaynak pointer
`~/.claude/projects/-Users-HasanSalihSahin-jarvis/914d8e47-f03d-46d2-a755-114e700f687e/subagents/workflows/wf_5cd68941-2b0/journal.jsonl` — S-8 için İKİNCİ bağımsız antitez/V26/hakem seti (12 işçi, tam-kapsam antitez, 549k). Rapor-8'le hüküm farkları çıkarsa m.40b kör-triangülasyon verisi sayılır; derleme gerekmez, sentezci şüpheli hükümde buraya iner.
