# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Off-by-one boundaries | "Identify edge cases for the check_guess function and generate pytest cases to verify the game handles them correctly." | Tested guesses immediately above and below the secret number. | Yes | Boundary values are important because comparison bugs often occur when values are close to the target. |
| Extreme range values | "Generate pytest cases for unusual inputs that could break check_guess." | Tested extremely large guesses compared to the secret number. | Yes | Large values verify that the comparison logic works correctly beyond normal gameplay ranges. |
| Zero and negative guesses | "Suggest edge cases for a number guessing game and create tests for them." | Tested zero and negative guesses against a positive secret number. | Yes | These inputs verify that invalid or unusual guesses still return the correct Too Low/Too High result. |

All generated tests were reviewed manually and verified by running pytest. The final test result was:
```text
7 passed in 0.04s
```



## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
