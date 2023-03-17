# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n_length = int(input('Введите длину: '))
m_width = int(input('Введите ширину: '))
k_slices = int(input('Введите колличество долек: '))

if (((  k_slices % n_length) == 0) or (( k_slices % m_width) == 0)):
    print(f'{n_length} {m_width} {k_slices}-> Yes')
else:
    print(f'{n_length} {m_width} {k_slices}-> No')
