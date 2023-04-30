
book1 = 499
book2 = 855
book3 = 645
deliveryCharges = 250
b1 = int(input("Enter number of books: "))
b2 = int(input("Enter number of books: "))
b3 = int(input("Enter number of books : "))
total = (b1*book1)+(b2*book2)+(b3*book3)
totalAmt = total +(0.12 *total)+deliveryCharges
print("Total Invoice Amount : ",totalAmt)