from pulp import *


# Variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
y1 = LpVariable("y1", 0)
y2 = LpVariable("y2", 0)
y3 = LpVariable("y3", 0)
z1 = LpVariable("z1", 0)
z2 = LpVariable("z2", 0)
z3 = LpVariable("z3", 0)

prob = LpProblem("Modelo 4", LpMaximize)

# Objective
prob += 400*(x1 + x2 + x3) + 300*(y1 + y2 + y3) + 100*(z1 + z2 + z3)

# Constraints
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

prob.solve()
print(f"Status: {LpStatus[prob.status]}")
for var in prob.variables():
    print(f"{var.name} = {var.varValue}")
print(f"Objective = {value(prob.objective)}")
