# coding: utf8
"""
## Credit Card Verification

Credit cards numbers are verified using the Luhn formula. The formula verifies a number against
its included check digit, which is usually appended to a partial account number to generate
the full account number. This number must pass the following test:

1. From the **rightmost** digit, which is the check digit, and moving left, double the value
   of every second digit. If the result of this doubling operation is greater than 9 (e.g., 8 × 2 = 16),
   then add the digits of the product (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or, alternatively, the same
   result can be found by subtracting 9 from the product (e.g., 16: 16 − 9 = 7, 18: 18 − 9 = 9).
2. Take the sum of all the digits.
3. If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to
   the Luhn formula; else it is not valid.

Assume an example of a card number "79927398713":

|---------------------|----|----|----|----|----|----|----|----|----|----|----|
| Digit index         | 10 |  9 |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |  0 |
|---------------------|----|----|----|----|----|----|----|----|----|----|----|
| Card number         |  7 |  9 |  9 |  2 |  7 |  3 |  9 |  8 |  7 |  1 |  3 |
| Double every second |  7 | 18 |  9 |  4 |  7 |  6 |  9 | 16 |  7 |  2 |  3 |
| Sum digits          |  7 |  9 |  9 |  4 |  7 |  6 |  9 |  7 |  7 |  2 |  3 |
|---------------------|----|----|----|----|----|----|----|----|----|----|----|


The sum of all the digits in the third row is 70, which means the card number is valid (70 module 10 is 0).

Write a function `check_card(number)` that implements the following algorithm and returns `True` of `False`
indicating if the card number is correct.

Use it to verify your credit card number. You may also check the correctness of the following numbers:
`79927398710`, `79927398711`, `79927398712`, `79927398713`, `79927398714`, `79927398715`, `79927398716`,
`79927398717`, `79927398718`, `79927398719`.
"""


def check_card(number):
   
   
   numero = str(number)[::-1]
   print(numero)
   contadorpares=0
   sumador=0
   aux=0
   for i in range (0,len(numero),1):
      contadorpares=contadorpares+1
      aux=int(numero[i])
      if contadorpares%2==0: 
         aux=int(numero[i])*2
      if aux>=10: 
         aux=aux-9
      sumador=sumador+aux
   if sumador%10==0: return True
   else: return False