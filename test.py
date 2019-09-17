import matfin

#matfin.Capitalize().simple(debug=True)
#matfin.Capitalize().simple(debug=False)
#x = matfin.Capitalize(interest=0.25,periods=3,future_value=250000).simple()

cap = matfin.Capitalize
x = cap(interest= 0.02,
    present_value= 150000,
    future_value= 600000,
    )

print(x.continuous())