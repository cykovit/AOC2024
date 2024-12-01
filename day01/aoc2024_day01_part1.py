def calculate_total_distance(file_path):
   with open(file_path, 'r') as file:
       data = file.readlines()
   
   left_list = []
   right_list = []
   
   for line in data:
       left, right = map(int, line.strip().split())
       left_list.append(left)
       right_list.append(right)
   
   left_list.sort()
   right_list.sort()
   
   return sum(abs(left - right) for left, right in zip(left_list, right_list))

file_path = r'input_day01.txt'
print(calculate_total_distance(file_path))
