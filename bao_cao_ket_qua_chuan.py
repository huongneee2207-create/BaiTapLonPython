import os
import pandas as pd

# 1. Khởi tạo tập dữ liệu đầy đủ từ 2 ảnh (10 dòng dữ liệu)
data = {
    "Khu Vực (Quận)": [
        "Cầu Giấy",
        "Đống Đa",
        "Hoàn Kiếm",
        "Hai Bà Trưng",
        "Cầu Giấy",
        "Ba Đình",
        "Hà Đông",
        "Tây Hồ",
        "Đống Đa",
        "Nam Từ Liêm",
    ],
    "Nhóm Sản Phẩm": [
        "Chăm sóc da (Skincare)",
        "Chăm sóc da (Skincare)",
        "Trang điểm (Make-up)",
        "Chăm sóc da (Skincare)",
        "Trang điểm (Make-up)",
        "Trang điểm (Make-up)",
        "Chăm sóc da (Skincare)",
        "Chăm sóc da (Skincare)",
        "Trang điểm (Make-up)",
        "Chăm sóc da (Skincare)",
    ],
    "Loại Sản Phẩm": [
        "Kem chống nắng",
        "Serum",
        "Son môi",
        "Kem chống nắng",
        "Cushion / Kem nền",
        "Cushion / Kem nền",
        "Nước tẩy trang",
        "Serum",
        "Son môi",
        "Serum",
    ],
    "Phân Khúc": [
        "Bình dân (Mass)",
        "Tầm trung (Mid-end)",
        "Cao cấp (High-end)",
        "Bình dân (Mass)",
        "Tầm trung (Mid-end)",
        "Bình dân (Mass)",
        "Bình dân (Mass)",
        "Cao cấp (High-end)",
        "Tầm trung (Mid-end)",
        "Bình dân (Mass)",
    ],
    "Kênh Bán Hàng": [
        "TikTok Shop",
        "Shopee",
        "Trung tâm thương mại",
        "Cửa hàng offline",
        "Shopee",
        "Trung tâm thương mại",
        "TikTok Shop",
        "Cửa hàng offline",
        "Shopee",
        "Cửa hàng offline",
    ],
    "Số Lượng": [150, 85, 40, 120, 95, 200, 180, 30, 210, 500],
    "Doanh Thu (VNĐ)": [
        37500000,
        42500000,
        36000000,
        24000000,
        33250000,
        30000000,
        27000000,
        45000000,
        42000000,
        15000000,
    ],
    "Đối Tượng Mua Chính": [
        "Học sinh / Sinh viên",
        "Nhân viên văn phòng",
        "Phụ nữ > 30 tuổi",
        "Sinh viên / Người đi làm",
        "Khách hàng trẻ",
        "Hộ gia đình",
        "Học sinh / Sinh viên",
        "Phụ nữ > 30 tuổi",
        "Học sinh / Sinh viên",
        "Khách hàng trẻ",
    ],
}

# Chuyển đổi thành DataFrame
df = pd.DataFrame(data)

# Tính giá bán trung bình thực tế của từng sản phẩm trên mỗi đơn
df["Giá Bán Trung Bình"] = df["Doanh Thu (VNĐ)"] / df["Số Lượng"]

# 2. Xử lý tính toán số liệu tổng hợp
tong_doanh_thu = df["Doanh Thu (VNĐ)"].sum()
tong_so_luong = df["Số Lượng"].sum()

doanh_thu_theo_nhom = (
    df.groupby("Nhóm Sản Phẩm")["Doanh Thu (VNĐ)"].sum().sort_values(ascending=False)
)
doanh_thu_theo_kenh = (
    df.groupby("Kênh Bán Hàng")["Doanh Thu (VNĐ)"].sum().sort_values(ascending=False)
)
doanh_thu_theo_quan = (
    df.groupby("Khu Vực (Quận)")["Doanh Thu (VNĐ)"].sum().sort_values(ascending=False)
)

# 3. Định dạng chuỗi văn bản báo cáo
report = f"""===========================================================================
               BÁO CÁO PHÂN TÍCH SỐ LIỆU KINH DOANH MỸ PHẨM
===========================================================================
[1] CHỈ SỐ TỔNG QUAN CHUNG:
---------------------------------------------------------------------------
* Tổng doanh thu hệ thống:       {tong_doanh_thu:,} VNĐ
* Tổng sản lượng tiêu thụ:       {tong_so_luong:,} sản phẩm
* Giá trị trung bình một sản phẩm: {int(tong_doanh_thu / tong_so_luong):,} VNĐ

[2] HIỆU SUẤT THEO NGÀNH HÀNG (NHÓM SẢN PHẨM):
---------------------------------------------------------------------------
"""
for k, v in doanh_thu_theo_nhom.items():
    report += f"- {k:<25}: {v:>12,} VNĐ ({v/tong_doanh_thu*100:.1f}%)\n"

report += "\n[3] HIỆU SUẤT DOANH THU THEO KÊNH BÁN HÀNG:\n---------------------------------------------------------------------------\n"
for k, v in doanh_thu_theo_kenh.items():
    report += f"- {k:<25}: {v:>12,} VNĐ ({v/tong_doanh_thu*100:.1f}%)\n"

report += "\n[4] TỐP KHU VỰC ĐÓNG GÓP DOANH THU CAO NHẤT:\n---------------------------------------------------------------------------\n"
for k, v in doanh_thu_theo_quan.items():
    report += f"- Quận {k:<20}: {v:>12,} VNĐ\n"

# 4. In trực tiếp ra Terminal
print(report)

# 5. Xuất file text tự động
with open("ket_qua_phan_tich.txt", "w", encoding="utf-8") as f:
    f.write(report)
print(
    f"[THÀNH CÔNG] Đã tự động xuất file báo cáo tại: {os.path.abspath('ket_qua_phan_tich.txt')}"
)