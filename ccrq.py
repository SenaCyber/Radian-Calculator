import webbrowser
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def calculator():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to Radian Quadro's Calculator!\n")

    while True:
        print(Fore.YELLOW + "\nChoose an operation:")
        print(Fore.GREEN + "1. Addition (+)")
        print(Fore.RED + "2. Subtraction (-)")
        print(Fore.MAGENTA + "3. Multiplication (*)")
        print(Fore.BLUE + "4. Division (/)")
        print(Fore.CYAN + "5. Visit my Facebook")
        print(Fore.WHITE + "6. Exit")

        choice = input(Fore.LIGHTWHITE_EX + "\nEnter your choice (1-6): ")

        if choice == '5':
            fb_link = "https://www.facebook.com/radianquadro"
            print(Fore.LIGHTBLUE_EX + "Opening Facebook profile...")
            webbrowser.open(fb_link)

        elif choice == '6':
            print(Fore.LIGHTGREEN_EX + "Thanks for using the calculator. Goodbye!")
            break

        elif choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input(Fore.LIGHTYELLOW_EX + "Enter first number: "))
                num2 = float(input(Fore.LIGHTYELLOW_EX + "Enter second number: "))
                
                if choice == '1':
                    result = num1 + num2
                elif choice == '2':
                    result = num1 - num2
                elif choice == '3':
                    result = num1 * num2
                elif choice == '4':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        print(Fore.LIGHTRED_EX + "Error: Division by zero!")
                        continue

                print(Fore.LIGHTGREEN_EX + "Result:", result)
            except ValueError:
                print(Fore.RED + "Invalid input! Please enter numbers only.")
        else:
            print(Fore.LIGHTRED_EX + "Invalid choice! Please select from 1 to 6.")

# Run the calculator
calculator()