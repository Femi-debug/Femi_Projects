"""
Shoe inventory management task.

This task contains the Shoe class and functions to read, capture, 
view, restock, search, and save shoe inventory data.

"""
# ======== The beginning of the class ========

class Shoe:
    """Class to represent a shoe with various attributes."""

    def __init__(self, country, code, product, cost, quantity):
        """Initialize shoe attributes."""
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """String representation of the shoe."""
        return (
            f"Country: {self.country}, Code: {self.code}, Product: "
            f"{self.product}, Cost: {self.cost}, Quantity: {self.quantity}"
        )

# ============ Shoe list ===========
shoe_list = []

# ========== Functions outside the class ==========

def read_shoes_data():
    """Read shoe data from inventory file and populate shoe_list."""
    try:
        with open('inventory.txt', 'r') as file:
            next(file)  # Skip header line
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    country = parts[0]
                    code = parts[1]
                    product = parts[2]
                    try:
                        cost = float(parts[3])
                    except ValueError:
                        print(f"Oops! Invalid cost: {parts[3]}")
                        continue
                    try:
                        quantity = int(parts[4])
                    except ValueError:
                        print(f"Oops! Invalid quantity: {parts[4]}")
                        continue
                    shoe_one = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe_one)
    except FileNotFoundError:
        print("The file that you are trying to open does not exist")

def capture_shoes():
    """Capture shoe details from user and append to shoe_list."""
    print("\nEnter shoe details:")
    country = input("Country: ").lower()
    code = input("Code: ").lower()
    product = input("Product: ").lower()
    cost = float(input("Cost: "))
    quantity = int(input("Quantity: "))
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

def view_all(shoe_list):
    """Print all shoes in shoe_list."""
    for shoe in shoe_list:
        print(shoe)

def re_stock(shoe_list):
    """Restock shoe with the lowest quantity."""
    if not shoe_list:
        print("No shoes in inventory to restock.")
        return
    lowest_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(
        f"Please enter the quantity to add for restocking: {lowest_shoe}"
    )
    add_quantity = int(input("Enter the quantity to add: "))
    lowest_shoe.quantity += add_quantity
    save_inventory(shoe_list)  # Remember to save changes

def save_inventory(shoe_list):
    """Save current shoe_list inventory to file."""
    with open('inventory.txt', 'w') as file:
        for shoe in shoe_list:
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},"
                f"{shoe.cost},{shoe.quantity}\n"
            )

def search_shoe(shoe_list):
    """Search for a shoe in shoe_list by code."""
    shoe_code = input("Please enter the shoe code here: ").lower()
    for shoe in shoe_list:
        if shoe_code == shoe.code.lower():
            return shoe
    return None

def value_per_item(shoe_list):
    """Calculate and print total value for all shoes."""
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(
            f"Total Value for the item: {shoe.product} "
            f"({shoe.code}) is {value}"
        )

def highest_qty(shoe_list):
    """Print the shoe with the highest quantity."""
    if not shoe_list:
        print("No shoes in inventory.")
        return
    highest_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"Shoe item: {highest_shoe} is for sale")

# ========== Main Menu ==========

def menu():
    """Main menu loop to interact with the shoe inventory."""
    while True:
        print(
            "Welcome to the shoe inventory menu.\n"
            "Please choose between options 1 through 8 to proceed:"
        )
        print("Option 1: Create a new shoe or capture data for a shoe")
        print("Option 2: View all shoes available")
        print("Option 3: View shoes that need to be restocked")
        print("Option 4: Search for shoe")
        print("Option 5: View total cost of a shoe")
        print("Option 6: Show highest quantity shoe for sale")
        print("Option 7: Exit")
        read_shoes_data()

        choice = input("Please enter your option here: (1-7) ").strip()

        if choice == "1":
            capture_shoes()
            print("Data has been captured for shoe.")
        elif choice == "2":
            view_all(shoe_list)
            print("Shoes in inventory have been viewed.")
        elif choice == "3":
            re_stock(shoe_list)
            print("Shoe has been restocked.")
        elif choice == "4":
            shoe = search_shoe(shoe_list)
            if shoe:
                print("Shoe has been found:", shoe)
            else:
                print(
                    "Shoe has not been found, try again or return to menu."
                )
        elif choice == "5":
            value_per_item(shoe_list)
        elif choice == "6":
            highest_qty(shoe_list)
        elif choice == "7":
            print("You are exiting the program. Goodbye!")
            break
        else:
            print(
                "Invalid entry. Please exit or choose options 1 through 8."
            )

# Run the menu loop
menu()
