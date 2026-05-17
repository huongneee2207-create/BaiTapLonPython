def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    giai_thua = 1
    for i in range(2, n + 1):
        giai_thua *= i
    return giai_thua

so = 5
print(f"Giai thừa của {so} là: {tinh_giai_thua(so)}")
def tinh_trung_binh(day_so):
    if len(day_so) == 0:
        return 0
    return sum(day_so) / len(day_so)

danh_sach = [15, 20, 25, 30, 35]
print(f"Giá trị trung bình của dãy số là: {tinh_trung_binh(danh_sach)}")
def tinh_loi_nhuan_sau_12_thang(tien_ban_dau, lai_suat_thang):
    """
    tien_ban_dau: Số vốn gốc
    lai_suat_thang: Tỷ lệ lãi suất mỗi tháng (ví dụ 0.01 cho 1%)
    """
    so_thang = 12
    # Tính tổng tiền thu về sau 12 tháng (Gốc + Lãi)
    tong_tien = tien_ban_dau * ((1 + lai_suat_thang) ** so_thang)
    
    # Tính riêng phần lợi nhuận (Lãi)
    loi_nhuan = tong_tien - tien_ban_dau
    
    return tong_tien, loi_nhuan

# Giả sử vốn ban đầu là 10 triệu VNĐ, lãi suất 1.5%/tháng
von = 10000000 
lai_suat = 0.015 

tong_ket, tien_lai = tinh_loi_nhuan_sau_12_thang(von, lai_suat)

print(f"--- KẾT QUẢ ĐẦU TƯ SAU 12 THÁNG ---")
print(f"Số tiền gốc: {von:,.0f} VNĐ")
print(f"Lợi nhuận (Tiền lãi): {tien_lai:,.0f} VNĐ")
print(f"Tổng tiền nhận được: {tong_ket:,.0f} VNĐ")