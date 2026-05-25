import random


name= input("Nhập tên bệnh nhân: ")
gender = input("Nhập Giới Tính: ")
year = int(input("Nhập năm sinh: "))
phone_number = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
initial_symptoms = input("Nhập triệu chứng ban đầu: ")
examination_fee = float(input("Nhập chi phí khám: "))



random_number = random.randint(100,999) 
patient_id = f"BN{year}{random_number}"


print("\n=====Thẻ bệnh nhân====")
print("Mã bệnh nhân: ",patient_id)
print("Tên Bệnh Nhân: ",name)
print("Giới tính: ",gender)
print("Năm sinh: ",year)
print("Số điện thoại: ",phone_number)
print("Email: ",email)
print("Triệu chứng ban đầu: ",initial_symptoms)
print("Chi phí khám: ",examination_fee)