#Program yang akan membalik nama belakang menjadi nama depan dan akan menampilkan tanggal lahir juga tempat lahir
nama = input("Nama: ")
lahir = input("Tempat tanggal lahir : ")

a = nama.split()
b = lahir.split()

print("Haloo!", a[1], ",", a[0])
print("Anda lahir di", b[0], "pada tanggal", b[1], b[2], b[3])

nama = input("Nama: ")
lahir = input("Tempat tanggal lahir : ")

a = nama.split()
b = lahir.split()

print("Haloo!", a[2], ",", a[0], a[1])
print("Anda lahir di", b[0], "pada tanggal", b[1], b[2], b[3])

