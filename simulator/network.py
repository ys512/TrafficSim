from __future__ import annotations

from typing import List

from simulator.junction import Junction
from simulator.road import Road
import random


class Network:
    """
    Class of a road network, represented as a graph with junctions being its
    vertices and roads being its edges

    Attributes
    ----------
    junctions: junctions in the network
    roads: roads in the network
    """

    def __init__(self, junctions: List[Junction] = None,
                 roads: List[Road] = None):
        if junctions is None:
            self.junctions = []
        else:
            self.junctions = junctions

        if roads is None:
            self.roads = []
        else:
            self.roads = roads

    def generate_network(self, junction_num, max_road_length=5):
        self.junctions = []
        for i in range(junction_num):
            self.junctions.append(Junction(name=f'junction_{i}'))

        road_num = junction_num * 2
        # flag represents number of times a junction becomes an exit of a road,
        # which is equivalent to the length of out_rds of the junction
        flag = [0] * junction_num

        for i in range(road_num):
            length = random.randint(1, max_road_length)
            exit_idx = i // 2  # every junction is exit for two roads
            # junction number starts from 0
            if flag[exit_idx] == 0:
                origin_idx = exit_idx + 1 if exit_idx < junction_num - 1 else 0
            else:
                origin_idx = exit_idx - 1 if exit_idx > 1 else junction_num - 1  # two roads starts from different origins end at exit_idx

            flag[exit_idx] += 1

            road = Road(name=f'road_{origin_idx}_{exit_idx}', length=length,
                        origin=self.junctions[origin_idx],
                        exit=self.junctions[exit_idx])
            self.junctions[origin_idx].out_rds.append(road)
            self.junctions[exit_idx].in_rds.append(road)
            self.roads.append(road)
