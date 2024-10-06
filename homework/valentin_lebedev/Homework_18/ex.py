import requests


def get_post(id_post):
    headers = {'Content-Type': 'application/json'}

    response = requests.get(
        url=f"http://167.172.172.115:52353/object/{id_post}",
        headers=headers
    )
    assert response.json()["name"] == "Holidays"
    return response


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

    response = requests.post(
        url="http://167.172.172.115:52353/object",
        json=body,
        headers=headers
    )
    assert response.status_code == 200
    return response


def put_post():
    id_post = create_post().json()["id"]
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
        url=f"http://167.172.172.115:52353/object/{id_post}",
        json=body,
        headers=headers
    )
    assert len(response.json()["data"]) == 11
    return response


def patch_post():
    id_post = create_post().json()["id"]
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
        url=f"http://167.172.172.115:52353/object/{id_post}",
        json=body,
        headers=headers
    )
    assert response.json()["data"]["April"] == "There are no holidays"
    return response


print("Пост создан с id: ", create_post().json()["id"])
print("Пост:", get_post(create_post().json()["id"]).json(), sep="\n")
print("Пост изменен методом PUT", put_post().json(), sep="\n")
print("Пост изменен методом PATCH", patch_post().json(), sep="\n")
