import os
import pytest
import json
import sqlite3 


@pytest.fixture()
def results():
    file_path = os.path.join(os.path.dirname(__file__), "results_sample.json")
    f = open(file_path)
    return json.load(f)['results']


@pytest.fixture()
def api_url():
    return "https://fake_api.com/api/v2/pokemon/"


@pytest.fixture()
def conn():
    return sqlite3.connect('pokemons.db')


@pytest.fixture()
def table_name():
    return "pokemons"
