#b1.a
print('-'*20,"Bài 1A",'-'*20)
n = int(input("Nhập N = "))
def tong(n):
    arr = [] 
    tong = 0 
    for i in range (n):
        x = input(f"Input ITEM[{i}]: ")
        arr.append(int(x))
        tong+=arr[i]
    return tong
print("Tổng các phần tử là: ",tong(n))
print('*'*100)
print(" ")

#b1.b
print('-'*20,"Bài 1B",'-'*20)
n = int(input("Nhập N = "))
def tich(n):
    arr = [] 
    tich = 1
    for i in range (n):
        x = input(f"Input ITEM[{i}]: ")
        arr.append(int(x))
        tich*=arr[i]
    return tich
print("Tích các phần tử là: ",tich(n))
print('*'*100)
print(" ")

#b1.c
print('-'*20,"Bài 1C",'-'*20)
n = int(input("Nhập N = "))
def max(n):
    arr = []
    
    for i in range (n):
        x = input(f"Input ITEM[{i}]: ")
        arr.append(int(x))
    ma = arr[0]
    for i in range (1, len(arr)):
        if(arr[i] > ma):
            ma=arr[i]
    return ma
print("Số lớn nhất là: ",max(n))

#b1.d
print('-'*20,"Bài 1C",'-'*20)
n = int(input("Nhập N = "))
def max(n):
    arr = []
    
    for i in range (n):
        x = input(f"Input ITEM[{i}]: ")
        arr.append(int(x))
    ma = arr[0]
    for i in range (1, len(arr)):
        if(arr[i] < ma):
            ma=arr[i]
    return ma
print("Số nhỏ nhất là: ",max(n))