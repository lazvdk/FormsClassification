from typing import Generator, Any
import numpy as np
from itertools import *

def vector_space(dim: int, p: int) -> Generator[np.array, None, None]:
    return (elements for elements in product(range(p), repeat=dim))
    
def GL(n: int, p: int) -> Generator[np.array, None, None]:
    return (np.array(elements).reshape((n, n)) for elements in product(range(p), repeat=n*n) if (round(np.linalg.det(np.array(elements).reshape((n, n))))%p) !=0)
    # for data in product(range((p), repeat=n*n)):
    #    round(np.linalg.det(np.array(elements))) 

