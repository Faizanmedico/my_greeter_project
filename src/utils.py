# src/utils.py

def create_greeting(name):
    """
    Generates a personalized greeting message for a given name.
    """
    if not isinstance(name, str) or not name.strip():
        return "Hello there! Welcome."
    return f"Hello, {name.strip().title()}! Welcome to our simple greeter application."

if __name__ == '__main__':
    # This block runs only when utils.py is executed directly
    # Useful for testing individual functions
    print(create_greeting("alice"))
    print(create_greeting("bob"))
    print(create_greeting(""))