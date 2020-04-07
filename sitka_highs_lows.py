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
            high_F = int(row[5])
            low_F = int(row[6])
            #rain = int(row[3])
        except ValueError:
            print("Error")
        else:
            # Fahrenheit into C°
            high_C = (high_F - 32) / (9/5)
            low_C = (low_F - 32) / (9 / 5)
            dates.append(current_date)
            highs.append(high_C)
            lows.append(low_C)
            #rains.append(rain)

#Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plots.
plt.title("Daily high&lows temperatures, 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=16)
plt.ylim(-10, 60)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
