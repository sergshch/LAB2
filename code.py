import csv
import matplotlib.pyplot as plt

bytes = 0
tableTime = []
tableBytes = []

# Чтение из файла
f = open("nfcapd.202002251200", "r")
reader = csv.reader(f)

# Заполнение списков для графика и подсчет объема трафика для тарификации
i = '00:00:00.000'
for row in reader:
    if'192.168.250.59' in row[5]  or '192.168.250.59' in row[6]:
        if row[1] != i:
            i = row[1]
            k = float(row[9])
            tableTime.append([row[1]])
            tableBytes.append(float(row[9]))
            bytes += float(row[9])
        else:
            tableBytes.pop()
            tableBytes.append(float(k)+float(row[9]))
            k += float(row[9]) 
            bytes += float(row[9])         
tableTime.sort()
mbbytes = bytes / 1024 / 1024
kbbytes = bytes / 1024

# Тарификация трафика
if mbbytes >= 500: cost = 500*0.5 + (mbbytes-500)*1 
else: cost = 500*0.5 + (kbbytes-500)*1
print('Итоговая стоимость: {:.2f}'.format(cost))

# Потроение графика зависимости объема трафика от времени
fig, ax = plt.subplots()
for i in range(len(tableTime)):
            ax.bar(tableTime[i], tableBytes[i])
plt.ylabel('Traffic')
plt.xlabel('Time')
plt.show()
