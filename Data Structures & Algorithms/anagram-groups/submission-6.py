class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = []
        used = set()

        for i in range(len(strs)):

            if i in used:
                continue

            group = [strs[i]]

            for j in range(i + 1, len(strs)):

                if len(strs[i]) != len(strs[j]):
                    continue

                s_count = {}
                t_count = {}

                for k in range(len(strs[i])):
                    s_count[strs[i][k]] = s_count.get(strs[i][k], 0) + 1
                    t_count[strs[j][k]] = t_count.get(strs[j][k], 0) + 1

                if s_count == t_count:
                    group.append(strs[j])
                    used.add(j)

            used.add(i)
            x.append(group)

        return x