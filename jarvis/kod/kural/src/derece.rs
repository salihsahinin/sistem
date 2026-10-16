//! `halusinasyon-engelleyici/scripts/derece.py` karşılığı: görev-müsaitlik derecesi H(görev) ve tetik hükmü (core/halusinasyon-paketi.md §2).
//! Spec: `jarvis/lean/Kanon/Halusinasyon.lean` (`hukum`, `cikisKodu`); ağırlıklar ve eşikler üç yerde birebir aynıdır (fark testi).
//! Çıkış: 0 tetik gerekmez · 10 skill TETİKLENİR · 5 F1+F2 zorunlu · 2 kullanım.
use crate::py;
use serde_json::json;

const BELGE: &str = include_str!("belge/derece.txt");

/// (bayrak, ağırlık, açıklama); sıra Python sözlüğünün sırasıdır.
pub const AGIRLIK: [(&str, i32, &str); 15] = [
    ("v1", 2, "NADİRLİK (uzun-kuyruk varlık/konu; arama 1-2 sonuç = singleton bölgesi)"),
    ("v2", 3, "TAZELİK (cevap ≤1 yılda değişir ∨ kesim-sonrası)"),
    ("v3a", 3, "ÇIKTI-TÜRÜ atıf/künye/DOI/URL/kaynakça — OVERRIDE: skill zorunlu"),
    ("v3b", 2, "ÇIKTI-TÜRÜ yapılandırılmış-veri → düzyazı"),
    ("v3c", 2, "ÇIKTI-TÜRÜ kod API/paket/araç adı ∨ prosedür adımları"),
    ("v3d", 1, "SAYISAL/TARİH iddiaları"),
    ("v4", 1, "UZUNLUK >~10 atomik iddia ∨ >300 kelime"),
    ("v5", 2, "BİLEŞİKLİK ≥3 atlamalı/adımlı"),
    ("v6", 2, "ÖNCÜL/CEVAPLANABİLİRLİK şüphesi"),
    ("v7a", 2, "KAYNAK YOK (kapalı-kitap)"),
    ("v7b", 1, "kaynak HAM/uzun (>32K ∨ örtüşmesiz)"),
    ("v7c", -1, "kaynak yapılandırılmış+provenanslı (indirim sınırlı)"),
    ("v8", -2, "DOĞRULAYICI/YÜRÜTÜCÜ VAR (test·yürütme·registry·hesap)"),
    ("v9", 1, "RUNTIME thinking-on ∧ araç-çağrısı [? Claude ölçülmemiş]"),
    ("v10", 1, "DİL Türkçe/az-kaynaklı olgusal çıktı [? kör — kanıtsız-tercih]"),
];

/// Saf hüküm: (H, eşik, çıkış kodu). Lean `Kanon.Halusinasyon.derece/esik/hukum/cikisKodu` ile aynı.
pub fn hukum(bayrak: &[bool; 15], pahali: bool) -> (i32, i32, i32) {
    let h: i32 = AGIRLIK.iter().zip(bayrak).filter(|(_, a)| **a).map(|((_, w, _), _)| w).sum();
    let esik = if pahali { 4 } else { 7 };
    let atif = bayrak[2];
    let kod = if atif || h >= esik {
        10
    } else if h >= 4 {
        5
    } else {
        0
    };
    (h, esik, kod)
}

pub fn kos(argv: &[String]) -> i32 {
    let var = |a: &str| argv.iter().any(|x| x == a);
    let mut bayrak = [false; 15];
    for (i, (k, _, _)) in AGIRLIK.iter().enumerate() {
        bayrak[i] = var(&format!("--{k}"));
    }
    let pahali = var("--pahali-geri-alma");
    let json = var("--json");
    if !bayrak.iter().any(|&b| b) && var("--help") || argv.is_empty() {
        py::print(BELGE);
        return 2;
    }
    let (h, esik, kod) = hukum(&bayrak, pahali);
    let override_ = bayrak[2];
    let karar = match kod {
        10 => "TETİK — halusinasyon-engelleyici skill ile üret",
        5 => "F1+F2 ZORUNLU (kaynak + destek-kontrolü); skill opsiyonel",
        _ => "GEREKMEZ — kanon frenleri (m.39 · D/K/X · bulunamadı) yeter",
    };
    let ima = if pahali {
        "kaçırma bedeli yanlış-alarmdan ≥3× kötü (pahalı-geri-alma sınıfı: m.31)"
    } else {
        "skill bedeli ≈3-5× çağrı ↔ kaçırma bedeli = geri-alma (normal görev)"
    };
    let aktif: Vec<String> = AGIRLIK.iter().zip(&bayrak).filter(|(_, a)| **a).map(|((k, w, ac), _)| format!("{k} ({w:+}) {ac}")).collect();
    let damga = "deneysel m.29 · ağırlıklar kanıtsız-tercih · ≥50 olayda yeniden kalibre · her koşum kuyruk/halusinasyon-kayit.md";
    if json {
        let v = json!({"H": h, "esik": esik, "override_v3a": override_, "karar": karar, "ima_edilen_maliyet": ima, "aktif": aktif, "damga": damga});
        py::print(&py::json_girintili(&v));
    } else {
        py::print(&format!("H = {h} · eşik = {esik}{} → {karar}", if override_ { " · OVERRIDE v3a" } else { "" }));
        py::print(&format!("ima edilen maliyet: {ima}"));
        for a in &aktif {
            py::print(&format!("  + {a}"));
        }
        py::print(&format!("damga: {damga}"));
    }
    kod
}
