"""
1) Create the chore list.
   a) Create a list named `chores`.
   b) Store all chores that need to be completed today.

2) Store the original chore count.
   a) Use `len()` to count the number of chores.
   b) Store the value in `original_count`.
   c) Print how many chores are assigned.

3) Create a completed counter.
   a) Create `completed_count`.
   b) Start it from 0 before any chores are finished.

4) Use a while loop for the checklist.
   a) Repeat while the chore list still has items.
   b) Use `chores[0]` to get the next chore.
   c) Ask the user if the chore is completed.

5) Remove completed chores.
   a) Use `if` to check if the answer is "yes".
   b) Use `pop(0)` to remove the finished chore.
   c) Increase `completed_count` by 1.
   d) Print a success message.

6) Handle unfinished chores.
   a) Use `else` when the chore is not completed.
   b) Remind the user to finish it and check again.

7) Show progress after each check.
   a) Use `len(chores)` to count remaining chores.
   b) Print the number of chores left.
   c) Add a blank line for neat output.

8) Print the completion message.
   a) Show a heading when all chores are complete.
   b) Print a message praising the user.

9) Demonstrate an infinite loop safely.
   a) Create `test_value` and `safety_counter`.
   b) Use a while loop with a condition that does not change.
   c) Increase the safety counter each time.
   d) Use `break` to stop the loop after 3 rounds.

10) Print the final checklist summary.
   a) Print the chore checklist summary heading.
   b) Show chores assigned, completed, and remaining.
   c) Print a closing line to complete the summary.
"""