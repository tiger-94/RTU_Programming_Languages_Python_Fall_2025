"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.
"""


temperatures = [23, 25, 22, 24, 26, 21, 23]  # temperatures for a week
city_population = {
    "New York": 8419000,
    "Los Angeles": 3980000,
    "Chicago": 2716000,
    "Houston": 2328000,
    "Phoenix": 1690000
}



average_temperature = sum(temperatures) / len(temperatures)


largest_city = max(city_population, key=city_population.get)
largest_population = city_population[largest_city]


smallest_city = min(city_population, key=city_population.get)
smallest_population = city_population[smallest_city]


total_population = sum(city_population.values())


print(f"Average temperature for the week: {average_temperature:.2f}°C")
print(f"Largest city: {largest_city} - {largest_population}")
print(f"Smallest city: {smallest_city} - {smallest_population}")
print(f"Total population of all cities: {total_population}")
