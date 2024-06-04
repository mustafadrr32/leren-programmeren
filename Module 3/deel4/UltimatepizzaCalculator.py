# MUSTAFA DURUR OPDRACHT PIZZACALCULATOR

def get_pizza_prices():
    return {
        'Small': 7.99,
        'Medium': 9.99,
        'Large': 11.99,
        'X-Large': 13.99,
    }

def get_pizza_order():
    try:
        pizza_order = {}
        for size in pizza_prices.keys():
            quantity = int(input(f"Hoeveel {size.lower()} pizza's? "))
            pizza_order[size] = quantity
        return pizza_order
    except ValueError:
        print("Ongeldige invoer. Voer een geheel getal in voor het aantal pizza's.")
        return None

def calculate_totals(pizza_order):
    total_pizzas = sum(pizza_order.values())
    total_costs = {size: pizza_prices[size] * qty for size, qty in pizza_order.items()}
    total_amount = sum(total_costs.values())
    return total_pizzas, total_costs, total_amount

def print_order_summary(total_pizzas, total_costs, total_amount, pizza_order):
    print("\n-----------------------------------------")
    print(f"Aantal bestelde pizza's: {total_pizzas}")
    for size, qty in pizza_order.items():
        print(f"Aantal {size.lower()} pizza's: {qty}")
    print("-----------------------------------------")
    for size, cost in total_costs.items():
        print(f"Prijs {size.lower()} pizza: {cost:.2f} euro")
    print(f"TOTAAL: {total_amount:.2f} euro")
    print("-----------------------------------------")

if __name__ == "__main__":
    pizza_prices = get_pizza_prices()
    
    print("Keuze uit: Small, Medium, Large")
    for size, price in pizza_prices.items():
        print(f"{size}: {price:.2f} euro")
    
    pizza_order = get_pizza_order()
    
    if pizza_order:
        total_pizzas, total_costs, total_amount = calculate_totals(pizza_order)
        print_order_summary(total_pizzas, total_costs, total_amount, pizza_order)
