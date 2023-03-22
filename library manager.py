f = open("books.txt", "a")
c = 1
while c == 1:
    book_id = input("Enter the book ID : ")
    book_name = input("Enter the name of the book : ")
    author = input("Enter the name of the author of the book : ")
    price = input("Enter the price : ")
    book_rec = f"{book_id}, {book_name}, {author}, {price}\n"
    f.write(book_rec)
    print("Book added to record successfully ! ")
    c = int(input("Do you want to add more records? (1:YES    2:NO) : "))

f.close()
