print("Hey! Welcome to Building Material Cost Estimator")

materials = {
    1: {"name": "Wood", "cost": 8},
    2: {"name": "Concrete", "cost": 12},
    3: {"name": "Brick", "cost": 10},
    4: {"name": "Tiles", "cost": 5},
    5: {"name": "Steel", "cost": 20},
}

projects = []
total_cost = 0 

while True:
    try:
        # Validate the length input
        while True:
            try:
                length = float(input("\nLength of the room (m2): "))
                if length <= 0:
                    print("Length must be a positive number. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Validate the width input
        while True:
            try:
                width = float(input("Width of the room (m2): "))
                if width <= 0:
                    print("Width must be a positive number. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        area = length * width
        print("The total area of the room is", (area), "m2")

        # Material selection
        print("Choose material for the floor:")
        for key, value in materials.items():
            print(f"{key}. {value['name']} (${value['cost']}/m2)")

        while True:
            try:
                choice = int(input("\nEnter your material (1/2/3/4/5): "))
                if choice in materials:
                    material = materials[choice]
                    break
                else:
                    print("Invalid choice. Please select a valid material (1/2/3/4/5).")
            except ValueError:
                print("Invalid input. Please enter a numeric value (1/2/3/4/5).")

        cost = area * material["cost"]
        total_cost += cost
        print(f"\n{material['name']} costing ${material['cost']}/m2.")
        print(f"The total cost for this room is: ${cost:.2f}\n")

        # Add the room details to the project
        projects.append({
            "dimensions": f"{length} x {width} m2",
            "material": material["name"],
            "area": area,
            "cost": cost
        })

        # Ask if the user wants to add another room
        another = input("Do you want to add another room? (y/n): ").strip().lower()
        if another not in ["y", "yes"]:
            break

    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")
        continue

# Save project details
try:
    save = input("Do you want to save this project? (y/n): ").strip().lower()
    if save in ["y", "yes"]:
        with open("multi_room_project_details.txt", "w") as file:
            for i, project in enumerate(projects, 1):
                file.write(f"Room {i}: {project['dimensions']}, {project['material']}, Area: {project['area']:.2f} m2, Cost: ${project['cost']:.2f}\n")
            file.write(f"\nTotal cost for all rooms: ${total_cost:.2f}\n")
        print("Project saved successfully!\n")
except IOError:
    print("Error: Unable to save the file. Please check your file permissions.")

print("Adios!")
