import pandas as pd
import matplotlib.pyplot as plt


class Visualization:

    @staticmethod
    def show_graph(csv_file="hasil_pengujian.csv"):

        try:
            df = pd.read_csv(csv_file)

        except FileNotFoundError:
            print("File hasil benchmark tidak ditemukan!")
            print("Silakan jalankan benchmark terlebih dahulu.")
            return

        plt.figure(figsize=(8, 5))

        plt.plot(
            df["Jumlah Data"],
            df["Sequential Avg (ms)"],
            marker="o",
            linewidth=2,
            color="royalblue",
            label="Sequential Search"
        )
        for x, y in zip(df["Jumlah Data"], df["Sequential Avg (ms)"]):
            plt.text(x, y, f"{y:.4f}", fontsize=8)

        plt.plot(
            df["Jumlah Data"],
            df["BST Avg (ms)"],
            marker="s",
            linewidth=2,
            color="red",
            label="BST (Unbalanced)"
        )
        for x, y in zip(df["Jumlah Data"], df["BST Avg (ms)"]):
            plt.text(x, y, f"{y:.4f}", fontsize=8)

        plt.plot(
            df["Jumlah Data"],
            df["BST Balanced Avg (ms)"],
            marker="^",
            linewidth=2,
            color="green",
            label="BST (Balanced)"
        )
        for x, y in zip(df["Jumlah Data"], df["BST Balanced Avg (ms)"]):
            plt.text(x, y, f"{y:.4f}", fontsize=8)
            
        plt.title("Perbandingan Waktu Eksekusi\nSequential Search, BST Unbalanced, dan BST Balanced")

        plt.xlabel("Jumlah Data")

        plt.ylabel("Waktu (ms)")

        plt.grid(
            linestyle="--",
            alpha=0.5
        )

        plt.legend()

        plt.tight_layout()

        plt.savefig("grafik_perbandingan.png", dpi=300)

        plt.show()

        print("\nGrafik berhasil disimpan sebagai:")
        print("grafik_perbandingan.png")