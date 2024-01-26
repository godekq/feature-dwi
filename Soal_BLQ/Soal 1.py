Hrg_kacamata = [500, 600, 700, 800]
Hrg_baju = [200, 400, 350]
Hrg_sepatu = [400, 350, 200, 300]
Hrg_buku = [100, 50, 150]

jumlah_uang = int(input("Jumlah Uang: "))

count = 0

for a in range(len(Hrg_kacamata)):
    for b in range(len(Hrg_baju)):
        for c in range(len(Hrg_sepatu)):
            for d in range(len(Hrg_buku)):
                sisa = jumlah_uang
                item = 0

                sisa -= Hrg_kacamata[a]
                if sisa >= 0:
                    item += 1

                    sisa -= Hrg_baju[b]
                    if sisa >= 0:
                        item += 1

                        sisa -= Hrg_sepatu[c]
                        if sisa >= 0:
                            item += 1

                            sisa -= Hrg_buku[d]
                            if sisa >= 0:
                                item += 1

                if item > count:
                    count = item

print("Jumlah Item Yang Bisa Dibeli : " + str(count)+" Item")
