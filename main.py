# import จาก value_operations.py
import value_operations

print(__name__)

if __name__ == '__main__':
    results = value_operations.swap(5, 1)
    print(results)

# เรียกใช้ function ที่ def ไว้
results = value_operations.swap(5, 1)
print(results)

# import แบบนี้ได้เหมือนกัน ถ้าใช้แบบนี้ไม่ต้องใส่ value_operations นำหน้า
# from value_operations import swap
# results = swap(5, 1)
# print(results)


# Type Number
number = 4
print(number)

# Type String
name = 'Peng'
print(name)

# If
if number == 4:
    print('Number is 4')
    print('inside if')

print('outside if')

# List
fruits = ['Orange', 'Apple', 'Durian'] # iterable
print(fruits[0])

# Loop วิธีนี้ ในภาษาคน อ่านยากกว่าวิธีด้านล่าง
for i in range(0,len(fruits)):
    print(i, fruits[i])

# Loop วิธีนี้ อ่านง่ายกว่า
for fruit in fruits:
    print(fruit)

# เอา Index มาด้วย
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Tuple ต่างจาก List ตรงเปลี่ยนค่าข้างในไม่ได้
company = ('GitHub', 'SF, USA')
# ใส่ 2 ตัวแบบนี้ได้ค่าตามตำแหน่งเลย
company_name, location = company
print(company_name, location)

# ใช้สลับตัวแปรแบบนี้ได้
a = 5
b = 10
print(a, b)

a, b = b, a
print(a, b)

# create function
# def swap(a, b):
#     return b, a
# ย้ายไปไว้ที่ value_operations.py แล้ววนกลับมาเรียกใช้ตอนต้นไฟล์นี้แทน

# print(swap(1, 2))
print(value_operations.swap(1, 2))


# สร้าง function รับเลข
1. ถ้าหาร 3 ลงตัว, ได้คำว่า Fizz
2. ถ้าหาร 5 ลงตัว, ได้คำว่า Buzz
3. ถ้าหาร 3 และ 5 ลงตัว, ได้คำว่า FizzBuzz
4. ถ้าไม่ตกกรณีไหนเลย ได้เลข input นั้นๆ

