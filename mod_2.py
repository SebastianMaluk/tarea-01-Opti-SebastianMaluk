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
print(f"Status: {LpStatus[prob.status]}")
for var in prob.variables():
    print(f"{var.name} = {var.varValue}")
print(f"Objective = {value(prob.objective)}")
