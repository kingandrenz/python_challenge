
import timeit

a = range(1000000)
x = set(a)
y = list(a)

n = 999999

stmt1 = f"{n} in x"
stmt2 = f"{n} in y"

#define the setup code to run before the stament
setup = "from __main__ import x, y, n"

#measure the time for each statement
t1 = timeit.timeit(stmt1, setup=setup, number=1000)
t2 = timeit.timeit(stmt2, setup=setup, number=1000)

print(f"searching for {n} in the list took {t1:.6f} seconds")
print(f"searching for {n} in the set took {t2:.6f} seconds")

if t1 < t2:
    print("set is faster")
else:
    print("list is faster.")
