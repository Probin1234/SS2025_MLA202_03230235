## RL Module Practicals  

Name: Probin Monger  
Student Number: 30230235  

Reflection  

## Q. A brief summary of the tasks you completed.  
Ans:  
In Exercise 1, I worked with the CartPole-v1 environment. I set up the environment with `render_mode="human"` and printed out both the action space and observation space. I also ran the agent with completely random actions for one episode to observe the reward system.  

In Exercise 2, I adapted the FrozenLake-v1 code by removing unnecessary delays (`render()`, `time.sleep()`, and extra prints) to make the execution faster. I introduced an outer loop to run the environment for "1000 episodes", and I kept track of rewards using a list. At the end, I calculated the average reward from all episodes to evaluate how poorly a random agent performs.  


### Q. The answers to the questions from Exercise 1 about the CartPole environment's action and observation spaces.  
**Ans:**  
- **Action Space:**  
  - Type: `Discrete(2)`  
  - Meaning: There are two possible moves → `0` (push cart to the left) and `1` (push cart to the right).  

- **Observation Space:**  
  - Type: `Box(4,)` → A continuous space with four values.  
  - The four values represent:  
    1. Cart position (location of the cart on the track)  
    2. Cart velocity (speed and direction of the cart)  
    3. Pole angle (how far the pole is tilted)  
    4. Pole angular velocity (the speed at which the pole is rotating/falling)  

---

### Q. Run the random agent for one episode. What does the reward seem to represent in this environment?  
**Ans:**  
The reward increases by **+1 for every step** the pole remains balanced. If the pole falls or the cart moves out of bounds, the episode stops and no further rewards are given.  

---

### Q. The final average reward you calculated for the random agent in Exercise 2.  
**Ans:**  
From running the random agent for **1000 episodes**, I got an **average reward of around 0.0150**. (The exact value may vary slightly depending on randomness).  

---

### Q. A section on challenges: What was the most difficult part of this practical for you?  
**Ans:**  
The biggest challenge was making sure I understood the **step function outputs** (`observation, reward, terminated, truncated, info`). At first it was a bit confusing to track both `terminated` and `truncated`, but once I structured the loop properly it worked fine. Another challenge was making sure the results averaged correctly across all episodes.  

---

### Q. A section on key takeaways: What is the most important or surprising thing you learned?  
**Ans:**  
The most interesting takeaway for me was seeing how **ineffective random agents are**. Even after running 1000 episodes, the average reward was extremely low, proving that random guessing doesn’t work well in reinforcement learning. This highlighted the need for proper algorithms like **Q-Learning** that can learn from experience and actually improve performance.  
