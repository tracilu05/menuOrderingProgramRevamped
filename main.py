

menu = {
  
  'A':{'item': 'Cheeseburger','price': 3.30 },
  'B': {'item': 'Big Mac', 'price': 5.30},
  'C': {'item': 'McFlurry', 'price': 3.99},
  'D': {'item': 'McNuggets 6 pc', 'price': 5.15},
  'E': {'item': 'Double Quarter Pounder', 'price': 7.13},
  'F': {'item': 'Large Fries', 'price': 3.87}}


def menuOutput():
  print('Welcome to Mcdonalds: what would you like to order?: ')
  for item in menu.keys():
    print(item + ": " + str(menu[item]['item']) + ' ' + '$' + str(menu[item]    
   ['price']))

          
def welcome(): 
  ordering = True
  orderPrice = []
  orderItems = []
  orderTotal = 0
  orderAsk = 'What would you like to order? Please choose an option: '
  orderConfirm = 'Would you like to order something else? Y/N'

  while ordering:
    ret = input(orderAsk)
    if ret not in menu.keys():
      print("This item is not a part of the menu. Please choose one of the following")
      for item in menu.keys():
        print(item + ": " + str(menu[item]['item']) + ' ' + '$' + str(menu[item]    
   ['price']))

    if ret:
      orderItems.append(ret)
      orderPrice.append(menu[ret]['price'])
      confirm = input(orderConfirm)
      if "y" in confirm.lower():
        ordering = True 
      if "n" in confirm.lower():
        ordering = False
        for item in range(0,len(orderPrice)):
          orderTotal = orderTotal + orderPrice[item]
        print("your order: ")
        print()
        order_print_item = [str(menu[i]['item'])+ ": " + str(menu[i]["price"])
        for i in orderItems]
        for i in order_print_item:
            print(*i, sep= '')
            print()
        print("Your Total: ")
        print(orderTotal)
  return
menuOutput()

welcome()
