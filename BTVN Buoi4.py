#Bài 1 : Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
print('-'*20,"Bài 1",'-'*20)
chuoi=input("nhap chuoi:")
def manual_replace(s, char, index):
    return s[:index] + char + s[index +1:]
print(manual_replace(chuoi,"$", 0))
print('*'*100)
print(" ")

#Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
print('-'*20,"Bài 2",'-'*20)
chuoi=input("nhap chuoi:")
def remove_char_m(str, n):
      phan_dau=str[:n] 
      phan_cuoi=str[n+1:]
      return phan_dau + phan_cuoi
print(remove_char_m(chuoi,int(input("thu tu muon xoa:"))))
print('*'*100)
print(" ")

#Bài 03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
print('-'*20,"Bài 3",'-'*20)
chuoi = input("nhap chuoi:")
def even_values_string(str):
  ketqua = "" 
  for i in range(len(str)):
    if i % 2 != 0:
      ketqua = ketqua + str[i]
  return ketqua
print(even_values_string(chuoi))
print('*'*100)
print(" ")

#Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào ___ nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
print('-'*20,"Bài 4",'-'*20)
chuoi = input("nhap chuoi:")
def dau_va_duoi(str):
  if len(str) < 2:
    return "chuoi rong"
  return str[0:2] + str[-2:]
print(dau_va_duoi(chuoi))
print('*'*100)
print(" ")

#Bài 05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
print('-'*20,"Bài 5",'-'*20)
chuoi = input("nhap chuoi:")
print("ki tu lon nhat cua chuoi:", max(chuoi))
print("ki tu nho nhat cua chuoi:", min(chuoi))
print('*'*100)
print(" ")

#Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
print('-'*20,"Bài 6",'-'*20)
chuoi = input("nhap chuoi:")
print(chuoi.swapcase())
print('*'*100)
print(" ")