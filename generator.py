import random

def grid(width,height):
  row = []
  grid = []
  for l in range(height):
    for i in range(width):
      if i == 0:
        row = [' ']
      else:
        row.append(' ')
    grid.append(row[:])
  i = 0
  for y in range(height):
    for x in range(width):
      grid[y][x] = chr(random.randrange(65,91))
  return grid

grid = grid(15,15)

words = ['TEST', 'TRIAL']

for i,v in enumerate(words):
  x = random.randint(0,len(grid[0])-1)
  y = random.randint(0,len(grid)-1)
  direction = random.chocie['up','down','left','right']
  while True:
    if direction == 'left':
      if x-len(v)<0:
        direction = 'right'
      for iteration,letter in enumerate(v):
        
    elif direction == 'right':
      if len(grid[y])-x<len(v):
        direction = 'up'
    elif direction == 'up':
      if y-len(v)<0:
        direction = 'up'
    elif direction == 'down':
      if y+len(v)>len(grid):
        direction = 'up'
grid[y][x] = 0


print('\n',x,y)

print(*[v for i,v in enumerate(grid)],sep='\n')
