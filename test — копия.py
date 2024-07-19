import json

def load_books(filename="books.json"):
    """Загружает список книг из файла."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books, filename="books.json"):
    """Сохраняет список книг в файл."""
    with open(filename, "w") as f:
        json.dump(books, f, indent=4)

def generate_id(books):
    """Генерирует уникальный ID для новой книги."""
    max_id = 0
    for book in books:
        if book["id"] > max_id:
            max_id = book["id"]
    return max_id + 1

def add_book(books):
    """Добавляет новую книгу в библиотеку."""
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год издания: "))
    new_book = {
        "id": generate_id(books),
        "title": title,
        "author": author,
        "year": year,
        "status": "в наличии"
    }
    books.append(new_book)
    save_books(books)
    print("Книга добавлена!")

def delete_book(books):
    """Удаляет книгу из библиотеки."""
    book_id = int(input("Введите ID книги для удаления: "))
    for i, book in enumerate(books):
        if book["id"] == book_id:
            del books[i]
            save_books(books)
            print("Книга удалена!")
            return
    print("Книга с таким ID не найдена.")

def search_book(books):
    """Ищет книги по названию, автору или году."""
    search_term = input("Введите поисковый запрос: ")
    found_books = []
    for book in books:
        if search_term.lower() in book["title"].lower() or \
           search_term.lower() in book["author"].lower() or \
           str(book["year"]) == search_term:
            found_books.append(book)

    if found_books:
        print("Найденные книги:")
        for book in found_books:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
    else:
        print("Книги не найдены.")

def display_books(books):
    """Отображает список всех книг."""
    if books:
        print("Список книг:")
        for book in books:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
    else:
        print("В библиотеке нет книг.")

def change_book_status(books):
    """Изменяет статус книги."""
    book_id = int(input("Введите ID книги для изменения статуса: "))
    for book in books:
        if book["id"] == book_id:
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            if new_status.lower() in ("в наличии", "выдана"):
                book["status"] = new_status
                save_books(books)
                print("Статус книги изменен!")
                return
            else:
                print("Неверный статус.")
                return
    print("Книга с таким ID не найдена.")

def main():
    """Главная функция программы."""
    books = load_books()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            delete_book(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            display_books(books)
        elif choice == "5":
            change_book_status(books)
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()