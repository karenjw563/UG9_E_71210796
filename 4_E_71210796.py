#Program perhitungan deret geometri
u = int(input("Suku dari berapa : "))
Un = int(input("Suku ke-n : "))
a = float(input("Suku pertama : "))
r = float(input("Rasio : "))

hasil = 0
for n in range(u, Un+1):
    suku = a*(r**(n-1))
    hasil = hasil + suku
    print(suku)
