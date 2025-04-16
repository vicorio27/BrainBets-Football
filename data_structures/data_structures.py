def arrays():
    arr = ["one", "two", "three"]
    print(arr[0])
    #'one'
    print(arr)
    # ['one', 'two', 'three']

    # Lists are mutable:
    arr[1] = "hello"
    print(arr)
    # ['one', 'hello', 'three']

    del arr[1]
    print(arr)
    ##['one', 'three']

    # Lists can hold arbitrary data types:
    arr.append(23)
    print(arr)
    # ['one', 'three', 23]


def tuples():
    arr = ("one", "two", "three")
    print(arr[0])
    #'one'

    # Tuples have a nice repr:
    print(arr)
    # ('one', 'two', 'three')

    # Tuples are immutable:
    arr[1] = "hello"
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # TypeError: 'tuple' object does not support item assignment

    del arr[1]
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # TypeError: 'tuple' object doesn't support item deletion

    # Tuples can hold arbitrary data types:
    # (Adding elements creates a copy of the tuple)
    arr + (23,)
    # ('one', 'two', 'three', 23)


def arrays_module():
    import array

    arr = array.array("f", (1.0, 1.5, 2.0, 2.5))
    print(arr[1])
    # 1.5

    # Arrays have a nice repr:
    print(arr)
    # array('f', [1.0, 1.5, 2.0, 2.5])

    # Arrays are mutable:
    arr[1] = 23.0
    print(arr)
    # array('f', [1.0, 23.0, 2.0, 2.5])

    del arr[1]
    print(arr)
    # array('f', [1.0, 2.0, 2.5])

    arr.append(42.0)
    print(arr)
    # array('f', [1.0, 2.0, 2.5, 42.0])

    # Arrays are "typed":
    arr[1] = "hello"
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # TypeError: must be real number, not str


def string_and_arrays():
    arr = "abcd"
    print(arr[1])
    #'b'

    print(arr)
    #'abcd'

    # Strings are immutable:
    arr[1] = "e"
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # TypeError: 'str' object does not support item assignment

    del arr[1]
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # TypeError: 'str' object doesn't support item deletion

    # Strings can be unpacked into a list to
    # get a mutable representation:
    print(list("abcd"))
    # ['a', 'b', 'c', 'd']
    print("".join(list("abcd")))
    #'abcd'

    # Strings are recursive data structures:
    print(type("abc"))
    # "<class 'str'>"
    print(type("abc"[0]))
    # "<class 'str'>"


def dicts():
    car1 = {
        "color": "red",
        "mileage": 3812.4,
        "automatic": True,
    }
    car2 = {
        "color": "blue",
        "mileage": 40231,
        "automatic": False,
    }

    # Dicts have a nice repr:
    print(car2)
    # {'color': 'blue', 'automatic': False, 'mileage': 40231}

    # Get mileage:
    print(car2["mileage"])
    # 40231

    # Dicts are mutable:
    car2["mileage"] = 12
    car2["windshield"] = "broken"
    print(car2)
    # {'windshield': 'broken', 'color': 'blue','automatic': False, 'mileage': 12}

    # No protection against wrong field names,
    # or missing/extra fields:
    car3 = {
        "colr": "green",
        "automatic": False,
        "windshield": "broken",
    }
