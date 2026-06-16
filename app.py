C=float(input("Nhập số tiền khách hàng gửi tiết kiệm:"))

i=float(input("Nhập lãi suất tiết kiệm theo năm:"))

n=float(input("Nhập số tháng khách hàng gửi tiết kiệm:"))

An=C*(1+(i/12)*n)

Bn=C*(1+(i/12))**n

print(f"Tổng tiền lãi khách hàng nhận được theo lãi đơn: {An:,.4f} triệu đồng")

print(f"Tổng tiền lãi khách hàng nhận được theo lãi kép: {Bn:,.4f} triệu đồng")

