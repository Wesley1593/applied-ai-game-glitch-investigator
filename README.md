# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

This project involved using an AI coding assistant as a debugging and refactoring partner. The AI helped identify bugs, suggest code improvements, and create tests to verify fixes.

I used AI to move the check_guess function from app.py into logic_utils.py, which separated game logic from UI code. I also used AI suggestions to identify incorrect hint behavior and fix the comparison logic.

I verified every change by reviewing the code, running pytest, and manually testing the Streamlit game.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 40.
2. The game checks the guess against the secret number and returns "Too Low".
3. User enters a guess of 70.
4. The game returns "Too High" and tells the user to guess lower.
5. User enters the correct guess.
6. The game returns "Win" and the game ends successfully.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```text
tests/test_game_logic.py::test_winning_guess PASSED                      [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 42%]
tests/test_game_logic.py::test_guess_below_secret_returns_too_low PASSED [ 57%]
tests/test_game_logic.py::test_off_by_one_boundaries PASSED              [ 71%]
tests/test_game_logic.py::test_extreme_range_values PASSED               [ 85%]
tests/test_game_logic.py::test_zero_and_negative_guesses PASSED          [100%]

============================== 7 passed in 0.04s ==============================
```

