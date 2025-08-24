import pytest
from unittest.mock import patch
import api
from new_activities import add_activities
from filter import filter_activities_list
from sort_by import sort_activities_list


@pytest.fixture
def sample_activities():
    return [
        {"id": "1", "activity": "Read", "type": "fun", "participants": 1, "price": 0.2, "accessibility": 0.5, "link": ""},
        {"id": "2", "activity": "Walk", "type": "sport", "participants": 2, "price": 0.0, "accessibility": 0.1, "link": "http://link"},
        {"id": "3", "activity": "Code", "type": "work", "participants": 1, "price": 0.0, "accessibility": 0.2, "link": ""}
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
    new = [{"id": "2", "activity": "WalkDuplicate", "type": "sport", "participants": 2, "price": 0.0, "accessibility": 0.1, "link": "http://link"}]
    updated = add_activities(new, sample_activities)
    ids = [a["id"] for a in updated]
    assert ids.count("2") == 1


def test_filter_by_field(sample_activities):
    filtered = filter_activities_list(sample_activities, field="participants", value="1")
    assert len(filtered) == 2
    assert all(str(a["participants"]) == "1" for a in filtered)


def test_sort_by_field(sample_activities):
    sorted_list = sort_activities_list(sample_activities, field="price", ascending=False)
    prices = [float(a["price"]) for a in sorted_list]
    assert prices == sorted(prices, reverse=True)

    sorted_list2 = sort_activities_list(sample_activities, field="participants", ascending=True)
    participants = [a["participants"] for a in sorted_list2]
    assert participants == sorted(participants)
