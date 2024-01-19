#import pandas as pd
#data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'], 
  #      'Usia': [25, 35, 30, 28],
 #       'Gaji': [50000, 60000, 70000, 55000]}

#df = pd.DataFrame(data)
# Definisikan fungsi lambda untuk menghitung peningkatan gaji
#kenaikan_gaji = lambda gaji: gaji * 1.05
# Iterasi melalui DataFrame
#for i in range(len(df)):
# Hitung gaji baru
  #df.loc[i, 'Gaji'] = kenaikan_gaji(df.loc[i, 'Gaji'])
# Tampilkan DataFrame
#print(df)
import pandas as pd
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],	
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data) 
#Peningkatan gaji 5% untuk semua karyawan
df['Gaji'] = df['Gaji'].apply(lambda x: x * 1.05)
#DataFrame setelah peningkatan gaji 5%
print("\nDataFrame setelah peningkatan gaji 5% untuk semua karyawan:")
print(df)
#Peningkatan gaji 2% untuk karyawan di atas 30 tahun
for index, row in df.iterrows():
    if row['Usia'] > 30:
       df.at[index, 'Gaji'] = (1 + 0.02) * row['Gaji']
#DataFrame setelah peningkatan gaji untuk usia di atas 30 tahun
print("DataFrame setelah peningkatan gaji untuk usia di atas 30 tahun:")
print(df)
