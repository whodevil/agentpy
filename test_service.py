import requests

print(
    requests.post(
        "http://0.0.0.0:10000",
        json={
            "query": "Best practices for building AI Agents?"
        }
    ).json()
)
