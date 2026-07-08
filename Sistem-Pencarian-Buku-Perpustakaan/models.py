from dataclasses import dataclass

@dataclass
class Book:
    kode: str
    judul: str
    salin: int
    penulis: str
    edisi: str
    tahun: int
    penerbit: str
    tempat_terbit: str
    kategori: str
    status: str

    def __str__(self):
        return (
            f"[{self.kode}] "
            f"{self.judul} | "
            f"{self.penulis} | "
            f"{self.tahun} | "
            f"{self.status}"
        )