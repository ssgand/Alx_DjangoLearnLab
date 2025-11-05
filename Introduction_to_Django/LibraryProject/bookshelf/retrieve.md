book = Book.objects.get(title='1984')

print(book.title) # output: 1984
print(book.author) # output: George Orwell
print(book.published_year) # output: 1949
