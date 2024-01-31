komanda = {
    "Jonas": 12,
    "Tadas": 15,
    "Rimas": 25,
    "Pranas": 23,
    "Arunas": 14
}
pagalVarda = dict(sorted(komanda.items()))
print(pagalVarda)
pagalTaskus = dict(sorted(komanda.items(), key= lambda kv: kv[1]))
print(pagalTaskus)

cities = [
	{
		"name": "New York City",
		"country": "United States",
		"population": 20.14,
		"area": 1223.59
	},
	{
		"name": "Tokyo",
		"country": "Japan",
		"population": 37.47,
		"area": 2194.07,
	},
	{
		"name": "Los Angeles",
		"country": "United States",
		"population": 13.2,
		"area": 1299.01,
	},
	{
		"name": "Madrid",
		"country": "Spain",
		"population": 6.79,
		"area": 604.31,
	},
	{
		"name": "Osaka",
		"country": "Japan",
		"population": 19.3,
		"area": 5107.0,
	},
	{
		"name": "London",
		"country": "United Kingdom",
		"population": 14.26,
		"area": 8382.0,
	}
]
cities1 = sorted(cities, key= lambda city: city['population'])
print(cities1)