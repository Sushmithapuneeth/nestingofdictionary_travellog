travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country_visited, Times_visited, Cities_visited):
    new_country = {}
    new_country["country"] = "country_visited"
    new_country["visits"] = "Times_visited"
    new_country["cities"] = "Cities_visited"
    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
