import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Get high temperatures from this file.
    dates, highs, lows = [], [], []
    rains = []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            rain = float(row[3])
            print(row[3])
        except ValueError:
            print("Error")
        else:
            dates.append(current_date)
            rains.append(rain)

#Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='red', alpha=0.5)


#Format plots.
plt.title("Daily rains temperatures, 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rains', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
