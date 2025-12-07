# ---------------------------------------------------------
        # ตัวอย่างโปรแกรมคัดกรองชื่อผลไม้ที่มีตัวอักษร 'a'
# ---------------------------------------------------------

# รายการชื่อผลไม้
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

def filter_fruits_with_a(fruit_list):
    """
    รับลิสต์ผลไม้ และคืนค่าเฉพาะรายการที่มีตัวอักษร 'a'
    """
    result = []

    for item in fruit_list:
        # ตรวจว่ามีตัว 'a' อยู่ในชื่อผลไม้หรือไม่
        if 'a' in item:
            result.append(item)

    return result


# เรียกใช้งานฟังก์ชัน
selected_fruits = filter_fruits_with_a(fruits)

# แสดงผลลัพธ์
print("ผลไม้ที่มีตัวอักษร 'a' ได้แก่:", selected_fruits)
