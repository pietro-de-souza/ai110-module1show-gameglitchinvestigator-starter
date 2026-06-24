# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1 - The hints are broken. It always tell me to go lower, no matter if the number is 100 or 1. I expected the message to change if my number was actually lower than the target number by saying "go higher"
2 - Once I run out of guesses, if I want to start a new game, the button to do so doesn't work. The attempt number restart, but when I submit the answers nothing happens, and the message of "game over" continues to appear". I expected the website to allow me to continue submitting answers after I restarted the game, and I also expected the game over message to disappear
3 - When there is still 1 attempt left, the website incorrectly says I am out of attempts and give me the answer. I expected the website to not show me any "out of attempts" message when I still have and attempt left, and I also didn't expect the website to show me the answer before the game is over.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 1      | "go higher"      | "go lower"      |  none                  |
| 129    |"go higher"| "This is not a valid number between 1 and 100| none |
|"new game" | game over disappears and submission is allowed| game over - no submission allowed| Game over. Start a new game to try again. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).



- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
