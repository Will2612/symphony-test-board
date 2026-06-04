from greet import greet, shout


def test_greet_basic() -> None:
    assert greet("World") == "Hello, World!"


def test_greet_empty() -> None:
    # NOTE: current implementation does not handle empty input.
    # This test documents the existing (buggy?) behavior.
    assert greet("") == "Hello, !"


def test_shout_basic() -> None:
    assert shout("World") == "HELLO, WORLD!"


def test_shout_empty() -> None:
    assert shout("") == "HELLO, !"
