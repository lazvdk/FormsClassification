from matrix_homomorphism_generator import *
from alg_structures import *
from tqdm import tqdm
import numpy as np


def cut_with_group_action(vector_space, group, p, t) -> list:
    # vector_space[0] = True
    print("Cutting vector space by group")
    equvivalence_classes = []
    # equvivalence_classes.append(set((index_to_vector(0, t=3, p=p))))
    for vector_index in tqdm(range(-1, len(vector_space)-1), total=len(vector_space)-1):
        vector = vector_index+1
        
        if vector_space[vector] == True:
            continue
        else:
            vec = np.array(index_to_vector(vector, t=t, p=p))
            # print(vec)
            equvivalence_class_of_vector = set([])
            # print(equvivalence_class_of_vector)
            for g in group:
                new_vector = (np.array(g) @ np.array(vec)) %p
                vector_space[vector_to_index(vector=new_vector, p=p, t=t)] = True
                equvivalence_class_of_vector.add(tuple(new_vector.tolist()))
            equvivalence_classes.append(equvivalence_class_of_vector)

    return equvivalence_classes


def stabilizer(vector, group, p):
    fix_set = []
    for g in group:
        if (((np.array(g) @ np.array(vector)) %p) == np.array(vector)).all():
            fix_set.append(g)
    return fix_set


def X_to_g(g, vector_space, p):
    x_to_g = []
    for vec in vector_space:
        if (((np.array(g) @ np.array(vec)) % p) == np.array(vec)).all():
            x_to_g.append(vec)
    return x_to_g