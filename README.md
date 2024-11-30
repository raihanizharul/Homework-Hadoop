# Hadoop MapReduce Word Count Project

## Deskripsi Proyek

Proyek ini menggunakan Hadoop Streaming untuk menjalankan operasi MapReduce pada mode standalone cluster menggunakan Hadoop versi 3.2.3. Fokus proyek adalah menghitung frekuensi kemunculan kata dalam file teks pembukaan_uud1945.txt.


## Penjelasan File

1. Tugas_Hadoop_Hands_On_MapReduce.ipynb 
* Notebook ini berisi langkah-langkah praktis untuk menjalankan MapReduce menggunakan Hadoop Streaming. Disertai penjelasan mengenai konfigurasi Hadoop mode standalone dan eksekusi task MapReduce.

2. mapper.py
* Script Python untuk menjalankan fungsi Map. Fungsi ini membaca input dari Hadoop Streaming dan mengeluarkan pasangan key-value berupa kata dan angka 1 untuk setiap kemunculan kata.

3. reducer.py
* Script Python untuk menjalankan fungsi Reduce. Fungsi ini mengumpulkan semua pasangan key-value dari tahap Map dan menghitung total frekuensi kata.

4. pembukaan_uud1945.txt
* File teks yang berisi pembukaan Undang-Undang Dasar 1945, digunakan sebagai input untuk proses MapReduce.

5. hdfs-wordcount.txt
* File hasil output MapReduce yang berisi daftar kata dan jumlah kemunculannya.
