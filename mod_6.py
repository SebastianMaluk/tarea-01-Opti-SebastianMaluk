from pulp import *


# Variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)

prob = LpProblem("Modelo 6", LpMaximize)

# Objective
prob += 4*x1 + 5*x2

# Constraints
prob += 8*x1 + 3*x2 <= 22
prob += x1 + 2*x2 <= 7

prob.solve()
print(f"Status: {LpStatus[prob.status]}")
for var in prob.variables():
    print(f"{var.name} = {var.varValue}")
print(f"Objective = {value(prob.objective)}")
