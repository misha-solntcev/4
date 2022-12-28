countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
text = f"ERROR: Country for {city} not found"
for item in countries.items():
    if city in item[1]:
        text = f"INFO: {city} is a city in {item[0]}"
print(text)