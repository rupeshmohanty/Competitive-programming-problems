# Exercise link: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGx4V3BGaDZrUzhBYVdmaGxEa2FwbENhNEZGZ3xBQ3Jtc0tsMW83VEJTMUhndnk4RkpHWnk0X3VLZHlhR2hPWDEzazFKZHlCWV9yamFjeHd2NE5pTWVhNUEwRmFlV0lBZnZVOUpiZTd5Z01TemI1WXp3YVd1Nk5UU1hJQjZHY1Vmd2lJUlhhN0FWdDJsemhqdjBRQQ&q=https%3A%2F%2Fgithub.com%2Fcodebasics%2Fdata-structures-algorithms-python%2Ftree%2Fmaster%2Fdata_structures%2F5_Stack%2F5_stack_exercise.md
from collections import deque

# Problem 1!
def reverse_string(s):
    t = ""
    for i in range(len(s)):
        t += s[-1]
        s.pop()

    print(t)

# Problem 2!
def is_balanced(s):
    count1,count2,count3 = 0,0,0
    for i in range(len(s)):
        if s[-1] == '{' or s[-1] == '}':
            count1 += 1
            s.pop()
        elif s[-1] == '(' or s[-1] == ')':
            count2 += 1
            s.pop()
        elif s[-1] == '[' or s[-1] == ']':
            count3 += 1
            s.pop()
        else:
            s.pop()
    
    if(count1 == count2 or count1 == count3 or count3 == count2):
        return True
    else:
        return False 

if __name__ == "__main__":
    stack1 = deque()
    stack2 = deque()

    s = "We will conquer COVID-19"
    s1 = "))((a+b}{"

    for i in s:
        stack1.append(i)

    for j in s1:
        stack2.append(j)

    reverse_string(stack1)
    res = is_balanced(stack2)
    print(res)