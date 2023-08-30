# สร้าง function รับเลข
# 1. ถ้าหาร 3 ลงตัว, ได้คำว่า Fizz
# 2. ถ้าหาร 5 ลงตัว, ได้คำว่า Buzz
# 3. ถ้าหาร 3 และ 5 ลงตัว, ได้คำว่า FizzBuzz
# 4. ถ้าไม่ตกกรณีไหนเลย ได้เลข input นั้นๆ


def fizzbuzz(number):
    if number % 15 == 0:
        print('FizzBuzz')
    elif number % 3  == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

    python -m venv /path/to/new/virtual/environment