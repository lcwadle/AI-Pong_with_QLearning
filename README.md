# Pong-with-QLearning

## Single Player

### Markov Decision Process (MDP)
**State:** A tuple (ball_x, ball_y, velocity_x, velocity_y, paddle_y)
* ball_x and ball_y are real numbers on the interval [0,1]
* x=0, y=0, and y=1 are walls
* the ball bounces off a wall when it hits it
* x=1 is the plane for the paddle
* abs(velocity_x) >= 0.03
* paddle_y is the top of the paddle and is on the interval [0, 1-paddle_height]
* paddle_height=0.2

**Actions:** {none, paddle_y +/- 0.04}
* paddle_y >= 0
* paddle_y + paddle_height <= 1

**Rewards:**
* +1 on paddle bounce
* -1 on ball_x > 1
* 0 in all other states

**Initial State:** (0.5, 0.5, 0.03, 0.01, 0.5 - paddle_height / 2)
* ball in center
* paddle in middle

**Termination:** 
* ball_x > 1

### Game Loop
1. Increment ball_x and ball_y by velocity_x and velocity_y respectfully
2. Check for bounce
  **Ball hit top of screen**
  ball_y < 0, ball_y = -ball_y and velocity_y = -velocity_y
  **Ball hit bottom of screen**
  ball_y > 1, ball_y = 2 - ball_y and velocity_y = -velocity_y
  **Ball hit left screen**
  ball_x < 0, ball_x = -ball_x and velocity_x = -velocity_x
  **Ball hit paddle**
  ball_x > 1 and paddle_y >= ball_y >= paddle_y - paddle_height,
        ball_x = 2 - ball_x and
        velocity_x = -velocity_x + U and
        velocity_y = velocity_y + V
        where U is chosen uniformly on [-0.015, 0.015] and
        V is chosen uniformly on [-0.03, 0.03]
        
### Q-Learning
Because the state space is currently continuous we have to convert it to be discrete and finite for Q-Learning to work.

* board is a 12x12 grid based on ball position, ie 144 possible ball positions
* discretize velocity_x to {-1, +1}
* discretize velocity_y to {-1, 0, -1}, if abs(velocity_y) < 0.015 then 0



## Multiplayer
