import sys

def get_whatever(to_find: str):
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
    # Llamar a uno o al otro
    print(to_find)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        for str in sys.argv[1].split(','):
            get_whatever(str.strip().capitalize())