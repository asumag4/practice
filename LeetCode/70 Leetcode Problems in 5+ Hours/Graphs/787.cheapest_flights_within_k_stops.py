from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        flightsCost = [float('inf')] * n
        flightsCost[src] = 0

        qStops = deque([(src,0)]) # (city_i, cost_i)
        stops = 0

        while (qStops and (stops <= k)):
            # print("=================================") # DEBUG
            # print(flightsCost) # DEBUG
            
            for _ in range(len(qStops)):

                city_i, cost_i = qStops.popleft()
                # print(city_i, cost_i) # DEBUG

                for from_i, to_i, price_i in flights:

                    if ((city_i == from_i) and (cost_i + price_i < flightsCost[to_i])):
                        
                        flightsCost[to_i] = cost_i + price_i
                        qStops.append((to_i, flightsCost[to_i]))

            stops += 1

        return -1 if flightsCost[dst] == float('inf') else flightsCost[dst]
