import requests

api_url = 'https://pokeapi.co/api/v2/pokemon/'


def get_pokemons(api_url):
    print(f"Getting Pokemons from: {api_url}")
    results = requests.get(api_url)
    return results.json()


if __name__ == "__main__":
    result = get_pokemons(api_url)
    print(result)