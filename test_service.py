import requests

print(
    requests.post(
        "http://0.0.0.0:10000",
        json={
            "key": "A_SECRET_KEY_MADE_UP_FOR_THIS_PROJECT",
            "query": "Best practices for building AI Agents?"
        }
    ).json()
)
