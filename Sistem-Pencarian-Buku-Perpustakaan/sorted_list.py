from models import Book


class SortedBookList:

    def __init__(self):
        self.books = []

    def load(self, books):
        """
        Memuat seluruh buku lalu mengurutkannya berdasarkan kode buku.
        """
        self.books = sorted(books, key=lambda x: x.kode)

    def get_books(self):
        return self.books

    def add_book(self, book: Book):
        """
        Menambahkan buku kemudian menjaga list tetap terurut.
        """
        self.books.append(book)
        self.books.sort(key=lambda x: x.kode)

    def delete_book(self, kode):
        """
        Menghapus buku berdasarkan kode.
        """
        for i, book in enumerate(self.books):
            if book.kode == kode:
                del self.books[i]
                return True

        return False

    def update_book(self, kode, new_book: Book):

        for i, book in enumerate(self.books):

            if book.kode == kode:
                self.books[i] = new_book
                self.books.sort(key=lambda x: x.kode)
                return True

        return False

    def display(self):

        print("=" * 120)

        print(
            f"{'Kode':10}"
            f"{'Judul':45}"
            f"{'Penulis':25}"
            f"{'Tahun':8}"
            f"{'Status':15}"
        )

        print("=" * 120)

        for book in self.books:

            print(
                f"{book.kode:10}"
                f"{book.judul[:42]:45}"
                f"{book.penulis[:22]:25}"
                f"{book.tahun:<8}"
                f"{book.status:15}"
            )