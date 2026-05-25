import random

name_patient = input("Nhập tên bệnh nhân: ")
clinic = input("Phòng khám chỉ định: ")
id_patient = random.randint(1000,9999)
print("| Bệnh Nhân: " + name_patient +"|Mã BA: BA"+ str(id_patient) +" | Chuyển tới:"+ clinic +" |")
