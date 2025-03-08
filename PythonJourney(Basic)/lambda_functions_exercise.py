print('Lambdas Exercise')

# def f(x): return x + 5
# f = lambda x: x + 5
# print(f(2))
# 
# def strip_spaces(str):
  #  return ''.join(str.split(' '))
# strip_spaces1 = lambda str: ''.join(str.split(' '))
# print(strip_spaces('Monty Pythons Flying Circus')) 
# print(strip_spaces1('Monty Pythons Flying Circus')) 

# list_a = [1,2,3,4]
# list_b = [3,4,5,6,7]
# j = lambda a, y: (list(set(a + y))) 
# print(j(list_a, list_b))

# def create_quad_func(a,b,c):
    # '''return function f(x) = ax^2 + bx + c'''
    # return lambda x: a*x**2 + b*x + c
# create_quad_func(2, 4, -5)

# import re
# 
# signups = ['kpD222', 'MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
# 
# def sort_number_in_string(list_of_strings):
  # numbers = []
  # 
  # for n in list_of_strings:
    # numbers.append(int(re.findall(r'\d+', n)[0]))
# 
  # numbers.sort()
  # 
  # sorted_signups = []
  # for n in numbers:
    # n = str(n)
    # for s in list_of_strings:
      # if n in s and len(n) == len(re.findall(r'\d+', s)[0]):
        # sorted_signups.append(s)
        # 
  # return sorted_signups
# 
# 
# print(sort_number_in_string(signups))
# 
# 
# print(sorted(signups, key = lambda x: int(x[3:])))
# print(sorted(signups, key = lambda x: int(re.findall(r'\d+', x)[0])))
  

# class Player:
  #  def __init__(self, name, score):
      #  self.name = name
      #  self.score =  score
  # 
  #  def __repr__(self):
        # return f"Player({self.name}, {self.score})"
# 
# Eric = Player('Eric', 116700)
# John = Player('John', 24327)
# Terry = Player('Terry', 150000)
# player_list = [Eric, John, Terry]
  # 
# print("\n".join(sorted(player_list, key = lambda x: x.score)))


teams = ['1real madrid' , '9geicelona', '5atl  madrid', '3nekvi dr', '2seltic', '4womaans']
print(sorted(teams, key = lambda x: int(x[0])))

