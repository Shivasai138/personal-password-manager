import string
import secrets

passwords = {}

# load existing password file
def load_passwords():
    try:
        with open("passwords.txt", 'r') as file:
            for line in file:
                website, pwd = line.strip().split(':')
                passwords[website] = pwd

    except FileNotFoundError:
        pass

load_passwords()


def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(secrets.choice(chars) for _ in range(16))
    return password

def save_password():
    site = input("Enter website: ")
    if site in passwords:
        print("Website already exists.")
    else:
        pwd = input("Enter password: ")
        passwords[site] = pwd

        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Saved!")

def view_passwords():
    if not passwords:
        print("No data")
    else:
        for site, pwd in passwords.items():
            print(site, ":", pwd)

def search_site():
    website = input("Enter website name :")
    if website in passwords:
        print(f"{website} password :{passwords[website]}")
    else:
        print("Website not found")

def save_to_file():
    with open("passwords.txt", "w") as file:
        for site, pwd in passwords.items():
            file.write(f"{site}:{pwd}\n")

def update_password():
    website = input("Enter the website you want to update password: ")
    if website in passwords:
        pwd = input("Enter the new password: ")
        passwords[website] = pwd

        save_to_file()
        print("Password updated successfully!")

    else:
        print("Website not found")

def delete_password():
    website = input("Enter the website which you want to delete :")
    if website not in passwords:
        print("Website not found")
    else:
        del passwords[website]
        save_to_file()
        print("Website and its password deleted successfully")


while True:
    print("\n--------PERSONAL PASSWORD MANAGER--------")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Search Site")
    print("5. Update Password")
    print("6. Delete Password")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Save Password
    if choice == '1':
        save_password()

    # View Password
    elif choice == '2':
        view_passwords()

    # Generate Password
    elif choice == '3':
        print("Generate Password ", generate_password())

    # Search Site
    elif choice == '4':
        search_site()

    # Update Password
    elif choice == '5':
       update_password()

    # Delete Password
    elif choice == '6':
        delete_password()
    # Exit
    elif choice == '7':
        print("Ok bye ..")
        break

    else:
        print("Invalid input")
