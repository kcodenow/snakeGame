from turtle import Turtle

START_INDS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake():
	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		for position in START_INDS:
			self.add_segment(position)

	def add_segment(self, position):
		x = Turtle(shape='square')
		x.color('white')
		x.penup()
		x.goto(position)
		self.segments.append(x)

	def reset(self):
		for seg in self.segments:
			seg.goto(1000,1000)
		self.segments.clear()
		self.create_snake()
		self.head = self.segments[0]
	
	def grow(self):
		self.add_segment(self.segments[-1].position())

	def move(self):
		for part in range(len(self.segments)-1, 0, -1):
			new_x = self.segments[part-1].xcor()
			new_y = self.segments[part-1].ycor()
			self.segments[part].goto(new_x, new_y)
		self.head.forward(MOVE_SPEED)

	def up(self):
		if(self.head.heading() != DOWN):
			self.head.setheading(UP)

	def down(self):
		if(self.head.heading() != UP):
			self.head.setheading(DOWN)

	def left(self):
		if(self.head.heading() != RIGHT):
			self.head.setheading(LEFT)

	def right(self):
		if(self.head.heading() != LEFT):
			self.head.setheading(RIGHT)