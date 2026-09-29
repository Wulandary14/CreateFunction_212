def konversi_temperatur(value, unit) :
    if unit == "C":
        return (value * 9/5) + 32
    elif unit == "F":
        return (value - 32) * 5/9

value = float (input("Masukan suhu:"))
unit = input("Masukkan satuan (C/F):")

hasil = konversi_temperatur(value, unit)

print("Hasil:", hasil)