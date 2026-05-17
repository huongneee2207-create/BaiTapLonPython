def tinh_loi_nhuan_12_thang(so_tien_goc, lai_suat_nam):
    lai_suat_thang = (lai_suat_nam / 100) / 12
    so_tien_hien_tai = so_tien_goc
    
    print("\n--- Tiến trình tăng trưởng tài sản qua 12 tháng ---")
    for thang in range(1, 13):
        tien_lai_thang = so_tien_hien_tai * lai_suat_thang
        so_tien_hien_tai += tien_lai_thang
        print(f"Tháng {thang:2d}: Số tiền tổng = {so_tien_hien_tai:,.2f} VND (Tiền lãi tháng: {tien_lai_thang:,.2f} VND)")
    
    loi_nhuan_thuan = so_tien_hien_tai - so_tien_goc
    return so_tien_hien_tai, loi_nhuan_thuan

try:
    goc = float(input("Nhập số tiền ban đầu (VND): "))
    lai_suat = float(input("Nhập tỷ lệ lãi suất năm (ví dụ: 6.5 cho 6.5%): "))
    
    tong_tien, loi_nhuan = tinh_loi_nhuan_12_thang(goc, lai_suat)
    
    print("\n--- KẾT QUẢ SAU 12 THÁNG ---")
    print(f"Số tiền gốc ban đầu: {goc:,.2f} VND")
    print(f"Tổng số tiền nhận được (cả gốc lẫn lãi): {tong_tien:,.2f} VND")
    print(f"Tổng lợi nhuận thuần: {loi_nhuan:,.2f} VND")
except ValueError:
    print("Vui lòng nhập số hợp lệ!")