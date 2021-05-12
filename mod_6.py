import pulp as p

x1 = p.LpVariable("x1", 0)
x2 = p.LpVariable("x2", 0)
prob = p.LpProblem("myProblem", p.LpMaximize)
prob += 4*x1 + 5*x2
prob += 8*x1 + 3*x2 <= 22
prob += x1 + 2*x2 <= 7
status = prob.solve()
print(p.LpStatus[status])
print("")
print(f"x1: {p.value(x1)}")
print(f"x2: {p.value(x2)}")