def main():
    print("calculating S.I\ Enter Principal, Rate and Time")

    principal = int(input("Principal: "))
    rate = float(input("Rate: "))
    time = float(input("Time: "))

    calc_simple_interest = ((principal*rate*time)/100)
    print("calc_Simple_interest: {}")



main()