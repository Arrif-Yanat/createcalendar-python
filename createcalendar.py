import calendar  # นำเข้าโมดูล calendar

# ฟังก์ชันแสดงเมนูหลัก
def display_menu():
    print("โปรแกรมสร้างปฏิทิน 📅")
    print("1. แสดงปฏิทินทั้งปี")
    print("2. แสดงปฏิทินรายเดือน")
    print("3. ออกจากโปรแกรม")

# ฟังก์ชันหลัก
def main():
    while True:
        display_menu()  # แสดงเมนู
        choice = input("เลือกเมนู (1-3): ")  # รับอินพุตจากผู้ใช้
        
        if choice == '1':  # แสดงปฏิทินทั้งปี
            year = int(input("ป้อนปีที่ต้องการ (เช่น 2024): "))
            print(calendar.TextCalendar().formatyear(year))  # แสดงปฏิทินทั้งปี
        
        elif choice == '2':  # แสดงปฏิทินรายเดือน
            year = int(input("ป้อนปีที่ต้องการ (เช่น 2024): "))
            month = int(input("ป้อนเดือนที่ต้องการ (1-12): "))
            if 1 <= month <= 12:  # ตรวจสอบว่าเดือนอยู่ในช่วง 1-12
                print(calendar.TextCalendar().formatmonth(year, month))  # แสดงปฏิทินรายเดือน
            else:
                print("โปรดป้อนเดือนที่ถูกต้อง (1-12)!")
        
        elif choice == '3':  # ออกจากโปรแกรม
            print("ขอบคุณที่ใช้โปรแกรม!")
            break
        
        else:
            print("โปรดเลือกเมนูที่ถูกต้อง (1-3)")

# เริ่มโปรแกรม
main()