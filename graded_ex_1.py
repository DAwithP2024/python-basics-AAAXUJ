# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == 'ascending':
        sorted_products = sorted(products_list, key=lambda x: x['price'])
    elif sort_order == 'descending':
        sorted_products = sorted(products_list, key=lambda x: x['price'], reverse=True)
    else:
        print("Invalid sort order.")
        return

    for product in sorted_products:
        print(f"Product Name: {product['name']}, Price: ${product['price']}")

def display_products(products_list):
    for index, product in enumerate(products_list, start=1):
        name, price = product
        print(f"{index}. {name}: {price}")

def display_categories():
    categories = ["IT Products", "Electronics", "Groceries"]
    print(categories)
    while True:
        print("Available categories:")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")
        
        try:
            choice = int(input("Enter the number corresponding to the category you want to explore: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")
    
def add_to_cart(cart, product, quantity):
    cart[product] = cart.get(product, 0) + quantity
def display_cart(cart):
    print("Your Cart:")
    for item in cart:
        print(f"Product: {item['product']}, Quantity: {item['quantity']}")

    total_cost = 0
    for item in cart:
        total_cost += item['price'] * item['quantity']

    address = input("Please enter your delivery address: ")
    return total_cost, address

def generate_receipt(name, email, cart, total_cost, address):
    print("Receipt:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Order Details:")
    for item in cart:
        print(f"Product: {item['product']}, Quantity: {item['quantity']}, Price: ${item['price']}")
    print(f"Total Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Thank you for shopping with us! Your order will be delivered in 3 days.")
    print("Payment will be charged after the successful delivery.")

def validate_name(name):
    part = name.split()
    # Check if the name contains both first and last names
    if len(name.split()) < 2:
        return False
    elif len(part)==2:
        for i in part:
            if not i.isalpha():
                return False
        return True
    return False
    
def validate_email(email):
    for i in email:
        if i == '@':
            return True
    return False

def main():
    name = input("Enter the name: ")
    validate_name(name)
    email = input("Enter the email address: ")
    validate_email(email)
    display_categories()
    display_products(products)

    cart = []
    while True:
        print("Please select an option:")
        print("1. Select a product to buy")
        print("2. Sort the products by price")
        print("3. Go back to category selection")
        print("4. Finish shopping")
        choice = input()

        if choice == '1':
            print("Select a product by entering its number:")
            for i, product in enumerate(products):
                print(f"{i + 1}. {product['name']} - ${product['price']}")
            product_choice = int(input())
            if 1 <= product_choice <= len(products):
                quantity = int(input("Enter the quantity you want to buy: "))
                add_to_cart(cart, products[product_choice - 1], quantity)
            else:
                print("Invalid product number. Please try again.")
        elif choice == '2':
            print("Sort products by price:")
            print("1. Ascending")
            print("2. Descending")
            sort_order = input()
            if sort_order in ['1', '2']:
                display_sorted_products(products, sort_order)
            else:
                print("Invalid sort order. Please try again.")
        elif choice == '3':
            display_categories()
        elif choice == '4':
            if cart:
                display_cart(cart)
                total_cost = sum(item['price'] * item['quantity'] for item in cart)
                print(f"Total cost: ${total_cost}")
                address = input("Enter your delivery address: ")
                generate_receipt("Your Name", "youremail@example.com", cart, total_cost, address)
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")
    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
