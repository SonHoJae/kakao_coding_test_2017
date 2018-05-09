# 3	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”]	50
# 3	[“Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”]	21
# 2	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “SanFrancisco”, “Seoul”, “Rome”, “Paris”, “Jeju”, “NewYork”, “Rome”]	60
# 5	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “SanFrancisco”, “Seoul”, “Rome”, “Paris”, “Jeju”, “NewYork”, “Rome”]	52
# 2	[“Jeju”, “Pangyo”, “NewYork”, “newyork”]	16
# 0	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”]	25

cacheSize = int(input())
cache = dict()

cities = input() # Maximum 100,000
cities = cities.replace('[','')
cities = cities.replace(']','')
cities = cities.split(',')
for idx, city in enumerate(cities):
    cities[idx] = city.strip().strip('“').strip('”').lower()
execution_time = 0
# 2
# [“Jeju”, “Pangyo”, “NewYork”, “newyork”]

for city in cities:
    if city in cache:
        execution_time += 1 # cache hit
        cache[city] = 0
    else:
        execution_time += 5
        max = -9999
        if len(cache) == cacheSize:
            leastUsedCity = None
            for unit in cache:
                if cache[unit] > max:
                    leastUsedCity = unit
                    max = cache[unit]
            cache.pop(leastUsedCity,None)
        cache[city] = 0
    for unit in cache:
        cache[unit] += 1
    print(cache)
    print(len(cache))
print(execution_time)

#[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “SanFrancisco”, “Seoul”, “Rome”, “Paris”, “Jeju”, “NewYork”, “Rome”]