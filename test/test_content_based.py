from core import ContentBased as cb
from core import LoadData as ld
import time
import sys


def test_content_based_similarity(isbn_list):
    books = ld.load_processed_data()
    book_names = ld.load_books(columns=['ISBN','Book-Title'])

    print("You have seached for:")
    for isbn in isbn_list:
        print('ISBN', isbn, book_names.loc[isbn].loc['Book-Title'])

    content_based = cb.ContentBased(books=books, query_list_isbn=isbn_list, k=10, sample_size=2000)
    sim_list = content_based.get_similar_books()

    print()
    print("You may also like:")
    for x in sim_list:
        print('ISBN', x[0], book_names.loc[x[0]]['Book-Title'], '-- Similarity =', round(x[1],ndigits=3))


def main():
    filename = sys.argv[1]
    file = open(filename)
    isbn_list = []
    for isbn in file.readlines():
        isbn_list.append(isbn.strip())
    now = time.time()
    test_content_based_similarity(isbn_list)
    print()
    print("Query processed in ", round(time.time() - now, ndigits=2), " seconds")


if __name__ == '__main__':
    main()
