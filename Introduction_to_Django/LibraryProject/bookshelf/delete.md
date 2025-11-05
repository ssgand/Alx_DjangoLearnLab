book = Book.objects.filter(title='Nineteen Eighty-Four')
book.delete() # output: (1, {'bookshelf.Book': 1})
