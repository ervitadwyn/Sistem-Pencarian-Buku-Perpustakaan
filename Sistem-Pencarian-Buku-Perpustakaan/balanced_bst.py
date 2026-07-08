import time
from bst import BSTNode


class BalancedBST:
    def __init__(self):
        self.root = None
        self.comparisons = 0

    def build_tree(self, books):
        """
        Membangun Balanced BST dari list buku.
        """
        sorted_books = sorted(books, key=lambda book: book.kode)
        self.root = self._build(sorted_books, 0, len(sorted_books) - 1)

    def _build(self, books, left, right):
        if left > right:
            return None

        mid = (left + right) // 2

        node = BSTNode(books[mid])

        node.left = self._build(books, left, mid - 1)
        node.right = self._build(books, mid + 1, right)

        return node

    def search(self, kode_buku):
        self.comparisons = 0
        start = time.perf_counter()
        book = self._search(self.root, kode_buku)
        end = time.perf_counter()

        return {
            "found": book is not None,
            "book": book,
            "comparisons": self.comparisons,
            "time": (end - start)
        }

    def _search(self, node, kode):
        if node is None:
            return None

        self.comparisons += 1

        if kode == node.book.kode:
            return node.book

        elif kode < node.book.kode:
            return self._search(node.left, kode)

        else:
            return self._search(node.right, kode)

    def get_height(self):
        return self._height(self.root)

    def height(self):
        return self.get_height()

    def _height(self, node):
        if node is None:
            return 0

        return 1 + max(
            self._height(node.left),
            self._height(node.right)
        )