from turtle import Turtle

FONT = ('Courier', 18, 'normal')

class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()

		self.score = 0
		self.high_score = 0
		self.color('yellow')
		self.penup()
		self.goto(0, 270)
		self.hideturtle()
		self.update_scoreboard()

	def increment_score(self):
		self.score += 1
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.write(f'Score: {self.score}\tHigh Score: {self.high_score}', align='center', font=FONT)

	def reset(self):
		if(self.score > self.high_score):
			self.high_score = self.score
		self.score = 0
		self.update_scoreboard()

	def game_over(self):
		self.clear()
		self.goto(0,0)
		self.write(f'Game Over!!!\nScore: {self.score}', align='center', font=FONT)

