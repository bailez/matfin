import matfin

#matfin.Capitalize().simple(debug=True)
#matfin.Capitalize().simple(debug=False)
#x = matfin.Capitalize(interest=0.25,periods=3,future_value=250000).simple()

cap = matfin.Interest
x = cap(present_value= 100000,
    periods=3*12,
    future_value=350000
    )

print(x.continuous())