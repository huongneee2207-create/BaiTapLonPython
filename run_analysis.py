import os
import pandas as pd

# 1. Khởi tạo tập dữ liệu từ bảng nguồn
data = {
    "Mã Đơn": ["HD005", "HD006", "HD007", "HD008", "HD009", "HD010"],
    "Khu Vực (Quận)": [
        "Cầu Giấy",
        "Ba Đình",
        "Hà Đông",
        "Tây Hồ",
        "Đống Đa",
        "Nam Từ Liêm",
    ],
    "Nhóm Sản Phẩm": [
        "Trang điểm (Make-up)",
        "Chăm sóc cơ thể",
        "Chăm sóc da (Skincare)",
        "Chăm sóc da (Skincare)",
        "Trang điểm (Make-up)",
        "Chăm sóc da (Skincare)",
    ],
    "Loại Sản Phẩm": [
        "Cushion / Kem nền",
        "Sữa tắm / Dưỡng thể",
        "Nước tẩy trang",
        "Serum chống lão hóa",
        "Son môi",
        "Mặt nạ giấy",
    ],
    "Phân Khúc": [
        "Tầm trung (Mid-end)",
        "Bình dân (Mass)",
        "Bình dân (Mass)",
        "Cao cấp (High-end)",
        "Bình dân (Mass)",
        "Bình dân (Mass)",
    ],
    "Kênh Bán Hàng": [
        "Shopee",
        "Siêu thị",
        "TikTok Shop",
        "Website thương hiệu",
        "Shopee",
        "Cửa hàng offline",
    ],
    "Số Lượng": [95, 200, 180, 30, 210, 500],
    "Doanh Thu (VNĐ)": [
        33250000,
        30000000,
        27000000,
        45000000,
        42000000,
        15000000,
    ],
    "Đối Tượng Mua Chính": [
        "Khách hàng trẻ (Gen Z)",
        "Hộ gia đình",
        "Học sinh / Sinh viên",
        "Phụ nữ > 30 tuổi",
        "Học sinh / Sinh viên",
        "Khách hàng trẻ",
    ],
}

# Chuyển đổi dữ liệu sang dạng DataFrame
df = pd.DataFrame(data)

# Tính đơn giá trung bình của từng sản phẩm
df["Giá Bán Lẻ / SP"] = df["Doanh Thu (VNĐ)"] / df["Số Lượng"]

# 2. Xử lý logic và tính toán các chỉ số kinh doanh
tong_doanh_thu = df["Doanh Thu (VNĐ)"].sum()
tong_san_luong = df["Số Lượng"].sum()
gia_trung_binh_don = df["Doanh Thu (VNĐ)"].mean()

# Gom nhóm dữ liệu
doanh_thu_theo_nhom = (
    df.groupby("Nhóm Sản Phẩm")["Doanh Thu (VNĐ)"].sum().sort_values(ascending=False)
)
doanh_thu_theo_kenh = (
    df.groupby("Kênh Bán Hàng")["Doanh Thu (VNĐ)"].sum().sort_values(ascending=False)
)

# 3. Chuẩn bị nội dung văn bản báo cáo
report_content = f"""===========================================================================
               BÁO CÁO PHÂN TÍCH TIỀM NĂNG VÀ KẾT QUẢ KINH DOANH
===========================================================================
Ngày xuất báo cáo: 17/05/2026
Trạng thái: Hoàn thành tự động bằng Python

I. KẾT QUẢ KINH DOANH TỔNG QUAN
---------------------------------------------------------------------------
* Tổng doanh thu hệ thống gộp: {tong_doanh_thu:,} VNĐ
* Tổng sản lượng tiêu thụ:      {tong_san_luong:,} sản phẩm
* Giá trị đơn hàng trung bình:  {int(gia_trung_binh_don):,} VNĐ/đơn

II. HIỆU SUẤT DOANH THU CHI TIẾT

1. Theo Nhóm Sản Phẩm:
"""
for nhom, doanh_thu in doanh_thu_theo_nhom.items():
    ty_trong = (doanh_thu / tong_doanh_thu) * 100
    report_content += (
        f"  - {nhom:<25}: {doanh_thu:>12,} VNĐ ({ty_trong:.1f}%)\n"
    )

report_content += "\n2. Theo Kênh Bán Hàng:\n"
for kenh, doanh_thu in doanh_thu_theo_kenh.items():
    report_content += f"  - {kenh:<25}: {doanh_thu:>12,} VNĐ\n"

report_content += """
III. ĐÁNH GIÁ TIỀM NĂNG SẢN PHẨM & PHÂN KHÚC
---------------------------------------------------------------------------
[+] Dòng Cao cấp (High-end): Serum chống lão hóa (Website thương hiệu)
    - Tiềm năng sinh lời cực lớn. Dù chỉ bán ra 30 sản phẩm (ít nhất), nhưng 
      mang lại doanh thu cao nhất (45,000,000 VNĐ). Tệp khách hàng phụ nữ trên 
      30 tuổi tại Tây Hồ có biên lợi nhuận rất dày và độ trung thành cao.

[+] Dòng Bình dân (Mass): Mặt nạ giấy (Offline) & Son môi (Shopee)
    - Đóng vai trò là dòng sản phẩm "Phễu" thu hút lượng lớn khách hàng (Sản lượng 
      Mặt nạ giấy đạt kỷ lục 500 chiếc). Tiềm năng phát triển nằm ở việc khai thác 
      bán chéo (Cross-selling) các sản phẩm khác khi khách tới cửa hàng.

IV. GHI CHÚ & KHUYẾN NGHỊ VẬN HÀNH (NOTES)
---------------------------------------------------------------------------
📌 Ghi chú 1: Cần lưu ý tối ưu chi phí logistics đối với đơn hàng Mặt nạ giấy (HD010). 
   Sản lượng rất lớn (500) nhưng giá trị tổng thấp (15 triệu), dễ làm tăng chi phí 
   đóng gói và vận chuyển, làm giảm biên lợi nhuận ròng thực tế.

📌 Ghi chú 2: Kênh sàn TMĐT (Shopee/TikTok Shop) hoạt động cực tốt đối với tệp học 
   sinh/sinh viên và Gen Z. Nên thiết kế các gói combo sản phẩm làm đẹp giá tầm trung 
   để nâng cao giá trị trên mỗi đơn hàng (AOV).
===========================================================================
"""

# 4. In trực tiếp ra màn hình Terminal
print(report_content)

# 5. Tự động xuất kết quả thành file text
file_name = "bao_cao_kinh_doanh.txt"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(report_content)

print(
    f"\n[THÀNH CÔNG] Đã xuất file báo cáo chi tiết: '{os.path.abspath(file_name)}'"
)