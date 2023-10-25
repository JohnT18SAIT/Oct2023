pi = 3.14159

def circumference(radius):
    circumference = 2 * pi * radius
    return circumference

def area(radius):
    area = pi * radius**2
    return area

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("Welcome to the Circle Calculator!")

    radius = get_positive_float("Enter the radius of the circle: ")
    circumference = circumference(radius)
    area = area(radius)

    print(f"The circumference of the circle with radius {radius} is {circumference:.2f}.")
    print(f"The area of the circle with radius {radius} is {area:.2f}.")