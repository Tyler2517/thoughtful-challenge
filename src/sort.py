def sort(width, height, length, mass):
    """
    Sorts a package based on its dimensions and mass into the appropriate stack.

    :param width: Width of the package in centimeters.
    :param height: Height of the package in centimeters.
    :param length: Length of the package in centimeters.
    :param mass: Mass of the package in kilograms.
    :return: A string indicating the stack: 'STANDARD', 'SPECIAL', or 'REJECTED'.
    """
    # Calculate volume
    volume = width * height * length
    
    # Check if the package is bulky
    is_bulky = False
    if volume >= 1_000_000 or max(width, height, length) >= 150:
        is_bulky = True
    
    # Check if the package is heavy
    is_heavy = False
    if mass >= 20:
        is_heavy = True
    
    # Determine the stack
    if is_heavy and is_bulky:
        return "REJECTED"
    
    if is_heavy or is_bulky:
        return "SPECIAL"
    
    return "STANDARD"

# Example Test Cases
print(sort(200, 100, 50, 25))
print(sort(300, 300, 200, 10))
print(sort(10, 10, 10, 1))    
print(sort(200, 200, 200, 25)) 