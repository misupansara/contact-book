import os

FILENAME = "contacts.txt"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    with open(FILENAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("✅ Contact added successfully!")

def view_contacts():
    if not os.path.exists(FILENAME):
        print("❌ No contacts found.")
        return

    print("\n📖 Your Contacts:")
    with open(FILENAME, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(',')
            print(f"👤 Name: {name}, 📞 Phone: {phone}, 📧 Email: {email}")

def search_contact():
    query = input("Enter name to search: ").lower()
    found = False

    with open(FILENAME, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(',')
            if query in name.lower():
                print(f"🔍 Found: 👤 Name: {name}, 📞 Phone: {phone}, 📧 Email: {email}")
                found = True

    if not found:
        print("❌ No contact found with that name.")

def main():
    while True:
        print("\n📇 Contact Book Menu")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid option. Try again.")

if __name__ == "__main__":
    main()
