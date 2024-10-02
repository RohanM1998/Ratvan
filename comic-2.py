#comic book store
print("WELCOME TO THE SUPERHEROES COMIC BOOK STORE...!")

# Sign in or Create Account
options = int(input('''CHOOSE Sign In options:
1. Sign in
2. Create an account
'''))

if options == 1:  
    User_name = input("USERNAME: ")
    Password = input("Password: ")
    
    if Password == "Trex100":
        options = int(input('''CHOOSE A CATEGORY OF INTEREST:
1. MARVEL
2. DC
'''))

        if options == 1:  
            marvel_comics = int(input('''Choose a comic of your interest:
1. DOCTOR STRANGE
2. MOON KNIGHT
'''))
            
            if marvel_comics == 1:
                print("BOOK SELECTED: DOCTOR STRANGE")
                price = 10000
                discount = 40
                cal = price * discount / 100
                final_price = price - cal
                print(f"Amount after discount: {final_price}")
                upi = input("Enter your UPI code: ")  
                if len(upi) >= 6:  
                    print(f"Rs.{final_price} received through PhonePe")
                else:
                    print("Invalid UPI code")
                    print("Payment Failed")
            
            elif marvel_comics == 2:
                print("BOOK SELECTED: MOON KNIGHT")
                price = 4000
                discount = 4
                cal = price * discount / 100
                final_price = price - cal
                print(f"Amount after discount: {final_price}")
                upi = input("Enter your UPI code: ")  # Input UPI code as a string
                if len(upi) >= 6:  # Check UPI code length
                    print(f"Rs.{final_price} received through PhonePe")
                else:
                    print("Invalid UPI code")
                    print("Payment Failed")
            
            else:
                print("Out of stock")
        elif options == 2:  
            DC_COMICS = int(input('''Choose a comic book:
1. BATMAN: COURT OF OWLS
2. SUPERMAN EARTH-1
'''))
            
            if DC_COMICS == 1:
                print("BOOK SELECTED: BATMAN: COURT OF OWLS")
                price = 200
                discount = 6
                cal = price * discount / 100
                final_price = price - cal
                print(f"Amount after discount: {final_price}")
                upi = input("Enter your UPI code: ")  
                if len(upi) >= 6: 
                    print(f"Rs.{final_price} received through PhonePe")
                else:
                    print("Invalid UPI code")
                    print("Payment Failed")
            
            elif DC_COMICS == 2:
                print("BOOK SELECTED: SUPERMAN EARTH-1")
                price = 900
                discount = 10
                cal = price * discount / 100
                final_price = price - cal
                print(f"Amount after discount: {final_price}")
                upi = input("Enter your UPI code: ")  
                if len(upi) >= 6:  
                    print(f"Rs.{final_price} received through PhonePe")
                else:
                    print("Invalid UPI code")
                    print("Payment Failed")
            
            else:
                print("Out of stock")
        
        else:
            print("Other comics are not available at this time")
    else:
           print("invalid password check once")
elif options == 2:  
    FULL_NAME = input("FULL NAME: ")
    LAST_NAME = input("LAST NAME: ")
    EMAIL_ID = input("EMAIL: ")
    PASSWORD = input("PASSWORD: ")
    CONFIRM_PASSWORD = input("CONFIRM PASSWORD: ")
    
    if CONFIRM_PASSWORD == PASSWORD:
        choose = int(input('''Choose a category from the following:
1. MARVEL COMICS
2. DC COMICS
'''))
        
        if choose == 1:  
            COMICS1 = int(input('''Choose a comic:
1. IRON MAN
2. X-MEN: DAYS OF FUTURE PAST
'''))
            
            if COMICS1 == 1:
                print("COMIC SELECTED: IRON MAN")
                price = 450
                print(f"Total Amount: {price}")
                upi = input("Enter your UPI code: ")  
                print(f"Rs.{price} received through PhonePe")
                print("Thank you, visit us again")
            
            elif COMICS1 == 2:
                print("COMIC SELECTED: X-MEN: DAYS OF FUTURE PAST")
                price = 20000
                print('''Final price is high for this book because it's one of the collectibles:
* Grade = 10
* Authenticity = Minted comic
There are no discounts for Minted comics''')
                upi = input("Enter your UPI code: ")  
                print(f"Rs.{price} received through PhonePe")
                print("Thank you, visit us again")
            
            else:
                print("Out of stock")
        
        elif choose == 2:  
            DC_COMICS = int(input('''Choose a comic from DC category:
1. BATMAN: WHITE KNIGHT
2. FLASHPOINT PARADOX
'''))
            
            if DC_COMICS == 1:
                print("COMIC SELECTED: BATMAN: WHITE KNIGHT")
                price = 40000
                discount = 60
                percentage = price * discount / 100
                total = price - percentage
                print(f"Total price: {total}")
                upi = input("Enter your UPI code: ")  
                print(f"Rs.{total} received through PhonePe")
                print("Thank you, visit us again")
            
            elif DC_COMICS == 2:
                print("COMIC SELECTED: FLASHPOINT PARADOX")
                price = 100
                print(f"Total Price: {price}")
                upi = input("Enter your UPI code: ")  
                print(f"Rs.{price} received through PhonePe")
                print("Thank you, visit us again")
            
            else:
                print("Out of stock")
    
    else:
        print("Passwords do not match")

else:
    print("Invalid option selected")
    
