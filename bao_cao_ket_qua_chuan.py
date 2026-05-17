# =========================================
#         BÁO CÁO PHÂN TÍCH DỮ LIỆU        
# =========================================

# -> Tổng doanh thu hệ thống: 192,250,000 VNĐ
# -> Tổng số lượng sản phẩm tiêu thụ: 1,215 sản phẩm

# --- DOANH THU THEO NHÓM SẢN PHẨM ---
# * Chăm sóc da (Skincare): 87,000,000 VNĐ
# * Trang điểm (Make-up): 75,250,000 VNĐ
# * Chăm sóc cơ thể: 30,000,000 VNĐ

# --- DOANH THU THEO KÊNH BÁN HÀNG ---
# * Shopee: 75,250,000 VNĐ
# * Website thương hiệu: 45,000,000 VNĐ
# * Siêu thị: 30,000,000 VNĐ
# * TikTok Shop: 27,000,000 VNĐ
# * Cửa hàng offline: 15,000,000 VNĐ

# --- GIÁ BÁN TRUNG BÌNH CỦA CÁC LOẠI SẢN PHẨM ---
# * Cushion / Kem nền (Tầm trung (Mid-end)): 350,000 VNĐ/sản phẩm
# * Sữa tắm / Dưỡng thể (Bình dân (Mass)): 150,000 VNĐ/sản phẩm
# * Nước tẩy trang (Bình dân (Mass)): 150,000 VNĐ/sản phẩm
# * Serum chống lão hóa (Cao cấp (High-end)): 1,500,000 VNĐ/sản phẩm
# * Son môi (Bình dân (Mass)): 200,000 VNĐ/sản phẩm
# * Mặt nạ giấy (Bình dân (Mass)): 30,000 VNĐ/sản phẩm

def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    giai_thua = 1
    for i in range(2, n + 1):
        giai_thua *= i
    return giai_thua

def tinh_trung_binh(day_so):
    if len(day_so) == 0:
        return 0
    return sum(day_so) / len(day_so)

def tinh_loi_nhuan_sau_12_thang(tien_ban_dau, lai_suat_thang):
    """
    tien_ban_dau: Số vốn gốc
    lai_suat_thang: Tỷ lệ lãi suất mỗi tháng (ví dụ 0.01 cho 1%)
    """
    so_thang = 12
    # Giả sử đây là công thức tính lãi kép đơn giản sau 12 tháng
    return tien_ban_dau * (1 + lai_suat_thang)**so_thang

if __name__ == "__main__":
    so = 5
    print(f"Giai thừa của {so} là: {tinh_giai_thua(so)}")
    
    danh_sach = [15, 20, 25, 30, 35]
    print(f"Giá trị trung bình của dãy số là: {tinh_trung_binh(danh_sach)}")
