#Calculator
from replit import clear
from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Dictionary
operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}

#calculator
def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the second number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer1}")
  
  if input("Type 'y' to continue calculating with 3.0, or type 'n' to start a new calculation: ").lower() == "y":
    num1 = answer
  else:
    should_continue = False
    clear()
    calculator()

calculator()
