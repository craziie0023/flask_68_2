def find_odd_even(start, end):
    odds = []
    evens = []

    for n in range(start, end + 1):
        (evens if n % 2 == 0 else odds).append(n)

    return odds, evens

odds, evens = find_odd_even(21, 40)
print("เลขคี่:", odds)
print("เลขคู่:", evens)