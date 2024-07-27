import numpy as np
from itertools import *
from tqdm import tqdm
import operator

def GL(n, p):
    GLnp = []
    total_combinations = p ** (n * n)
    print(f'Generating GL{n}(F_{p})...')
    for elements in tqdm(product(range(p), repeat=n*n), total=total_combinations):
        matrix = np.array(elements).reshape((n, n))
        if (round(np.linalg.det(matrix)) % p) != 0:
            GLnp.append(matrix)
    
    return GLnp

def vector_space(t, p):
    return list(repeat(False, p**t))

def vector_to_index(vector, p, t):
    counter = count()
    powers_of_p = reversed(list(map(lambda  x: p**x, [next(counter) for i in range(t)])))
    
    return int(sum(list(starmap(operator.mul, zip(vector, powers_of_p))))) 

def index_to_vector(index, t, p):
    vec = str(np.base_repr(index, p))
    while len(vec)<t:
        vec = "0" + vec

    return list(float(i) for i in tuple(vec))

def linear_combinations(vectors, p):
    arr_vectors = list(map(np.array, vectors))
    
    counter = count()
    coefficent_tuples = list(product([next(counter) for _ in range(p)], repeat=len(vectors)))

    spanned_space = set([])

    for coeff_tuple in coefficent_tuples:
        vector = tuple(np.array(sum(np.array(list(starmap(operator.mul, list(zip(coeff_tuple, arr_vectors)))))%p)%p).tolist())
        spanned_space.add(vector)

    spanned_space = np.array(spanned_space)
    return spanned_space.tolist()

