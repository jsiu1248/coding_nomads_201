rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("What symbol? (Symbol can only be one.): ")
if len(symbol) > 1:
    print("Symbol length can only be one")

for i in range(rows):
    for j in range(columns):
        print(f'{symbol}', end="" )
    print() #moves to the next line
