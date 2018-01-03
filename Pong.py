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
        self.grid[int(self.ball.y*(self.board_y_size-1))][int(self.ball.x*(self.board_x_size-1))] = "*"

    def move_ball(self):
        reward = 0

        # Reset current position to " "
        self.grid[int(self.ball.y*(self.board_y_size-1))][int(self.ball.x*(self.board_x_size-1))] = " "

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
            self.ball.x = 2 - self.ball.x - self.ball.x_velocity
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
            reward = -1
            self.ball.missed = True
        else:
            # Update grid display
            self.grid[int(self.ball.y*(self.board_y_size-1))][int(self.ball.x*(self.board_x_size-1))] = "*"

        if self.ball.x <= 0:
            self.paddle2.missed = True

        return reward

    def create_paddle(self, paddle_y, paddle_height, paddle_speed, paddle_num):
        if paddle_num == 1:
            # Create paddle
            self.paddle = Paddle.Paddle(paddle_y, paddle_height, paddle_speed)

            for i in range(int(self.paddle.height*self.board_y_size)):
                self.grid[int(self.paddle.y*(self.board_y_size-1)+i)][self.board_x_size-1] = "|"
        else:
            self.paddle2 = Paddle.Paddle(paddle_y, paddle_height, paddle_speed)

            for i in range(int(self.paddle.height*self.board_y_size)):
                self.grid[int(self.paddle.y*(self.board_y_size-1)+i)][0] = "|"

    def move_paddle(self, paddle, action):
        if paddle == self.paddle:
            x = self.board_x_size-1
        if paddle == self.paddle2:
            x = 0

        # Reset current position to " "
        for i in range(int(paddle.height*self.board_y_size)):
            self.grid[int(paddle.y*(self.board_y_size-1)+i)][x] = " "

        # Move = 1
        if action == 1 and paddle.y - paddle.speed >= 0:
            paddle.y -= paddle.speed
            for i in range(int(paddle.height*self.board_y_size)):
                self.grid[int(paddle.y*(self.board_y_size-1)+i)][x] = "|"
        elif action == 1:
            paddle.y == 0
            for i in range(int(paddle.height*self.board_y_size)):
                self.grid[int(paddle.y*(self.board_y_size-1)+i)][x] = "|"

        # Move = -1
        if action == -1 and paddle.y + paddle.height + paddle.speed <= 1:
            paddle.y += paddle.speed
            for i in range(int(paddle.height*self.board_y_size)):
                self.grid[int(paddle.y*(self.board_y_size-1)+i)][x] = "|"
        elif action == -1:
            paddle.y == 1 - paddle.height
            for i in range(int(paddle.height*self.board_y_size)):
                self.grid[int(paddle.y*(self.board_y_size-1)+i)][x] = "|"

        # Move = 0
        if action == 0:
            for i in range(int(paddle.height*self.board_y_size)):
                self.grid[int(paddle.y*(self.board_y_size-1)+i)][x] = "|"

    def print_board(self):
        for _ in range(self.board_x_size-1):
            print("-", end="")
        print("-")
        for i in range(self.board_y_size):
            for j in range(self.board_x_size-1):
                print(self.grid[i][j], end="")
            print(self.grid[i][self.board_x_size-1])
        for _ in range(self.board_x_size-1):
            print("-", end="")
        print("-")
