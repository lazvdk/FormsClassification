from alg_structures import *
from equivalence_class_generator import *
from matrix_homomorphism_generator import *
from math import comb




primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]


#-------------stabilizers-------------

#n = 3
#d = 2
#t = comb(d+n-1, d)


# #x^2 + yz u n=3 d=2
# q1 = [1.0, 1.0, 0.0, 0.0, 0.0, 0.0]

# for p in primes[:3]:
#     phi_of_G = phi(phi_matrix=phi_matrix(n, d), group=GL(n, p), n=n, t=t, p=p)
#     print(stabilizer(vector=q1, group=phi_of_G, p=p))


#-------------orbits-------------

# #x^2 + yz u n=3 d=2
#n = 3
#d = 2
#t = comb(d+n-1, d)

# q1 = [1, 1, 0, 0, 0, 0]

# orbit = set([])

# for p in primes[:3]:
#     phi_of_G = phi(phi_matrix=phi_matrix(n, d), group=GL(n, p), n=n, t=t, p=p)
#     for g in phi_of_G:
#         #cast to tuple because tuple is hashable
#         orbit.add((tuple((np.array(g) @ np.array(q1)).tolist())))
#     print(orbit)
#     orbit = set([])


#-------------orbit counting/representatives-------------

n = 3

partitioned_space = []

#calculating phi(G) is the limiting factor
#for reference, calculating phi(GL3(F_5)) takes ~10mins; everything for smaller parameters is fast (<30s)
for d in [2, 3]:
    aux_matrix = phi_matrix(n, d)
    t = comb(d+n-1, d)
    for p in primes[:4]:
        phi_of_G = phi(phi_matrix=aux_matrix, group=GL(n, p), n=n, t=t, p=p)
        partitioned_space.append(cut_with_group_action(vector_space=vector_space(t, p), group=phi_of_G, p=p, t=t))
    

print(partitioned_space)

