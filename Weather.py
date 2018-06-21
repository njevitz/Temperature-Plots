# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 20:53:39 2018

@author: NJevi
"""
import matplotlib.pyplot as plt

Temperature = [75, 74, 79, 80, 74, 80, 81, 73, 81, 71, 69, 81, 83, 81, 89, 93, 95, 95, 84]
Dates = ['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11', '6/12', '6/13', '6/14', '6/15', '6/16', '6/17', '6/18', '6/19']
Historic = [75, 76, 76, 76, 77, 77, 77, 78, 78, 78, 79, 79, 79, 80, 80, 80, 81, 81, 81]

plt.figure(figsize=(11, 8))
plt.plot(Dates, Temperature, color = '#DC3512', marker = 'o')
plt.plot(Dates, Historic, linestyle = '--', color = '#3C4CA7', marker = 's')
plt.legend(['Temperature', 'Historic'])
plt.xlabel('Day')
plt.ylabel('Temperature in Fahrenheit')
plt.title('Chicago Temperatures this Year vs. Historic')
plt.savefig('Temperature2018.png')
plt.show()


waterpark_searches = [27, 29, 27, 26, 23, 22, 26, 21, 32, 18, 31, 28, 39, 36, 29, 100, 87, 59, 0]

plt.figure(figsize=(11, 8))
ax1 = plt.subplot()
ax1.plot(Dates, Temperature, color = '#DC3512', marker = 'o')
ax1.set_xlabel('Day', labelpad = 10)
ax1.set_ylabel('Temperatue', color = '#DC3512', labelpad = 15)
ax1.tick_params('Temperature', color = '#DC3512')

ax2 = ax1.twinx()
ax2.plot(Dates, waterpark_searches, color = '#333D76', marker = 's')
ax2.set_ylabel('Searches', Color = '#333D76', labelpad = 10)
plt.title('Temperature vs. Waterpark Searches')
plt.savefig('Waterpark.png')
plt.show()

