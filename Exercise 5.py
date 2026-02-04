string = input("Input string: ")
length = len(string)
if length % 2 == 0:
    chars = [
        string[length // 2 - 1],
        string[-(length // 2)],]  
    print(''.join(chars))
else:
    chars = string[ length // 2]  
    print(chars)