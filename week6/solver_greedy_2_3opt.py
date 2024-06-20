#!/usr/bin/env python3

import sys
import math
from common import print_tour, read_input

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    # 2-opt
    tour = two_opt(tour, dist)

    # 3-opt
    tour = three_opt(tour, dist)

    return tour

def two_opt(tour, dist):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_length(new_tour, dist) < tour_length(tour, dist):
                    tour = new_tour
                    improved = True
    return tour

def three_opt(tour, dist):
    improved = True
    while improved:
        improved = False
        for i in range(len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                for k in range(j + 1, len(tour)):
                    new_tours = generate_3opt_moves(tour, i, j, k)
                    for new_tour in new_tours:
                        if tour_length(new_tour, dist) < tour_length(tour, dist):
                            tour = new_tour
                            improved = True
    return tour

def generate_3opt_moves(tour, i, j, k):
    # Generate all 3-opt moves
    a, b, c, d, e, f = tour[i], tour[i+1], tour[j], tour[j+1], tour[k], tour[(k+1) % len(tour)]
    return [
        tour[:i+1] + tour[i+1:j+1][::-1] + tour[j+1:],
        tour[:i+1] + tour[j:j+1] + tour[i+1:j] + tour[j+1:],
        tour[:i+1] + tour[j:j+1] + tour[i+1:j][::-1] + tour[j+1:],
        tour[:i+1] + tour[i+1:j+1][::-1] + tour[j+1:],
        tour[:i+1] + tour[j:j+1] + tour[j+1:k+1] + tour[i+1:j] + tour[k+1:],
        tour[:i+1] + tour[j:j+1] + tour[j+1:k+1][::-1] + tour[i+1:j] + tour[k+1:],
        tour[:i+1] + tour[j:j+1] + tour[j+1:k+1][::-1] + tour[i+1:j][::-1] + tour[k+1:]
    ]

def tour_length(tour, dist):
    return sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) + dist[tour[-1]][tour[0]]

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
