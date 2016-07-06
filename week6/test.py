#!/usr/bin/env python3

import sys
import math
import itertools

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)
    
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]
    
    def distance_from_current_city(to):
        return dist[current_city][to]
    
    p_city = list(itertools.permutations(cities))
#    print len(p_city)
    min_sum_path = [0,0]

    for i in range(len(p_city)):
        sum_path = [distance(p_city[i][N-1],p_city[i][0]) , p_city[i]]
        for j in range(N-1):
            sum_path[0] += distance(p_city[i][j],p_city[i][j+1])
        if min_sum_path[0] == 0 : min_sum_path = sum_path
        elif min_sum_path[0] > sum_path[0]: min_sum_path = sum_path
    
    print min_sum_path

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city

    return solution





if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
