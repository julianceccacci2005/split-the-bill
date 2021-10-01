# Programmer: Julian Ceccacci   
# Date: october 1, 2021 
# Description: 


try:
  bill_cost = float(input("Enter the bill cost: "))
except ValueError:
    print("Invalid bill cost!.")
    exit()
try:
  number_of_people = float(input("Enter the number of people: "))
except ValueError:
    print("Invalid number of people!.")
    exit()
each_person = bill_cost/number_of_people 

print(f"Each person must pay ${each_person:,.2f}")