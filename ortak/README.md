# ortak/ — ortak çalışma alanı

`durum-olay.jsonl`: ekle-yalnız olay kütüğü, doğruluk kaynağı; satır = bir JSON olay (`ac`, `al`, `bitir`, `tuket`, `bayatla`).
Güncel durum olayların katlanmasıyla hesaplanır; kütük elle düzenlenmez, silinmez.
Kayıt: `id`, `alan`, `durum` (acik, islemde, tamam, tuketildi, bayat), `is`, `sonraki_eylem`, `kanit`, `girdi`, `son_gecerlilik`, `ts`, `oturum`.
Ajan mesaj yazmaz, görev atamaz: oturum başında kendi alanının açık durumunu okur, tükettiğini `tuket` ile işaretler.
Kod: `jarvis/kod/durum/` (`cargo run -q -p durum -- ...`).
Örnek: `durum ac --alan sage --is "S4 dersi" --sonraki "Meditations 4. kitap PROBE"` · `durum al 1` · `durum bitir 1 --kalan "S5|PROBE"` · `durum oturum-basi --alan sage`
