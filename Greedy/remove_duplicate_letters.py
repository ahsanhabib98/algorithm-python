class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_location = {}
        for i in range(len(s)):
            last_location[s[i]] = i

        res, seen = [], set()
        for i in range(len(s)):
            if s[i] not in seen:
                while res and res[-1] > s[i] and last_location[res[-1]] > i:
                    seen.remove(res.pop())
                res.append(s[i])
                seen.add(s[i])
            else:
                continue
        return ''.join(res)