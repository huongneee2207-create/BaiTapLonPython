import pandas as pd

# 1. Khởi tạo dữ liệu từ bảng của bạn
data = {
    "Mã Đơn": ["HD005", "HD006", "HD007", "HD008", "HD009", "HD010"],
    "Khu Vực (Quận)": ["Cầu Giấy", "Ba Đình", "Hà Đông", "Tây Hồ", "Đống Đa", "Nam Từ Liêm"],
    "Nhóm Sản Phẩm": ["Trang điểm (Make-up)", "Chăm sóc cơ thể", "Chăm sóc da (Skincare)", "Chăm sóc da (Skincare)", "Trang điểm (Make-up)", "Chăm sóc da (Skincare)"],
    "Loại Sản Phẩm": ["Cushion / Kem nền", "Sữa tắm / Dưỡng thể", "Nước tẩy trang", "Serum chống lão hóa", "Son môi", "Mặt nạ giấy"],
    "Phân Khúc": ["Tầm trung (Mid-end)", "Bình dân (Mass)", "Bình dân (Mass)", "Cao cấp (High-end)", "Bình dân (Mass)", "Bình dân (Mass)"],
    "Kênh Bán Hàng": ["Shopee", "Siêu thị", "TikTok Shop", "Website thương hiệu", "Shopee", "Cửa hàng offline"],
    "Số Lượng": [95, 200, 180, 30, 210, 500],
    "Doanh Thu (VNĐ)": [33250000, 30000000, 27000000, 45000000, 42000000, 15000000],
    "Đối Tượng Mua Chính": ["Khách hàng trẻ (Gen Z)", "Hộ gia đình", "Học sinh / Sinh viên", "Phụ nữ > 30 tuổi", "Học sinh / Sinh viên", "Khách hàng trẻ"]
}

# Chuyển đổi thành DataFrame
df = pd.DataFrame(data)

# Tính toán giá bán trung bình trên mỗi sản phẩm (Đơn giá)
df['Giá Bán Trung Bình'] = df['Doanh Thu (VNĐ)'] / df['Số Lượng']

print("=========================================")
print("        BÁO CÁO PHÂN TÍCH DỮ LIỆU        ")
print("=========================================\n")

# 2. Tổng quan chung
tong_doanh_thu = df['Doanh Thu (VNĐ)'].sum()
tong_so_luong = df['Số Lượng'].sum()
print(f"-> Tổng doanh thu hệ thống: {tong_doanh_thu:,} VNĐ")
print(f"-> Tổng số lượng sản phẩm tiêu thụ: {tong_so_luong:,} sản phẩm\n")

# 3. Phân tích theo Nhóm Sản Phẩm
print("--- DOANH THU THEO NHÓM SẢN PHẨM ---")
nhom_sp = df.groupby("Nhóm Sản Phẩm")["Doanh Thu (VNĐ)"].sum().sort_values(ascending=False)
for k, v in nhom_sp.items():
    print(f"* {k}: {v:,} VNĐ")
print()

# 4. Phân tích theo Kênh Bán Hàng
print("--- DOANH THU THEO KÊNH BÁN HÀNG ---")
kenh_ban = df.groupby("Kênh Bán Hàng")["Doanh Thu (VNĐ)"].sum().sort_values(ascending=False)
for k, v in kenh_ban.items():
    print(f"* {k}: {v:,} VNĐ")
print()

# 5. Hiệu suất dòng sản phẩm (Đơn giá cao nhất/thấp nhất)
print("--- GIÁ BÁN TRUNG BÌNH CỦA CÁC LOẠI SẢN PHẨM ---")
for index, row in df.iterrows():
    print(f"* {row['Loại Sản Phẩm']} ({row['Phân Khúc']}): {int(row['Giá Bán Trung Bình']):,} VNĐ/sản phẩm")