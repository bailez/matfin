import matfin

cap = matfin.Interest
x = cap(rate=0.1,
    periods=12,
    present_value=100)

x = x.compound(interest_frequency='Y', period_frequency='M')
print(x)