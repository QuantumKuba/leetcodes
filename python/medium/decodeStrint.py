class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = ""
        for c in s:
            if c != ']':
                if c.isdigit():
                    n += c
                else:
                    if n != "":
                        stack.append(n)
                        n = ""
                    stack.append(c)
            elif c == ']':
                rep = ""
                while (c := stack.pop()) != '[':
                    rep = c + rep
                
                num = stack.pop()
                stack.append(rep*int(num))
                
        return ''.join(stack)
    
if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a2[c]]"))  # Example usage
    # print(s.decodeString("2[abc]3[cd]ef"))  # Example usage
    # print(s.decodeString("abc3[cd]xyz"))  # Example usage
    # print(s.decodeString("2[3[a]b]"))  # Example usage
    # print(s.decodeString("10[a]"))  # Example usage