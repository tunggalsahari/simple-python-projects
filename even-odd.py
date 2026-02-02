while True:
    try:
        number = int(input("Enter a number to check if it's an Even or Odd number: "))
        
        if number % 2 == 0:
            print(f"{number} is an even number")
            break
        elif number % 4 == 0:
            print(f"{number} is an even number")
            break
        else:
            print(f"{number} is an odd number")
            break
        
    except ValueError:
        message = ("Invalid input!")
        print(message)
