import time
import pandas as pd

from sequential_search import SequentialSearch
from bst import BinarySearchTree
from balanced_bst import BalancedBST


class Benchmark:

    def __init__(self, books):
        self.books = books
        self.test_sizes = [100, 500, 1000, len(books)]

    def run(self):

        hasil = []

        print("\n" + "=" * 70)
        print("BENCHMARK SEQUENTIAL SEARCH vs BST")
        print("=" * 70)

        for size in self.test_sizes:

            sample_books = self.books[:size]

            target = sample_books[len(sample_books) // 2].kode

            # ===============================
            # Sequential Search
            # ===============================

            seq_total = 0

            for _ in range(100):

                hasil_seq = SequentialSearch.search_by_code(
                    sample_books,
                    target
                )

                seq_total += hasil_seq["time"] * 1000

            seq_avg = seq_total / 100
            seq_compare = hasil_seq["comparisons"]

            # ===============================
            # BST Biasa
            # ===============================

            bst = BinarySearchTree()
            bst.build_tree(sample_books)

            bst_total = 0

            for _ in range(100):

                hasil_bst = bst.search(target)

                bst_total += hasil_bst["time"] * 1000

            bst_avg = bst_total / 100
            bst_compare = hasil_bst["comparisons"]

            # ===============================
            # Balanced BST
            # ===============================

            balanced = BalancedBST()
            balanced.build_tree(sample_books)

            bal_total = 0

            for _ in range(100):
                hasil_bal = balanced.search(target)
                bal_total += hasil_bal["time"] * 1000

            bal_avg = bal_total / 100
            bal_compare = hasil_bal["comparisons"]

            # ===============================
            # Simpan hasil
            # ===============================

            hasil.append({

                "Jumlah Data": size,

                "Sequential Avg (ms)": round(seq_avg, 6),
                "Sequential Compare": seq_compare,

                "BST Avg (ms)": round(bst_avg, 6),
                "BST Compare": bst_compare,

                "BST Balanced Avg (ms)": round(bal_avg, 6),
                "BST Balanced Compare": bal_compare,

                "BST Height": bst.height(),
                "Balanced Height": balanced.height()

            })

        df = pd.DataFrame(hasil)

        pd.set_option("display.max_columns", None)

        print(df)

        df.to_csv(
            "hasil_pengujian.csv",
            index=False
        )

        print("\nHasil benchmark disimpan ke hasil_pengujian.csv")