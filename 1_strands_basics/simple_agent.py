import logging

from strands import Agent

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

agent = Agent(system_prompt="You are a game master for a Dungeon & Dragon game")

if __name__ == "__main__":
    agent("Hi, I am an adventurer ready for adventure!")
