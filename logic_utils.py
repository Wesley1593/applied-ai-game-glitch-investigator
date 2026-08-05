def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

# FIX: Refactored check_guess logic into logic_utils.py with AI coding assistant support.
# Verified behavior using pytest tests for Win, Too High, and Too Low cases.


def check_guess(guess, secret):
    """
    Compare a guess to the secret number and return the outcome.

    Args:
        guess: The player's guessed number.
        secret: The secret target number.

    Returns:
        "Win"      if the guess equals the secret,
        "Too Low"  if the guess is below the secret,
        "Too High" if the guess is above the secret.
    """
    if guess == secret:
        return "Win"
    if guess < secret:
        return "Too Low"
    return "Too High"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
