tict = int(input("Enter number of ticket: "))
vist = [int(input("Enter age of everyone visitor: ")) for i in range(tict)]
price_1 = 0
price_2 = 0
price_3 = 0
totl_prc = 0
price_1 = (int(sum(True for i in vist if i < 18))) * 0
print("Price for visitors under 18 ", price_1, "RUB")
price_2 = (int(sum(True for i in vist if 18 <= i < 25))) * 990
print("Price for visitors under 25 ", price_2, "RUB")
price_3 = (int(sum(True for i in vist if i >= 25))) * 1390
print("Price for visitors over 25 ", price_3, "RUB")
totl_prc = price_1 + price_2 + price_3
if tict <= 3:
    print("Total price: ", totl_prc, "RUB")
else:
    print("You choose over 3 tickets, your total price with discout 10 per cent: ", totl_prc * 0.9, "RUB")