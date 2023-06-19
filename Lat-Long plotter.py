import csv
import matplotlib.pyplot as plt

latitudes = []    # establish lists to store our values in which we're going to pull out of the CSV file
longitudes = []


with open('coordinates3.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        lats = row[5]   # extract latitude and longitude data
        lons = row[6]
        latcor = float(lats.strip('N')) #convert lats and longs to floats so they can be plotted as well as strip chars "latcor" means latitude corrected
        loncor = float(lons.strip('W'))
        latitudes.append(latcor)        # add the formatted lats and longs to the list
        longitudes.append(loncor)
        


fig = plt.figure()
ax = plt.axes()


plt.scatter(latitudes, longitudes, color = 'red', marker = 'o')    #plot the lats and longs and some styling
plt.title('Aircraft Positions')
plt.ylabel('Longitude')
plt.xlabel('Latitude')

plt.show()
