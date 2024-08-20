def calculate_monthly_payment(principal, annual_rate, years):
    R = annual_rate / 100 / 12
    P = principal
    N = years * 12
    payment = (P * R * (1 + R)  N) / ((1 + R)  N - 1)
    return payment

principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")