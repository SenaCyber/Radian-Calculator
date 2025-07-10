import webbrowser

def calculator():
    print("Welcome to Radian Quadro's Calculator!\n")
    print("এটি একটি সিম্পল ক্যালকুলেটর যেটি আপনি টারমাক্সে চালাচ্ছেন")
    while True:
        print("\nChoose an operation:")
        print("1. যোগ (+)")
        print("2. বিয়োগ (-)")
        print("3. গুন (*)")
        print("4. ভাগ (/)")
        print("5. Visit my Facebook")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '5':
            fb_link = "https://www.facebook.com/radianquadro"
            print("Opening Facebook profile...")
            webbrowser.open(fb_link)
        elif choice == '6':
            print("ধন্যবাদ Radian Quadro স্যারের ক্যালকুলেটর ব্যবহার করার জন্য!")
            break
        elif choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
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
                        print("Error: Division by zero!")
                        continue

                print("Result:", result)
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        else:
            print("Invalid choice! Please select from 1 to 6.")

# Run the calculator
calculator()