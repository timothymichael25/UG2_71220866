def volumeKubus(sisi):
    volume = sisi ** 3
    return volume

def volumeTabung(diameter, tinggi):
    volume = 22/7 * diameter * tinggi
    return volume

def volumeBalok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume


print("================ KALKULATOR CERDAS ================")
print("Pilihlah bangun yang akan dihitung: ")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")

pilihan = int(input(">>"))

if pilihan == 1:
    diameter = float(input("Masukkan diameter: "))
    tinggi = float(int(input("Masukkan tinggi: ")))
    print("Volume tabung adalah ", volumeTabung(diameter, tinggi),"cm")
elif pilihan == 2:
    sisi = float(input("Masukkan panjang sisi kubus : "))
    print("volume kubus adalah ",volumeKubus(sisi),"cm")
elif pilihan == 3:
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan Lebar balok: "))
    tinggi = float(input("Masukkan Tinggi balok : "))
    print("Volume balok adalah", volumeBalok(panjang, lebar, tinggi),"cm")
else:
    print("Input yang anda masukkan salah !!")