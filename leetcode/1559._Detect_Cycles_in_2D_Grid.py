'''
THIS DOES NOT PASS LC! NEED HELP

Link to problem: https://leetcode.com/problems/detect-cycles-in-2d-grid/
Loom explaining solution you wrote (5m):
Solution:
Description
Key ideas
- Should realize it's DFS on first sight
- Need to realize there might be small distinct graphs all littered throughout

Difficulty:
- Easy to come up with approach
- Hard to optimize for "Memory Limit Exceeded"
'''

def pairwise_add(base: tuple[int], diff: tuple[int]) -> tuple[int]:
    return base[0] + diff[0], base[1] + diff[1]

# typing could be improved with generics, which leetcode does not support
def at(grid: List[List[any]], cord: tuple[int]) -> any:
    return grid[cord[0]][cord[1]]

def mark(grid: List[List[bool]], cord: tuple[int]) -> None:
    grid[cord[0]][cord[1]] = True

def next_unmarked(grid: List[List[bool]]) -> tuple[int] | None:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if not grid[y][x]:
                return y, x
    return None

class Solution:
    '''
    Intuition: DFS

    This fails on the memory front for m x n of size 500
    '''
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def out_of_bound(cord: tuple[int]) -> bool:
            return not (0 <= cord[0] < len(grid)) or not (0 <= cord[1] < len(grid[0]))

        globally_visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def visit_from(start: tuple[int]) -> bool:
            character = at(grid, start)
            to_visit = [(start, dict())]

            # we need to do a dfs here
            while to_visit:
                current_cord, currently_visited = to_visit.pop()

                if current_cord in currently_visited:
                    if len(currently_visited) - currently_visited[current_cord] >= 4:
                        print(current_cord, at(grid, current_cord))
                        print(currently_visited)
                        return True
                    # else handled by below

                # setting up next iteration
                if at(globally_visited, current_cord):
                    continue
                currently_visited[current_cord] = len(currently_visited)
                mark(globally_visited, current_cord)

                for cord_diff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_cord = pairwise_add(current_cord, cord_diff)
                    if out_of_bound(new_cord):
                        continue
                    if at(grid, new_cord) != character:
                        continue
                    to_visit.append((new_cord, currently_visited.copy()))

            return False

        while (next_start := next_unmarked(globally_visited)) is not None:
            if visit_from(next_start):
                return True

        return False