from test_lib import test, report
from math_operations import increment, decrement, add, substract, multiply, divide

number1 = 3
number2 = 11
number3 = 37
number4 = 79

result1 = number3 * 7
result2 = multiply(number3, 7)
test('example', result1, result2)

result1 = number1 + number2
result2 = add(number1, number2)
test('add', result1, result2)

result1 = (number1 + number2) * number3
result2 = multiply(add(number1, number2), number3)
test('expression-1', result1, result2)

result1 = (number4 - (number1 * (number4 - number3)) / (number2 + number3))
result2 = substract(number4, divide(multiply(number1, substract(number4, number3)), add(number2, number3)))
test('expression-4', result1, result2)

result1 = ((number4 - (number1 * (number4 - number3)) / (number2 + number3)) * 23) - 1
result2 = decrement( (multiply((substract(number4, (divide( (multiply(number1, (substract(number4, number3)))), add(number2, number3))))), 23)) )
test('expression-5', result1, result2)

report()
