class Solution:
    def compress(self, chars: List[str]) -> int:
        output = []
        count = 0
        curr = chars[0]
        for c in chars:
            if c == curr:
                count += 1
            else:
                output.append(curr)
                if count > 1:
                    for n in str(count):
                        output.append(n)
                count = 1
                curr = c
        output.append(curr)
        if count > 1:
            print(count)
            for n in str(count):
                print(str(n))
                output.append(str(n))
        print(output)
        chars[:] = output
        return len(chars)
           