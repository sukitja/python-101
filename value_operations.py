def swap(a, b):
    return b, a


# การใส่ if นี้ไว้จะทำให้เวลา import ไปใช้ในที่อื่น ไม่ execute print(swap(100, 999))
# ถ้าไม่ใส่ไว้จะ execute ทุกครั้งที่ import ไป
if __name__ == '__main__':
    print(swap(100, 999))