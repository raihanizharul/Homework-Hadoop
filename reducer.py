#!/usr/bin/env python

import sys
from collections import defaultdict

# Dictionary untuk melacak jumlah kata
word_count = defaultdict(int)
# List untuk melacak urutan input
order = []

# Membaca seluruh baris dari input
for line in sys.stdin:
    # Hilangkan spasi di awal dan akhir baris
    line = line.strip()
    # Pisahkan data menjadi indeks dan kata
    try:
        index, word = line.split('\t', 1)
        index = int(index)

        # Tambahkan kata ke urutan jika belum ada
        if word not in word_count:
            order.append((index, word))

        # Tambahkan jumlah kemunculan kata
        word_count[word] += 1
    except ValueError:
        # Abaikan baris yang tidak valid
        continue

# Urutkan berdasarkan indeks untuk menjaga urutan asli
order.sort(key=lambda x: x[0])

# Loop melalui data yang sudah diurutkan dan cetak hasilnya
for _, word in order:
    print(f"{word}\t{word_count[word]}")
