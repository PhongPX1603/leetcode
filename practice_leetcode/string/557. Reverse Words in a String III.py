class Solution:
    def reverseWords(self, s: str) -> str:
#solution 1: faster than 6%, less than 15%
#         s = list(s)
#         end = 0
#         start = 0
        
#         while end < len(s):
#             if s[end] == ' ':
#                 s[start: end] = reversed(s[start: end])
#                 start = end + 1
#             elif end == len(s) - 1:
#                 s[start: end+1] = reversed(s[start: end+1])
#             end += 1
#         return ''.join(s)

#solution 2: faster than 33%, less than 85%
        # s = s.split(' ')
        # for i in range(len(s)):
        #     s[i] = ''.join(reversed(list(s[i][:])))
        # return ' '.join(s)
    
#solution 3: faster than 90%, less than 50%
        # s = s.split(' ')
        # for i in range(len(s)):
        #     s[i] = s[i][::-1]
        # return ' '.join(s)

#solution 4: similar solution 3
        res = ''
        for char in s.split(' '):
            char = char[::-1]
            res += char + ' '
        return res[:-1]