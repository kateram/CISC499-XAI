from pyparsing import deque


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)]) #position, speed, length
        
        visited = set()
            
        while queue:
            pos, speed, length = queue.popleft()
            if pos == target:
                return length
            if (pos, speed) in visited:
                continue
            visited.add((pos, speed))
            queue.append((pos+speed, speed*2, length+1))
            if speed > 0:
                queue.append((pos, -1, length+1))
            else:
                queue.append((pos, 1, length+1))
            
solution = Solution()
print(solution.racecar(3))          
                
                    