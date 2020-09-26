#1 Viết chương trình in ra màn hình dòng chữ "Xin chào...!"
print('*'*100)
print("Câu 1:")
print('-'*20,"Xin Chào...!",'-'*20)
print('*'*100)
print(" ")

#2 Viết chương trình nhập vào 2 số nguyên in ra màn hình tổng bình phương của 2 số nguyên đó. VD: S = a*a + b*b
print('*'*100)
print("Câu 2: ")
a=int(input('Nhập vào số nguyên thứ nhất: '))
b=int(input('Nhập vào số nguyên thứ hai: '))
print(f"Tổng bình phương của 2 số nguyên đó là:",a*a+b*b)
print('*'*100)
print(" ")

#3 Viết chương trình nhập vào tiền lương cơ bản, phụ cấp và số ngày đi làm trong tháng in ra màn hình Lương chính nhận được
print('*'*100)
print("Câu 3: ")
x=int(input('Tiền lương cơ bản là: '))
y=int(input('Tiền phụ cấp là: '))
z=int(input('Số ngày đi làm trong tháng là: '))
print(f"Lương chính nhận được là:",((x+y)/22)*z)
print('*'*100)
print(" ")

#4 Viết chương trình tính chu vi và diện tích hình tròn sau khi người dùng nhập chiều dài bán kính r. VD: CV = r*2*PI, DT = r*r*PI
print('*'*100)
print("Câu 4: ")
PI=float(3.14)
r=int(input('Nhập chiều dài bán kính r = '))
print(f"Chu vi hình tròn là:",r*2*PI)
print(f"Diện tích hình tròn là:",r*r*PI)
print('*'*100)
print(" ")

#5 Viết chương trình nhập vào một số gồm 2 chữ số, in ra màn hình số hàng đơn vị và hàng chục
print('*'*100)
print("Câu 5: ")
n=int(input('Nhập vào một số gồm 2 chữ số: '))
print(f"Chữ số hàng chục =",n//10)
print(f"Chữ số hàng đơn vị =",n%10)
print('*'*100)
print(" ")

#6 Viết chương trình nhập vào họ tên sinh viên, mssv, tuổi, sau đó cho biết họ tên sinh viên, mssv, tuổi là kiểu dữ liệu gì?
print('*'*100)
print("Câu 6: ")
x=input('Tên sinh viên: ')
print(">>>",type(x))
y=int(input('Mã số sinh viên: '))
print(">>>",type(y))
z=int(input('Tuổi: '))
print(">>>",type(z))
print('*'*100)
print(" ")

#7 Viết Chương trình nhập họ tên sinh viên đếm chiều dài chuỗi và in ra ký tự ở vị trí thứ nhất
print('*'*100)
print("Câu 7: ")
a=str(input('Nhập họ tên sinh viên: '))
print(f"Chiều dài của chuỗi là:",len(a))
print("Kỹ tự thứ nhất trong chuỗi là:",a[0])
print('*'*100)
print(" ")

#8 Viết chương trình nhập một số gồm 2 chữ số, in ra màn hình số đảo ngược 
print('*'*100)
print("Câu 8: ")
n=int(input('Nhập vào một số gồm 2 chữ số: '))
print(str(n)[::-1])
print('*'*100)
print(" ")
