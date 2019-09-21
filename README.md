# matfin 0.0.2
Financial Mathematics library with interest rate functions.

## Instalation
 ``` pip install matfin```
## Use

#### Capitalization

Capitalization with simple, discrete compound and continous compound interest rates:

In:
```
import matfin

cap = matfin.Interest
fv = cap(rate=0.1,
        present_value=100,
        periods=3)

spl = fv.simple()
dis = fv.compound()
con = fv.continuous()

print(spl)
print(dis)
print(con)
```
Out:
```
130.0
133.10000000000005
134.9858807576003
```

#### Interest rates and periods frequencies

You can pass arguments in interest functions to define the frequency of interest rates and periods:
In:
```
cap = matfin.Interest
fv = cap(rate=0.1,
        present_value=100,
        periods=3)

spl = fv.simple(interest_frequency='M', period_frequency='Y')
print(spl)
```
Out:
```
460.00000000000006
```

#### Converting interest rate frequencies

In:
```
freq = matfin.FrequencyAjustment
r = freq(input_frequency = 'd',
        output_frequency = 'M',
        rate= 0.15)

spl = r.simple()

print(spl)
```
Out:
```
4.5625
```
#### Converting periods frequencies
In:
```
freq = matfin.FrequencyAjustment
n = freq(input_frequency = 'Q',
        output_frequency = 'h',
        periods= 3)

k = n.simple()

print(k)
```
Out:
```
6570.0
```
