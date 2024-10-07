import requests
import pytest


@pytest.fixture(scope="session", autouse=True)
def start_stop():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture()
def before_after():
    print("\nBefore testing")
    yield
    print("\nAfter testing")


@pytest.fixture()
def create_post():
    body = {
        "name": "Holidays",
        "data":
            {
                "January": ["New Year Holidays", "Christmas Day"],
                "February": ["Defender of the Fatherland Day"],
                "March": ["International Women’s Day"],
                "May": ["Spring and Labour Holiday", "Victory Day"],
                "June": ["Day of Russia"],
                "November": ["National Unity Day"],
            }
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url="http://167.172.172.115:52353/object", json=body, headers=headers)

    post_id = response.json()["id"]
    print("Post ID:", post_id)

    yield post_id

    requests.delete(url=f"http://167.172.172.115:52353/object/{post_id}")


def test_put_post(create_post, before_after):
    body = {
        "name": "Holidays",
        "data":
            {
                "January": ["New Year Holidays", "Christmas Day"],
                "February": ["Defender of the Fatherland Day"],
                "March": ["International Women’s Day"],
                "April": ["National Unity Day"],
                "May": ["Spring and Labour Holiday", "Victory Day"],
                "June": ["Day of Russia"],
                "July": ["National Unity Day"],
                "September": ["National Unity Day"],
                "October": ["National Unity Day"],
                "November": ["National Unity Day"],
                "December": ["National Unity Day"],
            }
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(
        url=f"http://167.172.172.115:52353/object/{create_post}",
        json=body,
        headers=headers
    )
    # assert response.status_code == 200
    assert len(response.json()["data"]) == 11


def test_patch_post(create_post, before_after):
    body = {
        "name": "Holidays",
        "data":
            {
                "January": ["New Year Holidays", "Christmas Day"],
                "February": ["Defender of the Fatherland Day"],
                "March": ["International Women’s Day"],
                "April": "There are no holidays",
                "May": ["Spring and Labour Holiday", "Victory Day"],
                "June": ["Day of Russia"],
                "July": "There are no holidays",
                "September": "There are no holidays",
                "October": "There are no holidays",
                "November": ["National Unity Day"],
                "December": "There are no holidays",
            }
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.patch(
        url=f"http://167.172.172.115:52353/object/{create_post}",
        json=body,
        headers=headers
    )
    assert response.json()["data"]["April"] == "There are no holidays"


def test_get_post(create_post, before_after):
    headers = {'Content-Type': 'application/json'}

    response = requests.get(
        url=f"http://167.172.172.115:52353/object/{create_post}",
        headers=headers
    )
    assert response.status_code == 200, "Status code should be 200"


@pytest.mark.parametrize("name", ["Holidays", "Vacations", "Celebrations"])
def test_create_post(before_after, name):
    body = {
        "name": name,
        "data": {
            "January": ["New Year Holidays", "Christmas Day"],
            "February": ["Defender of the Fatherland Day"]
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url="http://167.172.172.115:52353/object", json=body, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == name
