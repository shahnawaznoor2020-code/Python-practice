#show balance
#withdraw
#deposit
balance=0.0
kyc_documents={}

def check_balance():
    print(f"Your current balance is {balance}")

def deposit():
    global balance
    deposit_amount = float(input("Enter your deposit amount: "))
    if deposit_amount > 0:
        balance = balance + deposit_amount
        check_balance()
        print(f"You have deposited {deposit_amount} in your account")
    elif deposit_amount == 0 & deposit_amount is None:
        print("Deposit amount can't be zero")
    else:
        print("Invalid deposit amount")

def withdraw():
    global balance
    if balance>0:
        withdraw_amount=float(input("Enter the withdrawing amount: "))
        if withdraw_amount>balance:
            print("You can't withdraw money more than your account balance")
        else:
            if withdraw_amount >0:
                balance = balance - withdraw_amount
                check_balance()
                print(f"{withdraw_amount} has been withdrew from your account")
            else:
                print("Enter a valid withdraw amount")
    elif balance==0 :
        print("Your balance is 0")
        print("You can't withdraw money")
    else:
        print("Negative Balance")
        print("You can't withdraw money")
        print("Please clear your negative balance")

def check_kyc():
    global kyc_documents
    if len(kyc_documents)==0:
        print("Kyc Not Done")
    else:
        for document in kyc_documents:
            print(f"{document} : {kyc_documents[document]}")


def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)


if __name__ == "__main__":
    print("===============================")
    print("Welcome to Banking Application")
    print("===============================")
    while True:

        print("1. Check Your Balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check Kyc")
        print("5. Update Kyc")
        print("6. Quit")
        choice = input("Enter your choice(1-6): ")
        if choice == "1":
            check_balance()
            print()
        elif choice == "2":
            deposit()
            print()
        elif choice == "3":
            withdraw()
            print()
        elif choice == "4":
            check_kyc()
            print()
        elif choice == "5":
            kyc_docs={}
            n_documents=int(input("Enter the number of documents you want to add: "))
            for i in range (n_documents):
                key=input("Enter the document type :")
                value=input("Enter the document number :")
                kyc_docs[key]=value
            update_kyc(kyc_docs)
        elif choice == "6":
            break
        else:
            print("Invalid Choice")
            print()
        print("==============================")
    print("Thank you for banking with us")