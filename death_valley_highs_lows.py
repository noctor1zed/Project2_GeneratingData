import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Get high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high_F = int(row[4])
            low_F = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            # Fahrenheit into C°
            high_C = (high_F - 32) / (9 / 5)
            low_C = (low_F - 32) / (9 / 5)
            dates.append(current_date)
            highs.append(high_C)
            lows.append(low_C)

#Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plots.
plt.title("Daily high&lows temperatures, 2018, Death Valley", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=16)
plt.ylim(-10, 60)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()