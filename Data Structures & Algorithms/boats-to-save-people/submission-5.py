class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        data = [0] * (max(people) + 1)

        for x in people:
            data[x] += 1

        i = 1
        j = len(data) - 1
        c = 0

        while i <= j:
            if data[i] <= 0:
                i += 1
                continue

            if data[j] <= 0:
                j -= 1
                continue

            if i + j <= limit:
                data[i] -= 1
                data[j] -= 1
            else:
                data[j] -= 1

            c += 1

        return c