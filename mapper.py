#!/usr/bin/env python

import sys

# Inisialisasi indeks untuk melacak urutan
index = 0

# Membaca seluruh baris dari input
for line in sys.stdin:
    # Hilangkan spasi di awal dan akhir baris
    line = line.strip()
    # Pisahkan baris menjadi kata-kata
    words = line.split()

    # Loop untuk setiap kata dan tambahkan indeks
    for word in words:
        # Cetak indeks dan kata
        print(f"{index}\t{word}")
        index += 1
