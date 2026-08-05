"""
Reliability evaluation harness for the Game Glitch Investigator agent.

This script runs the GameAgent against a set of predefined (secret, guess)
cases, checks that the agent's hint and the validator's verification agree
with the expected outcome, and prints a pass/fail summary.

Run it with:
    python eval_harness.py
"""

from agent import GameAgent

agent = GameAgent()

# Each case: (secret, guess, expected_hint)
CASES = [
    (50, 75, "Too High"),
    (50, 20, "Too Low"),
    (50, 50, "Correct"),
    (1, 100, "Too High"),
    (100, 1, "Too Low"),
    (1, 1, "Correct"),
    (50, 49, "Too Low"),
    (50, 51, "Too High"),
]


def run_eval():
    results = []

    for secret, guess, expected_hint in CASES:
        outcome = agent.investigate_guess(secret, guess)

        hint_ok = outcome["hint"] == expected_hint
        verified_ok = outcome["verified"] is True
        passed = hint_ok and verified_ok

        results.append({
            "secret": secret,
            "guess": guess,
            "expected_hint": expected_hint,
            "actual_hint": outcome["hint"],
            "verified": outcome["verified"],
            "passed": passed,
        })

    return results


def print_report(results):
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    confidence = passed / total if total else 0

    print("Case | Secret | Guess | Expected | Actual | Verified | Result")
    print("-" * 70)
    for i, r in enumerate(results, start=1):
        status = "PASS" if r["passed"] else "FAIL"
        print(
            f"{i:>4} | {r['secret']:>6} | {r['guess']:>5} | "
            f"{r['expected_hint']:<8} | {r['actual_hint']:<8} | "
            f"{str(r['verified']):<8} | {status}"
        )

    print("-" * 70)
    print(f"Summary: {passed}/{total} cases passed "
          f"(confidence score: {confidence:.2f})")


if __name__ == "__main__":
    print_report(run_eval())