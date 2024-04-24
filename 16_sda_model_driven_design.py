# Model Driven Design (MDD)
# MODELS
class Book:
    def __init__(self, judul, penulis, isbn):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn


class PerpustakaanMember:
    def __init__(self, nama, member_id):
        self.nama = nama
        self.member_id = member_id


# MODEL REPOSITORY
class ModelRepository:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book_data: Book):
        self.books.append(book_data)

    def add_member(self, member: PerpustakaanMember):
        self.members.append(member)


# create some book
book1 = Book("buku 1", "jaka", "9780743273565")
book2 = Book("buku 2", "prima", "9780061120084")

# create library members
member1 = PerpustakaanMember("maulana", 1001)
member2 = PerpustakaanMember("jono", 1002)

# simpan book dan member dalam repository
repository = ModelRepository()
repository.add_book(book1)
repository.add_book(book2)

repository.add_member(member1)
repository.add_member(member2)

# access data dari repository
for book in repository.books:
    print(f"judul buku: {book.judul} penulis: {book.penulis} isbn: {book.isbn}")

for member in repository.members:
    print(f"nama: {member.nama} member id: {member.member_id}")
