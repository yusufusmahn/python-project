def add_task(store, description):
	task = {"description": description}
	store.append(task)
	return "Task added"


def view_tasks(store):
	if len(store) == 0:
		return "No task added, Kindly select one to add a task"

	else:
		result = "My tasks\n"
		for i in range(len(store)):
			result += f"{i + 1}. {store[i]['description']}\n"
	return result



def mark_task_as_completed(store, user, completed_tasks):
	if len(store) == 0:
		return "No task added, Kindly select one to add a task"

	else:
		if user >= 0 and user < len(store):
			completed_tasks.append(user)
			return f"Task '{store[user]['description']}' marked as completed!"
	return "Invalid task number!"
			


def delete_task(store, user_input):
	if len(store) == 0:
		return "No task added, Kindly select one to add a task"

	else:
		if user_input >= 0 and user_input < len(store):
			deleted_task = store.pop(user_input)
			return f"Task '{deleted_task['description']}' deleted!"			




def main():

	store = []
	completed_tasks = []
	
	print("TO-DO LIST MANAGER")
	print("=======================")
	
	while True:
		print("""
1. Add a task
2. View taks
3. Mark task as completed
4. Delete a task
5. Exit
""")

		choice = int(input("Select an option to continue: "))
		while choice not in {1,2,3,4,5}:
			choice = int(input("Invalid option, Kindly select options between 1 and 5: "))

		if choice == 1:
			description = input("Enter the task: ")
			result = add_task(store, description)
			print(result)

		elif choice == 2:

			result = view_tasks(store)
			print(result)

		elif choice == 3:
			user = int(input("Enter completed task: "))
			result = mark_task_as_completed(store, user, completed_tasks)
			print(result)

		elif choice == 4:
			user_input = int(input("Enter completed task: "))
			result = delete_task(store, user_input)
			print(result)


		elif choice == 5:

			print("Exiting the app!!!")
			break



main()
