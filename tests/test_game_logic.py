from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_guess_below_secret_returns_too_low():
    assert check_guess(40, 50) == "Too Low"


# --- Edge cases ---

def test_off_by_one_boundaries():
    # One below the secret is still "Too Low"; one above is still "Too High".
    # This pins down the strict < / > boundary where comparison bugs hide.
    assert check_guess(49, 50) == "Too Low"
    assert check_guess(51, 50) == "Too High"

def test_extreme_range_values():
    # Smallest guess vs. largest secret and vice versa, at the edges of the range.
    assert check_guess(1, 100) == "Too Low"
    assert check_guess(100, 1) == "Too High"
    assert check_guess(1, 1) == "Win"

def test_zero_and_negative_guesses():
    # parse_guess can still produce 0 or negatives; check_guess must handle them.
    assert check_guess(0, 50) == "Too Low"
    assert check_guess(-10, 50) == "Too Low"