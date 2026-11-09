
def add_training(trainings, client, date, time):
    trainings.append((client, date, time))
    return "Training added successfully!"

def list_trainings(trainings):
    if len(trainings) == 0:
        return "No trainings available."
    else:
        result = "List of Trainings:\n"
        numer = 1
        for training in trainings:
            result += f"{numer}. {training[0]} - {training[1]} at {training[2]}\n"
            numer += 1
        return result

def delete_training(trainings,number):
    if len(trainings) == 0:
        raise ValueError("No trainings available to delete.")

    if number >=1 and number <= len(trainings):
        del trainings[number - 1]
        return "Training deleted successfully!"
    else:
        return "Invalid training number. Please try again."

       
def find_client_trainings(trainings,client_name):
    for training in trainings:
      if client_name == training[0]:
        return f"Trainings for {client_name}:\n{training[0]} - {training[1]} at {training[2]}"

    return "Client not found."

if __name__ == "__main__":
 trainings = []

 while True:
    print("\n===== FITNESS CENTER =====")
    print("1. Add training")
    print("2. Show all trainings")
    print("3. Delete training")
    print("4. Find client trainings")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
       client = input("Enter the name of the client: ")
       date = input("Enter the date of the training (DD.MM): ")
       time = input("Enter the time of the training (HH:MM): ")
       print(add_training(trainings, client, date, time))

    elif choice == "2":
       print(list_trainings(trainings))

    elif choice == "3":
        number = int(input("Enter the number of the training to delete: "))
        print(delete_training(trainings, number))

    elif choice == "4": 
        client_name = input("Enter the name of the client: ")
        print(find_client_trainings(trainings, client_name))   

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")  
              