from strands import Agent, tool

@tool
def roll_dice(faces: int = 6) -> int:
    """Roll one die and return a random result between 1 and the number of faces.

    Use this tool once for every die needed in a D&D roll. For the traditional
    ability-score method, roll four six-sided dice and keep the three highest
    results (4d6, drop lowest).

    Args:
        faces: The number of faces on the die. Must be at least 1; defaults to 6.

    Returns:
        A random integer from 1 through faces, inclusive.
    """

    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)


dice_master = Agent(
    tools=[roll_dice],
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in D&D adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about D&D mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die."""
)

if __name__ == "__main__":
    print(roll_dice.tool_spec)  # what Strands tells the model about your tool
    dice_master("Help me create a new D&D character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")
