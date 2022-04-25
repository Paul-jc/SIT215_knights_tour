squares = 10
middle = squares / 2

for i in range(squares):
    print(f"{i}: {i*100 - middle*100 + 50}")
    #if i < middle:
    #    print(f"{i}: {i*100 - middle*100 + 50}")
    #else:
    #    print(f"{i}: {i*100 - middle*100 + 50}")

print("=========================================")

for i in range(squares):
    print(f"{i}: {middle*100 - i*100 - 50}")
    #if i < middle:
    #    print(f"{i}: {i*100 - middle*100 + 50}")
    #else:
    #    print(f"{i}: {i*100 - middle*100 + 50}")