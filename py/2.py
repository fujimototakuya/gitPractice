inpf = float(input('input natural number: '))
inp = int(inpf)
if inp <= 0 or inpf != inp:
    exit(1)
elif inp % 3 ==0 and inp % 5 ==0:
    print(str(inp) + ' FizzBuzz')
elif inp % 3 == 0:
    print(str(inp) + ' buzz')
elif inp % 5 == 0:
    print(str(inp) + ' fizz')

else:
    print(str(inp))