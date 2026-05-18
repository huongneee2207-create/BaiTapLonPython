import os
import pandas as pd


# ===========================================================================
# PHẦN 1: CÁC HÀM TOÁN HỌC & TÀI CHÍNH CƠ BẢN
# ===========================================================================
def tinh_giai_thua(n):
    if n < 0:
        return "Không tính được giai thừa cho số âm"
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua


def tinh_trung_binh(day_so):
    if len(day_so) == 0:
        return 0
    return sum(day_so) / len(day_so)


def tinh_lai_suat_12_thang(goc, lai_suat_nam):
    lai_suat_thang = lai_suat_nam / 12
    so_tien = goc
    for _ in range(12):
        so_tien += so_tien * lai_suat_thang
    return so_tien, so_tien - goc


# ===========================================================================
# PHẦN 2: KHỞI TẠO & XỬ LÝ DỮ LIỆU MỸ PHẨM (10 ĐƠN HÀNG)
# ===========================================================================
# Dữ liệu tổng hợp từ các ảnh bạn cung cấp
data_my_pham = {
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
}

df = pd.DataFrame(data_my_pham)

# Tính toán các chỉ số tổng hợp bằng Pandas
tong_doanh_thu = df["Doanh Thu (VNĐ)"].sum()
tong_san_luong = df["Số Lượng"].sum()
doanh_thu_theo_nhom = (
    df.groupby("Nhóm Sản Phẩm")["Doanh Thu (VNĐ)"].sum().sort_values(ascending=False)
)
doanh_thu_theo_kenh = (
    df.groupby("Kênh Bán Hàng")["Doanh Thu (VNĐ)"].sum().sort_values(ascending=False)
)

# Chạy thử các hàm toán học ở phần 1 để lấy số liệu đưa vào báo cáo
giai_thua_5 = tinh_giai_thua(5)
day_so_test = [10, 20, 30, 40, 50]
trung_binh_day = tinh_trung_binh(day_so_test)
tong_tien_sau_12t, lai_rong = tinh_lai_suat_12_thang(100000000, 0.065)


# ===========================================================================
# PHẦN 3: TỔNG HỢP VÀ XUẤT BÁO CÁO VĂN BẢN
# ===========================================================================
noi_dung_bao_cao = f"""===========================================================================
                BÁO CÁO TỔNG HỢP: KẾT QUẢ TOÁN HỌC & PHÂN TÍCH KINH DOANH
===========================================================================
Ngày xuất báo cáo: 18/05/2026
Hệ thống vận hành: Tự động hoàn toàn bằng Python & Pandas

---------------------------------------------------------------------------
A. KẾT QUẢ THỰC HÀNH CÁC PHÉP TOÁN CƠ BẢN:
---------------------------------------------------------------------------
1. Tính giai thừa:
   - Giai thừa của 5 (5!) = {giai_thua_5}

2. Tính giá trị trung bình:
   - Dãy số khảo sát: {day_so_test}
   - Giá trị trung bình của dãy = {trung_binh_day}

3. Tính lợi nhuận tích lũy (Lãi kép sau 12 tháng):
   - Số tiền gốc ban đầu: 100,000,000 VNĐ (Lãi suất: 6.5%/năm)
   - Lợi nhuận ròng thu về: {lai_rong:,.0f} VNĐ
   - Tổng số tiền nhận được (Gốc + Lãi) = {tong_tien_sau_12t:,.0f} VNĐ

---------------------------------------------------------------------------
B. KẾT QUẢ KINH DOANH & ĐÁNH GIÁ TIỀM NĂNG MỸ PHẨM:
---------------------------------------------------------------------------
1. Chỉ số tổng quan:
   - Tổng doanh thu hệ thống gộp: {tong_doanh_thu:,} VNĐ
   - Tổng sản lượng tiêu thụ:      {tong_san_luong:,} sản phẩm
   - Giá trị trung bình / sản phẩm: {int(tong_doanh_thu / tong_san_luong):,} VNĐ

2. Hiệu suất doanh thu theo Ngành hàng:
"""
for nhom, doanh_thu in doanh_thu_theo_nhom.items():
    noi_dung_bao_cao += (
        f"   - {nhom:<25}: {doanh_thu:>12,} VNĐ ({doanh_thu/tong_doanh_thu*100:.1f}%)\n"
    )

noi_dung_bao_cao += "\n3. Hiệu suất doanh thu theo Kênh bán hàng:\n"
for kenh, doanh_thu in doanh_thu_theo_kenh.items():
    noi_dung_bao_cao += (
        f"   - {kenh:<25}: {doanh_thu:>12,} VNĐ ({doanh_thu/tong_doanh_thu*100:.1f}%)\n"
    )

noi_dung_bao_cao += """
---------------------------------------------------------------------------
C. ĐÁNH GIÁ VÀ GHI CHÚ VẬN HÀNH TỪ CHUYÊN GIA (NOTES):
---------------------------------------------------------------------------
📌 Ghi chú 1: Nhóm hàng Chăm sóc da (Skincare) chiếm tỷ trọng doanh thu cao nhất
   (gần 58.5%). Dòng này có tiềm năng tái mua vòng đời ngắn, cực kỳ bền vững.

📌 Ghi chú 2: Rủi ro logistics lớn tại đơn hàng Nam Từ Liêm (Serum Bình dân).
   Sản lượng xuất kho cực lớn (500 sản phẩm) nhưng doanh thu thu về rất thấp 
   (15,000,000 VNĐ). Đơn giá quá rẻ (30,000 VNĐ/chai) có rủi ro bị chi phí đóng 
   gói và vận chuyển triệt tiêu hết lợi nhuận thực tế.

📌 Ghi chú 3: Kênh thương mại điện tử (Shopee, TikTok Shop) chiếm trên 50% doanh 
   thu toàn hệ thống. Cần tập trung tạo các gói combo sản phẩm giá tầm trung 
   để nâng cao giá trị trung bình trên mỗi đơn hàng (AOV) đối với giới trẻ.
===========================================================================
"""

# In thẳng ra màn hình Terminal để xem ngay tại chỗ
print(noi_dung_bao_cao)

# Tự động ghi lại nội dung vào file text sạch đẹp
ten_file_xuat = "bao_cao_tong_hop_cuoi_ky.txt"
with open(ten_file_xuat, "w", encoding="utf-8") as f:
    f.write(noi_dung_bao_cao)

print(
    f"\n[XỬ LÝ THÀNH CÔNG] File báo cáo đã được lưu trữ tại: {os.path.abspath(ten_file_xuat)}"
)