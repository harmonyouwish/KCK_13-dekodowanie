import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import aseegg as ag

# Załadowanie danych
dane = pd.read_csv("C:/Users/Natalia/Desktop/dekodowanie/sub1trial19.csv")
#print(dane)


# Definiowanie zmiennych
kolumna2 = dane["kolumna2"]
kolumna3 = dane["kolumna3"]
kolumna4 = dane["kolumna4"]
kolumna5 = dane["kolumna5"]
kolumna6 = dane["kolumna6"]

# Sygnał nieprzefiltrowany
t = np.linspace(0,37.99,200*37.99)
sygnal1 = dane["kolumna2"]
plt.subplot(2, 1, 1)
plt.plot(t, sygnal1, label="Sygnał nieprzefiltrowany")
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [mV]')
plt.legend(loc= "upper right")


sygnal2 = dane["kolumna6"]
plt.subplot(2, 1, 2)
plt.plot(t, sygnal2, label= "Wyświetlane cyfry")
plt.xlabel('Czas [s]')
plt.ylabel('Wyświetlana cyfra [-]')
plt.legend(loc= "upper right")

#plt.show()

#Sygnał przefiltrowany
filtr11 = ag.pasmowozaporowy(kolumna2, 200, 49, 51)
filtr12 = ag.pasmowoprzepustowy(filtr11, 200, 1, 50)
plt.subplot(2, 1, 1)
plt.plot(t, filtr12, label="Sygnał przefiltrowany")
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [mV]')
plt.legend(loc= "upper right")


plt.subplot(2, 1, 2)
plt.plot(t, sygnal2, label= "Wyświetlane cyfry")
plt.xlabel('Czas [s]')
plt.ylabel('Wyświetlana cyfra [-]')
plt.legend(loc= "upper right")

plt.show()

# "Dekodowanie"
#print(kolumna2.min()) #0.84
#print(kolumna2.max()) #1.09
mrug=[]
odp=[]
for i in range(len(kolumna2)):
    if kolumna2[i]>0.95: #powyżej 0.95 - mrugnięcia, z analizy wykresu
        mrug.append(i)
        odp.append(kolumna6[i])
#print(mrug) #wszystkie momenty wzrostu sygnału
#print(len(mrug))
#print(kolumna2[214:229], kolumna6[214:229]) #kolumna 6 - cyferki odpowiadające wzrostowi sygnału, przykładowy dla 1 wzrostu
#
#print(kolumna6[220])
odp=[]
odp.append(kolumna6[220])
odp.append(kolumna6[664])
odp.append(kolumna6[1003])
odp.append(kolumna6[1867])
odp.append(kolumna6[2445])
odp.append(kolumna6[3381])
odp.append(kolumna6[3959])
odp.append(kolumna6[4278])
odp.append(kolumna6[5171])
odp.append(kolumna6[5776])
odp.append(kolumna6[6354])
odp.append(kolumna6[6979])

print("Wymrugane cyfry to", odp)
