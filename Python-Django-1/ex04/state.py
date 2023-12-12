import sys

def get_state(capital_to_find):
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }

    for key, value in capital_cities.items():
        if value == capital_to_find:
            for state_key, state_value in states.items():
                if state_value == key:
                    print(state_key)
                    exit()
    print("Unkown capital city")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_state(sys.argv[1])