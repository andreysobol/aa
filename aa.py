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
    return Set([[Set([i, j]) for j in set2] for i in set1])


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


# Group https://en.wikipedia.org/wiki/Group_(mathematics)

def is_associative(target_set, operation):
    bc = cartesian_product(target_set, target_set)
    a_bc = cartesian_product(target_set, bc)
    abc = [{
        "a": item[0],
        "b": item[1][0],
        "c": item[1][1],
    } for item in a_bc]
    return all([
        operation(operation(i["a"], i["b"]), i["c"]) == operation(i["a"], operation(i["b"], i["c"])) 
        for i in abc
    ])

def is_identity_element(target_set, operation, identity_element):
    ise = is_element(identity_element, target_set)
    isi = all([operation(identity_element, j) == identity_element for j in target_set])
    return ise and isi

def is_inverse_operation(target_set, operation, identity_element, inverse_operation):
    return all([
        (operation(j, inverse_operation(j)) == operation(inverse_operation(j), j) == identity_element)
        for j in target_set
    ])

def is_group(target_set, operation, identity_element, inverse_operation):
    return all([
        is_associative(target_set, operation),
        is_identity_element(target_set, operation, identity_element),
        is_inverse_operation(target_set, operation, identity_element, inverse_operation),
    ])