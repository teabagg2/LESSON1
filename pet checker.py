# Pet Care Checklist Program

# List of pet care tasks
tasks = [
    "Feed the pet",
    "Give fresh water",
    "Take the pet for a walk",
    "Brush the pet",
    "Clean the food bowl"
]

completed = 0

print("=== Pet Care Checklist ===\n")

# Show one task at a time
while tasks:
    task = tasks[0]
    print(f"Task: {task}")

    answer = input("Is this task complete? (yes/no): ").strip().lower()

    if answer == "yes":
        tasks.pop(0)          # Remove completed task
        completed += 1        # Count completed tasks
        print("Task completed!\n")
    else:
        print("Complete this task before moving on.\n")

# Final summary
print("=== Daily Summary ===")
print(f"Tasks completed: {completed}")
print("All pet care tasks are finished!")

# -----------------------------------------
# Safe example of an infinite loop using break
# -----------------------------------------

print("\nSafe Infinite Loop Example:")

count = 0

while True:
    print("Checking pet status...")
    count += 1

    if count == 3:
        print("Stopping the loop safely.")
        break