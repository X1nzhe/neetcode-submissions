class Solution:

    def encode(self, strs: List[str]) -> str:
        res = '_START_'
        for s in strs:
            n = len(s)
            current_s = '_SUB_LEN_' + str(n) + '_SUB_START_' + s + '_SUB_END_'
            res += current_s
        return res + '_END_'


    def decode(self, s: str) -> List[str]:
        START = '_START_'
        SUB_LEN = '_SUB_LEN_'
        SUB_START = '_SUB_START_'
        SUB_END = '_SUB_END_'
        END = '_END_'

        assert s.startswith(START) and s.endswith(END) 
        body = s[len(START):-len(END)]

        result = []
        i = 0
        while i < len(body):
            # 1. read '_SUB_LEN_'
            assert body.startswith(SUB_LEN, i)
            i += len(SUB_LEN)
            
            # 2. read length of sub string
            j = i
            while j < len(body) and body[j].isdigit():
                j += 1
            length = int(body[i:j])
            i = j
            
            # 3. read '_SUB_START_'
            assert body.startswith(SUB_START, i)
            i += len(SUB_START)
            
            # 4. read sub string by length
            result.append(body[i:i+length])
            i += length

            # 5. read '_SUB_END_'
            assert body.startswith(SUB_END, i)
            i += len(SUB_END)
        
        return result

            


        

