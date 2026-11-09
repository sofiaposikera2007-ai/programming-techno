
import unittest
from fastapi.testclient import TestClient
from training_service import app, trainings

client = TestClient(app)


class TestTrainingsService(unittest.TestCase):

    def setUp(self):
        # Очищаємо список перед кожним тестом
        trainings.clear()

        # Додаємо початкові дані
        trainings.append(
            type("TrainingData", (), {
                "client": "Sasha",
                "date": "01.10",
                "time": "10:00"
            })()
        )
        trainings.append(
            type("TrainingData", (), {
                "client": "Dasha",
                "date": "02.10",
                "time": "12:30"
            })()
        )

    def test_add_training(self):
        response = client.post(
            "/trainings",
            json={
                "client": "Solomia",
                "date": "03.10",
                "time": "18:00"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["message"],
            "Training added successfully!"
        )
        self.assertEqual(len(trainings), 3)

    @unittest.expectedFailure
    def test_add_wrong_count(self):
            client.post(
                "/trainings",
                json={"client": "Solomia", "date": "03.10", "time": "18:00"},
            )
            self.assertEqual(len(trainings), 5)
     
    def test_list_trainings(self):
        response = client.get("/trainings")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]["client"], "Sasha")

    def test_list_empty(self):
        trainings.clear()

        response = client.get("/trainings")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["message"],
            "No trainings available."
        )

    def test_delete_training(self):
        response = client.delete("/trainings/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["message"],
            "Training deleted successfully!"
        )
        self.assertEqual(len(trainings), 1)

    def test_delete_invalid_number(self):
        response = client.delete("/trainings/10")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json()["detail"],
            "Invalid training number. Please try again."
        )

    def test_delete_empty(self):
        trainings.clear()

        response = client.delete("/trainings/1")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json()["detail"],
            "No trainings available to delete."
        )

    def test_find_client(self):
        response = client.get("/trainings/client/Dasha")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["date"], "02.10")

    def test_find_client_not_found(self):
        response = client.get("/trainings/client/Nobody")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json()["detail"],
            "Client not found."
        )

if __name__ == "__main__":
    unittest.main()
