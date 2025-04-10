import sys
import os

# Add the src directory to the Python path
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
sys.path.insert(0, src_path)

from blender_mcp.server import main as server_main

def main():
    """Entry point for the blender-mcp package"""
    server_main()

if __name__ == "__main__":
    main()
