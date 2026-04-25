from collections import defaultdict
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        sim_dict = defaultdict(set)
        for pair in similarPairs:
            sim_dict[pair[0]].add(pair[1])
            sim_dict[pair[1]].add(pair[0])
        if len(sentence1) != len(sentence2):
            return False

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            
            if word1 != word2:
                if word2 not in sim_dict[word1]:
                    return False
                
        return True


        
            

        