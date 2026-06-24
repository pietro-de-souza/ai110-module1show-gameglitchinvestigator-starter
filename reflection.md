# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  Bug 1 - The hints are broken. It always tell me to go lower, no matter if the number is 100 or 1. I expected the message to change if my number was actually lower than the target number by saying "go higher"
Bug 2 - Once I run out of guesses, if I want to start a new game, the button to do so doesn't work. The attempt number restart, but when I submit the answers nothing happens, and the message of "game over" continues to appear". I expected the website to allow me to continue submitting answers after I restarted the game, and I also expected the game over message to disappear
Bug 3 - When there is still 1 attempt left, the website incorrectly says I am out of attempts and give me the answer. I expected the website to not show me any "out of attempts" message when I still have and attempt left, and I also didn't expect the website to show me the answer before the game is over.

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

I used Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Claude correctly identified that when the result was too higher, the programmed message was incorreclty "go higher". To verify, I looked at the code myself. However, for the second bug, I asked Claude follow up questions and asked it to explain to me the logic so that I could verify whether the bug was indeed there.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I didn't get any AI suggestions that were incorrect so far in this project.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I verified the code myself, and I ran the game on the browser and play tested it.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I play tested the game on browser and it showed the messages were appearing correctly. I input 1, and it correctly showed "go higher", since that was not the correct answer. I also input 100, and it correctly showed "go lower", since that was not the answer. This was swapped before.

- Did AI help you design or understand any tests? How?

I asked Claude to create a pytest for me. I didn't really understand how it worked, and it ran everything for me and told me 8 tests passed. Since I didn't understand, I did my own manual test on the browser. UPDATE: I now could run the pytest myself. It's the same one Claude generated for me, but the difference is that now I could run it directly on my terminal. I asked Claude to help me debug the error message I was getting. I needed to run pytest as a module instead for it to work.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I still don't understand what's Streamlit, but from what I've seen in this project, I assume it's a tool. I learned that, like in many other programming tools, you must reset all of its functions to achieve a desired outcome. For example, the code was not reseting its game over message or the submission, and adding lines that explicitly reseted those, corrected the bugs.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

The habit of asking AI to explain its fixes and discoveries before applying them to the code. This prevents me from applying fixes blindly and/or not understanding what's happening

- What is one thing you would do differently next time you work with AI on a coding task?

Sometimes, I didn't quite understand what the AI was doing, but I understood it enough to see that it was right. However, next time, I would ask AI to keep explaining me more about that line of code, so not only I can ensure it's a correct fix, but I can also understand what's the logic behind it.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I didn't use a lot of AI generated code in the past, and I think I viewed it as something that replaces the coding itself. However, now I view AI generated code as more useful and as a copilot that helps coders code repeated lines of code faster, saving time, and helping coders identify bugs faster, rather than replacing the coding itself.