import matfin

#matfin.Capitalize().simple(debug=True)
#matfin.Capitalize().simple(debug=False)
#x = matfin.Capitalize(interest=0.25,periods=3,future_value=250000).simple()

cap = matfin.Interest
x = cap(
        future_value=106.83425,
        periods=7,
        rate=0.12
    )
freq = matfin.FrequencyAjustment
y = freq(input_frequency= 'M',
        output_frequency= 'Y',
        rate=0.015
        )
print(x.compound(interest_frequency='Y',period_frequency='M'))