class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        

        #initialize a result frequency map using the first word
        result = Counter(words[0])
        #1st loop: {b:1,e:1,l:2,a:1}
        #Now result represents the maximum possible common letters. As you compare with other words, you shrink it.

        #starting from 1, 0 is skipped
        for word in words[1:]:
            word_count=Counter(word)

            for c in result:
                result[c]=min(word_count[c],result[c])

        
        #convert frequency map into a list of characters

        return list(result.elements())


            



        

            