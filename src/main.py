# src/main.py

import os
from .utils import create_greeting # Relative import from utils.py

def run_greeter():
    """
    Main function to run the personalized greeter.
    Reads names from a file and prints greetings.
    """
    print("✨ Starting the Personalized Greeter! ✨\n")

    # Construct the path to the names.txt file robustly
    # os.path.abspath(__file__) gives the full path to main.py
    # os.path.dirname(...) removes the filename, giving the directory (e.g., .../my_greeter_project/src)
    # os.path.dirname(...) again goes up to the project root (e.g., .../my_greeter_project)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    names_file_path = os.path.join(project_root, 'data', 'names.txt')

    names_to_greet = []
    try:
        with open(names_file_path, 'r') as f:
            # Read names, strip whitespace, and ignore empty lines
            names_to_greet = [line.strip() for line in f if line.strip()]
        print(f"Successfully loaded names from: {names_file_path}")
    except FileNotFoundError:
        print(f"Warning: '{names_file_path}' not found. Using default names.")
        names_to_greet = ["Alice", "Bob", "Charlie", "Diana"]
    except Exception as e:
        print(f"An error occurred while reading the names file: {e}. Using default names.")
        names_to_greet = ["Alice", "Bob", "Charlie", "Diana"]


    if not names_to_greet:
        print("No names found in the file or after processing. Using default names.")
        names_to_greet = ["Alice", "Bob", "Charlie", "Diana"]


    # Print greetings for each name
    for name in names_to_greet:
        print(create_greeting(name))

    print("\n✅ Greeter finished successfully! ✅")

# This ensures run_greeter() is called only when main.py is executed directly
if __name__ == "__main__":
    run_greeter()