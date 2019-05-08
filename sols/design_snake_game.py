from collections import deque
class SnakeGame(object):
    def __init__(self, width, height, food):
        self.n = height
        self.m = width
        self.snake = deque([(0, 0)])
        self.food = deque(food)
        self.dir = {}
        self.dir["U"] = (-1, 0)
        self.dir["D"] = (1, 0)
        self.dir["R"] = (0, 1)
        self.dir["L"] = (0, -1)
        self.score = 0
        
    def move(self, direction):
        i, j = self.snake[0]
        di, dj = self.dir[direction]
        ni, nj = i + di, j + dj
        
        if 0 <= ni < self.n and 0 <= nj < self.m:
            if self.food and [ni, nj] == self.food[0]:
                self.food.popleft()
                self.score += 1
                self.snake.appendleft((ni, nj))
                return self.score
            else:
                self.snake.pop()
                if (ni, nj) in self.snake:
                    return -1
                self.snake.appendleft((ni, nj))
                return self.score
        else:
            return -1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)