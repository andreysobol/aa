# https://en.wikipedia.org/wiki/Set_(mathematics)

class Set():

    def __init__(self, elements):
        self.elements = elements

    def get_elements(self):
        return self.elements

    def __getitem__(self, item):
        return self.elements[item]

def is_element(element, target_set):
    return element in target_set

def is_subset(possible_subset, target_set):
    return all([is_element(i, target_set) for i in possible_subset])

def intersection(set1, set2):
    return Set([i for i in set1 if is_element(i, set2)])

def difference(set1, set2):
    r1 = [i for i in set1 if not is_element(i, set2)]
    r2 = [i for i in set2 if not is_element(i, set1)]
    return Set(r1 + r2)

def subtract(subtracted_set, subtractor_set):
    return Set([i for i in subtracted_set if not is_element(i, subtractor_set)])

def cartesian_product(set1, set2):
    return [[Set([i, j]) for j in set2] for i in set1]


# Magma (groupoid) https://en.wikipedia.org/wiki/Magma_(algebra)

def is_closed(target_set, operation, arguments):
    if arguments == 1:
        return all([operation(a) in target_set for a in target_set])
    if arguments == 2:
        return all(
            [
                (operation(param[0], param[1]) in target_set)
                for param in cartesian_product(target_set, target_set)
            ]
        )
    return None

def is_magma(target_set, operation):
    return is_closed(target_set, operation, 1)