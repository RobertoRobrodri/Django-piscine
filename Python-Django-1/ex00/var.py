def my_var():
    var = 42
    print(var, "has a type", type(var))
    var = "42"
    print(var, "has a type", type(var))
    var = "quarante-deux"
    print(var, "has a type", type(var))
    var = 42.0
    print(var, "has a type", type(var))
    var = True
    print(var, "has a type", type(var))
    # List
    # List items are ordered, changeable, and allow duplicate values.
    var = [42]
    print(var, "has a type", type(var))
    # Dictionary
    # Key value
    var = {42: 42}
    print(var, "has a type", type(var))
    # Tuple
    # Tuple items are ordered, unchangeable, and allow duplicate values.
    var = (42,)
    print(var, "has a type", type(var))
    # Set
    # A set is a collection which is unordered, unchangeable*, and unindexed
    # Duplicates not allowed
    var = set()
    print(var, "has a type", type(var))

if __name__ == '__main__':
    my_var()