book = Book.objects.filter(title='1984').first()

print(book.title) # output: 1984
print(book.author) # output: George Orwell
print(book.published_date) # output: 1949
