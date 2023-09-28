def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and b>c:
        return b
    if b>a and a>c:
        return a
    if b>c and c>a:
        return c
    if a>c and c>b:
        return c
    if c>a and a>b:
        return a
    if c>b and b>a:
        return b
print (main(2,3,4))