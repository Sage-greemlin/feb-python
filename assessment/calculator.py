num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

print( "for addtion enter +")
print( "for subtraction enter -")
print( "for multiplication enter *")
print( "for division enter /")
operator = input("Enter an operator: ")

if operator == "+":
    print( "the sum of " + str(num1) + " and " + str(num2) + " is equal to = " + str( float(num1) + float(num2) ) )
elif operator == "-":
    print("the difference of " + str(num1) + " and " + str(num2) + " is equal to = " + str( float(num1) - float(num2) ) )
elif operator == "*":
    print( "the product of " + str(num1) + " and " + str(num2) + " is equal to = " + str( float(num1) * float(num2) ) )
elif operator == "/":
    print( "the division of " + str(num1) + " and " + str(num2) + " is equal to = " + str( float(num1) / float(num2) ) )
else:
    print("Invalid operator")