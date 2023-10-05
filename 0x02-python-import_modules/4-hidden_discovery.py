#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    functions = dir(hidden_4)
    for f in functions:
        if f[:2] != "__":
            print(f)

