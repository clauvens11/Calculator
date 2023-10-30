##--CALCULATOR--##

##--USER INPUTS--##
mathtype = input("""
1 Addition
2 Subtraction
3 Multiplication
4 Division
5 Exponet
""")

num1 = int(input("what's the first number"))

num2 = int(input("what's the second number"))
##--IF AND ELIF'S--##
if mathtype == "1":
    print(num1 + num2)
elif mathtype == "2":
    print(num1 - num2)
elif mathtype == "3":
    print(num1 * num2)
elif mathtype == "4":
    print(num1/num2)
elif mathtype == "5":
    print(num1 ** num2)
else:
    print("Please properly input a number 1-5 based on corresponding operation")
##--THE END--##
##--ps. hopefully in future plan to upgrade all theese reposits to make them more complex as i advance--##
