def generate(n):
    def next(prev):
        result = []
        count = 0
        while count < len(prev):
            occurs = 1
            while count + 1 < len(prev) and prev[count] == prev[count + 1]:
                count += 1
                occurs += 1
            result.append(str(occurs) + prev[count])
            count += 1
        return "".join(result)
        
    if n == 1:
        return "1"
    else:
        prev = "1"
        for i in range(n - 1):
            prev = next(prev)

    return prev
        

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 11
    print(generate(3)) # 21
    print(generate(4)) # 1211
    print(generate(5)) # 111221