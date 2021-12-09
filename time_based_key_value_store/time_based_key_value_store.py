from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int):
        self.storage[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        entities = self.storage[key]

        left = 0
        right = len(entities)

        # Binary search
        while right > left:
            middle = (right + left) // 2
            middle_timestamp = entities[middle][0]

            if timestamp >= middle_timestamp:
                left = middle + 1

            elif timestamp < middle_timestamp:
                right = middle

        return "" if right == 0 else entities[right - 1][1]
