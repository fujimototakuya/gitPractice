
inpf = float(input('input natural number: '))
inp = int(inpf)
if inp <= 0 or inpf != inp:
    exit(1)
elif inp == 1:
    print(str(inp)+' is not prime')
elif inp == 2:
    print(str(inp)+' is prime')
else:
    for i in range(2, inp):
        if inp%i == 0:
            print(str(inp)+' is not prime')
            break
        if i == inp-1:
            print(str(inp)+' is prime')