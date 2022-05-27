food = ["Sandwich", "Drinks", "Hotdog","Coffee","Pizza", "Donuts"]
prices=[2.30,1.50,2.45,1.50,3.50,1.50]

orderFood=[]
orderCost=[]
counter=0
total=0

print("Welcome!")
order= input("Can I take your order? Y/N\n")
if order == "N":
  print("Goodbye!")
  exit()
else:
  print ("Thank you!")    

nextOrder = True

while nextOrder==True:
  print("Menu:\n1. Sandwich \n2. Drinks \n3. Hotdog \n4. Coffee \n5. Pizza \n6. Donuts")
  foodOrder = input("Please enter the number of item.\n")
  if foodOrder == "1":
    orderFood.append(food[0])
    orderCost.append(prices[0])
    counter=counter+1
    total=total+(prices[0])

  elif foodOrder == "2":
    orderFood.append(food[1])
    orderCost.append(prices[1])
    counter=counter+1
    total=total+(prices[1])

  elif foodOrder == "3":
    orderFood.append(food[2])
    orderCost.append(prices[2])
    counter=counter+1
    total=total+(prices[2])
  
  elif foodOrder == "4":
    orderFood.append(food[3])
    orderCost.append(prices[3])
    counter=counter+1
    total=total+(prices[3])
  
  elif foodOrder == "5":
    orderFood.append(food[4])
    orderCost.append(prices[4])
    counter=counter+1
    total=total+(prices[4])

  elif foodOrder == "6":
    orderFood.append(food[5])
    orderCost.append(prices[5])
    counter=counter+1
    total=total+(prices[5])    

  else:
    print("Not on menu!")

  finished = input("Have you finished ordering? Y/N \n")
  if finished == "N":
    nextOrder = True
  else:
    nextOrder = False

y=0

print("Here is your order")
print("      ")
print("*************************")
while y<counter:
    
  print("Item: "+ (orderFood[y]))
  print("Cost: $"+ str(orderCost[y]))
  y=y+1
    
print ("The total cost is: $"+str(total))
print ("*************************")