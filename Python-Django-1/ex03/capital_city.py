import sys

def get_capital(state_to_find):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # for match, value in states.items():
    #     if match == state_to_find:
    #         print(capital_cities[value])
    #         exit()

    if state_to_find in states:
        print(capital_cities[states[state_to_find]])
    else:
        print("Unkown state")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_capital(sys.argv[1])