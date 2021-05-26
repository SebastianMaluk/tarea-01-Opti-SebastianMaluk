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
print("\n"*100)
print(f"Status: {LpStatus[prob.status]}")
i = 1
for var in prob.variables():
    if "1" in var.name:
        print(f"ton producidas diariamente de pintura para exteriores, {var.name} = {var.varValue}")
    elif "2" in var.name:
        print(f"ton producidas diariamente de pintura para interiores, {var.name} = {var.varValue}")
    i += 1
print(f"Objective = {value(prob.objective)}")
