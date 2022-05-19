import os
import pytest
import json


@pytest.fixture()
def results():
    file_path = os.path.join(os.path.dirname(__file__), "results_sample.json")
    f = open(file_path)
    return json.load(f)


@pytest.fixture()
def api_url():
    return "https://fake_api.com/api/v2/pokemon/"
