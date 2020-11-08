#Bài 10.1 Viết chương trình tạo một tập tin văn bản với tên và nội dung do người dùng chỉ định.
print('-'*20,"Bài 1",'-'*20)
a = open("abc.txt", 'w', encoding='utf-8')
a.write("Hello Word\n")
a.close()
print('*'*100)
print(" ")

#Bài 10.2 Viết chương trình đọc nội dung của một tập tin văn bản cho trước. Tên tập tin do người dùng chỉ định. Trong tập tin có nhiều dòng chữ.
print('-'*20,"Bài 2",'-'*20)
f = open("abc.txt",'r',encoding='Utf8')
str = f.read(5)
print ('Noi dung file cua ban la:\n', str)
print('*'*100)
print(" ")

#Bài 10.3 Viết chương trình đọc một danh sách các số được ghi trong một tập tin văn bản, với mỗi số cách nhau bằng dấu khoảng trắng. Hiển thị danh sách ra màn hình và tính tổng các số đó.
print('-'*20,"Bài 3",'-'*20)
f = open("abc1.txt",'r' , encoding='utf-8' )
a=f.read()
print(a)
chuoi1=a.split(" ")
kq=0
for i in range (len(chuoi1)):
    kq=kq + float(chuoi1[i])
print("kết quả tổng các số trong danh sách: ",kq)
print('*'*100)
print(" ")