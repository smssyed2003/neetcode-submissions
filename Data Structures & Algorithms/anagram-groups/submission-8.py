# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = []
#         used = {}
#         for i in range(len(strs)):
#             if i in used:
#                 continue
#             for j in range(i+1, len(strs)):
#                 group = [strs[i]]
#                 if(len(strs[i]) != len(strs[j])):
#                     continue
#                 s_counts = {}
#                 t_counts = {}
#                 for k in range(len(strs)):
#                     s_counts[strs[i][k]] = s_counts.get(strs[i][k], 0) + 1
#                     t_counts[strs[j][k]] = t_counts.get(strs[j][k], 0) + 1
#                 if(s_counts==t_counts):
#                     group.append(strs[j])
#                     used.add(j)
#             used.add(i)
#             x.append(group)
#         return x

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        used = set()
        for i in range(len(strs)):
            if i in used:
                continue
            group = [strs[i]]
            for j in range(i+1, len(strs)):
                if(len(strs[i]) != len(strs[j])):
                    continue
                s_counts = {}
                t_counts = {}
                for k in range(len(strs[i])):
                    s_counts[strs[i][k]] = s_counts.get(strs[i][k], 0) + 1
                    t_counts[strs[j][k]] = t_counts.get(strs[j][k], 0) + 1
                if(s_counts==t_counts):
                    group.append(strs[j])
                    used.add(j)
            used.add(i)
            res.append(group)
        return res  