income = 0
expense = 0

num_transactions = int(input("Enter number of transactions: "))

for i in range(num_transactions):
    print("\n1 - Add Income")
    print("2 - Add Expense")
    type_choice = int(input("Select choice (1 or 2): "))
    
    # Check if choice is valid
    if type_choice != 1 and type_choice != 2:
        print("Error: Invalid choice!")
        continue
        
    amount = int(input("Enter amount: "))
    
    if type_choice == 1:
        income = income + amount
    elif type_choice == 2:
        expense = expense + amount

# Final calculations
balance = income - expense

print("\n-----------------------------")
print("Total Income:", income)
print("Total Expense:", expense)
print("Net Balance:", balance)

if balance > 0:
    print("Status: Profit (Saved money)")
elif balance < 0:
    print("Status: Loss (Overspent)")
else:
    print("Status: Zero Balance")
print("-----------------------------")
