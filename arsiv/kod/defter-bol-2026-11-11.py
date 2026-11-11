# Tek seferlik: karar defterini tüzük yöntemiyle (ana dosya + @ parçalar) böler. Karar 130 D26.
import io, shutil, sys
kok = "C:/sistem/sistem/jarvis/kuyruk/"
ana = kok + "senaryo-defteri.md"
yedek = sys.argv[1]
shutil.copyfile(ana, yedek)
ham = open(ana, "rb").read()
satirlar = ham.split(b"\n")  # son öğe: son satır sonundan sonrası
# (ilk satır no, son satır no, ad) 1-tabanlı, kapalı aralık
parcalar = [(214, 235, "k100"), (236, 249, "k104"), (250, 261, "k112"), (262, 269, "k118"), (270, len(satirlar), "k124")]
def dilim(a, b):
    return b"\n".join(satirlar[a - 1:b])
govde = dilim(1, 213) + b"\n"
toplam = govde
adlar = []
for i, (a, b, ad) in enumerate(parcalar):
    veri = dilim(a, b)
    if i < len(parcalar) - 1:
        veri += b"\n"
    toplam += veri
    dosya = "senaryo-defteri-%s.md" % ad
    open(kok + dosya, "wb").write(veri)
    adlar.append(dosya)
assert toplam == ham, "bayt eşitliği tutmadı"
ek = "\n*Parçalı defter (Karar 130 D26, 2026-11-11): kararlar aşağıdaki parçalarda sırayla durur; yeni karar en son parçanın (`%s`) sonuna eklenir; parça 20 KB'ı geçince yeni parça açılır ve buraya `@` satırı eklenir. Sırayla okuma: `baglam genislet`.*\n" % adlar[-1]
ek += "".join("@%s\n" % a for a in adlar)
open(ana, "wb").write(govde + ek.encode("utf-8"))
print("ana", len(govde), "ek", len(ek.encode("utf-8")), [(a, len(open(kok + a, "rb").read())) for a in adlar])
