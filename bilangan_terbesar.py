max = 0

while True:
    bilangan = int(input("Masukan bilangan(0 untuk berhenti): "))
    if bilangan == 0:
        break
    if bilangan > bilangan_max:
        bilangan_max = bilangan

print(f"Bilangan terbesar: {bilangan_max}")