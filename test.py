import matfin

#matfin.Capitalize().simple(debug=True)
#matfin.Capitalize().simple(debug=False)
#x = matfin.Capitalize(interest=0.25,periods=3,future_value=250000).simple()

cap = matfin.Interest
x = cap(present_value= 150000,
    rate=0.02,
    future_value=600000
    )

print(x.continuous())