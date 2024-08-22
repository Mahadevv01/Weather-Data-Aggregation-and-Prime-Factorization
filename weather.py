def aggregate_weather_data(records):
    city_data = {}
    
    for record in records:
        city = record['city']
        if city not in city_data:
            city_data[city] = {'temperature_sum': 0, 'humidity_sum': 0, 'temperature_count': 0, 'humidity_count': 0}
        
        if 'temperature' in record:
            city_data[city]['temperature_sum'] += record['temperature']
            city_data[city]['temperature_count'] += 1
        
        if 'humidity' in record:
            city_data[city]['humidity_sum'] += record['humidity']
            city_data[city]['humidity_count'] += 1
    
    for city, data in city_data.items():
        avg_temperature = data['temperature_sum'] / data['temperature_count'] if data['temperature_count'] > 0 else None
        avg_humidity = data['humidity_sum'] / data['humidity_count'] if data['humidity_count'] > 0 else None
        print(f"City: {city}, Average Temperature: {avg_temperature}, Average Humidity: {avg_humidity}")
