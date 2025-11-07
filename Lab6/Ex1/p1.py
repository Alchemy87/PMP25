import sympy as sp

P_B = 0.01
P_not_B = 1 - P_B
sens = 0.95
spec = 0.90

P_Pos = sens * P_B + (1 - spec) * P_not_B
P_B_given_Pos = sens * P_B / P_Pos
print("P(B|+):", float(P_B_given_Pos))

spec_x = sp.symbols('spec_x')
eq = sp.Eq(0.5, sens * P_B / (sens * P_B + (1 - spec_x) * P_not_B))
spec_min = sp.solve(eq, spec_x)[0]
print("Spec for 50%:", float(spec_min))
