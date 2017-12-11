import Ball
import Paddle
import random

class Pong:
    def __init__(self, board_x_size, board_y_size):
        self.board_x_size = board_x_size
        self.board_y_size = board_y_size

        # Create board
        self.grid = []
        for j in range(board_y_size):
            grid_row = []
            for i in range(board_x_size):
                grid_row.append(" ")
            self.grid.append(grid_row)

    def create_ball(self, x, y, init_x_velocity, init_y_velocity):
        # Create ball
        self.ball = Ball.Ball(x, y, init_x_velocity, init_y_velocity)

        # Convert ball to discrete integers based on board size
        #self.ball.x *= self.board_x_size
        #self.ball.y *= self.board_y_size
        #self.ball.x_velocity *= self.board_x_size
        #self.ball.y_velocity *= self.board_y_size

        self.grid[int(self.ball.y*(self.board_y_size-1))][int(self.ball.x*(self.board_x_size-1))] = "*"

    def move_ball(self):
        reward = 0

        #print("Ball - " + str(self.ball.y + self.ball.y_velocity) + "," + str(self.ball.x + self.ball.x_velocity))
        #print("Paddle - " + str(self.paddle.y) + "," + str(self.paddle.y + self.paddle.height))

        # Reset current position to " "
        self.grid[int(self.ball.y*(self.board_y_size-1))][int(self.ball.x*(self.board_x_size-1))] = " "

        # Velocity
        # X velocity
        #if (self.ball.x_velocity > 0):
            #ball_x_velocity = 1
        #else:
            #ball_x_velocity = -1

        # Y velocity
        #if (abs(self.ball_y_velocity) < 0.015):
            #ball_y_velocity = 0
        #elif self.ball.y_velocity > 0:
            #ball_y_velocity = 1
        #else:
            #ball_y_velocity = -1

        # Ball bounce
        # X bounce
        if self.ball.x + self.ball.x_velocity < 0:
            self.ball.x = -self.ball.x
            self.ball.x_velocity = -self.ball.x_velocity

        # Y bounce
        if self.ball.y + self.ball.y_velocity < 0:
            self.ball.y = -self.ball.y
            self.ball.y_velocity = -self.ball.y_velocity
        if self.ball.y + self.ball.y_velocity > 1:
            self.ball.y = 2 - self.ball.y
            self.ball.y_velocity = -self.ball.y_velocity

        # Paddle bounce
        if self.ball.x + self.ball.x_velocity >= 1 and self.ball.y + self.ball.y_velocity >= self.paddle.y and self.ball.y + self.ball.y_velocity <= self.paddle.y + self.paddle.height:
            #print("bounce!")
            self.ball.x = 2 - self.ball.x - self.ball.x_velocity
            #print(self.ball.x)
            self.ball.x_velocity = -self.ball.x_velocity + random.uniform(-0.015, 0.015)
            self.ball.y_velocity = self.ball.y_velocity + random.uniform(-0.03, 0.03)

            # Maintain minimum x velocities
            if self.ball.x_velocity < 0 and self.ball.x_velocity > -0.03:
                self.ball.x_velocity = -0.03
            if self.ball.x_velocity > 0 and self.ball.x_velocity < 0.03:
                self.ball.x_velocity = 0.03

            reward = 1

        self.ball.x = self.ball.x + self.ball.x_velocity
        self.ball.y = self.ball.y + self.ball.y_velocity

        if self.ball.x >= 1:
            #print(self.ball.x)
            reward = -1
            self.ball.missed = True
        else:
            # Update grid display
            #print(str(self.ball.x) + "," + str(self.ball.y))
            #print(str(int(self.ball.y*self.board_y_size)) + "," + str(int(self.ball.x*self.board_x_size)))
            self.grid[int(self.ball.y*(self.board_y_size-1))][int(self.ball.x*(self.board_x_size-1))] = "*"

        return reward

    def create_paddle(self, paddle_y, paddle_height, paddle_speed):
        # Create paddle
        self.paddle = Paddle.Paddle(paddle_y, paddle_height, paddle_speed)

        # Convert paddle to discrete integers based on board size
        #self.paddle.y *= self.board_y_size
        #self.paddle.height *= self.board_y_size

        for i in range(int(self.paddle.height*self.board_y_size)):
            self.grid[int(self.paddle.y*(self.board_y_size-1)+i)][self.board_x_size-1] = "|"

    def move_paddle(self, action):
        # Reset current position to " "
        for i in range(int(self.paddle.height*self.board_y_size)):
            self.grid[int(self.paddle.y*(self.board_y_size-1)+i)][self.board_x_size-1] = " "

        # Move = 1
        if action == 1 and self.paddle.y - self.paddle.speed >= 0:
            #print("Move 1")
            self.paddle.y -= self.paddle.speed
            for i in range(int(self.paddle.height*self.board_y_size)):
                self.grid[int(self.paddle.y*(self.board_y_size-1)+i)][self.board_x_size-1] = "|"
        elif action == 1:
            #print("Move 1")
            self.paddle.y == 0
            for i in range(int(self.paddle.height*self.board_y_size)):
                self.grid[int(self.paddle.y*(self.board_y_size-1)+i)][self.board_x_size-1] = "|"

        # Move = -1
        if action == -1 and self.paddle.y + self.paddle.height + self.paddle.speed <= 1:
            #print("Move -1")
            self.paddle.y += self.paddle.speed
            for i in range(int(self.paddle.height*self.board_y_size)):
                self.grid[int(self.paddle.y*(self.board_y_size-1)+i)][self.board_x_size-1] = "|"
        elif action == -1:
            #print("Move -1")
            self.paddle.y == 1 - self.paddle.height
            for i in range(int(self.paddle.height*self.board_y_size)):
                self.grid[int(self.paddle.y*(self.board_y_size-1)+i)][self.board_x_size-1] = "|"

        # Move = 0
        if action == 0:
            #print("Move 0")
            for i in range(int(self.paddle.height*self.board_y_size)):
                self.grid[int(self.paddle.y*(self.board_y_size-1)+i)][self.board_x_size-1] = "|"

    def print_board(self):
        for _ in range(self.board_x_size):
            print("-", end="")
        print("-")
        for i in range(self.board_y_size):
            print("|", end="")
            for j in range(self.board_x_size-1):
                print(self.grid[i][j], end="")
            print(self.grid[i][self.board_x_size-1])
        for _ in range(self.board_x_size):
            print("-", end="")
        print("-")
