import scipy.stats as sc
import pandas as pd
import random

data = pd.read_excel("Book1.xlsx")
df = pd.DataFrame(data) # ngubah jadi dataframe
pd.options.display.max_columns = 20
df = df.drop(['derajat','menit','radian','θawal'],axis=1)

# a = n, b = n + 1, c = n + 2, d = n + 3
#m adalah
eps = 10 #toleransi
x = list(range(12))
y = [random.randint(10, 1000) for iter in range(12)]
print('m','n','p_value','slope')
for m in range(1, 10):
    for n in range(1,10):
        if n>m:
            for i in range(12):
                df = df.replace({'a': n, 'b': n+1, 'c': n+2, 'd': n+3})
                trans = df.at[i,'n']
                x[i] = m**2*trans**2/(trans**2 - m**2) #ambil data dari df
                y[i] = df.at[i,'λ'] # ambil data dari df    
            slope, intercept, r_value, p_value, std_err = sc.linregress(x, y)
            df = df.replace({n:'a', n+1:'b', n+2:'c', n+3:'d'})
            if abs(p_value) < abs(eps):
                    mbagus = m
                    nbagus = n
                    eps = p_value
            print(m, n, p_value, slope)
                   



        
