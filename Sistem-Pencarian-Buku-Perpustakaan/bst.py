import time
from collections import deque


class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # =====================================
    # INSERT (ITERATIF)
    # =====================================

    def insert(self, book):

        new_node = BSTNode(book)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:

            if book.kode < current.book.kode:

                if current.left is None:
                    current.left = new_node
                    return

                current = current.left

            elif book.kode > current.book.kode:

                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

            else:
                return
    def _build_balanced(self, books, left, right):

        if left > right:
            return None

        mid = (left + right) // 2

        node = BSTNode(books[mid])

        node.left = self._build_balanced(
            books,
            left,
            mid - 1
    )

        node.right = self._build_balanced(
            books,
            mid + 1,
            right
    )

        return node
    # =====================================
    # BUILD TREE
    # =====================================

    def build_tree(self, books):

        self.root = None

        for book in books:
            self.insert(book)

    # =====================================
    # SEARCH (ITERATIF)
    # =====================================

    def search(self, kode):

        start = time.perf_counter()

        comparisons = 0

        current = self.root

        while current:

            comparisons += 1

            if kode == current.book.kode:

                end = time.perf_counter()

                return {
                    "found": True,
                    "book": current.book,
                    "comparisons": comparisons,
                    "time": end - start
                }

            elif kode < current.book.kode:
                current = current.left

            else:
                current = current.right

        end = time.perf_counter()

        return {
            "found": False,
            "book": None,
            "comparisons": comparisons,
            "time": end - start
        }

    # =====================================
    # INORDER (ITERATIF)
    # =====================================

    def inorder(self):

        stack = []

        current = self.root

        books = []

        while stack or current:

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            books.append(current.book)

            current = current.right

        return books

    # =====================================
    # COUNT NODE (ITERATIF)
    # =====================================

    def count_nodes(self):

        if self.root is None:
            return 0

        queue = deque([self.root])

        count = 0

        while queue:

            node = queue.popleft()

            count += 1

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return count

    # =====================================
    # HEIGHT (ITERATIF)
    # =====================================

    def height(self):

        if self.root is None:
            return 0

        queue = deque([self.root])

        height = 0

        while queue:

            level_size = len(queue)

            for _ in range(level_size):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            height += 1

        return height

        