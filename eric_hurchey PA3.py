#Eric Hurchey
#Programming Assignment #3
#2/17/2022
#

def main(): #overall main function
  total = int(input("How many cents "))
  print ("For", total, "cents change, I give")  
  greedy1(total)
  total = int(input("How many cents "))
  print ("For", total, "cents change, I give")
  greedy2(total)
  total = int(input("How many cents "))
  chaos(total)


def Printcoins1(q, d, n, p): #printing functions
    print (q, "quraters")
    print (d, "dimes")
    print (n, "nickels")
    print (p, "pennies")

def greedy1(total): #cents using >
  q = 0
  d = 0
  n = 0
  p = 0

  for i in range(3): #quarter
    if total >= 25 and total > 0:
      total = total - 25
      q = q + 1

  for i in range(2): #dime
    if total >= 10 and total > 0:
      total = total - 10 
      d = d + 1

  for i in range(1): #nickel
    if total >= 5 and total > 0:
      total = total - 5
      n = n + 1

  for i in range(4): #penny
    if total >= 1 and total > 0:
      total = total - 1
      p = p + 1
  Printcoins1(q, d, n, p)
  return q, d, n, p 

def greedy2(total): #quarter dime nickel and penny function using // and %
    q = total // 25
    d = (total % 25) // 10
    n = total % 25 % 10 // 5
    p = total % 5
    Printcoins2(q, d, n, p)
  
def Printcoins2(q, d, n, p): #printing functions
  if q != 0:
    print (q, "quraters")
  if d != 0:
    print (d, "dimes")
  if n != 0:
    print (n, "nickels")
  if p != 0:
    print (p, "pennies")

def chaos(total): #change chaotcally
  q = 0
  d = 0
  n = 0
  p = 0
  while total != 0:
    guess = guesscoin()
    if guess == 25 and total >= 25: #quarter
      q += 1
      total -= 25

    if guess == 10 and total >= 10: #dime
      d += 1
      total -= 10

    if guess == 5 and total >= 5: #nickel
      n += 1
      total -= 5

    if guess == 1 and total >= 1: #penny
      p += 1
      total -= 1
  Printcoins3(q, d, n, p)

def Printcoins3(q, d, n, p): #printing functions
  if q == 1:
    print(q, "quarter")
  else:
    print(q, "quarters")
  if d == 1:
    print(d, "dime")
  else:
    print(d, "dimes")
  if n == 1:
    print(n, "nickel")
  else:
    print(n, "nickels")
  if p == 1:
    print(p, "penny")
  else:
    print(p, "pennies")

import random

def guesscoin(): #dice rolling command 
  guess = random.randint(1,4)
  if guess == 4: #quarter
    return 25
  if guess == 3: #dime
    return 10
  if guess == 2: #nickel
    return 5
  if guess == 1: #penny
    return 1


main()
