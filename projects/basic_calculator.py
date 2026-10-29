class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2

    def div(self):
        if(self.num2 == 0):
            return "Error: Cannot divide by zero"
        return self.num1/self.num2


print("=====Calculator=====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

try: 
    choice = int(input("Enter your choice (1-4): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    calc = Calculator(num1,num2)

    if choice == 1:
        print("Result: ",calc.add())
    elif choice == 2:
        print("Result: ",calc.sub())
    elif choice == 3:
        print("Result: ",calc.mult())
    elif choice == 4:
        print("Result: ",calc.div())
    else:
        print("Invalid Choice")

except ValueError:
    print("Please enter valid inputs")
