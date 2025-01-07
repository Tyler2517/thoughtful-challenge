def sort(width, height, length, mass):
    """
    Sorts a package based on its dimensions and mass into the appropriate stack.

    :param width: Width of the package in centimeters (must be a positive number).
    :param height: Height of the package in centimeters (must be a positive number).
    :param length: Length of the package in centimeters (must be a positive number).
    :param mass: Mass of the package in kilograms (must be a positive number).
    :return: A string indicating the stack: 'STANDARD', 'SPECIAL', or 'REJECTED'.
    :raises ValueError: If any input is not a positive number.
    """
    # Validate inputs
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)) or not isinstance(length, (int, float)) or not isinstance(mass, (int, float)):
        raise ValueError("All inputs must be numbers (int or float).")
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All inputs must be positive numbers.")
    
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
