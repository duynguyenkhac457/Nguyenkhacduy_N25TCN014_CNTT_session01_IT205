id_patient = input("Nhập mã bệnh Nhân (3 số): ")
body_temperature = float(input("Nhập nhiệt độ cơ thể: "))
heart_rate = int(input("Nhập nhịp tim: "))


print("\n---KẾT QUẢ CHUẨN HÓA DỮ LIỆU---")
print("Mã Bệnh Nhân: BN",id_patient)
print("Nhiệt độ: ",str(body_temperature) + " độ C")
print("==> Kiểu dữ liệu hệ thồng ghi nhận: ",type(body_temperature))
print("Nhịp tim: ",str(heart_rate) + " nhịp/phút")
print("==> Kiểu dữ liệu hệ thống ghi nhận: ",type(heart_rate))
print("------------------------------------")
print("Thông báo. Dữ liệu hợp lệ. Màng hình Monitor đã sẵn dàng kết nối!")