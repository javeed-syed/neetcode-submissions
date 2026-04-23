class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        l = len(digits)
        res = []

        def solve(i, path):
            if i == l:
                res.append("".join(path))
                return
            
            digit = digits[i]
            chars = hash_map[digit]

            for char in chars:
                path.append(char)
                solve(i + 1, path)
                path.pop()
        
        if len(digits) == 0:
            return []
            
        solve(0, [])
        return res