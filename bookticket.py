# Create account function
def create_account():
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    print("Your account has been created successfully!\n")
    login(username, password)

# Login function
def login(stored_username, stored_password):
    while True:
        id = input("Enter your username: ")
        pas = input("Enter your password: ")
        if id == stored_username and pas == stored_password:
            print("You logged in successfully!\n")
            book_show()
            break
        else:
            print("Wrong username or password. Try again.\n")

# Price function
def price(show, seat):
    if show == 1:
        prc = 200 * seat
    elif show == 2:
        prc = 500 * seat
    elif show == 3:
        prc = 100 * seat
    else:
        print("Invalid show choice!")
        return
    print("The total price of the ticket is:", prc)

# Booking function
def book_show():
    print("Available Shows:\n1. Saiyara\n2. Narshima\n3. Dilbar")
    show = int(input("Choose the show (1-3): "))
    seat = int(input("How many seats do you want to book: "))
    price(show, seat)

# Start the program
def main():
    print("HELLO, WELCOME TO BOOKmySHOW")
    choice = input("Do you have an account? (Y/N): ").strip().upper()
    if choice == "Y":
        # If user has an account, ask for login credentials to match
        stored_username = input("Enter your previously created username: ")
        stored_password = input("Enter your previously created password: ")
        print("\nNow login using the same credentials to proceed.")
        login(stored_username, stored_password)
    elif choice == "N":
        create_account()
    else:
        print("Invalid choice. Please enter Y or N.")

main()
