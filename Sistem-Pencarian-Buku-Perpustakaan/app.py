from utils import DataLoader
from sorted_list import SortedBookList
from sequential_search import SequentialSearch
from bst import BinarySearchTree


loader = DataLoader("Buku Induk Perpustakaan.csv")
books = loader.load_books()

library = SortedBookList()
library.load(books)

tree = BinarySearchTree()
tree.build_tree(books)


while True:

    print("\n==============================")
    print(" SISTEM PERPUSTAKAAN ")
    print("==============================")
    print("1. Tampilkan Buku")
    print("2. Sequential Search")
    print("3. BST Search")
    print("4. Tambah Buku")
    print("5. Hapus Buku")
    print("6. Benchmark")
    print("7. Tampilkan Grafik")
    print("8. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":

        library.display()

    elif pilihan == "2":

        kode = input("Masukkan kode buku : ")

        hasil = SequentialSearch.search_by_code(
            library.get_books(),
            kode
        )

        if hasil["found"]:

            print("\nData ditemukan\n")
            print(hasil["book"])

            print("\nJumlah Perbandingan :", hasil["comparisons"])

            print(f"Waktu : {hasil['time']*1000:.6f} ms")

        else:

            print("Data tidak ditemukan.")

    elif pilihan == "3":

        kode = input("Masukkan kode buku : ")

        hasil = tree.search(kode)

        if hasil["found"]:

            print("\nData ditemukan\n")

            print(hasil["book"])

            print("\nJumlah Node Dikunjungi :", hasil["comparisons"])

            print(f"Waktu : {hasil['time']*1000:.6f} ms")

        else:

            print("Data tidak ditemukan.")

    elif pilihan == "4":

        print("\nTambah Buku")

        from models import Book

        kode = input("Kode : ")
        judul = input("Judul : ")
        salin = int(input("Salin : "))
        penulis = input("Penulis : ")
        edisi = input("Edisi : ")
        tahun = int(input("Tahun : "))
        penerbit = input("Penerbit : ")
        tempat = input("Tempat Terbit : ")
        kategori = input("Kategori : ")
        status = input("Status : ")

        buku = Book(
            kode,
            judul,
            salin,
            penulis,
            edisi,
            tahun,
            penerbit,
            tempat,
            kategori,
            status
        )

        library.add_book(buku)

        tree.insert(buku)

        print("Buku berhasil ditambahkan.")

    elif pilihan == "5":

        kode = input("Kode Buku : ")

        if library.delete_book(kode):

            tree.build_tree(library.get_books())

            print("Data berhasil dihapus.")

        else:

            print("Data tidak ditemukan.")

    elif pilihan == "6":

        from benchmark import Benchmark

        Benchmark(
            library.get_books()
        ).run()

    elif pilihan == "7":

        from visualization import Visualization

        Visualization.show_graph()

    elif pilihan == "8":

        print("Program selesai.")

        break

    else:

        print("Pilihan tidak tersedia.")