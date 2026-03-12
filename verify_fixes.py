import traceback
import sys

def check_imports():
    print("Python version:", sys.version)
    
    try:
        import agents
        from agents import Agent, Runner, set_default_openai_key
        print("OK: agents and top-level members imported")
    except ImportError as e:
        print("ERROR: Failed to import from agents")
        traceback.print_exc()

    try:
        from manager import TourManager
        print("OK: TourManager imported")
    except Exception as e:
        print("ERROR: Failed to import TourManager")
        traceback.print_exc()

    try:
        import agent
        print("OK: agent module imported")
    except Exception as e:
        print("ERROR: Failed to import agent module")
        traceback.print_exc()

if __name__ == "__main__":
    check_imports()
    print("Verification finished.")
