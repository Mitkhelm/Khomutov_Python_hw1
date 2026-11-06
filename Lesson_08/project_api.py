import requests

class ProjectApi:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create(self, body):
        return requests.post(
            f"{self.base_url}/projects", headers=self.headers, json=body
        )

    def update(self, project_id, body):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            json=body,
        )

    def get(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}", headers=self.headers
        )
