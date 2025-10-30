"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Bryce Joseph]
Date: [Oct 24, 2025]

AI Usage: There was no AI used for this project
Example: AI helped with file I/O error handling logic in save_character function
"""

import os

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    stats = calculate_stats(character_class, 1)
    #returns dictionary of character values
    return {"name" : name, "class" : character_class, "level" : 1, "strength" : stats[0], "magic" : stats[1], "health" : stats[2], "gold" : 100}

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)

    #initializes stats list depending on character chosen
    if character_class == "Warrior":
        stats = [15, 5, 120]
    elif character_class == "Mage":
        stats = [5, 15, 80]
    elif character_class == "Rogue":
        stats = [10, 10, 40]
    else:
        stats = [10, 15, 120]
    #multiply base stats by level
    stats[0] *= level
    stats[1] *= level
    stats[2] *= level
    #return stats as tuple instead of list
    return tuple(stats)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully

    #titles used when writing to the file
    titles = [
        "Character Name",
        "Class",
        "Level",
        "Strength",
        "Magic",
        "Health",
        "Gold"]
    #mac specifically cannot have "/" in a file name, this returns False if / is in the file name
    if filename.find("/") != -1:
        return False
    #writes characteristics of character to file and returns True
    with open(filename, "w") as file:
        for i in range(7):
            file.write(f"{titles[i]}: {list(character.values())[i]}\n")
    file.close()
    return True

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors

    #keys used to form character dictionary
    keys = [
        "name",
        "class",
        "level",
        "strength",
        "magic",
        "health",
        "gold"]
    #check if path exists
    if os.path.exists(filename):
        character = {}
        with open(filename, "r") as file:
            #loop to get values for character dictionary
            for i, line in enumerate(file):
                key = keys[i]
                val = line[line.find(": ")+2:line.find("\n")]
                if val.isdigit():
                    val = int(val)
                character[key] = val
        file.close()
        return character

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function

    #print the character sheet
    print("=== CHARACTER SHEET ===")
    for key, val in character.items():
        print(f"{key.capitalize()}: {val}")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level

    #increase level in character dictionary and update stats with calculate_stats then assign stats to character dictionary accordingly
    character["level"] += 1
    stats = calculate_stats(character["class"], character["level"])
    character["strength"] = stats[0]
    character["magic"] = stats[1]
    character["health"] = stats[2]

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")

    #testing example
    char = create_character("TestHero", "Warrior")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")