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
def pre_and_post_conditions():
    """Пре и пост условия"""
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


@pytest.fixture()
def pre_condition():
    """Предусловие"""
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


def test_edit_object_with_put_method(pre_and_post_conditions, before_after):
    """Редактирование объекта с помощью метода PUT"""
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
        url=f"http://167.172.172.115:52353/object/{pre_and_post_conditions}",
        json=body,
        headers=headers
    )
    # assert response.status_code == 200
    assert len(response.json()["data"]) == 11


def test_edit_object_with_patch_method(pre_and_post_conditions, before_after):
    """Редактирование объекта с помощью метода PATCH"""
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
        url=f"http://167.172.172.115:52353/object/{pre_and_post_conditions}",
        json=body,
        headers=headers
    )
    assert response.json()["data"]["April"] == "There are no holidays"


def test_get_object(pre_and_post_conditions, before_after):
    """Получение объекта с помощью метода GET"""
    headers = {'Content-Type': 'application/json'}

    response = requests.get(
        url=f"http://167.172.172.115:52353/object/{pre_and_post_conditions}",
        headers=headers
    )
    assert response.status_code == 200, "Status code should be 200"


@pytest.mark.parametrize("name", ["Holidays", "Vacations", "Celebrations"])
def test_create_object(before_after, name):
    """Создание объекта с помощью метода POST"""
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


def test_delete_object(before_after, pre_condition):
    """Удаление объекта с помощью метода delete"""
    response = requests.delete(url=f"http://167.172.172.115:52353/object/{pre_condition}")
    assert response.status_code == 200
