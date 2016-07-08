#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def initial_solve(cities):
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
    used = 0
    N = len(solution)
    for i in range(N):
        for j in range (N):
            if i != j:
                if minimumlength(cities[solution[i]],cities[solution[(i+1)%N]],cities[solution[j]],cities[solution[(j+1)%N]]) == 1:
#                    print "(i,j+1)=(%s,%s)" % (i,j+1)
                    new_sol=solution[i+1 : j+1]
                    solution[i+1 : j+1] = new_sol[::-1]
                    used = 1
    return solution,used

def solvewaste(solution,cities):
    N = len(solution)
    used = 0
    for i in range(N):
        for j in range(N):
            if i<j:
                if minimumlength_6(cities[solution[i]],cities[solution[(i+1)%N]],cities[solution[(i+2)%N]],cities[solution[(i+3)%N]],cities[solution[j]],cities[solution[(j+1)%N]]) == 1:
                    new_sol = solution[i+1 : j+1]
                    new_sol_initial = new_sol[0:2]
                    del new_sol[0:2]
                    new_sol.extend(new_sol_initial)
                    solution[i+1 : j+1]=new_sol
                    used = 1
    return solution,used

#def intersection(city1,city2,city3,city4):
#    if (((city1[0]-city2[0])*(city3[1]-city1[1])+(city1[1]-city2[1])*(city1[0]-city3[0]))*((city1[0]-city2[0])*(city4[1]-city1[1])+(city1[1]-city2[1])*(city1[0]-city4[0]))<0) and (((city3[0]-city4[0])*(city1[1]-city3[1])+(city3[1]-city4[1])*(city3[0]-city1[0]))*((city3[0]-city4[0])*(city2[1]-city3[1])+(city3[1]-city4[1])*(city3[0]-city2[0]))<0):
#        return 1
#    else:
#        return 0



def minimumlength(city1,city2,city3,city4):
    if distance(city1,city2) + distance(city3,city4) > distance(city1,city3) + distance(city2,city4):
        return 1
    else: return 0

def minimumlength_6(city1,city2,city3,city4,city5,city6):
    if distance(city1,city2)+distance(city2,city3)+distance(city3,city4)+distance(city5,city6)>distance(city1,city4)+distance(city5,city2)+distance(city2,city3)+distance(city3,city6):
        return 1
    else : return 0

def solve(cities):
    solution = initial_solve(cities)
#    solution = solvecross(solution,cities)
#    old_solution = solution
    used = 1
    while used == 1:
        #        print "while"
        solution,used = solvewaste(solution,cities)
        solution,used = solvecross(solution,cities)
#        old_solution = solution
    return solution

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
    cities = read_input(sys.argv[1])
