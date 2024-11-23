class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode = {' ': ' '}
        res = []
        letter = ord('a')
        for k in key:
            if letter > ord('z'):
                break
            if k not in decode:
                decode[k] = chr(letter)
                letter += 1

        for c in message:
            res.append(decode[c])
        
        return ''.join(res)