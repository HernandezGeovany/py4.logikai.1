"""1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
"""
szam = int(input('Adj meg egy számot! '))
if szam >0 and szam %2 == 0 :
  print ("páros és pozitiv") 
elif szam <0 and not szam %2 == 0 :
  print("negativ és minusz")
 
elif szam <0 and szam %2 == 0:
  print ("negativ de páros")
elif szam >0 and not szam %2 == 0:
  print("pozitiv de páratlan ")