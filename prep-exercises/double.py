def half(value):
    return value / 2


def double(value):
    return value * 2


def second(value):
    return value[1]


print(double("22"))

# Prediction:
# Expected: 44

# Actual:
# 2222

# Explanation:
# Python allows strings to be multiplied by integers.
# "22" * 2 repeats the string twice, producing "2222".