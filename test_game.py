import game
import pytest

def test_game_str_rock():
    # Arrange
    x: str = "rock"
    expected: int = 2

    # Activate
    actual: int = game.check_validity(x)

    # Assert
    assert actual == expected


def test_game_str_scissors():
    # Arrange
    x: str = "scissors"
    expected: int = 1

    # Activate
    actual: int = game.check_validity(x)

    # Assert
    assert actual == expected

def test_game_str_paper():
    # Arrange
    x: str = "paper"
    expected: int = 0

    # Activate
    actual: int = game.check_validity(x)

    # Assert
    assert actual == expected


def test_game_str_rock_capital():
    # Arrange
    x: str = "Rock"
    expected: int = 2

    # Activate
    actual: int = game.check_validity(x)

    # Assert
    assert actual == expected


def test_game_str_scissors_capital():
    # Arrange
    x: str = "Scissors"
    expected: int = 1

    # Activate
    actual: int = game.check_validity(x)

    # Assert
    assert actual == expected


def test_game_str_paper_capital():
    # Arrange
    x: str = "Paper"
    expected: int = 0

    # Activate
    actual: int = game.check_validity(x)

    # Assert
    assert actual == expected

def test_game_error():
    x: str = "rockk"
    with pytest.raises(ZeroDivisionError) as ex:
        actual: int = game.check_validity(x)

    assert str(ex.value) == "Wrong string!"


def test_game_tie1():
    # Arrange
    x: int = 2
    y: int = 2
    expected: int = 0

    # Activate
    actual: int = game.check_winner(x, y)

    # Assert
    assert actual == expected


def test_game_player2_1():
    # Arrange
    x: int = 2
    y: int = 0
    expected: int = 2

    # Activate
    actual: int = game.check_winner(x, y)

    # Assert
    assert actual == expected


def test_game_player1_1():
    # Arrange
    x: int = 2
    y: int = 1
    expected: int = 1

    # Activate
    actual: int = game.check_winner(x, y)

    # Assert
    assert actual == expected


def test_game_player1_2():
    # Arrange
    x: int = 0
    y: int = 2
    expected: int = 1

    # Activate
    actual: int = game.check_winner(x, y)

    # Assert
    assert actual == expected


def test_game_tie2():
    # Arrange
    x: int = 0
    y: int = 0
    expected: int = 0

    # Activate
    actual: int = game.check_winner(x, y)

    # Assert
    assert actual == expected


def test_game_player2_2():
    # Arrange
    x: int = 0
    y: int = 1
    expected: int = 2

    # Activate
    actual: int = game.check_winner(x, y)

    # Assert
    assert actual == expected


def test_game_player2_3():
    # Arrange
    x: int = 1
    y: int = 2
    expected: int = 2

    # Activate
    actual: int = game.check_winner(x, y)

    # Assert
    assert actual == expected


def test_game_player1_3():
    # Arrange
    x: int = 1
    y: int = 0
    expected: int = 1

    # Activate
    actual: int = game.check_winner(x, y)

    # Assert
    assert actual == expected


def test_game_tie3():
    # Arrange
    x: int = 1
    y: int = 1
    expected: int = 0

    # Activate
    actual: int = game.check_winner(x, y)

    # Assert
    assert actual == expected


def test_game_wrong_option():
    x: int = 1
    y: int = 1
    expected: int = 2
    with pytest.raises(ZeroDivisionError) as ex:
        actual: int = game.check_winner(x, y)

    assert str(ex.value) == "Wrong!"