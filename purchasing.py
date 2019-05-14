#beginning of receipt program

#1. first catalog item
lovely_loveseat_description = "Lovely Loveseat: Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red of white\n"
#2. first catalog item price
lovely_loveseat_price = 254.00

#3. second catalog item
stylish_settee_description = "Stylish Settee: Faux leather on birch. 29.50 inches high x 54.75 inches wife x 28 inches deep. Black.\n"
#4. second catalog item price
stylish_settee_price = 180.50

#5. third catalog item
luxurious_lamp_description = "\nLuxurious lamp: Glass and iron. 36 inches tall. Brown with cream shade.\n"
#6. third catalog item price
luxurious_lamp_price = 52.15

#7. defining the sales tax which is 8.8%
sales_tax = .088

#8. first customer purchase
customer_one_total = 0
#9. first customers items
customer_one_itemization = ""

#10. first item the customer is buying
customer_one_total += lovely_loveseat_price

#11. keeping track of what the item is
customer_one_itemization += lovely_loveseat_description

#12. second item the customer is buying
customer_one_total += luxurious_lamp_price

#13. adding description to the second item
customer_one_itemization += "\n" + luxurious_lamp_description

#14. calculating sales tax
customer_one_tax = customer_one_total * sales_tax

#15. adding sales tax to the customers total
customer_one_total += customer_one_tax

#16. printing out the header for the items
print("Customer One Items:" + "\n")

#17. printing our the customers list
print(customer_one_itemization)

#18. adding the header for the total cost
print("Customer One Total is:" + "\n")

#19. printing out the first customers total
print(customer_one_total)

#20. second customer
customer_two_total = 0

#21. itemizing the 2nd customers lists
customer_two_itemization = ""

#22. customer 2 buys the settee
customer_two_total += stylish_settee_price

#23. adding the description to the item
customer_two_itemization += stylish_settee_description

#24. adding the lamp to the list
customer_two_total += luxurious_lamp_price

#25. adding the lamp description
customer_two_itemization += luxurious_lamp_description

#26. calulating the sales tax
customer_two_tax = customer_two_total * sales_tax

#27. adding the tax to the total
customer_two_total += customer_two_tax

#28. printing out the receipt heading
print("\nCustomer Two Items:\n")

#29. print out the list
print(customer_two_itemization)

#30. adding the heading for the cost now
print("Customer Two's Total is:\n")

#31. printing out 2nd customers total
print(customer_two_total)



