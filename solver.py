def find_answers(answers, data, text_color='RED'):
  import copy, random
  answers_found = []

  #Data
  output_data = copy.deepcopy(data)
  horizontal_data = copy.deepcopy(data)
  diagonal_data = copy.deepcopy(data)
  horizontal_data_2 = copy.deepcopy(data)

  #Diagonal
  data_y_len = len(diagonal_data)
  data_x_len = len(diagonal_data[0])
  for y,y_char in enumerate(diagonal_data):
    for x,x_char in enumerate(diagonal_data[y]):
      diagonal_data[y][x] = (diagonal_data[y][x],(x,y))
  diagonal_data_2 = copy.deepcopy(diagonal_data)
  diagonal_data_1 =  copy.deepcopy(diagonal_data)
  diagonal_data_reversed_1 = copy.deepcopy(diagonal_data)

  colors = {'RED':31,'GREEN':32,'YELLOW':33,'BLUE':34,'PURPLE':35,'BLACK':30}
  color = colors[text_color]

  #Diagonal data 1 tl->br 45 left
  output = []
  ctr = 0
  while(ctr < 2 * data_x_len-1):
      row = []
      for y in range(data_y_len):
          for x in range(data_x_len):
              if y + x == ctr:
                  row.append(diagonal_data[y][x])
      row.reverse()
      ctr += 1
      output.append(row)
  for y,y_char in enumerate(output):
    current_row = ''
    for x,n in enumerate(y_char):
      current_row += y_char[x][0]
    for number,answer in enumerate(answers):
      if answer in current_row:
        word_start = current_row.find(answer)
        y_char = list(y_char)
        for iteration,letter in enumerate(answer):
          output[y][word_start+iteration] = ('\033['+str(color)+'m'+letter+'\033[0m',(y_char[word_start+iteration][1][0],y_char[word_start+iteration][1][1]))
  output_2 = []
  ctr = 0
  while(ctr < 2 * data_x_len-1):
      row = []
      for y in range(data_y_len):
          for x in range(data_x_len):
              if y + x == ctr:
                  row.append(diagonal_data_1[y][x])
      ctr += 1
      output_2.append(row)
  for y,y_char in enumerate(output_2):
    current_row = ''
    for x,n in enumerate(y_char):
      current_row += y_char[x][0]
    for number,answer in enumerate(answers):
      if answer in current_row:
        word_start = current_row.find(answer)
        y_char = list(y_char)
        for iteration,letter in enumerate(answer):
          output_2[y][word_start+iteration] = ('\033['+str(color)+'m'+letter+'\033[0m',(y_char[word_start+iteration][1][0],y_char[word_start+iteration][1][1]))

  #Diagonal data 1 tl->br 45 Right
  diagonal_data_reversed_1.reverse()
  diagonal_data_reversed_2 = copy.deepcopy(diagonal_data_reversed_1)
  output_reversed_1 = []
  ctr = 0
  while(ctr < 2 * data_x_len-1):
      row = []
      for y in range(data_y_len):
          for x in range(data_x_len):
              if y + x == ctr:
                  row.append(diagonal_data_reversed_1[y][x])
      ctr += 1
      output_reversed_1.append(row)
  for y,y_char in enumerate(output_reversed_1):
    current_row = ''
    for x,n in enumerate(y_char):
      current_row += y_char[x][0]
    for number,answer in enumerate(answers):
      if answer in current_row:
        word_start = current_row.find(answer)
        y_char = list(y_char)
        for iteration,letter in enumerate(answer):
          output_reversed_1[y][word_start+iteration] = ('\033['+str(color)+'m'+letter+'\033[0m',(y_char[word_start+iteration][1][0],y_char[word_start+iteration][1][1]))

  output_reversed_2 = []
  ctr = 0
  while(ctr < 2 * data_x_len-1):
      row = []
      for y in range(data_y_len):
          for x in range(data_x_len):
              if y + x == ctr:
                  row.append(diagonal_data_reversed_2[y][x])
      row.reverse()
      ctr += 1
      output_reversed_2.append(row)
  for y,y_char in enumerate(output_reversed_2):
    current_row = ''
    for x,n in enumerate(y_char):
      current_row += y_char[x][0]
    for number,answer in enumerate(answers):
      if answer in current_row:
        word_start = current_row.find(answer)
        y_char = list(y_char)
        for iteration,letter in enumerate(answer):
          output_reversed_2[y][word_start+iteration] = ('\033['+str(color)+'m'+letter+'\033[0m',(y_char[word_start+iteration][1][0],y_char[word_start+iteration][1][1]))


  #Horizontal
  for i,v in enumerate(data):
    v = ''.join(v)
    for number,answer in enumerate(answers):
      if answer in v:
        word_start = v.find(answer)
        v = list(v) 
        for iteration,letter in enumerate(answer):
          v[word_start+iteration] = '\033['+str(color)+'m'+letter+'\033[0m'
        horizontal_data[i] = v
  for i,v in enumerate(horizontal_data_2):
    v.reverse()
    v = ''.join(v)
    for number,answer in enumerate(answers):
      if answer in v:
        word_start = v.find(answer)
        v = list(v) 
        for iteration,letter in enumerate(answer):
          v[word_start+iteration] = '\033['+str(color)+'m'+letter+'\033[0m'
        horizontal_data_2[i] = v
  for i,v in enumerate(horizontal_data_2):
    v.reverse()

  #Vertical and Vertical Reversed
  rotated_data = [[data[x][y] for x in range(len(data[0]))] for y in range(len(data))]
  rotated_data_2 = [[data[x][y] for x in range(len(data[0]))] for y in range(len(data))]
  for i,v in enumerate(rotated_data):
    v = ''.join(v)
    for number,answer in enumerate(answers):
      if answer in v:
        word_start = v.find(answer)
        v = list(v)
        for iteration,letter in enumerate(answer):
          v[word_start+iteration] = '\033['+str(color)+'m'+letter+'\033[0m'
        rotated_data[i] = v
  for i,v in enumerate(rotated_data_2):
    v.reverse()
    v = ''.join(v)
    for number,answer in enumerate(answers):
      if answer in v:
        word_start = v.find(answer)
        v = list(v)
        for iteration,letter in enumerate(answer):
          v[word_start+iteration] = '\033['+str(color)+'m'+letter+'\033[0m'
        rotated_data_2[i] = v
  for i,v in enumerate(rotated_data_2):
    v.reverse()
  rotated_data = [[rotated_data[x][y] for x in range(len(rotated_data[0]))] for y in range(len(rotated_data))]
  rotated_data_2 = [[rotated_data_2[x][y] for x in range(len(rotated_data_2[0]))] for y in range(len(rotated_data_2))]

  #           Combine data from all dimensions
  #Vertical
  for y in range(len(rotated_data)):
    for x in range(len(rotated_data[y])):
      if '\033' in rotated_data[y][x]:
        output_data[y][x] = rotated_data[y][x]
  for y in range(len(rotated_data_2)):
    for x in range(len(rotated_data_2[y])):
      if '\033' in rotated_data_2[y][x]:
        output_data[y][x] = rotated_data_2[y][x]
  #Horizontal
  for y in range(len(horizontal_data)):
    for x in range(len(horizontal_data[y])):
      if '\033' in horizontal_data[y][x]:
        output_data[y][x] = horizontal_data[y][x]
  for y in range(len(horizontal_data_2)):
    for x in range(len(horizontal_data_2[y])):
      if '\033' in horizontal_data_2[y][x]:
        output_data[y][x] = horizontal_data_2[y][x]
  #Digaonal
  for y,y_char in enumerate(output):
    for x,x_char in enumerate(output[y]):
      if '\033' in output[y][x][0]:
        output_data[output[y][x][1][1]][output[y][x][1][0]] = output[y][x][0]
  for y,y_char in enumerate(output_2):
    for x,x_char in enumerate(output_2[y]):
      if '\033' in output_2[y][x][0]:
        output_data[output_2[y][x][1][1]][output_2[y][x][1][0]] = output_2[y][x][0]
  #Diagonal other side
  for y,y_char in enumerate(output_reversed_1):
    for x,x_char in enumerate(output_reversed_1[y]):
      if '\033' in output_reversed_1[y][x][0]:
        output_data[output_reversed_1[y][x][1][1]][output_reversed_1[y][x][1][0]] = output_reversed_1[y][x][0]
  for y,y_char in enumerate(output_reversed_2):
    for x,x_char in enumerate(output_reversed_2[y]):
      if '\033' in output_reversed_2[y][x][0]:
        output_data[output_reversed_2[y][x][1][1]][output_reversed_2[y][x][1][0]] = output_reversed_2[y][x][0]

  
  return output_data
