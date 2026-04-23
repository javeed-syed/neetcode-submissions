class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # eliminate extra values

        for x, y, z in triplets[:]:
            if x > target[0] or y > target[1] or z > target[2]:
                triplets.remove([x, y, z])

        a, b, c = target
        found = [False, False, False]

        for x, y, z in triplets:
            found[0] = found[0] or a == x
            found[1] = found[1] or b == y
            found[2] = found[2] or c == z
        
        return all(found)

