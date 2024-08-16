dollar = int(input("Enter how many dollars it costs: "))
cent =  int(input("How many cents does it cost? "))

amount = int(input("how many cookies are being baught"))

total = (dollar + cent/100) * amount

garfield="The total cost of {} cookies is ${}"
print(garfield.format(amount,total))