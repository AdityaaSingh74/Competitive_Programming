from collections import deque

class Solution:
    def processStr(self, s: str) -> str:
        dq = deque()
        rev = False

        for ch in s:

            if 'a' <= ch <= 'z':
                if not rev:
                    dq.append(ch)
                else:
                    dq.appendleft(ch)

            elif ch == '*':
                if dq:
                    if not rev:
                        dq.pop()
                    else:
                        dq.popleft()

            elif ch == '%':
                rev = not rev

            else:  # '#'
                if not dq:
                    continue

                temp = list(dq)

                if not rev:
                    dq.extend(temp)
                else:
                    for x in reversed(temp):
                        dq.appendleft(x)

        return "".join(dq if not rev else reversed(dq))