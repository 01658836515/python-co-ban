#In thông tin sinh viên
print('*'*100)
teacher = "Nguyễn Minh Tân"
name = "Nguyễn Minh Khánh"
mssv = "1813020024"
age = "22"
lop = "12MMC"
print('-'*20,"Thông Tin Sinh Viên",'-'*20)
print("Hello thầy {teacher}!  Em là: {name} - MSSV: {mssv} - tuổi: {age} - Lớp: {lop}") 
print('*'*100)
print(" ")

#Bài 1
#Viết Chương trình nhập vào 2 số nguyên, in ra màn hình tổng bình phương của 2 số nguyên đó
print('*'*100)
print("Bài 1: ")
a=int(input('Số nguyên thứ nhất: '))
b=int(input('số nguyên thứ hai:' ))
s=a*a+b*b
print(f'Tổng bình phương của 2 số nguyên đó là: {s}')
print('*'*100)
print(" ")

#Bài 2
#viết chương trình nhập vào tiền lương cơ bản, phụ cấp và số ngày đi làm trong  tháng, in ra màn hình lương chính nhận được theo công thức:
#Nhập tiền lương cơ bản, phụ cấp và số ngày đi làm. Lương chính = ((lương cơ bản + phụ cấp)/22) * số ngày đi làm
print('*'*100)
print("Bài 2:")
x=int(input('Tiền lương cơ bản: '))
#print(type(x))
#print(f'Tiền lương cơ bản là {x}')
y=int(input('Tiền phụ cấp: '))
#print(type(y))
#print(f'Tiền phụ cấp là: {y} ')
z=int(input('Số ngày đi làm: '))
#print(type(z))
#print(f'Số ngày đi làm là: {z}')
lc=((x+y)/22)*z
print(f'Lương chính là: {lc}')
#print(type(lc))
print('*'*100)
print(" ")

#Bài 3
#Viết chương trình tính chu vi diện tích hình tròn sau khi người dùng nhập chiều dài bán kính (r)
#Chu vi = r * 2 * PI. Diện tích = r * r * PI
print('*'*100)
print("Bài 3")
PI=float(3.14)
#print("PI",type(PI))
r=int(input('Bán kính đường tròn: '))
#print(type(r))
cv=r*2*PI
print(f'Chu vi đường tròn là: {cv}')
#print(type(cv))
dt=r*r*PI
print(f'Diện tích đường tròn là: {dt}')
#print(type(dt))
print('*'*100)
print(" ")