import pytest
from unittest.mock import patch
import api
import pandas as pd
from new_activities import add_activities



@pytest.fixture
def sample_activities():
    return [
        {"id": "1", "activity": "Read", "type": "fun", "participants": 1, "price": 0.2, "accessibility": 0.5,
         "link": ""},
        {"id": "2", "activity": "Walk", "type": "sport", "participants": 2, "price": 0.0, "accessibility": 0.1,
         "link": "http://link"},
        {"id": "3", "activity": "Code", "type": "work", "participants": 1, "price": 0.0, "accessibility": 0.2,
         "link": ""}
    ]


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


def test_add_activities_deduplication(sample_activities):
    new = [{"id": "2", "activity": "WalkDuplicate", "type": "sport",
            "participants": 2, "price": 0.0, "accessibility": 0.1, "link": "http://link"}]

    updated = add_activities(new, sample_activities)

    ids = [a["id"] for a in updated]
    assert ids.count("2") == 1
    assert len(updated) == 3

def panda_sort_test(activities: list, column: str, ascending: bool = True) -> list:
    df = pd.DataFrame(activities)
    df.sort_values(by=column, ascending=ascending, inplace=True, ignore_index=True)
    return df.to_dict(orient="records")

def panda_filter_test(activities: list, column: str, min_val=None, max_val=None, exact_val=None) -> list:
    df = pd.DataFrame(activities)
    if exact_val is not None:
        df = df[df[column] == exact_val]
    else:
        if min_val is not None:
            df = df[df[column] >= min_val]
        if max_val is not None:
            df = df[df[column] <= max_val]
    return df.to_dict(orient="records")
