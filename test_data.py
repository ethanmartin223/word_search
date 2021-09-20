from solver import find_answers

data = [
  ['C','Q','F','G','A','O','V','Y','D','L','S','W','I','I','U','L','S','M','I','U','F','Q','K','Y','M','U','F','M','G','I'],
  ['A','P','P','G','C','R','W','Z','O','K','W','Q','Q','G','I','G','A','N','E','T','O','B','Z','O','I','C','E','V','N','I'],
  ['T','Z','O','L','A','T','F','Q','M','Z','Y','Y','T','B','Y','T','V','I','E','P','K','U','O','N','H','K','V','I','R','Z'],
  ['N','G','F','I','R','M','P','Z','I','A','W','I','T','M','B','E','P','X','T','R','P','R','V','L','T','R','T','P','D','P'],
  ['L','E','L','J','M','L','W','C','N','D','Z','U','Z','I','S','A','Z','P','A','N','H','B','L','N','I','I','A','T','F','Y'],
  ['F','A','K','U','Z','Z','N','R','A','Z','Z','M','O','T','R','J','P','M','H','T','E','S','W','F','A','N','A','O','O','E'],
  ['M','N','A','E','O','Z','C','G','T','B','T','U','I','B','D','O','E','W','A','P','A','D','X','T','Q','B','E','X','M','N'],
  ['T','N','A','H','P','E','L','E','E','C','Y','G','D','Z','K','R','I','B','O','Q','N','W','I','Y','A','U','X','N','J','K'],
  ['A','F','T','D','N','N','G','P','A','K','A','D','V','A','N','C','E','R','U','H','B','V','G','S','P','P','O','U','K','K'],
  ['Q','K','G','Z','E','A','O','Q','H','T','A','R','B','H','R','E','R','Y','P','Y','E','F','Y','W','E','H','E','C','S','E'],
  ['T','T','A','B','O','C','K','D','I','Z','G','A','S','B','I','C','A','C','S','Q','O','U','A','I','D','R','F','O','O','X'],
  ['M','N','R','E','D','C','W','O','I','S','F','D','D','D','E','D','Y','R','A','C','Z','L','K','H','E','H','P','K','M','U'],
  ['E','G','W','C','K','P','N','U','O','H','P','C','E','O','H','K','M','E','B','F','S','K','M','X','X','P','M','L','Y','F'],
  ['R','P','Y','H','F','A','O','T','M','C','K','J','K','E','Q','L','K','M','N','D','J','L','G','K','H','P','S','H','V','H'],
  ['K','M','T','M','B','A','S','K','E','T','B','A','L','L','I','E','A','P','E','J','O','T','M','I','L','O','M','O','S','G'],
  ['D','I','H','R','T','E','B','X','H','P','F','F','M','X','B','L','W','T','W','G','O','J','H','O','M','R','V','R','S','Y'],
  ['D','X','K','M','J','R','T','E','E','Z','D','U','E','X','O','D','F','M','S','T','Y','Y','V','N','E','W','N','Z','Z','F'],
  ['B','M','H','Z','A','X','O','O','E','Z','L','M','T','Q','R','N','H','R','K','L','F','P','D','F','O','U','W','M','L','J'],
  ['Y','V','Y','U','A','W','X','Z','D','V','O','R','N','U','E','U','K','O','M','P','B','O','U','U','K','F','F','R','T','R'],
  ['T','N','E','M','S','S','E','S','S','A','H','E','H','Y','R','B','E','R','R','J','S','E','M','I','E','K','X','H','Q','F'],
  ['O','W','D','M','O','M','F','I','O','I','F','R','B','S','X','E','G','X','P','I','D','O','U','F','Z','P','Y','M','J','B'],
  ['O','S','H','Y','J','P','R','L','D','R','T','U','H','P','J','R','O','R','B','Y','O','G','P','C','Y','X','V','X','D','K'],
  ['Q','G','B','I','L','Y','Y','G','Q','D','E','S','L','Q','I','S','I','P','D','M','U','A','Z','X','T','J','Q','U','Q','B'],
  ['P','G','A','S','Y','L','K','B','O','I','W','A','Z','Q','Q','N','E','N','O','Z','A','B','U','N','D','A','N','T','U','W'],
  ['H','T','L','U','W','U','I','H','I','Y','W','E','I','H','T','B','X','S','A','O','M','C','U','B','L','V','H','J','K','N'],
  ['X','Z','B','O','E','X','N','P','F','P','M','R','Q','E','I','G','R','B','J','O','H','A','Z','Y','Y','A','B','N','R','G'],
  ['X','S','E','J','O','M','R','K','S','I','O','T','R','J','K','X','R','W','T','P','G','L','F','E','H','O','Z','Q','T','P'],
  ['X','R','I','F','X','A','A','W','I','A','Q','D','Z','F','D','S','Z','U','N','Y','Y','D','I','Y','K','N','G','D','P','Q'],
  ['A','E','K','E','K','N','A','J','L','Z','P','T','M','V','R','W','A','C','G','E','P','X','S','G','F','W','N','Q','W','W'],
  ['B','K','J','M','X','W','S','Q','C','W','N','I','L','Q','N','W','F','G','L','E','O','T','A','Y','L','Z','R','S','D','S']
]

answers = ['abundant','advance','assessment','basketball','bathroom','bundle','cat','dominate','elephant','enjoy','future','hold','initiative','investigation','jest','linen','presidential','printer','priority','remark','spill','treasurer','zone']

for i,v in enumerate(answers):
  answers[i] = answers[i].upper()
print(answers,'\n')
output = find_answers(answers, data, text_color='PURPLE')

for i,v in enumerate(output):
    print(*v)

import timeit
print ('\nsolved in',timeit.timeit(setup = 'from solver import find_answers',stmt = f"find_answers({answers},{data})",number = 1),'seconds')