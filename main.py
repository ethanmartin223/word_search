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

color = 31

letter_locations = []

for i,v in enumerate(words):
  x = random.randint(0,len(grid[0])-1)
  y = random.randint(0,len(grid)-1)
  direction = random.choice(['up','down','left','right'])
  while True:
    print(direction)
    #Left
    if direction == 'left':
      if x-len(v)<=0:
        x = random.randint(0,len(grid[0])-1)
        y = random.randint(0,len(grid)-1)
        print(f'Changed: cords are now ({x},{y})')
      elif x-len(v)>0:
        try:
          for iteration,letter in enumerate(v):
            grid[y][x+iteration] = grid[y][x+iteration]
            if x+iteration > len(grid[y]):
              raise(IndexError)
        except IndexError:
          x = random.randint(0,len(grid[0])-1)
          y = random.randint(0,len(grid)-1)
          print(f'Changed: cords are now ({x},{y})')
        for iteration,letter in enumerate(v):
          grid[y][x+iteration] = f'\033[{color}m'+letter+'\033[0m'
          letter_locations.append((x+iteration,y))
        break
    #Right
    elif direction == 'right':
      print(f'{len(grid[y])-x}<{len(v)}')
      if len(grid[y])-x<len(v):
        x = random.randint(0,len(grid[0])-1)
        y = random.randint(0,len(grid)-1)
        print(f'Changed: cords are now ({x},{y})')
      elif len(grid[y])-x>=len(v):
        try:
          for iteration,letter in enumerate(v):
            grid[y][x+iteration] = grid[y][x-iteration]
            if x-iteration > 0:
              raise(IndexError)
        except IndexError:
          x = random.randint(0,len(grid[0])-1)
          y = random.randint(0,len(grid)-1)
          print(f'Changed: cords are now ({x},{y})')
        for iteration,letter in enumerate(v):
          grid[y][x-iteration] = f'\033[{color}m'+letter+'\033[0m'
          letter_locations.append((x-iteration,y))
        break
    #Up
    elif direction == 'up':
      print(f'{y-len(v)}<={0}')
      if y-len(v)<=0:
        x = random.randint(0,len(grid[0])-1)
        y = random.randint(0,len(grid)-1)
        print(f'Changed: cords are now ({x},{y})')
      elif y-len(v)>0:
        try:
          for iteration,letter in enumerate(v):
            grid[y+iteration][x] = grid[y][x+iteration]
            if y+iteration > len(grid):
              raise(IndexError)
        except IndexError:
          x = random.randint(0,len(grid[0])-1)
          y = random.randint(0,len(grid)-1)
          print(f'Changed: cords are now ({x},{y})')
        for iteration,letter in enumerate(v):
          grid[y+iteration][x] = f'\033[{color}m'+letter+'\033[0m'
          letter_locations.append((x,y-iteration))
        break
    #Down
    elif direction == 'down':
      if y+len(v)>len(grid):
        x = random.randint(0,len(grid[0])-1)
        y = random.randint(0,len(grid)-1)
        print(f'Changed: cords are now ({x},{y})')
      elif y+len(v)<=len(grid):
        try:
          for iteration,letter in enumerate(v):
            grid[y-iteration][x] = grid[y][x+iteration]
            if y+iteration > len(grid):
              raise(IndexError)
        except IndexError:
          x = random.randint(0,len(grid[0])-1)
          y = random.randint(0,len(grid)-1)
          print(f'Changed: cords are now ({x},{y})')
        for iteration,letter in enumerate(v):
          grid[y+iteration][x] = f'\033[{color}m'+letter+'\033[0m'
          letter_locations.append((x,y+iteration))
        break
        

print('\n',x,y)

#print(*[v for i,v in enumerate(grid)],sep='\n')
for i,v in enumerate(grid):
  print(*v)
print('\n',letter_locations)