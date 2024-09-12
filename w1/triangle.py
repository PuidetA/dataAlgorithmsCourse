def triangle(a, b, c):
    # For a triangle to be viable, the sum of two sides has to be greater than the third. source: https://en.wikipedia.org/wiki/Triangle_inequality "... triangle inequality states that for any triangle, the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side."
    if a+b<=c or a+c<=b or b+c<=a: # check two sides, if they are less than or equal to the third side, then it can't be a triangle. We have to check all three combinations, because the rule states "any two sides must be greater than or equal to the length of the remaining side."
        return False
    else:
        return True

if __name__ == "__main__":
    print(triangle(3, 5, 4))
    print(triangle(-1, 2, 3))
    print(triangle(5, 9, 14))
    print(triangle(30, 12, 29))