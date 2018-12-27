 В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве
 
 from random import random
N = 10
arr = []
for a in range(N):
        arr.append(int(random() * 200) - 70)
print(arr)
 
a = 0
index = -1
while a < N:
        if arr[a] < 0 and index == -1:
                index = a
        elif arr[a] < 0 and arr[a] > arr[index]:
                index = a
        a += 1
 
print('Номер элемента :' , index+1,'Максимальное отрицательное число :', arr[index])
