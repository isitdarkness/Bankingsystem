import random
data_base_dict = {}
while True:
    print("Welcome to the CLI based banking system")
    print("1. Login \n\n2. Create Account \n\n3. Exit")
    value = int(input("Enter the number next to the provided thing you want to proceed with --->  "))
    if value == 2:
        name = input("Enter the Name -->  ")
        while True:
            pin = input("Enter the 4 digit secret pin -->  ")
            if len(pin) == 4 and pin.isdigit():
                break
            else:
                print("Invalid pin Try again!")
        while True:
            acc_num = random.randint(1001,9999)
            if acc_num in data_base_dict:
                acc_num = random.randint(1001,9999)
            else:
                data_base_dict[acc_num] = {}
                break
        details = { #as we know values can be same
            "balance" : 0.0,
            "history" : [],
            "pin" : pin,
            "name" : name,
            "acc_num" : acc_num
        }
        data_base_dict.update({acc_num : details})
        print(f"\nAccount created successfully! Your Account Number is: {acc_num}\n\nNote: Please don't share this account number with anyone we will not be responsible")    
    elif value == 1:
        sucess = 0 
        account_number = int(input("Enter the account number-->  "))
        while True:
            pin = input("Enter the 4 digit secret pin -->  ")
            if len(pin) == 4 and pin.isdigit():
                break
            else:
                print("Invalid pin Try again!") 
        if account_number in data_base_dict:
            if data_base_dict[account_number]["pin"] == pin:
                sucess = 1
                user_data = data_base_dict[account_number]
            else:
                print("Invalid Pin Try Again!")
        else:
            print("Try entering Account Number")
            print("If you don't have account try creating one First!")
        if sucess == 1:
            while True:
                print("1.Balance \n2.Deposit \n3.Withdraw \n4.Statement \n5.Logout")
                num = int(input("Enter the number accordingly -->  "))
                if num == 1:
                    print(f"Your Current Balance is {user_data["balance"]}")
                elif num == 2:
                    amount = int(input("Enter the amount you want to deposit-->  "))
                    data_base_dict[account_number]["balance"] += amount
                elif num == 3:
                    amount = int(input("Enter the amount you want to withdraw -->  "))
                    if amount > data_base_dict[account_number]["balance"]:
                        print("Insufficent Balnace!")
                    else: 
                        print(f"Sucefullt withdrawn money {amount}")
                        data_base_dict[account_number]["balance"] -= amount
                elif num == 4:
                    pass
                elif num == 5:
                    break
                else: 
                    print("Invalid Statemnt")

