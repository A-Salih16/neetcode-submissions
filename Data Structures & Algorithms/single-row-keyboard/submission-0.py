class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dict={}
        for i in range(len(keyboard)):
            dict[keyboard[i]]=i
        time =0
        location=0
        for i in range (len(word)):
            time+=abs(location-dict[word[i]])
            location=dict[word[i]]
        return time
            
            
        