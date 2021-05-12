from turtle import Turtle

FONT = ('Courier', 18, 'normal')

class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.high_score = self.read_high_score()
		self.color('yellow')
		self.penup()
		self.goto(0, 270)
		self.hideturtle()
		self.update_scoreboard()

	def read_high_score(self):
		with open('scores.txt') as f:
			return int(f.read()) or 0

	def update_high_score(self, score):
		with open('scores.txt', 'w') as f:
			f.write(str(score))

	def increment_score(self):
		self.score += 1
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.write(f'Score: {self.score}\tHigh Score: {self.high_score}', align='center', font=FONT)

	def reset(self):
		if(self.score > self.high_score):
			self.high_score = self.score
			self.update_high_score(self.high_score)
		self.score = 0
		self.update_scoreboard()

	def game_over(self):
		self.clear()
		self.goto(0,0)
		self.write(f'Game Over!!!\nScore: {self.score}', align='center', font=FONT)

