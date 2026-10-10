class Author:
    def __init__(self, name):
        self.name = name

class LibraryItem:

    def __init__(self, title, subject="umumiy"):
        self.title = title
        self.subject = subject

    def get_info(self):
        return f"{self.title} | Mavzu: {self.subject}"

class Book(LibraryItem):
    def __init__(self, title, author: Author, subject="umumiy"):
        super().__init__(title, subject)
        self.author = author

    def get_info(self):
        return f"Kitob: '{self.title}' — {self.author} | mavzu: {self.subject}"

class Magazine(LibraryItem):
    def __init__(self, title, issue, subject="Jurnal"):
        super().__init__(title, subject)
        self.issue = issue

    def get_info(self):
        return f"{self.subject}: {self.title} - {self.issue}-son"

class DVD(LibraryItem):
    def __init__(self, title, director, genre):
        super().__init__(title, subject=genre)
        self.director = director

    def get_info(self):
        return f"DVD: {self.title} - rej. {self.director} | janr: {self.subject}"


class Catalog:
    def __init__(self):
        self.__items = []

    def add(self, item: LibraryItem):
        self.__items.append(item)
        print(f"Katalogga qo'shildi: {item.get_info()}")

    def search(self, query):
        q = query.lower()
        results = []
        for item in self.__items:
          found = q in item.title.lower()
          if hasattr(item, 'author') and isinstance(item.author, Author):
            if q in item.author.name.lower():
              found = True
          if found:
            results.append(item)
        return results

    def hammasi(self):
        for item in self.__items:
            print(item.get_info())

    def jami(self):
        return len(self.__items)


def main():
  catalog = Catalog()

  catalog.add(Book("O'tkan kunlar", Author('Abdulla Qodiriy'), 'roman'))
  catalog.add(Magazine('Fan va turmush', 5))
  catalog.add(DVD('Shum bola', 'D. Salimov', 'komediya'))

  while True:
    print("""===== USTUDY KUTUBXONA (OOP) =====
1. Kitob qo'shish
2. Jurnal qo'shish
3. DVD qo'shish
4. Qidirish
5. Hammasini ko'rsatish
0. Chiqish
""")

    choice = input('Tanlang: ').strip()

    if choice == '1':
      title = input('Kitob nomi: ').strip()
      author_name = input('Muallif: ').strip()
      subject = input('Mavzu (Enter = umumiy): ').strip()
      author = Author(author_name)
      if subject:
        book = Book(title, author, subject)
      else:
        book = Book(title, author)
      catalog.add(book)

    elif choice == '2':
      title = input('Jurnal nomi: ').strip()
      try:
        issue = int(input('Nechanchi son? ').strip())
        mag = Magazine(title, issue)
        catalog.add(mag)
      except ValueError:
        print('Xato: Son kiriting!')

    elif choice == '3':
      title = input('DVD nomi: ').strip()
      director = input('Rejissyor: ').strip()
      genre = input('Janr: ').strip()
      dvd = DVD(title, director, genre)
      catalog.add(dvd)

    elif choice == '4':
      query = input("Qidiruv so'zi: ").strip()
      results = catalog.search(query)
      if results:
        for item in results:
          print(item.get_info())
        print(f'Topildi: {len(results)} ta')
      else:
        print('Hech narsa topilmadi.')

    elif choice == '5':
      catalog.hammasi()
      print(f'Jami: {catalog.jami()} ta element')

    elif choice == '0':
      print("Xayr! Kitob o'qishni unutmang")
      break

    else:
      print("Bunday bo'lim yo'q!")

main()