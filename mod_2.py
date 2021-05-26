from pulp import *


# Variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)

prob = LpProblem("Modelo 2", LpMinimize)

# Objective
prob += 0.3*x1 + 0.9*x2

# Constraints
prob += x1 + x2 >= 800
prob += -0.21*x1 + 0.30*x2 >= 0
prob += 0.03*x1 - 0.01*x2 >= 0

prob.solve()
print("\n"*100)
print(f"Status: {LpStatus[prob.status]}")
i = 1
for var in prob.variables():
    if "1" in var.name:
        print(f"lb de maíz en la mezcla diaria, {var.name} = {var.varValue}")
    elif "2" in var.name:
        print(f"lb de soya en la mezcla diaria, {var.name} = {var.varValue}")
    i += 1
print(f"Objectivo = {value(prob.objective)}")
