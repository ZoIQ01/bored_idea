import pytest
from unittest.mock import patch
import api
import pandas as pd
from filter import panda_filter
from sort_idea_panda import  sort_activities

@pytest.fixture
def sample_activities():
    return pd.DataFrame({
        "id": [1, 2, 3],
        "activity": ["watch movie", "read the book", "paint the wall"],
        "type": ["fun", "learn", "draw"],
        "participants": [1, 2, 3],
        "price": [0, 0.5, 1],
        "accessibility": ["nan", "nan", "nan"],
        "link": ["https:", "https:", "https:"]
    })

def test_filter(sample_activities):
    result = panda_filter(sample_activities)
    ids = [item["id"] for item in result]
    assert all(i >= 1 for i in ids)
    assert len(result) == 3
    assert set(ids) == {1, 2, 3}

def test_sort_by_id_ascending(sample_activities):
    result = sort_activities(sample_activities, column="id", ascending=True)
    ids = [item["id"] for item in result]
    assert ids == [1, 2, 3]

def test_sort_by_price_descending(sample_activities):
    result = sort_activities(sample_activities, column="price", ascending=False)
    prices = [item["price"] for item in result]
    assert prices == [1.0, 0.5, 0.0]


def test_fetch_activity_mock():
    with patch("api.fetch_activity") as mock_fetch:
        mock_fetch.return_value = {
            "id": "10",
            "activity": "TestAPI",
            "type": "fun",
            "participants": 1,
            "price": 0.3,
            "accessibility": 0.2,
            "link": ""
        }
        idea = api.fetch_activity()
        assert idea["activity"] == "TestAPI"
        assert float(idea["price"]) == 0.3
        assert idea["id"] == "10"
        assert idea["participants"] == 1
        assert idea["type"] == "fun"
        assert idea["accessibility"] == 0.2
        assert idea["link"] == ""
