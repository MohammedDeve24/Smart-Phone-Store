def main():
  avilable_items = {
    "Iphone 15":{
        "price": 700,
        "quntity":4,
    },
    "Iphone 15 Pro":{
        "price":1000,
        "quntity":2,
    },
    "Iphone 15 Pro Max":{
        "price":1200,
        "quntity":1,
    },
    "Air Pods Pro":{
        "price":125,
        "quntity":5,
    },
    "Samsung Galaxy FE 24":{
        "price":500,
        "quntity":3,
    },
    "Samsung Galaxy S24 Ultra":{
        "price":1195,
        "quntity":4,
    },
    "Galaxy Buds 4":{
        "price":95,
        "quntity":6,
    }
        
}
# dictonary that I need
  cart = {}
 #----------------------
  print("---<|||Welcom to MOMO stor for Smart Phones📱|||>---")
  massage = """
What would you like to do ?
---------------------------
1.View avilable items
2.View cart
3.View total price of cart
4.Clear Cart🛒
5.Quite
---------------------------
"""
  while True:
     print(massage)
     #get user choice
     choice = input("Enter your choice: ")
      #if user enter 1.View avilable items
     if choice == "1":
        view(avilable_items,cart)
        #if user enter 2.View cart
     elif choice == "2":
       view_cart(cart)
     # if user enter 3 total 
     elif choice == "3":
       final_amount()
     #if user enter 4  clear cart
     elif choice == "4":
       clear_cart(avilable_items,cart)
     elif choice == "5":
        print("---<^>Thank you for shopping at MOMO store---<^>")
        break
     else:
        print("Pleease Enter between 1 and 5")
  final_cart(cart)




def view(avilable_items,cart):
    for i,item in enumerate(avilable_items):
              price= avilable_items[item]["price"]
              quntity= avilable_items[item]["quntity"]
              print("-"*35)
              if quntity == 0:
                  print(f"{i+1}.{item.title()}:${price}(item out of the stock)")
              else:
                  print(f"{i+1}.{item.title()}:${price}")
         #get item that user want to buy
    print("-"*35)
    user_item = input("Enter number of the product you want(Press Enter to back) : ")
    if user_item == "":
          return
    try:
    #add item to cart
      items_names = list(avilable_items.keys())[int(user_item)-1]
      check_quntity = avilable_items.get(items_names,{}).setdefault("quntity",)
      # check if item avilable or not
      if check_quntity != 0:
      #disply avilable quntity of product
       quntity= avilable_items[items_names]["quntity"]
       print(f"Avilable Quntity: {quntity}")
    #ask for quntity
       user_quntity = int(input("Please, Enter quntity: "))
        #check if the asked quntity is avilable
       if check_quntity < user_quntity:
                return print(f"Sorry we just have {check_quntity} of {items_names}")
               #get price
       item_price = avilable_items[items_names]["price"]
        #get quntity
       global item_quntity
       if items_names not in cart:
            item_quntity = user_quntity
       else:
            item_quntity+=user_quntity
        #save order info in the cart
       cart[items_names]= {"price":item_price,"quntity":item_quntity,}
       print("---New Phone---")
       print(f"{items_names.title()} has been added to cart succssfully")
        #decrease the quntity
       avilable_items[items_names]["quntity"]-=user_quntity
      else:
        print("The item out of the stock")
    except IndexError:
      print("Please enter number in range of the products list")
    except ValueError:
      print("Please, Enter Intger number!")
    
    pass

def view_cart(cart):
  total_price = 0
  global final_total
  final_total = 0
  print("----Check your cart🛒----")
  if cart:
      for item_brought in cart:
          # p for price
          p = cart[item_brought]["price"]
          # q for quntity
          q = cart[item_brought]["quntity"]
          #add price to total amount
          total_price=p*q
          final_total+=total_price
          print(f"{item_brought.title()}: ${p}x{q} = ${total_price}")
          print("-"*35)       
  else:
      print("--<>--Cart Empty--<>--")
      print("--NO item have been bought--")
  pass

def final_amount():
  if final_total !=0:
         print(f"---View Total price--- : ${final_total}")
  else:
            print("--NO item have been bought--")

def clear_cart(avilable_items,cart):
  if cart:
            check_to_clear = input("Are you sure you want to clear the cart? (y/n): ").lower()
            if check_to_clear == "y":
                for item in cart.keys():
                    avilable_items[item]["quntity"]+=cart[item]["quntity"]
                cart.clear()
                print("---Clear Cart Succssfully🛒---")
            elif check_to_clear == "n":
                print("--- Cancel clearing cart ---") 
            else:
              print("Please enter y for Yes or n for No") 
                
  else:
      print("The cart already empty!")   
  pass

def final_cart(cart):
  total_price = 0
  final_total = 0
  if cart:
    print("-----Final Cart🧾-----")
    for item_brought in cart:
            # p for price
             p = cart[item_brought]["price"]
             # q for quntity
             q = cart[item_brought]["quntity"]
             print(f"{item_brought.title()}: ${p}x{q}")
             print("-"*35)
            #add price to total amount
             total_price=p*q
             final_total+=total_price
    print(f"-----Final Total Price:${final_total}-----")
  else:
     print("Cart is empty")

main()


