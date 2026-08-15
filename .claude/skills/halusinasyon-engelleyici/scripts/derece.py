#!/usr/bin/env python3
"""derece.py — Görev-Müsaitlik Derece Formülü H(görev) (core/halusinasyon-paketi.md §2, v1 deneysel m.29).
Toplamsal, tamsayı ağırlıklı, işaret-beyanlı; ağırlıklar KANITSIZ-TERCİH damgalı (küçük-veri kilidi: <50 olay → öğrenilmez).
Kullanım: python3 derece.py [--v1 --v2 --v3a --v3b --v3c --v3d --v4 --v5 --v6 --v7a --v7b --v7c --v8 --v9 --v10] [--pahali-geri-alma] [--json]
Çıkış: H · eşik · TETİK/OPSİYONEL/GEREKMEZ · ima edilen maliyet beyanı · aktif değişkenler. Çıkış kodu: 0 = tetik gerekmez · 10 = skill TETİKLENİR · 5 = F1+F2 zorunlu (opsiyonel skill).
"""
import sys, json

W = {
 'v1':  (+2, 'NADİRLİK (uzun-kuyruk varlık/konu; arama 1-2 sonuç = singleton bölgesi)'),
 'v2':  (+3, 'TAZELİK (cevap ≤1 yılda değişir ∨ kesim-sonrası)'),
 'v3a': (+3, 'ÇIKTI-TÜRÜ atıf/künye/DOI/URL/kaynakça — OVERRIDE: skill zorunlu'),
 'v3b': (+2, 'ÇIKTI-TÜRÜ yapılandırılmış-veri → düzyazı'),
 'v3c': (+2, 'ÇIKTI-TÜRÜ kod API/paket/araç adı ∨ prosedür adımları'),
 'v3d': (+1, 'SAYISAL/TARİH iddiaları'),
 'v4':  (+1, 'UZUNLUK >~10 atomik iddia ∨ >300 kelime'),
 'v5':  (+2, 'BİLEŞİKLİK ≥3 atlamalı/adımlı'),
 'v6':  (+2, 'ÖNCÜL/CEVAPLANABİLİRLİK şüphesi'),
 'v7a': (+2, 'KAYNAK YOK (kapalı-kitap)'),
 'v7b': (+1, 'kaynak HAM/uzun (>32K ∨ örtüşmesiz)'),
 'v7c': (-1, 'kaynak yapılandırılmış+provenanslı (indirim sınırlı)'),
 'v8':  (-2, 'DOĞRULAYICI/YÜRÜTÜCÜ VAR (test·yürütme·registry·hesap)'),
 'v9':  (+1, 'RUNTIME thinking-on ∧ araç-çağrısı [? Claude ölçülmemiş]'),
 'v10': (+1, 'DİL Türkçe/az-kaynaklı olgusal çıktı [? kör — kanıtsız-tercih]'),
}

def main():
    flags = {k: (f'--{k}' in sys.argv) for k in W}
    pahali = '--pahali-geri-alma' in sys.argv
    as_json = '--json' in sys.argv
    if not any(flags.values()) and '--help' in sys.argv or len(sys.argv) == 1:
        print(__doc__); sys.exit(2)
    H = sum(W[k][0] for k, on in flags.items() if on)
    esik = 4 if pahali else 7
    override = flags['v3a']
    if override or H >= esik: karar, code = 'TETİK — halusinasyon-engelleyici skill ile üret', 10
    elif H >= 4: karar, code = 'F1+F2 ZORUNLU (kaynak + destek-kontrolü); skill opsiyonel', 5
    else: karar, code = 'GEREKMEZ — kanon frenleri (m.39 · D/K/X · bulunamadı) yeter', 0
    ima = ("kaçırma bedeli yanlış-alarmdan ≥3× kötü (pahalı-geri-alma sınıfı: m.31)" if pahali
           else "skill bedeli ≈3-5× çağrı ↔ kaçırma bedeli = geri-alma (normal görev)")
    out = {'H': H, 'esik': esik, 'override_v3a': override, 'karar': karar,
           'ima_edilen_maliyet': ima, 'aktif': [f"{k} ({W[k][0]:+d}) {W[k][1]}" for k, on in flags.items() if on],
           'damga': 'deneysel m.29 · ağırlıklar kanıtsız-tercih · ≥50 olayda yeniden kalibre · her koşum kuyruk/halusinasyon-kayit.md'}
    if as_json: print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        print(f"H = {H} · eşik = {esik}{' · OVERRIDE v3a' if override else ''} → {karar}")
        print(f"ima edilen maliyet: {ima}")
        for a in out['aktif']: print("  +", a)
        print("damga:", out['damga'])
    sys.exit(code)

if __name__ == '__main__':
    main()
