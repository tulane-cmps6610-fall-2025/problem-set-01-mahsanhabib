"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

def foo(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        x = min(a, b)
        y = max(a, b)
        return foo(y, y % x)


def longest_run(mylist, key):
    max_run = 0
    current_run = 0
    for item in mylist:
        if item == key:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    return max_run


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    if not mylist:
        return Result(0, 0, 0, True)
    elif len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    else:
        mid = len(mylist) // 2
        left = longest_run_recursive(mylist[:mid], key)
        right = longest_run_recursive(mylist[mid:], key)

        # Compute left_size
        if left.is_entire_range:
            left_size = left.left_size + right.left_size
        else:
            left_size = left.left_size

        # Compute right_size
        if right.is_entire_range:
            right_size = right.right_size + left.right_size
        else:
            right_size = right.right_size

        # Compute cross run: count consecutive keys from end of left and start of right
        if mylist[mid - 1] == key and mylist[mid] == key:
            cross_run = left.right_size + right.left_size
        else:
            cross_run = 0

        longest_size = max(left.longest_size, right.longest_size, cross_run)
        is_entire_range = left.is_entire_range and right.is_entire_range
        return Result(left_size, right_size, longest_size, is_entire_range)

    def longest_run_recursive_length(mylist, key):
        return longest_run_recursive(mylist, key).longest_size
    
    
    
## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


print(foo(8, 30))

test_longest_run()

print(longest_run_recursive([12,2,12,0,8,12,12,12,0,12,12], 12))