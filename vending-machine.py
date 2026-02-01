def products():
    product_list = ['red bull', 'monster energy', 'heineken', 'estrella galicia',
                    'coca-cola', 'pepsi', 'nescafe', 'pocari sweat',
                    'chimori', 'fanta']
    return product_list

def prices():
    prices_list = [3.25, 2.75, 2.50, 2.75, 1.75, 1.75, 2.00, 2.50, 2.25, 1.75]
    return prices_list

def main():
    header = (5*"="+" Vending Machine "+5*"=")
    print(header)

    menu = products()
    price = prices()

    for index, name in enumerate(menu, start=1):
        print(f"{index}. {name.title()}")
    
    try:
        order = int(input(f"=> Choose any number (1-{len(menu)}): ")) - 1
        quantity = int(input(f"=> How many {menu[order].title()} would you want: "))

        if quantity == 1:
            message = (f"=> Your order is a ${price[order]} {menu[order].title()}")
            print(message)
        
        elif quantity > 1 <= 10:
            calculation = quantity * price[order]
            message = (f"=> Your orders are {quantity} pieces of ${price[order]} {menu[order].title()} and that would be ${calculation}")
            print(message)

    except IndexError:
        print("=> Input Invalid")

if __name__ == "__main__":
    main()
