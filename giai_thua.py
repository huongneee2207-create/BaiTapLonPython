def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    giai_thua = 1
    for i in range(2, n + 1):
        giai_thua *= i
    return giai_thua

try:
    so = int(input("Nhập một số nguyên dương để tính giai thừa: "))
    if so < 0:
        print("Vui lòng nhập số lớn hơn hoặc bằng 0.")
    else:
        print(f"Giai thừa của {so} là: {tinh_giai_thua(so)}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")