import pandas as pd
from models import Book

def to_int(value):
    """
    Mengubah nilai menjadi integer dengan aman.
    Jika kosong, NaN, "\" atau bukan angka maka dikembalikan 0.
    """
    if pd.isna(value):
        return 0

    value = str(value).strip()

    if value in ("", "\\", "-", "None"):
        return 0

    try:
        return int(float(value))
    except ValueError:
        return 0


def to_str(value):
    """
    Mengubah NaN menjadi string kosong.
    """
    if pd.isna(value):
        return ""
    return str(value).strip()
class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_books(self):

        df = pd.read_excel(self.file_path)

        books = []

        for _, row in df.iterrows():

            buku = Book(

                kode=to_str(row["Kode Buku"]),
                judul=to_str(row["Judul"]),
                salin=to_int(row["Salin"]),
                penulis=to_str(row["Penulis"]),
                edisi=to_str(row["Edisi"]),
                tahun=to_int(row["Tahun"]),
                penerbit=to_str(row["Penerbit"]),
                tempat_terbit=to_str(row["Tempat Terbit"]),
                kategori=to_str(row["Kategori"]),
                status=to_str(row["Status"])

            )

            books.append(buku)

        return books