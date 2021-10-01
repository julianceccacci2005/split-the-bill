# Programmer: Julian Ceccacci   
# Date: october 1, 2021 
# Description: code where each persons cost is calculated

# where bill cost gets collected and displays an error code if worng 
try:
  bill_cost = float(input("Enter the bill cost: "))
except ValueError:
    print("Invalid bill cost!.")
    exit()
# same as bill except its for number of people
try:
  number_of_people = float(input("Enter the number of people: "))
except ValueError:
    print("Invalid number of people!.")
    exit()
# where the cost of each person is calculated
each_person = bill_cost/number_of_people 
# final answer
print(f"Each person must pay ${each_person:,.2f}")