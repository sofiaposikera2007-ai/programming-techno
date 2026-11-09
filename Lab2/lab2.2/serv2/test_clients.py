
import unittest
from fastapi.testclient import TestClient
from clients_service import app, clients

client = TestClient(app)


class TestClientsService(unittest.TestCase):

    def setUp(self):
        # Очищаємо список перед кожним тестом
        clients.clear()

        # Додаємо тестових клієнтів
        clients.append({"name": "Sasha"})
        clients.append({"name": "Dasha"})

    def test_add_client(self):
        response = client.post(
            "/clients",
            json={"name": "Solomia"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["message"],
            "Client added successfully!"
        )
        self.assertEqual(len(clients), 3)

    def test_add_existing_client(self):
        response = client.post(
            "/clients",
            json={"name": "Sasha"}
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()["detail"],
            "Client already exists."
        )

    @unittest.expectedFailure
    def test_add_wrong_count(self):
            client.post("/clients", json={"name": "Solomia"})
            self.assertEqual(len(clients), 5)    

    def test_list_clients(self):
        response = client.get("/clients")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]["name"], "Sasha")

    def test_list_clients_empty(self):
        clients.clear()

        response = client.get("/clients")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["message"],
            "No clients available."
        )

    def test_find_client(self):
        response = client.get("/clients/Dasha")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Dasha")

    def test_find_client_not_found(self):
        response = client.get("/clients/Nobody")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json()["detail"],
            "Client not found."
        )

if __name__ == "__main__":
    unittest.main()
