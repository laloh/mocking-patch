import json
import requests_mock
from pokemons import get_pokemons

def test_get_pokemons(api_url, results):
    with requests_mock.Mocker() as m:
		# Here we monkey patch the request object.
        m.get(api_url, text=json.dumps(results))
		# Here we want to test how get_pokemons behave
        result = get_pokemons(api_url)
        print(result)
    
    assert result['count'] > 0
