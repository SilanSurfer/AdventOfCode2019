
def solution_part_one(filename):
    with open(filename) as file:
        asteroid_map = [[sign for sign in input_line.rstrip()] for input_line
                        in file.readlines()]
    result = get_asteroids_visibility(asteroid_map)
    return max(result, key=lambda k: result[k])

def get_asteroids_visibility(asteroids_map):
    asteroids_visibility = {}
    return asteroids_visibility


if __name__ == '__main__':
    solution_part_one("Day10Input.txt")