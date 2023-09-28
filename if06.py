def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a1 = n//10000
    a2 = n%10000//1000
    a3 = n%1000//100
    a4 = n%100//10
    a5 = n%10
    if a1>a2 and a1>a3 and a1>a4 and a1>a5:
        return 1
    if a2>a1 and a2>a3 and a2>a4 and a2>a5:
        return 2
    if a3>a2 and a3>a1 and a3>a4 and a3>a5:
        return 3
    if a4>a2 and a4>a3 and a4>a1 and a4>a5:
        return 4
    if a5>a2 and a5>a3 and a5>a4 and a5>a1:
        return 5
print(main(15432))