import pulp as p


x1 = p.LpVariable("x1", 0)
x2 = p.LpVariable("x2", 0)
x3 = p.LpVariable("x3", 0)
y1 = p.LpVariable("y1", 0)
y2 = p.LpVariable("y2", 0)
y3 = p.LpVariable("y3", 0)
z1 = p.LpVariable("z1", 0)
z2 = p.LpVariable("z2", 0)
z3 = p.LpVariable("z3", 0)

prob = p.LpProblem("myProblem", p.LpMaximize)
prob += 400*(x1 + x2 + x3) + 300*(y1 + y2 + y3) + 100*(z1 + z2 + z3)

prob += x1 + y1 + z1 <= 400
prob += x2 + y2 + z2 <= 600
prob += x3 + y2 + z3 <= 300

prob += 3*x1 + 2*y1 + 1*z1 <= 600
prob += 3*x2 + 2*y2 + 1*z2 <= 800
prob += 3*x3 + 2*y3 + 1*z3 <= 375

prob += x1 + x2 + x3 <= 600
prob += y1 + y2 + y3 <= 500
prob += z1 + z2 + z3 <= 325

prob += (x1 + y1 + z1)/400 == (x2 + y2 + z2)/600
prob += (x2 + y2 + z2)/600 == (x3 + y3 + z3)/300
prob += (x3 + y3 + z3)/300 == (x1 + y1 + z1)/400

status = prob.solve()
print(p.LpStatus[status])
print("")
print(f"x1: {p.value(x1)}")
print(f"x2: {p.value(x2)}")
print(f"x3: {p.value(x3)}")
print(f"y1: {p.value(y1)}")
print(f"y2: {p.value(y2)}")
print(f"y3: {p.value(y3)}")
print(f"z1: {p.value(y1)}")
print(f"z2: {p.value(y2)}")
print(f"z3: {p.value(y3)}")
