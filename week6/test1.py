#!/usr/bin/env python3

import sys
import math

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
    
    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    return solution

def solvecross(solution,cities):
    N = len(solution)
    for i in range(N-4):
        if intersection(cities[solution[i]],cities[solution[i+1]],cities[solution[i+2]],cities[solution[i+3]]):
            sol=solution[i+1]
            solution[i+1]=solution[i+2]
            solution[i+2]=sol
    return solution

def intersection(city1,city2,city3,city4):
    if (((city1[0]-city2[0])*(city3[1]-city1[1])+(city1[1]-city2[1])*(city1[0]-city3[0]))*((city1[0]-city2[0])*(city4[1]-city1[1])+(city1[1]-city2[1])*(city1[0]-city4[0]))<0) and (((city3[0]-city4[0])*(city1[1]-city3[1])+(city3[1]-city4[1])*(city3[0]-city1[0]))*((city3[0]-city4[0])*(city2[1]-city3[1])+(city3[1]-city4[1])*(city3[0]-city2[0]))<0):
        return True
    else:
        return False



if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    solution = solvecross(solution,read_input(sys.argv[1]))
    print_solution(solution)
