# 피자 파티

num_people = int(input("How many people? "))
num_pizza = int(input("How many pizzas do you have? "))
pieces_per_pizza = int(input("How many pieces are in a pizza? "))
total_pieces = num_pizza * pieces_per_pizza
pieces_per_person = total_pieces // num_people
left_pieces = total_pieces % num_people

print()
print('{} people with {} pizzas'.format(num_people, num_pizza))
print('Each person gets {} pieces of pizza.'.format(pieces_per_person))
print('There are {} leftover pieces.'.format(left_pieces))
