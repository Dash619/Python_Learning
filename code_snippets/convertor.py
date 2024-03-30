def parse(feet_inches_local):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


if __name__ == "__main__":

    feet_inches = input("Enter feet and inches: ")

    parsed = parse(feet_inches)
    result = convert(parsed['feet'], parsed['inches'])


    print(f"{parsed['feet']} feet and inches {parsed['inches']} is equal to {result} meters")

    if result < 1:
        print("Kid is too small for ride")
    else:
        print("Kid can use the slide")
