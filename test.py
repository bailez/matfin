import matfin

#matfin.Capitalize().simple(debug=True)
#matfin.Capitalize().simple(debug=False)
#x = matfin.Capitalize(interest=0.25,periods=3,future_value=250000).simple()


x = matfin.Capitalize(interest=0.015,periods=2.5,present_value=15000).continuous(interest_freq='M', period_freq='Y')
print(x)