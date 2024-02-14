inventory = {}

def add_book():
    book_name = input("Enter the name of the book: ")
    quantity = int(input("Enter the quantity of the book: "))
    
    inventory[book_name] = quantity
    print(f"{quantity} copies of '{book_name}' added to the inventory.")

def display_inventory():
    print("\nCurrent Inventory:")
    for book, quantity in inventory.items():
        print(f"{book}: {quantity} copies")

def update_book_quantity():
    book_name = input("Enter the name of the book to update quantity: ")
    if book_name in inventory:
        new_quantity = int(input("Enter the updated quantity: "))
        inventory[book_name] = new_quantity
        print(f"Quantity of '{book_name}' updated to {new_quantity}.")
    else:
        print(f"Book '{book_name}' not found in inventory.")

while True:
    print("\n Main Options:")
    print("1. Add a book to inventory")
    print("2. Display current inventory")
    print("3. Update book quantity")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_inventory()
    elif choice == '3':
        update_book_quantity()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
