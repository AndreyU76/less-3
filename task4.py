Определить, какое число в массиве встречается чаще всего

from random import random
N = 10
arr = [0] * N
for a in range(N):
    arr[a] = int(random() * 20)
print(arr)
 
num = arr[0]
max_frq = 1
for a in range(N-1):
    frq = 1
    for k in range(a+1,N):
        if arr[a] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[a]
 
if max_frq > 1:
    print(max_frq, 'раз(a) повторяется число ', num)
else:
    print('Элементы уникальны')
