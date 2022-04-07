class Solution:
    def entityParser(self, text: str) -> str:
        chars = {'&quot;':'"', 
                 '&apos;':'\'', 
                 '&amp;':'&', 
                 '&gt;':'>', 
                 '&lt;':'<', 
                 '&frasl;':'/'}
        output = ''
        i = 0
        while i < len(text):
            if text[i] != '&':
                output += text[i]
                i += 1
            else:
                if i == len(text) - 1:
                    output += text[i]
                    break
                check = True
                next_idx = i + 1
                while text[next_idx] != ';':
                    if text[next_idx] == '&':
                        check = False
                        break
                    else:
                        next_idx += 1
                if check: 
                    next_idx += 1
                string = text[i:next_idx]
                if string in chars:
                    output += chars[string]
                else:
                    output += string
                i = next_idx
        return output