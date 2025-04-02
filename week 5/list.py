"""
features include
Menu
display content
remove item
compute total
quit

I have added a search for product both in the menu selection and the function to search and display a specific product
"""
item_name = []
item_price = []
item = ""
total = 0
#menu variable
menu =""


while menu!=6:
    #menu
    print("choose operation")
    print("1. Add new item")
    print("2. Display content of the shopping cart")
    print("3. Remove items from cart")
    print("4. Compute the total items")
    print("5. Search product")
    print("6. Quit")
    print("-" * 10)
    menu = input()
    menu = int(menu)

    if menu == 1:
#add new item
        print("type 'Done' when you are done entering the items")
        while item != "done":
            item=input("Item name: ")
            if item != "done":
              price=input("Price: $")
              item_name.append(item)
              item_price.append(price)
        print("Items has been saved succefully")
        
#display content
    elif menu == 2:
        print("Comfirm the list of items")
        for i in item_name:
            for j in item_price:
             convert_price = float(j)
             print(f"{i} - ${round(convert_price, 2)}")


## remove item
    elif menu == 3:
        print("Enter item name to remove from the list")
        name = input()
        for item in range(len(item_name)):
             if item_name[item] == name :
                index = item
                item_name.pop(item)
                item_price.pop(item)
        print("Product deleted successfully")

#compute total
    elif menu == 4:
                
                for i in range(len(item_price)):
                    price_in_list = float(item_price[i])
                    total +=price_in_list
                print(f"Total ${round(total, 2)}")

## Search item
    elif menu == 5:
        print("Enter the product name ")
        product_name = input()
        for item in range(len(item_name)):
            if item_name[item] == product_name :
                print(f"name exist index number is {item} and product name is {item_name[item]}")
            
