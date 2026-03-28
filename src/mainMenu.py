import sys
from account_operations import *

while True:
    print("---------------Bank Management System---------------")
    print("Enter your choice")
    print("1 : create account")
    print("2 : view all accounts")
    print("3 : view your account info")
    print("4 : deposite money")
    print("5 : withdraw money")
    print("6 : view all transations record")
    print("7 : delete account")
    print("8 : exit")

    choice= int(input("Enter your choice: "))

    if choice==1:
        create_account()
    elif choice==2:
        all_accounts()
    elif choice==3:
        search_account()
    elif choice==4:
        acc_id=input("Enter your Account Id: ")
        ammount=input("Enter Ammount to credit: ")
        credit_cash(acc_id, ammount)
        transaction_credit_update(acc_id, ammount)
    elif choice==5:
        acc_id=input("Enter your Account Id: ")
        ammount=input("Enter Ammount to credit: ")
        debit_cash(acc_id, ammount)
        transaction_debit_update(acc_id, ammount)
    elif choice==6:
        transactions_record_show()
    elif choice==7:
        delete_account()
    elif choice==8:
        sys.exit()
    else:
        print("Invalid choice. Please select the right choice.")