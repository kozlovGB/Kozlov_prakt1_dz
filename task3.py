#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)
x=int(input('Введите координату x: '))
y=int(input('Введите координату y: '))
if x>0 and y>0:
    print(x,y,"->",1)
elif x<0 and y>0:
    print(x,y,"->",2)
elif x<0 and y<0:
    print(x,y,"->",3)
elif x>0 and y<0:
    print(x,y,"->",1)
elif x==0 and y!=0:
    print("ТОчка находится на оси Y")
elif x!=0 and y==0: # Я понимаю, что здесь можно просто прописать else
    print("ТОчка находится на оси X")