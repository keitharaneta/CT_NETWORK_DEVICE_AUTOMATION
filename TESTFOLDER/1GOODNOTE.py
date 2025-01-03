from math import pi

# TOPIC: pi*(r**2) should not return a NEGATIVE VALUE or result when BOOLEAN are used! Might result in unreliable output and BUG.
# PERFORM TEST to realistically know if certain VALUE does not compliment REAL WORLD SCENARIO
# MAKE certain that inputs made by CLIENTS adheres to the purpose of the program! STRING and STRING only. No SPECIAL CHAR. etc.

def x1(r):
    if r < 0:
        raise ValueError('negative PIE result is unrealistic!')
    return pi*(r**2)

# Result shows that python accepts NEGATIVE result but in REALITY, 
# MATHEMATICALLY speaking, this should not be the case!
def unreliable_value():
    list1 = [2, -3, 3+5j, True, "huwat?"]

    for result in list1:
        test1 = 'Result from {x} is {y}'
        print(test1.format(x=result, y=pi*(result**2)))
        
