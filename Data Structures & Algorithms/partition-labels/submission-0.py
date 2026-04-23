class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {}
        res = []

        for idx, ch in enumerate(s):
            hash_map[ch] = idx
        
        idx = 0

        while idx < len(s):
            curr = s[idx]
            last_curr_idx = hash_map[curr]

            itr = idx + 1
            
            while itr < last_curr_idx:
                curr = s[itr]
                last_idx = hash_map[curr]

                if last_idx > last_curr_idx:
                    last_curr_idx = last_idx
                itr += 1
            
            res.append(last_curr_idx - idx + 1)
            idx = last_curr_idx + 1

        return res