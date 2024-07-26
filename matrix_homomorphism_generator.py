#exec((str(coefficients)[1:-1]).replace("'", "") + " = " + "sp.symbols(coefficients)") 
import itertools as it
import sympy as sp
import numpy as np
from math import comb, prod
from tqdm import tqdm

def homogenous_polynomial(n, d):
    t= comb((d+n-1), d)
    variables = ["x" + str(_) for _ in range(1, n+1)]
    coefficients = ["c" + str(_) for _ in range(1, t+1)]
    
    monomials_without_coeffs = map("*".join, (it.combinations_with_replacement(variables, r=d)))
    
    full_monomials = map("*".join, (zip(coefficients, monomials_without_coeffs)))
    
    polynomial = " + ".join(full_monomials)

    return polynomial
    
def phi_matrix(n, d):
    t= comb((d+n-1), d)

    names_of_coefficients = ["c" + str(i) for i in range(1, t+1)]
    names_of_variables = ["x" + str(i) for i in range(1, n+1)]
    new_variables = ["xp" + str(i) for i in range(1, n+1)]

    names_of_coefficients = sp.symbols(names_of_coefficients)
    names_of_variables = sp.symbols(names_of_variables)
    new_variables = sp.symbols(new_variables)

    ABCD_matrix = [list(map(lambda x: x+str(i), ["v" + str(i) for i in range(1, n+1)])) for i in range(1, n+1)]
    ABCD_matrix = np.array(ABCD_matrix).transpose()
    ABCD_matrix = ABCD_matrix.tolist()
    ABCD_matrix = sp.symbols(ABCD_matrix)

    change_of_vars_vector = sp.Matrix(ABCD_matrix) * sp.Matrix(new_variables)    

    change_of_vars = dict(zip(names_of_variables, change_of_vars_vector))

    polynomial = sp.poly(homogenous_polynomial(n, d), [*names_of_coefficients, *names_of_variables])

    new_polynomial = polynomial.subs(change_of_vars)

    new_polynomial = sp.Poly(new_polynomial.as_expr(), new_variables)
    new_coefficients = new_polynomial.coeffs()

    matrix = [sp.Poly(row, names_of_coefficients).coeffs() for row in new_coefficients]

    return str(matrix)

def phi(phi_matrix, group, n, t, p):
    matrix = phi_matrix
    counter = it.count(start=1)
    indices = list(it.starmap(lambda x, y: str(x) + str(y), it.product([next(counter) for _ in range(n)], repeat=2)))
    symbol_space_variables = list(map(lambda x: "v" + str(x), indices))
    code_space_variables = list(map(lambda x: "g[" + str(int(x[0])-1) + "][" + str(int(x[1])-1) + "]", indices))

    symbol_code_pairs = dict(zip(symbol_space_variables, code_space_variables))
    for symbol, code in symbol_code_pairs.items():
        matrix = matrix.replace(symbol, code)

    print("Calculating phi(GL" + str(n) + "(" + str(p) + "))")
    out_group =set()
    for g in tqdm(group, total=len(group)):
        phi_of_g = tuple(map(tuple, (np.array(eval(matrix)) % p).tolist()))
        out_group.add(phi_of_g)
        
    return out_group

