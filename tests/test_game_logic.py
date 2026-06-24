from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the high/low hint bug ---
# The original code told the player to "Go HIGHER!" when their guess was
# already too high (and vice versa), pushing guesses in the wrong direction.

def test_too_high_hint_says_go_lower():
    _, message = check_guess(60, 50)
    assert message == "📉 Go LOWER!"


def test_too_low_hint_says_go_higher():
    _, message = check_guess(40, 50)
    assert message == "📈 Go HIGHER!"


# --- Regression tests for the string-secret coercion bug ---
# app.py converts the secret to a str on even attempts. The original
# check_guess fell back to fragile string comparison ("9" > "50" is True),
# producing wrong outcomes. check_guess now coerces both sides to int.

def test_string_secret_too_low():
    # Numerically 9 < 50, even though "9" > "50" as strings.
    outcome, message = check_guess(9, "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_string_secret_win():
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"


def test_string_guess_and_secret_too_high():
    outcome, message = check_guess("60", "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"
