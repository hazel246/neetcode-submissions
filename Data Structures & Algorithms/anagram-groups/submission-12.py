class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group={} #lets say it has act

        for word in strs:
            key="".join(sorted(word))
            #key={act: }

            if key in group:
                group[key].append(word)

            else:
                group[key] = [word] # start new list with word

        return list(group.values())










       





        


    




       





        