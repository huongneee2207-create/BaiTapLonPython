def tinh_giai_thua(n):
    if n < 0:
        return "Không tính được giai thừa cho số âm"
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i  # Tương đương giai_thua = giai_thua * i
    return giai_thua


# Chạy thử với n = 5
print(f"Giai thừa của 5 là: {tinh_giai_thua(5)}")
def tinh_trung_binh(day_so):
    if len(day_so) == 0:
        return 0
    tong = sum(day_so)
    trung_binh = tong / len(day_so)
    return trung_binh


# Chạy thử với một dãy số mẫu
cac_so = [10, 20, 30, 40, 50]
print(f"Giá trị trung bình của dãy là: {tinh_trung_binh(cac_so)}")
def tinh_loi_nhuan_12_thang(so_tien_goc, lai_suat_nam):
    # lai_suat_nam nhập vào dạng số thập phân, ví dụ 6% thì nhập 0.06
    lai_suat_thang = lai_suat_nam / 12
    so_tien_hien_tai = so_tien_goc

    print(f"\n--- KẾ HOẠCH TÍCH LŨY TRONG 12 THÁNG ---")
    for thang in range(1, 13):
        tien_lai_thang = so_tien_hien_tai * lai_suat_thang
        so_tien_hien_tai += tien_lai_thang
        print(f"Tháng {thang:02d}: Tiền tích lũy tổng = {so_tien_hien_tai:,.0f} VNĐ")

    loi_nhuan_rong = so_tien_hien_tai - so_tien_goc
    return so_tien_hien_tai, loi_nhuan_rong


# Ví dụ: Gửi gốc 100,000,000 VNĐ với lãi suất 6.5%/năm (0.065)
goc = 100000000
lai = 0.065
tong_tien, loi_nhuan = tinh_loi_nhuan_12_thang(goc, lai)
print(f"\n=> Sau 12 tháng, tổng số tiền nhận về: {tong_tien:,.0f} VNĐ")
print(f"=> Lợi nhuận ròng kiếm được: {loi_nhuan:,.0f} VNĐ")