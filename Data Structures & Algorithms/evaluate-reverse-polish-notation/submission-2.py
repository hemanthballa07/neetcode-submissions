class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for ch in tokens:
            if ch in "+-*/":
                b = st.pop()
                a = st.pop()
                if ch == "+":
                    st.append(a+b)
                elif ch == "-":
                    st.append(a-b)
                elif ch == "*":
                    st.append(a*b)
                else:
                    st.append((-1 if a*b<0 else 1)*(abs(a)//abs(b)))
            else:
                st.append(int(ch))
            print(st)
        return(st[0])

        