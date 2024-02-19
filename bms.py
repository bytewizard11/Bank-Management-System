all_accounts = {'0544': 1000.0,
                '0879': 500.0,
                '0569': 1500.0,
                '1587': 2450.0}

while True:
    print("***********************************************************************")
    print("\t\t WELCOME TO SWISS BANK MANAGEMENT SYSTEM")
    print("***********************************************************************")
    print("1. Create a New Account")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Check Balance")
    print("5. Transfer Amount")
    print("6. Exit the Management System")

    option = input("\nPlease select one option: ")

    if option == '1':
        account_number = input("Enter your account number: ")
        initial_balance = float(input("Enter initial balance: "))
        all_accounts[account_number] = initial_balance
        print("Your account for the account number", account_number, "has successfully created")

    elif option == '2':
        account_number = input("Enter your account number: ")
        amount = float(input("Enter the amount you want to withdraw: "))
        if account_number in all_accounts:
            if all_accounts[account_number] >= amount:
                all_accounts[account_number] -= amount
                print('Withdrawal Successful. Remaining balance for account number:', account_number, 'is', all_accounts[account_number], 'PKR')
            else:
                print('Insufficient Funds')
        else:
            print('Account does not exist')

    elif option == '3':
        account_number = input("Enter your account number: ")
        amount = float(input("Enter the amount you want to deposit: "))
        if account_number in all_accounts:
            all_accounts[account_number] += amount
            print('Deposit Successful. Current balance for account number:', account_number, 'is', all_accounts[account_number], 'PKR')
        else:
            print('Account does not exist')

    elif option == '4':
        account_number = input("Enter your account number: ")
        if account_number in all_accounts:
            print('Current balance for account number:', account_number, 'is', all_accounts[account_number], 'PKR')
        else:
            print("Account does not exist")

    elif option == '5':
        from_account = input("Enter your account number: ")
        to_account = input("Enter the recipient's account number: ")
        amount = float(input("Enter the amount you want to transfer: "))
        if from_account in all_accounts and to_account in all_accounts:
            if all_accounts[from_account] >= amount:
                all_accounts[from_account] -= amount
                all_accounts[to_account] += amount
                print('Transfer Successful. Remaining balance for account number:', from_account, 'is', all_accounts[from_account], 'PKR')
            else:
                print('Insufficient Funds for transfer')
        else:
            print('One or both accounts do not exist')

    elif option == '6':
        print("Thank You for interacting with our online banking system")
        break

    else:
        print("Invalid choice. Please choose from (1-6).")
