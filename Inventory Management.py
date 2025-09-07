# Simple Inventory Management Program
# Author: Your Name
# Date: 2025-09-07
# Description: Add items with quantities and view the inventory list.

inventory = {}  # Using dictionary instead of list because automatically updates quantities of the item


def add_item():  # Function to add item
    # Input = allow user will type item name, .strip = remove extra spaces
    name = input("\nEnter item name: ").strip()
    try:  # Python will attempt this code
        # Allow user to type in qty of items but only in number
        qty = int(input("Enter item quantity: "))
    except ValueError:  # If user dont type number, it will print error
        print("Quantity must be a number.")
        return
    if name in inventory:
        # This will check if items already exist, if yes will add new qty
        inventory[name] += qty
    else:
        inventory[name] = qty  # If items not exist, it will create new entry
    # Uses f-string to print qty and name nicely
    print(f"Added {qty} x {name}")


def view_inventory():  # Function to view inventory
    if not inventory:  # If no items, will tell user Inventory is empty
        print("\nInventory is empty.")
    else:
        # Run this code if inventory is not empty
        print("\n--- Inventory List ---")
        for item, qty in inventory.items():  # Loop the list, automatically repeat for all items until all items is printed
            # Uses f-string to print item and qty nicely
            print(f"{item}: {qty}")


def main():  # Function in the main menu
    while True:  # Start an infinite loop - Menu will keep showing until break
        print("\n--- Inventory Menu ---")
        print("1. Add item")
        print("2. View inventory")
        print("3. Exit")
        # Allow user to type in input
        choice = input("Choose an option (1-3): ")

        if choice == "1":  # If user type 1, add_item function will run
            add_item()
        elif choice == "2":  # If user type 2, view_inventory function will run
            view_inventory()
        elif choice == "3":  # If user type 3, will print goodbye and break the loop
            print("Goodbye!")
            break
        else:  # If user type in other than 1,2 or 3, will print error
            print("Invalid choice, try again.")


if __name__ == "__main__":  # Only run if this file executed
    main()
