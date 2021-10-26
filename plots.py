import json
import matplotlib.pyplot as plt
import os
us_gdp = []
text = ''
with open('USA_gdp.json') as f:
    text = f.read()
us_gdp = json.loads(text)

gdp_value = {}
for year in range(1960,2021):
    gdp_value[year] = 0
    gdp_value[year] = us_gdp[1][year-1960]['value']

xs = sorted(gdp_value.keys())
ys = [ gdp_value[key] for key in xs ]

fig, ax = plt.subplots()
plt.xlabel('years')
plt.ylabel('Gross Domestic Product( dollars in trillions)')
plt.title ('USA GDP from 1960 - 2020')
ax.bar (xs, ys)
plt.show()






narcos = []
text = ''
with open('narcos.json') as f:
    text = f.read()
narcos = json.loads(text)

runtime = {}
episodes = 0
for episodes in range (0,30):
    runtime[episodes] = narcos["_embedded"]["episodes"][episodes]['runtime']
#print(runtime)

west_world = []
text = ''
with open('west_world.json') as f:
    text = f.read()
west_world = json.loads(text)

runtime2 = {}
episodes2 = 0
for episodes2 in range (0,28):
    runtime2[episodes2] = west_world["_embedded"]["episodes"][episodes2]['runtime']




x1 = sorted(runtime.keys())
y1 = [ runtime[key] for key in x1 ]
plt.plot(x1, y1, label = "Narcos")

x2 = sorted(runtime2.keys())
y2 = [ runtime2[key] for key in x2]
plt.plot(x2, y2, label = "Westworld")

plt.xlabel('episodes')
plt.ylabel('runtime (minutes)')
plt.title ('Narcos vs Westworld')
plt.legend
plt.show()















