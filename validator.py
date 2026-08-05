def validate_hint(secret, guess, hint):

    if guess > secret and hint == "Too High":
        return True

    if guess < secret and hint == "Too Low":
        return True

    if guess == secret and hint == "Correct":
        return True

    return False