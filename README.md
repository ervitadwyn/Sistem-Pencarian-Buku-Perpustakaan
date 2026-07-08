# Sistem-Pencarian-Buku-Perpustakaan
## Perbandingan Sequential Search, Binary Search Tree (Unbalanced), dan Binary Search Tree (Balanced)

---

## Deskripsi Project

Project ini merupakan implementasi sistem pencarian data buku pada perpustakaan menggunakan tiga algoritma pencarian, yaitu:

- Sequential Search
- Binary Search Tree (BST Unbalanced)
- Binary Search Tree (BST Balanced)

Selain melakukan pencarian data, program juga menyediakan fitur benchmark untuk membandingkan performa masing-masing algoritma berdasarkan waktu eksekusi, jumlah perbandingan (comparisons), dan tinggi pohon (tree height).

Project ini dibuat sebagai tugas mata kuliah **Analisis Algoritma**.

---

# Struktur Project

```
Tugas Project Kelompok Sm2/
│
├── app.py                      # Program utama
├── models.py                   # Class Book
├── sequential_search.py        # Algoritma Sequential Search
├── bst.py                      # Binary Search Tree (Unbalanced)
├── balanced_bst.py             # Binary Search Tree (Balanced)
├── sorted_list.py              # Implementasi Sorted List
├── benchmark.py                # Benchmark algoritma
├── visualization.py            # Visualisasi grafik benchmark
├── utils.py                    # Fungsi pendukung
│
├── Buku Induk Perpustakaan.csv # Dataset buku
├── hasil_pengujian.csv         # Output hasil benchmark
├── grafik_perbandingan.png     # Grafik hasil benchmark
│
├── README.md
│
└── __pycache__/
```

---

# Dataset

Dataset yang digunakan adalah:

```
Buku Induk Perpustakaan.csv
```

Dataset berisi data buku yang telah diurutkan berdasarkan **Kode Buku**.

Atribut dataset terdiri dari:

- Kode Buku
- Judul Buku
- Penulis
- Tahun Terbit
- Penerbit

Jumlah data yang digunakan sebanyak **1.141 buku**.

---

# Fitur Program

Program menyediakan beberapa menu sebagai berikut.

```
==============================
 SISTEM PERPUSTAKAAN
==============================
1. Tampilkan Buku
2. Sequential Search
3. BST Search
4. Tambah Buku
5. Hapus Buku
6. Benchmark
7. Tampilkan Grafik
8. Keluar
```

Fungsi setiap menu:

- **Tampilkan Buku** → Menampilkan seluruh data buku.
- **Sequential Search** → Mencari buku menggunakan algoritma Sequential Search.
- **BST Search** → Mencari buku menggunakan Binary Search Tree.
- **Tambah Buku** → Menambahkan data buku baru ke dalam dataset.
- **Hapus Buku** → Menghapus data buku berdasarkan kode.
- **Benchmark** → Membandingkan performa ketiga algoritma.
- **Tampilkan Grafik** → Menampilkan grafik hasil benchmark.
- **Keluar** → Mengakhiri program.

---

# Algoritma yang Digunakan

## 1. Sequential Search

Sequential Search melakukan pencarian secara berurutan mulai dari elemen pertama hingga data ditemukan.

Kompleksitas waktu:

| Kasus | Kompleksitas |
|-------|--------------|
| Best Case | O(1) |
| Average Case | O(n) |
| Worst Case | O(n) |

---

## 2. Binary Search Tree (BST Unbalanced)

BST dibangun menggunakan proses insert sesuai urutan data.

Karena dataset telah terurut, pohon yang terbentuk menjadi tidak seimbang (degenerate tree), sehingga performa pencarian menurun.

Kompleksitas waktu:

| Kasus | Kompleksitas |
|-------|--------------|
| Best Case | O(1) |
| Average Case | O(n) |
| Worst Case | O(n) |

---

## 3. Binary Search Tree (BST Balanced)

BST Balanced dibangun menggunakan metode pembagian data berdasarkan elemen tengah (middle element) sehingga tinggi pohon tetap seimbang.

Kompleksitas waktu:

| Kasus | Kompleksitas |
|-------|--------------|
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |

---

# Benchmark

Benchmark dilakukan untuk membandingkan performa tiga algoritma pencarian pada beberapa ukuran dataset.

Ukuran data yang diuji:

- 100 data
- 500 data
- 1000 data
- 1141 data

Parameter yang diukur:

- Waktu eksekusi (Execution Time)
- Jumlah perbandingan (Comparisons)
- Tinggi pohon BST (Tree Height)

Output benchmark disimpan pada file:

```
hasil_pengujian.csv
```

---

# Visualisasi

Program menyediakan visualisasi menggunakan **Matplotlib**.

Grafik membandingkan:

- Sequential Search
- BST Unbalanced
- BST Balanced

Parameter yang ditampilkan:

- Jumlah Data
- Rata-rata Waktu Eksekusi (ms)

Grafik akan disimpan sebagai:

```
grafik_perbandingan.png
```

---

# Hasil Pengujian

Berdasarkan hasil benchmark diperoleh bahwa:

- Sequential Search memiliki waktu pencarian yang meningkat secara linear seiring bertambahnya jumlah data.
- BST Unbalanced memiliki performa yang kurang baik karena dataset terurut menyebabkan pohon menjadi tidak seimbang.
- BST Balanced memiliki performa terbaik karena tinggi pohon lebih kecil sehingga jumlah node yang dilalui saat pencarian menjadi lebih sedikit.

---

# Kesimpulan

Berdasarkan hasil implementasi dan pengujian dapat disimpulkan bahwa:

1. Sequential Search memiliki kompleksitas **O(n)** sehingga waktu pencarian meningkat seiring bertambahnya jumlah data.

2. Binary Search Tree Unbalanced tidak memberikan peningkatan performa ketika dataset telah terurut karena struktur pohon berubah menjadi menyerupai linked list, sehingga kompleksitas pencarian menjadi **O(n)**.

3. Binary Search Tree Balanced menghasilkan performa pencarian terbaik dengan kompleksitas **O(log n)** karena tinggi pohon tetap seimbang.

Dengan demikian, struktur pohon pada Binary Search Tree sangat memengaruhi efisiensi proses pencarian.

---

# Library yang Digunakan

Program menggunakan library berikut:

- pandas
- matplotlib
- time
- collections

---

# Cara Menjalankan Program

1. Install library yang diperlukan.

```bash
pip install pandas matplotlib
```

2. Jalankan program.

```bash
python app.py
```

---

# Author

**Nama Project**

**Sistem Pencarian Buku Perpustakaan Menggunakan Sequential Search, Binary Search Tree (Unbalanced), dan Binary Search Tree (Balanced)**

Mata Kuliah: **Analisis Algoritma**
