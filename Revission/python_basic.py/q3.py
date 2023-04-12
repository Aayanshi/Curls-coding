''' Create a calculator function
Write a Python function that accepts three parameters. The first parameter is an integer. 
The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.

The function should perform a calculation and return the results. 
For example, if the function is passed 6 and 4, it should return 24.'''


n1 = int(input("your first number= "))
n2 = int(input("your second number= "))
op = input("what operation you want to continue= ")

k = 0
if op == "+":
    k = n1 + n2

elif op == "*":
    k = n1 * n2

elif op == "-":
    k = n1 - n2 

elif op == "/":
    k = n1 / n2       

else:
    print("phone me jake kar lo")

print(f" your answer = {k}")    



   


