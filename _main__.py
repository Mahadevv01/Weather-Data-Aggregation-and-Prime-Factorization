from weather import aggregate_weather_data
from prime_fc import prime_factors

if __name__ == "__main__":
    # Test Weather Aggregation Function
    weather_records = [
        {'city': 'CityA', 'temperature': 30, 'humidity': 70},
        {'city': 'CityA', 'temperature': 32},
        {'city': 'CityB', 'humidity': 65},
        {'city': 'CityA', 'temperature': 31, 'humidity': 72},
        {'city': 'CityB', 'temperature': 29, 'humidity': 68}
    ]
    aggregate_weather_data(weather_records)
    
    # Test Prime Factorization Function
    n = 60
    print(f"Prime factors of {n}: {prime_factors(n)}")
