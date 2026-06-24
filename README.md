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

- [ ] Describe the game's purpose.

The game's purpose is for a user to discover a secret number. As the user guesses numbers between 1 and 100, the game tells whether the guess is too high or too low compared to the secret number. The user uses these hints to guess the secret number.

- [ ] Detail which bugs you found.

1 - "Go higher" and "Go lower" messages were swapped
2 - Game would not properly restart after the game is over and user click in "new game"

- [ ] Explain what fixes you applied.

- Fixed the logic for the messages "go lower" and "go higher". Now when the guess is lower than the secret number, it says go higher, and when the guess is higher, it says go lower

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step --> User enters a guess of 1
2. <!-- Describe this step --> If 1 is not correct answer, game returns "Too Low"
3. <!-- Describe this step --> User enters a guess of 100 -> "Too high" if not the correct answer
4. <!-- Describe this step --> Score updates after each guess
5. <!-- Add more steps as needed --> Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
