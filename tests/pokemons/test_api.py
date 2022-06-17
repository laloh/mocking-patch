import json
from requests.api import delete
import requests_mock
from pokemons import get_pokemons, insert_into_snowflake, delete_pokemon

def test_get_pokemons(api_url, results):
    with requests_mock.Mocker() as m:
        # Here we monkey patch the request object.
        m.get(api_url, text=json.dumps(results))
        # Here we want to test how get_pokemons behave
        result = get_pokemons(api_url)
        print(result)
    
    assert len(result) > 0


def test_insert_into_snowflake(results, conn, table_name):
    success = insert_into_snowflake(results, conn, table_name)
    assert success is True


def test_delete_pokemon(conn, table_name):
    success = delete_pokemon(conn, "bulbasaur", table_name) 
    assert success is True
