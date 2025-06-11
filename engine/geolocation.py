import requests

LOCATIONIQ_API_KEY = 'pk.3c327a8e486c9d3697b9032b460a755a'

def get_location_by_ip():
    ip_response = requests.get('http://ip-api.com/json/')
    ip_data = ip_response.json()
    ip = ip_data.get('query')

    locationiq_url = f"https://us1.locationiq.com/v1/ipinfo.php?key={LOCATIONIQ_API_KEY}&ip={ip}&format=json"
    response = requests.get(locationiq_url)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code == 200:
        location = response.json()
        city = location.get('city', 'N/A')
        country = location.get('country', 'N/A')
        latitude = location.get('lat', 'N/A')
        longitude = location.get('lon', 'N/A')
        
        print(f"IP: {ip}")
        print(f"Location: {city}, {country}")
        print(f"Coordinates: {latitude}, {longitude}")
        return latitude, longitude
    else:
        print("Error fetching location from LocationIQ.")
        return None

get_location_by_ip()
