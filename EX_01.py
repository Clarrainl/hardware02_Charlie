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
    
    length = float(input("\nLength of the room (m2): "))
    width = float(input("Width of the room (m2): "))
    area = length * width
    print("The total area of the room is", (area), "m2")

    print("Choose material for the floor:")
    for key, value in materials.items():
        print(f"{key}. {value['name']} (${value['cost']}/m2)")

    choice = int(input("\nEnter your material (1/2/3/4/5): "))
    if choice in materials:
        material = materials[choice]
        cost = area * material["cost"]
        total_cost += cost  
        print(f"\n{material['name']} costing ${material['cost']}/m2.")
        print(f"The total cost for this room is: ${cost}\n")


        projects.append({
            "dimensions": f"{length} x {width} m2",
            "material": material["name"],
            "area": area,
            "cost": cost
        })
    else:
        print("Invalid material choice. Please try again.")
        continue

    another = input("Do you want to add another room? (y/n): ").strip().lower()
    if another != "y":
        break

#SAVE
save = input("Do you want to save this project? (y/n): ").strip().lower()
if save == "y":
    with open("multi_room_project_details.txt", "w") as file:
        for i, project in enumerate(projects, 1):
            file.write(f"Room {i}: {project['dimensions']}, {project['material']}, Area: {project['area']:.2f} m2, Cost: ${project['cost']:.2f}\n")
        file.write(f"\nTotal cost for all rooms: ${total_cost:.2f}\n")
    print("Project saved successfully!\n")

print("Adios!")
