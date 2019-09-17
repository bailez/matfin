import matfin

#matfin.Capitalize().simple(debug=True)
#matfin.Capitalize().simple(debug=False)
#x = matfin.Capitalize(interest=0.25,periods=3,future_value=250000).simple()
y = matfin.Capitalize(interest=(0.12)/7,periods=7, present_value=100).compound()
print(y)