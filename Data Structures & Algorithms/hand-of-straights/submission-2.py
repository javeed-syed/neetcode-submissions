class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = Counter(hand)

        for num in hand:
            freq = count.get(num)
            if freq == 0:
                continue
            for i in range(num, num + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
        return True