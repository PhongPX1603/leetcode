class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        counter = dict()
        n = len(s)
        result = ''
        min = len(s)
        for word in dictionary:
            i = 0
            j = 0
            count = 0
            while i < n:
                if s[i] != word[j]:
                    # print(i, j)
                    i += 1
                    count += 1
                else:
                    # print(i, j)
                    i += 1
                    j += 1
                if j == len(word):
                    count += (n - i)
                    break
# solotion 1: 50% faster, less 20% memory   
        #     if n - count == len(word):
        #         counter[word] = count
        #         if count < min:
        #             min = count
        #             result = word
        #         elif count == min:
        #             for k in range(len(word)):
        #                 if result[k] != word[k]:
        #                     if ord(result[k]) > ord(word[k]):
        #                         result = word
        #                     break
        # return result
    
# solution 2:
            if n - count == len(word):
                counter[count] = counter.get(count, []) + [word]
        if len(counter) == 0:
            return ''
        return min(counter[min(counter.keys())])
        