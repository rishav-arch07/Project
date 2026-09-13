FILE_NAME = "inventory.txt"


def load_products():
    """Load products from file"""
    products = {}
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, price, stock = line.strip().split(",")
                products[name] = {"price": float(price), "stock": int(stock)}
    except FileNotFoundError:
        pass
    return products


def save_products(products):
    """Save products to file"""
    with open(FILE_NAME, "w") as f:
        for name, details in products.items():
            f.write(f"{name},{details['price']},{details['stock']}\n")


def add_product(products):
    name = input("Product name: ")
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))

    products[name] = {"price": price, "stock": stock}
    save_products(products)
    print(f"'{name}' has been added!\n")


def view_products(products):
    if not products:
        print("No products available yet.\n")
        return

    print("\n" + "-" * 40)
    print(f"{'Product':<20}{'Price':<10}{'Stock':<10}")
    print("-" * 40)
    for name, details in products.items():
        print(f"{name:<20}₹{details['price']:<9}{details['stock']:<10}")
    print("-" * 40 + "\n")


def sell_product(products):
    view_products(products)
    name = input("Which product do you want to sell: ")

    if name not in products:
        print("This product is not in the inventory!\n")
        return

    qty = int(input("Quantity: "))

    if qty > products[name]["stock"]:
        print(f"Only {products[name]['stock']} units are available!\n")
        return

    total = products[name]["price"] * qty
    products[name]["stock"] -= qty
    save_products(products)

    print("\n" + "=" * 35)
    print("           BILL / INVOICE")
    print("=" * 35)
    print(f"Product: {name}")
    print(f"Price per unit: ₹{products[name]['price']}")
    print(f"Quantity: {qty}")
    print("-" * 35)
    print(f"TOTAL: ₹{total}")
    print("=" * 35 + "\n")


def delete_product(products):
    view_products(products)
    name = input("Which product do you want to delete: ")

    if name in products:
        del products[name]
        save_products(products)
        print(f"'{name}' has been deleted!\n")
    else:
        print("This product was not found.\n")


def main():
    products = load_products()

    while True:
        print("===== INVENTORY & BILLING SYSTEM =====")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Generate Bill (Sell Product)")
        print("4. Delete Product")
        print("5. Exit")
        print("=======================================")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_product(products)
        elif choice == "2":
            view_products(products)
        elif choice == "3":
            sell_product(products)
        elif choice == "4":
            delete_product(products)
        elif choice == "5":
            print("Thank you! See you again.")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
