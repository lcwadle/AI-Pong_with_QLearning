import QLearn
import Pong
import os

# Action List
actions = [1, 0, -1]
alpha = 0.2
gamma = 0.9
randomness = 200

qLearn = QLearn.QLearn(actions, randomness, 1.0, alpha, gamma)
trials = 100000

wins = 0
for i in range(trials):

    qLearn.epsilon = (trials - i) / trials

    pong = Pong.Pong(14, 14)
    pong.create_ball(0.5, 0.5, 0.03, 0.01)
    pong.create_paddle(0.5 - 0.2 / 2, 0.2, 0.04, 1)
    pong.create_paddle(0.5 - 0.2 / 2, 0.2, 0.02, 2)

    old_state = None

    # Make values discrete
    dis_x = int(pong.ball.x*(pong.board_x_size-1))

    dis_y = int(pong.ball.y*(pong.board_y_size-1))

    if pong.ball.x_velocity > 0:
        dis_x_velocity = 1
    else:
        dis_x_velocity = -1

    if (abs(pong.ball.y_velocity) < 0.015):
        dis_y_velocity = 0
    elif pong.ball.y_velocity > 0:
        dis_y_velocity = 1
    else:
        dis_y_velocity = -1

    dis_paddle_y = int(pong.paddle.y*(pong.board_y_size-1))

    new_state = (dis_x, dis_y, dis_x_velocity, dis_y_velocity, dis_paddle_y)
    bounces = 1

    # Game loop
    while not pong.ball.missed:
        action = qLearn.choose_action_n(new_state)

        # Move ball and paddle
        pong.move_paddle(pong.paddle, action)

        reward = pong.move_ball()

        bounces += reward

        old_state = new_state

        # Make values discrete
        dis_x = int(pong.ball.x*(pong.board_x_size-1))

        dis_y = int(pong.ball.y*(pong.board_y_size-1))

        if pong.ball.x_velocity > 0:
            dis_x_velocity = 1
        else:
            dis_x_velocity = -1

        if (abs(pong.ball.y_velocity) < 0.015):
            dis_y_velocity = 0
        elif pong.ball.y_velocity > 0:
            dis_y_velocity = 1
        else:
            dis_y_velocity = -1

        dis_paddle_y = int(pong.paddle.y*(pong.board_y_size-1))

        new_state = (dis_x, dis_y, dis_x_velocity, dis_y_velocity, dis_paddle_y)

        # Learn from previous actions
        qLearn.learn(old_state, action, reward, new_state)

# Tests
tests = 1000
average_bounces = 0
wins = 0
for i in range(tests):

    qLearn.epsilon = 0.0

    pong = Pong.Pong(14, 14)
    pong.create_ball(0.5, 0.5, 0.03, 0.01)
    pong.create_paddle(0.5 - 0.2 / 2, 0.2, 0.04, 1)
    pong.create_paddle(0.5 - 0.2 / 2, 0.2, 0.02, 2)

    old_state = None

    # Make values discrete
    dis_x = int(pong.ball.x*(pong.board_x_size-1))

    dis_y = int(pong.ball.y*(pong.board_y_size-1))

    if pong.ball.x_velocity > 0:
        dis_x_velocity = 1
    else:
        dis_x_velocity = -1

    if (abs(pong.ball.y_velocity) < 0.015):
        dis_y_velocity = 0
    elif pong.ball.y_velocity > 0:
        dis_y_velocity = 1
    else:
        dis_y_velocity = -1

    dis_paddle_y = int(pong.paddle.y*(pong.board_y_size-1))

    new_state = (dis_x, dis_y, dis_x_velocity, dis_y_velocity, dis_paddle_y)
    bounces = 1

    # Game loop
    while not pong.ball.missed:
        action = qLearn.choose_action(new_state)

        # Move ball and paddle
        pong.move_paddle(pong.paddle, action)

        reward = pong.move_ball()

        bounces += reward

        old_state = new_state

        # Make values discrete
        dis_x = int(pong.ball.x*(pong.board_x_size-1))

        dis_y = int(pong.ball.y*(pong.board_y_size-1))

        if pong.ball.x_velocity > 0:
            dis_x_velocity = 1
        else:
            dis_x_velocity = -1

        if (abs(pong.ball.y_velocity) < 0.015):
            dis_y_velocity = 0
        elif pong.ball.y_velocity > 0:
            dis_y_velocity = 1
        else:
            dis_y_velocity = -1

        dis_paddle_y = int(pong.paddle.y*(pong.board_y_size-1))

        new_state = (dis_x, dis_y, dis_x_velocity, dis_y_velocity, dis_paddle_y)

        # Learn from previous actions
        qLearn.learn(old_state, action, reward, new_state)

    average_bounces += bounces
    #if pong.paddle2.missed:
        #wins += 1

print("Average Bounces: " + str(average_bounces / tests))
print("Alpha: " + str(alpha))
print("Gamma: " + str(gamma))
print("Random factor: " + str(randomness))
