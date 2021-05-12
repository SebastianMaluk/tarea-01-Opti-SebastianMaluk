import pulp as p

x1 = p.LpVariable("x1", 0)
x2 = p.LpVariable("x2", 0)
prob = p.LpProblem("myProblem", p.LpMinimize)
prob += 0.3*x1 + 0.9*x2
prob += x1 + x2 >= 800
prob += -0.21*x1 + 0.30*x2 >= 0
prob += 0.03*x1 - 0.01*x2 >= 0
status = prob.solve()
print(p.LpStatus[status])
print("")
print(f"x1: {p.value(x1)}")
print(f"x2: {p.value(x2)}")