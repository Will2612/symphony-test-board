def greet(name: str) -> str:
    """Return a friendly greeting for `name`.

    >>> greet("World")
    'Hello, World!'
    >>> greet("Symphony")
    'Hello, Symphony!'
    """
    return f"Hello, {name}!"


def shout(name: str) -> str:
    """Return a loud greeting for `name`.

    >>> shout("World")
    'HELLO, WORLD!'
    """
    return greet(name).upper()


if __name__ == "__main__":
    print(greet("World"))
