username = input("Enter your username: ")
price = int(input("Enter your total shopping amount: "))
discount = 0

if price >= 500000:
    discount = 0.2
elif price >= 250000:
    discount = 0.1
elif price >= 100000:
    discount = 0.05
elif price < 100000:
    discount = 0
else:
    print("Invalid input")

total_shopping = price - (price * discount)

print("=== Struk Pembelian ===")
print("Nama Pembeli: ", username)
print("Total Belanja: ", price)
print("Diskon: ", discount * 100, "%")
print("Total Belanja Setelah Diskon: ", total_shopping)