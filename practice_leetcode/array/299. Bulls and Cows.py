class Solution:
    def getHint(self, secret: str, guess: str) -> str:      
# solution 1: faster than 5%, less than 35% 
        # cows, bulls =0, 0
        # secret = list(secret)
        # guess = list(guess)
        # for i, c in enumerate(secret):
        #     if c == guess[i]:
        #         bulls += 1
        #         secret[i] = '_'
        #         guess[i] = '_'
        # for i, c in enumerate(secret):
        #     if c in guess and c != '_':
        #         cows += 1
        #         guess[guess.index(c)] = '_'
        # return f'{bulls}A{cows}B' 
    
# solution 1: faster than 30%, less than 80%
        cows, bulls = 0, 0
        for i, num in enumerate(guess):
            if num not in guess[:i]:
                cows += min(secret.count(num), guess.count(num))
            if num == secret[i]:
                bulls += 1
                cows -= 1
        return f'{bulls}A{cows}B' 