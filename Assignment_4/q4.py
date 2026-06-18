def simple_interest(principal, rate=5, time=2):
    si = (principal * rate * time) / 100
    print("Simple Interest =", si)

simple_interest(10000)

simple_interest(principal=10000, rate=10, time=3)