#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from xmlrpc.client import boolean

for i in range (8):
    X= boolean(i //4)
    Y= boolean((i//2)%2)
    Z= boolean(i % 2)
    print(X," ",Y," ",Z,"->",not(X or Y or Z)==(not(X) and not(Y) and not(Z)))