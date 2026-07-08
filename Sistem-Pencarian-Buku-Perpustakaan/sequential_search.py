import time


class SequentialSearch:

    @staticmethod
    def search_by_code(book_list, kode):

        comparisons = 0

        start = time.perf_counter()

        for index, book in enumerate(book_list):

            comparisons += 1

            if book.kode == kode:

                end = time.perf_counter()

                return {
                    "found": True,
                    "book": book,
                    "index": index,
                    "comparisons": comparisons,
                    "time": end - start
                }

        end = time.perf_counter()

        return {
            "found": False,
            "book": None,
            "index": -1,
            "comparisons": comparisons,
            "time": end - start
        }

    @staticmethod
    def search_by_title(book_list, keyword):

        keyword = keyword.lower()

        comparisons = 0

        result = []

        start = time.perf_counter()

        for book in book_list:

            comparisons += 1

            if keyword in book.judul.lower():
                result.append(book)

        end = time.perf_counter()

        return {
            "books": result,
            "comparisons": comparisons,
            "time": end - start
        }