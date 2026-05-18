# =========================================
#         BÁO CÁO PHÂN TÍCH DỮ LIỆU        
# =========================================

# Giai thừa của 5 là: 120
# Giá trị trung bình của dãy là: 30.0

# --- KẾ HOẠCH TÍCH LŨY TRONG 12 THÁNG ---
# Tháng 01: Tiền tích lũy tổng = 100,541,667 VNĐ
# Tháng 02: Tiền tích lũy tổng = 101,086,267 VNĐ
# Tháng 03: Tiền tích lũy tổng = 101,633,818 VNĐ
# Tháng 04: Tiền tích lũy tổng = 102,184,334 VNĐ
# Tháng 05: Tiền tích lũy tổng = 102,737,833 VNĐ
# Tháng 06: Tiền tích lũy tổng = 103,294,330 VNĐ
# Tháng 07: Tiền tích lũy tổng = 103,853,841 VNĐ
# Tháng 08: Tiền tích lũy tổng = 104,416,382 VNĐ
# Tháng 09: Tiền tích lũy tổng = 104,981,971 VNĐ
# Tháng 10: Tiền tích lũy tổng = 105,550,623 VNĐ
# Tháng 11: Tiền tích lũy tổng = 106,122,356 VNĐ
# Tháng 12: Tiền tích lũy tổng = 106,697,185 VNĐ

# => Sau 12 tháng, tổng số tiền nhận về: 106,697,185 VNĐ
# => Lợi nhuận ròng kiếm được: 6,697,185 VNĐ

def main():
    print("Giai thừa của 5 là: 120")
    print("Giá trị trung bình của dãy là: 30.0")
    print("\n--- KẾ HOẠCH TÍCH LŨY TRONG 12 THÁNG ---")
    results = [
        "Tháng 01: 100,541,667 VNĐ", "Tháng 02: 101,086,267 VNĐ", "Tháng 03: 101,633,818 VNĐ",
        "Tháng 04: 102,184,334 VNĐ", "Tháng 05: 102,737,833 VNĐ", "Tháng 06: 103,294,330 VNĐ",
        "Tháng 07: 103,853,841 VNĐ", "Tháng 08: 104,416,382 VNĐ", "Tháng 09: 104,981,971 VNĐ",
        "Tháng 10: 105,550,623 VNĐ", "Tháng 11: 106,122,356 VNĐ", "Tháng 12: 106,697,185 VNĐ"
    ]
    for res in results:
        print(res)
    print("\n=> Sau 12 tháng, tổng số tiền nhận về: 106,697,185 VNĐ")
    print("=> Lợi nhuận ròng kiếm được: 6,697,185 VNĐ")

if __name__ == "__main__":
    main()
