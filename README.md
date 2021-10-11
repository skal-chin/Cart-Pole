# Cart and Pole Control Problem

---

The cart and pole problem gives the user a cart of a specific mass that
can only move in a 1-dimensional direction. The is a pole balanced vertically
from the middle of the cart. The objective is to write a control that
keeps the pole vertical by moving the cart either left or right. This
program produces a solution based on the observations of the pole angle to
the cart and the cart's velocity in either left or right direction.

## Dependencies

---

OpenAI Gym -> `pip install gym` \
NumPy	   -> `pip install numpy`

## Execute

---

In a command or git bash window, run `python cart-pole.py`

You should see the following window:

![1 episode of cart and pole](https://github.com/skal-chin/Cart-and-Pole/blob/main/Images/cp_1.gif =250x)

## Modify

---

  The file at its current state does 10 episode with 201 steps in each episode (the
  episode terminates at step 200 as per the environment's requirement). The episodes
  can be changed within the file.

  To Modify how the action is chosen, change the choose_action function.


## Results

---

The problem is considered solved with an average of 195 achieved steps over 100
episodes. The solution given here, as is, results in 189.44. So it is not solved,
but it came really close. It would not be good for a real bot and track since the
cart moves to the left infinitely.
