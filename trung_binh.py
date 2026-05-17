def tinh_trung_binh(danh_sach):
    if len(danh_sach) == 0:
        return 0
    return sum(danh_sach) / len(danh_sach)

try:
    chuoi_nhap = input("Nhập dãy số, cách nhau bằng dấu phẩy (Ví dụ: 5,10,15,20): ")
    day_so = [float(x.strip()) for x in chuoi_nhap.split(",")]
    
    ket_qua = tinh_trung_binh(day_so)
    print(f"Dãy số của bạn: {day_so}")
    print(f"Giá trị trung bình của dãy số là: {ket_qua}")
except ValueError:
    print("Định dạng nhập không hợp lệ. Vui lòng nhập số và cách nhau bằng dấu phẩy.")