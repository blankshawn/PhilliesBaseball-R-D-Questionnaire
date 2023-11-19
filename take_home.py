def is_palindrone(s):
    r=""
    for c in s:
        print("c: ",c)
        #r = c + r
        print("s: ",s[s.index(c)])
        if s[s.index(c)] == c:
            y = True
        else:

            return False
    return y
            

    # for x in range(0, len(s)):
    #     if s[x] == r[x]:
    #         x = True
    #     else:
    #         print(0)
    #         return False
    # return x

def main():
    print(is_palindrone("string"))

if __name__ == "__main__":
    main()
