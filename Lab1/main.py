from number import Number
from binarithmetic import plus, minus, multiplication, division, float_plus
from float import evaluate_mantissa, Float

int_num1 = Number(int(input("Enter first integer number: ")))
int_num2 = Number(int(input("Enter second integer number: ")))

print("+:\n")
print(plus(int_num1, int_num2))
print("-:\n")
print(minus(int_num1, int_num2))
print("*:\n")
print(multiplication(int_num1, int_num2))
print("/:\n")
print(division(int_num1, int_num2))

float_num1 = Float(float(input("\nEnter first float number: ")))
float_num2 = Float(float(input("Enter second float number: ")))

print("+:\n")
print(float_plus(float_num1, float_num2))


