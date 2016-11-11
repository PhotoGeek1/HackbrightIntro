menu_list = ["food: hotdog, price:5.50", "food:burger,price:9.50", "food:fries, price:4.00", "food:shake,price:5.00"]

# pseduocode
# create function
# 	create empty dictionary "food_name_and_price"
# 	loop through list. 	
# 		for each item in list (menu_list[i])
# 		split by comma ["food: hotdog"],["price:5.50"]
# 			for each item in sublist
# 				split by semicolon
# 				sublist[0] = food_name_and_price key
# 				sublist[1] = food_name_and_price value

def parse_groceries(menu):
	food_name_and_price = {}
	for menu_list_item in menu:
		food_sublist_item = menu_list_item.split(",")
		name_parts = food_sublist_item[0].split(":")
		name = name_parts[1]
		price_parts = food_sublist_item[1].split(":")
		price = price_parts[1]
		food_name_and_price[name] = price
	print food_name_and_price

parse_groceries(menu_list)










