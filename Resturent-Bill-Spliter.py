print ("Welcome to the tip calculator !")
bill = float(input("What was the total bill ? $ "))
tip = int(input("How mush tip you would like to give ? 10, 12 or 15 ? "))
people = int(input("How many people to split the bill ? "))
bill_with_tip = tip /100 *bill + bill
print(f"Total Bill : ${bill_with_tip}")
per_head = bill_with_tip/ people
final_amount = round(per_head, 2)
print(f"Each person should pay : ${final_amount}") 
