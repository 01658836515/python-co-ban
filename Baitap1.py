#Bài tập về nhà 1
print('-'*20,"Bài 1",'-'*20)
n = int(input("nhap n= "))
def daonguoc(n):
    return(str(n)[::-1])
print(daonguoc(n))
print('*'*100)
print(" ")

#Bài tập về nhà 2
print('-'*20,"Bài 2",'-'*20)
n = int(input("nhap n= "))
def tinhgiaithua(n):
    if n == 0:
        return 1
    return n * tinhgiaithua(n - 1)
print("Giai thua của ",n," là ",tinhgiaithua(n))
print('*'*100)
print(" ")

#Bài tập về  nhà 3
print('-'*20,"Bài 3",'-'*20)
n = int(input("nhap n= "))
s=0
for i in range (1,n+1):
    s= s + pow(i,3)
    print(s)
print('*'*100)
print(" ")

#bài tập về nhà 4
print('-'*20,"Bài 4",'-'*20)
def tong(n):
    s=0
    for i in range (0,n+1):
        if(i % 2 == 0):
            
            s+=i
    
    return s

n=int(input("nhap n= "))
print("tong cac so le ",tong(n))
print('*'*100)
print(" ")

#bài tập về nhà 5
print('-'*20,"Bài 5",'-'*20)
def tong(n):
    s=0
    for i in range (0,n+1):
        if(i % 2 == 0):
            s+=i
    print("tong cac so chan la: ", s)
    return 

n=int(input("nhap n= "))
print(tong(n))
print('*'*100)
print(" ")

#bài tập về nhà 6
print('-'*20,"Bài 6",'-'*20)
def songuyento(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return "là số nguyên tố"
    return "không phải là số nguyên tố"
n=int(input("nhap n= "))
print(songuyento(n))
print('*'*100)
print(" ")

#bài tập về nhà 7
print('-'*20,"Bài 7",'-'*20)
import math
n=int(input("nhap n= "))
x = math.sqrt(n)
def sochingphuong(n):
    if(x * x == n):
        return "là số chính phương"
    else:
        return  "không phải là số chính phương"
print(n,sochingphuong(n))
print('*'*100)
print(" ")

#bài tập về nhà 8
print('-'*20,"Bài 8",'-'*20)
def songuyento(n):
    count = 0
    s =0 
    for i in range(1, n + 1):
        if n % i == 0:
            s=s+i
            count += 1
    if count == 2:
        return s
    return "không phải là số nguyên tố"
n=int(input("nhap n= "))
print("tong cac so nguyen to la: ",songuyento(n))
print('*'*100)
print(" ")

#bài tập về nhà 9
print('-'*20,"Bài 9",'-'*20)
n= int(input("nhap n= "))
def bangcuuchuong(n):

    for j in range(1,10):
        s = n * j
        print(n, "*" ,j, "=" ,s)
    return s
print(bangcuuchuong(n))
print('*'*100)
print(" ")

#bài tập về nhà 10
print('-'*20,"Bài 10",'-'*20)
def fibonacci(n):
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n=int(input("nhap n = "))
print(fibonacci(n))
print('*'*100)
print(" ")