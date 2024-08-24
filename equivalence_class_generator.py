from matrix_homomorphism_generator import *
from alg_structures import *
from tqdm import tqdm
import numpy as np


def cut_with_group_action(group, vector_space) -> list:
    marked = set([])
    equvivalence_classes = []
    for vec in vector_space(n, p):
        if vec not in marked:
            equvivalence_class_of_vector = {tuple((g @ np.array(vec)) % p) for g in group}
            marked = marked.union(equvivalence_class_of_vector)
            equvivalence_classes.append(equvivalence_class_of_vector)

    return marked


def stabilizer(vector, group, p):
    fix_set = []
    for g in group:
        if (((np.array(g) @ np.array(vector)) %p) == np.array(vector)).all():
            fix_set.append(g)
    return fix_set


def fix(g, vector_space, p):
    fix_g = []
    for vec in vector_space:
        print(g)
        print(vec)
        if (((np.array(g) @ np.array(vec)) % p) == np.array(vec)).all():
            fix_g.append(vec)
    return fix_g