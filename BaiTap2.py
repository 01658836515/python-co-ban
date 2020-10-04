#Bai tap 1: Max and Min
print('-'*20,"Bài 1",'-'*20)
b=int(input('Nhap 1 so B bat ki: '))
a=[3,4,1,8,23,16,18,98,b]
lon = 0
nho = b
for i in a:
    if i < nho:
        nho=i
for i in a:
    if i > lon:
        lon=i
print(lon,' La so Max')
print(nho,' La so Min')
print('*'*100)
print(" ")

#Bai tap 2: Dao chu
print('-'*20,"Bài 2",'-'*20)
n= str(input("nhap vao mot chuoi bat ki "))
def reverse_string(n):
    return(str(n)[::-1])
print(reverse_string(n))
print('*'*100)
print(" ")

#Bai tap 3: SO hoan hao
print('-'*20,"Bài 3",'-'*20)
n=int(input("nhap n="))
def is_perfect(n):
    Tong=0
    for i in range (1,n):
        if n % i == 0:
            Tong=Tong+i
    if Tong==n:
        return "là số hoàn hảo"
    else:
        return "không phải là số hoàn hảo"
print(n,is_perfect(n))
print('*'*100)
print(" ")

#Bai tap 4: So nguyen to
print('-'*20,"Bài 4",'-'*20)
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return ' La so nguyen to'
    return ' Khong phai so nguyen to'

n = int(input('Nhap vao so n = ' ))
print(n,is_prime(n))
print('*'*100)
print(" ")

#Bai tap 5: Chu viet hoa, Chu viet thuong
print('-'*20,"Bài 5",'-'*20)
def count_upper_lower(s):
    count_upper = 0
    count_lower = 0
    for c in s:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1
    print("Cau tu da nhap la: ",s)
    print("So chu in hoa: ", count_upper)
    print("So chu in thuong: ", count_lower)
print('*'*100)
print(" ")

#Bai tap 6: Kiểm tra chuổi str
print('-'*20,"Bài 6",'-'*20)
import string
gram = str(input("nhap mot chuoi bat kì"))
def is_pangram (gram):
       gram = gram.lower()
       gram_list_old = sorted([c for c in gram if c != ' '])
       gram_list = []
       for c in gram_list_old:
           if c not in gram_list:
               gram_list.append(c)
       if gram_list == list(string.ascii_lowercase): return True
       else: return False
print(is_pangram(gram))
print('*'*100)
print(" ")

#Bai tap 9 : In hoa sang thường và in thường thành hoa trong str
print('-'*20,"Bài 9",'-'*20)
s = str(input('Viet 1 cau tu: '))
count_upper_lower(s)

s = str(input('Nhap chu vao : '))
def count_upper_lower(s):
    print(s.upper())
count_upper_lower(s)
print('*'*100)
print(" ")


