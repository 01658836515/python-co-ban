#1 : 1.	Xuất ra màn hình N lần câu thông báo “Hello Python”
print('-'*20,"Bài 1",'-'*20)
n = int(input('Nhap n = '))
for n in range (0,n,1):
    print("Hello Python")
print('*'*100)
print(" ")

#2 : 2.	Tính tổng từ 1 cho đến N
print('-'*20,"Bài 2",'-'*20)
n = int(input('Nhap N = '))
sum = 0
for i in range (1,n+1):
    sum += i
print("Tong tu 1 den", n ,"la: ", sum )
print('*'*100)
print(" ")

#3 : 3.	Tính tổng các số CHẴN nằm trong đoạn từ 0 đến N
print('-'*20,"Bài 3",'-'*20)
n = int(input('Nhap N = '))
chan=0
for i in range (0,n+1):
    if( i % 2 ==0 ):
        chan += i
        print (i)  
    else:
        print()
print("Tong cac so chan ", chan)
print('*'*100)
print(" ")

#4.	Tính tổng các số LẼ nằm trong đoạn từ 0 đến N
print('-'*20,"Bài 4",'-'*20)
n =int(input('Nhap n= '))
le=0
for i in range (0,n+1):
    if(i % 2 !=0 ):
        le +=i
        print (i)
    else:
        print()
print("Tong cac so le ", le)
print('*'*100)
print(" ")

#5.	Tính trung bình cộng các số trong mảng
print('-'*20,"Bài 5",'-'*20)
n = int(input('Nhap n= '))
tong=0
i=1
tongtrungbinh = int
for i in range(i,n+1):
    tong +=i
    print (tong)
tongtrungbinh = tong / n
print("Tong trung binh cong trong mang ", tongtrungbinh)
print('*'*100)
print(" ")

#6.	Tính tổng giá trị từ 1 đến N, nếu chạy đến số 13 thì không chạy nữa và xuất kết quả
print('-'*20,"Bài 6",'-'*20)
n = int(input('Nhap n= '))
tong = 0
for i in range (1,n+1):
    if (i == 13 ):
        break
    else:
        tong += i
        print(i, tong)
print (tong)
print('*'*100)
print(" ")

#7.	Tính tổng giá trị từ 1 đến N, riêng số 17 thì bỏ qua
print('-'*20,"Bài 7",'-'*20)
n= int(input('Nhap n= '))
tong= 0
for i in range (1,n+1):
    if(i == 17):
        continue
         
    else:
        tong += i
        print(i, tong)
print (tong)
print('*'*100)
print(" ")

#Bài tập về nhà 01
print('-'*20,"Bài tập về nhà 1",'-'*20)
from math import sqrt

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            print("Phương trình có 1 nghiệm x = ", -c / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
    else:
        print("Phương trình có 2 nghiệm phân biệt")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))
print('*'*100)
print(" ")

#Bài tập về nhà 02
print('-'*20,"Bài tập về nhà 2",'-'*20)
from math import sqrt
s=1
x=int(input("nhap x= "))
n=int(input("nhap n= "))
for i in range (1,n+1):
    s1= s  + pow(x,i)
print("kết quả của S1 là: ", s1  )
for i in range (0,n+1):
    s2=s + ((-1)* pow(x,i) )
print("kết quả của S2 là: ",s2)
print('*'*100)
print(" ")

#Bài tập về nhà 03
print('-'*20,"Bài tập về nhà 3",'-'*20)
n = int(input("Nhap n= "))
total = 0
while (n):
    if(n>100):
        print("Nhap lai n") 
        break
    if(n<100):
        while (n):
            total = total + n % 10
            n = int(n / 10)

print(total)
print('*'*100)
print(" ")

#Bài tập về nhà 04
print('-'*20,"Bài tập về nhà 4",'-'*20)
from math import sqrt
a=int(input("nhap a= "))
b=int(input("nhap b= "))
c=int(input("nhap c= "))
if( (a<b+c)&(b<a+c)&(c<a+b) ):
    if( (a*a==b*b+c*c) | (b*b==a*a+c*c) | (c*c== a*a+b*b)):
        print("đây là hình tam giác vuông")
    else:
       print("đây là hình tam giác nhưng không phải là hình tam giác vuông")
else:
    print("đây không phải hình tam giác")
print('*'*100)
print(" ")