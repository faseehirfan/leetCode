class Solution:
    def carFleetStack(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(list(zip(position, speed)), reverse=True)
        
        for car in cars:
            if not stack: 
                stack.append((target - car[0]) / car[1])
            else:
                cur_time = (target - car[0]) / car[1]
                if cur_time > stack[-1]:
                    stack.append(cur_time)

        return len(stack)

    def carFleetIterative(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse=True)
        fleets = 0
        fleet_time = 0
        
        for car in cars:
            time = (target - car[0]) / car[1]
            if time > fleet_time:
                fleets += 1
                fleet_time = time
               

        return fleets