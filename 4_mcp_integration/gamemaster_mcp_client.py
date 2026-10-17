from strands import Agent
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client

mcp_dice_client = MCPClient(
    lambda: streamablehttp_client("http://localhost:8002/mcp")
)

gamemaster = Agent(
    tools=[mcp_dice_client],
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in D&D adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about D&D mechanics, always use the appropriate tools when applicable - never make up results!"""
)

if __name__ == "__main__":
    gamemaster("Help me create a new D&D character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")
