import sys


# tuples
def main():

    # lat, long
    coords = (42.376, -71.115)
    print(coords)

    # print(f"Lat: {coords[0]}, Long: {coords[1]}")
    # print(f"Lat: {coords[0]}")
    # print(f"Long: {coords[1]}")

    # tuple assignment
    lat, long = coords
    print(f"Lat: {lat}")
    print(f"Long: {long}")

    # cant change tuples like lists
    # coords[0] = 777

    # tuples save on mem (efficiency over flexibility)
    coords_tuple = (42.376, -71.115)
    coords_list = [42.376, -71.115]
    print(f"Tuple = {sys.getsizeof(coords_tuple)} bytes")
    print(f"List = {sys.getsizeof(coords_list)} bytes")


main()
