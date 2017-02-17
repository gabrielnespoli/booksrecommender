# booksrecommender
System developed in Python for books recommendation using content based algorithm.

The system uses as content the following categories: title, author, year of publication and genre.
The first three features were present in the dataset BX-CSV-Dump, which can be downloaded here.
The genres was downloaded from GoodReads and GoogleBooks using their APIs. The code to prepare the data is also present here.

The books' title were processed using Natural Language Toolkit. The idea was to approximate books with similar names like Harry Potter 1 and Harry Potter 2.

The author column is unaltered.

I considered books from the same age (score similarity = 1) the ones that were published in a range of +- 5 years.

The genres were hashed. It was a design failure. When I downloaded the genres, the dataset grew imensely. I thought that it was due to the genre string, then I hashed. I took me some days to download, so I didn't want to re-download all of them. But it works anyway.
