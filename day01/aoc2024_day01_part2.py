def calculate_similarity(file_path):
   with open(file_path, 'r') as file:
       data = file.readlines()
   
   left_list = []
   right_list = []
   
   for line in data:
       left, right = map(int, line.strip().split())
       left_list.append(left)
       right_list.append(right)
   
   right_count = {}
   for num in right_list:
       right_count[num] = right_count.get(num, 0) + 1
   
   similarity = sum(left * right_count.get(left, 0) for left in left_list)
   
   return similarity

file_path = r'input_day01.txt'
print(calculate_similarity(file_path))
