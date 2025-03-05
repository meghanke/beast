#HW1/HW2 Review

#1. pwd will tell you what your working directory is.

#2. ls will display the contents of a directory.

#3. 
# cd..
# cd brianna_repo

#4. 
# mv homework.py ../judy_decal/homework/
# ls ~/python_decal/judy_decal/homework/

#5.
# cat homework.py

#6.
# vim homework.py

#7.
# cd ~/python_decal/judy_decal
# git status
# git add homework/homework.py
# git commit -m "completed homework.py"
# git push origin main

#8.
# git pull origin main --rebase
# git push origin main

#9. 
# cd ~/Recents

#HW3 Review

#2.1
def identify_data_type(value):
    return f"DataType: {type(value).__name__}"

#2.2
def evenOrOdd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#3 Loops
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#4.1
def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list

#4.2
# errors: missing colon after def square(num)
    # reuturn should be indented function
