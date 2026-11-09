import unittest
from unittest.mock import patch
from trainingss import add_training, list_trainings, delete_training, find_client_trainings

class TestTrainings(unittest.TestCase):

    def setUp(self):
                # Створюємо окремий список перед кожним тестом
                self.trainings = []
                self.trainings.append(("Sasha",  "01.10", "10:00"))
                self.trainings.append(("Dasha", "02.10", "12:30"))     

    @unittest.expectedFailure
    def test_add(self):
        with patch("builtins.input", side_effect=["Solomia", "03.10", "18:00"]):
         result = add_training(self.trainings, "Solomia", "03.10", "18:00")
        self.assertEqual(result, "Training added successfully!")
        self.assertEqual(len(self.trainings), 5)

    def test_list(self):
        result = list_trainings(self.trainings)
        self.assertIn("1. Sasha - 01.10 at 10:00", result)
        self.assertIn("2. Dasha - 02.10 at 12:30", result)

    def test_list_empty(self):
        self.trainings.clear()  # Очищаємо список тренувань перед тестом
        self.assertEqual(list_trainings(self.trainings), "No trainings available.")

    def test_delete(self):
        with patch("builtins.input", return_value="1"):
         result = delete_training(self.trainings,1)
        self.assertEqual(result, "Training deleted successfully!")
        self.assertEqual(len(self.trainings), 1)

    def test_delete_wrong_number(self):
        with patch("builtins.input", return_value="10"):
         result = delete_training(self.trainings,10)
        self.assertEqual(result, "Invalid training number. Please try again.")
        self.assertEqual(len(self.trainings), 2)

    def test_delete_empty(self):
        self.trainings.clear()
        with self.assertRaises(ValueError) as context:
            delete_training(self.trainings, 1)
        self.assertEqual(str(context.exception),  "No trainings available to delete.")  

    def test_find(self):
        with patch("builtins.input", return_value="Dasha"):
         result = find_client_trainings(self.trainings,"Dasha")
        self.assertIn("Dasha - 02.10 at 12:30", result)

    def test_find_not_found(self):
        with patch("builtins.input", return_value="Nobody"):
         result = find_client_trainings(self.trainings,"Nobody")
        self.assertEqual(result, "Client not found.") 

if __name__ == "__main__":
    unittest.main()