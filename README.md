# Pong-with-QLearning

## Single Player

State: A tuple (ball_x, ball_y, velocity_x, velocity_y, paddle_y)
* ball_x and ball_y are real numbers on the interval [0,1]
* x=0, y=0, and y=1 are walls
* the ball bounces off a wall when it hits it
* x=1 is the plane for the paddle
* abs(velocity_x) >= 0.03
* paddle_y is the top of the paddle and is on the interval [0, 1-paddle_height]
* paddle_height=0.2

Actions: {none, paddle_y +/- 0.04}
* paddle_y >= 0
* paddle_y + paddle_height <= 1

Rewards:
* +1 on paddle bounce
* -1 on ball_x > 1
* 0 in all other states

Initial State: (0.5, 0.5, 0.03, 0.01, 0.5 - paddle_height / 2)
* ball in center
* paddle in middle

Termination: 
* ball_x > 1

## Multiplayer
