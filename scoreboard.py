from turtle import Turtle

FONT = ('Courier', 18, 'normal')

class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()

		self.score = 0
		self.color('yellow')
		self.penup()
		self.goto(0, 270)
		self.hideturtle()
		self.update_scoreboard()

	def increment_score(self):
		self.score += 1
		self.clear()
		self.update_scoreboard()

	def update_scoreboard(self):
		self.write(f'Score: {self.score}', align='center', font=FONT)

	def game_over(self):
		self.clear()
		self.goto(0,0)
		self.write(f'Game Over!!!\nScore: {self.score}', align='center', font=FONT)

