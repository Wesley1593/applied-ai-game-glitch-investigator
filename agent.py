from validator import validate_hint
from logger import log_game


class GameAgent:

    def analyze_guess(self, secret, guess):

        if guess > secret:
            return "Guess is higher than the secret."

        elif guess < secret:
            return "Guess is lower than the secret."

        else:
            return "Guess matches the secret."


    def plan_response(self, secret, guess):

        if guess > secret:
            return "Suggest a lower number."

        elif guess < secret:
            return "Suggest a higher number."

        else:
            return "End game."


    def generate_hint(self, secret, guess):

        if guess > secret:
            return "Too High"

        elif guess < secret:
            return "Too Low"

        else:
            return "Correct"


    def verify_result(self, secret, guess, hint):

        return validate_hint(secret, guess, hint)


    def investigate_guess(self, secret, guess):

        analysis = self.analyze_guess(secret, guess)

        plan = self.plan_response(secret, guess)

        hint = self.generate_hint(secret, guess)

        verified = self.verify_result(secret, guess, hint)


        result = {
            "analysis": analysis,
            "plan": plan,
            "hint": hint,
            "verified": verified
        }


        log_game(result)

        return result