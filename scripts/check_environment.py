"""Check the workshop environment locally without invoking a model."""

import importlib
import sys
from importlib.metadata import version
from pathlib import Path


def main() -> None:
    expected = (Path(__file__).resolve().parents[1] / ".python-version").read_text().strip()
    actual = ".".join(map(str, sys.version_info[:3]))
    if actual != expected:
        raise SystemExit(f"Expected Python {expected}; got {actual}. Run uv sync first.")
    if sys.prefix == sys.base_prefix:
        raise SystemExit("Activate .venv first, or use uv run python scripts/check_environment.py")
    print(f"Python {actual} | virtual environment: {sys.prefix}")
    packages = {
        "strands": "strands-agents",
        "strands_harness": "strands-harness",
        "fastapi": "fastapi",
        "pydantic": "pydantic",
        "uvicorn": "uvicorn",
        "chromadb": "chromadb",
        "pypdf": "pypdf",
        "tinydb": "tinydb",
        "mcp": "mcp",
    }
    for module, distribution in packages.items():
        importlib.import_module(module)
        print(f"OK {distribution} {version(distribution)}")
    from strands import Agent
    from mcp.server import FastMCP
    from mcp.client.streamable_http import streamablehttp_client

    print("fours Agent environment ready. No model requests were made.")


if __name__ == "__main__":
    main()
