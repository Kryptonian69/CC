import requests
import json

def search_location(query):
    url = "https://nominatim.openstreetmap.org/search"
    
    params = {
        'q': query,
        'format': 'json',
        'limit': 5
    }
    
    headers = {
        'User-Agent': 'StudentPracticalApp/1.0'
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: API returned status code {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def main():
    print("--- OpenStreetMap Location Search ---")
    query = input("Enter a city or place name: ")
    
    print(f"\nSearching for '{query}'...")
    results = search_location(query)

    if results:
        print(f"\nFound {len(results)} result(s):\n")
        
        for index, place in enumerate(results, 1):
            print(f"Result #{index}")
            print(f"Name: {place.get('display_name')}")
            print(f"Type: {place.get('type')} ({place.get('class')})")
            print(f"Coordinates: {place.get('lat')}, {place.get('lon')}")
            print("-" * 40)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
