print('Петя загадай 2 числа')
a= int(input('Число А  '))
b= int(input('Число B '))

s=a+b
p=a*b

print(f"Катя вот тебе 2 подсказки,сумма этих чисел {s},а их произвидение {p}")

f=1000
i=0
j=0
while i<f:
    while j<f:
        if(i+j==s and i*j==p):
            break
        j+=1
    if (i+j==s and i*j==p):
        print(f'Катя ответила,что первое число это {i}, 30а втрое {j}')
        break
    j=0
    i+=1