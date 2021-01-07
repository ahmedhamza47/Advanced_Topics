from collections import Counter
sentence = 'My name is hamza ahmed. '
my_counter = Counter(sentence)
print(my_counter.items())
print(my_counter.most_common(1)[0][0])  # most common element print here '' is the most common
print(my_counter.keys())
print(list(my_counter.elements()))  # prints every elements in the sentence


from collections import namedtuple
class_tuple = namedtuple('class_tuple','x,y')
# namedtuple makes aa class. Here class_tuple is a class with x,y its parameters
# print(class_tuple(5,4))
c1 = class_tuple(5,4)
print(c1)
print(c1.x,c1.y)

from collections import deque
# deque is a double ended queue in which items can be added from both ends

my_queue = deque()
my_queue.append(1)
my_queue.append(2)
my_queue.appendleft(5)
print(my_queue)

my_queue.popleft()
print(my_queue)

my_queue.extend([4,8,12])  # helps to add multiple elements to the queue
print(my_queue)

my_queue.rotate(1) # rotates the elements 1 place
print(my_queue)

my_queue.clear()
print(my_queue)

