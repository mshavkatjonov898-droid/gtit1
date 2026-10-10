import requests
#
# params = {
#     "latitude": 41.3110,
#     "longitude": 69.2405,
#     "daily": "temperature_2m_max,temperature_2m_min",
#     "timezone": "Asia/Tashkent"
# }
#
# url = "https://api.open-meteo.com/v1/forecast"
# response = requests.get(url, params=params).json()
#
# print("7 days weather")
# print("-" * 45)
# print(f"{'Дата':<15} | {'Max (°C)':<15} | {'Min (°C)'}")
# print("-" * 45)
#
# daily = response['daily']
# for i in range(len(daily['time'])):
#     date = daily['time'][i]
#     t_max = daily['temperature_2m_max'][i]
#     t_min = daily['temperature_2m_min'][i]
#     print(f"{date:<15} | {t_max:<15} | {t_min}")

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url).json()

height = response['height']
weight = response['weight']

# Способности находятся в списке 'abilities', каждый элемент которого - словарь
# Мы извлекаем имя способности (ability -> name)
abilities = [item['ability']['name'] for item in response['abilities'][:3]]

print(f"Pokemon")
print(f"Height: {height}")
print(f"Weight: {weight}")
print(f"Abilities {', '.join(abilities).title()}")