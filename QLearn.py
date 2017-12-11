import random

class QLearn:
    def __init__(self, actions, randomness, epsilon=1.0, alpha=0.2, gamma=0.9):
        self.q_dict = {}
        self.n_dict = {}

        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.randomness = randomness
        self.actions = actions

    def get_q(self, state, action):
        # Return Q value for tuple or 0.0 if Q value if tuple doesn't exist in dict
        return self.q_dict.get((state, action), 0.0)

    def get_n(self, state, action):
        # Return N value for tuple or 0 if N value if tuple doesn't exist in dict
        return self.n_dict.get((state, action), 0)

    def inc_n(self, state, action):
        if (state, action) in self.n_dict:
            self.n_dict[(state, action)] += 1
        else:
            self.n_dict[(state, action)] = 1

    def learnQ(self, state, action, reward, value):
        # Terminal State
        if state[0] >= 1:
            self.q_dict[(state, None)] = reward

        if not state == None:
            sa_tuple = (state, action)

            # Increment N{}
            self.inc_n(state, action)

            # Update Q{}
            old_q_value = self.q_dict.get(sa_tuple, None)
            if old_q_value == None:
                self.q_dict[sa_tuple] = reward
            else:
                self.q_dict[sa_tuple] = old_q_value + self.alpha * (value - old_q_value)

    def learn(self, s1, action, reward, s2):
        max_q_new = max([self.get_q(s2, a) for a in self.actions])
        self.learnQ(s1, action, reward, reward + self.gamma*max_q_new)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            action = random.choice(self.actions)
        else:
            q = [self.get_q(state, a) for a in self.actions]
            max_q = max(q)
            count = q.count(max_q)
            if count > 1:
                best = [i for i in range(len(self.actions)) if q[i] == max_q]
                i = random.choice(best)
            else:
                i = q.index(max_q)

            action = self.actions[i]

            return action

    def choose_action_n(self, state):
            q = [self.get_q(state, a) for a in self.actions]
            max_q = max(q)
            count = q.count(max_q)
            if count > 1:
                best = [i for i in range(len(self.actions)) if q[i] == max_q]
                i = random.choice(best)
            else:
                i = q.index(max_q)

            action = self.actions[i]

            if self.get_n(state, action) > self.randomness:
                return action
            else:
                return random.choice(self.actions)
