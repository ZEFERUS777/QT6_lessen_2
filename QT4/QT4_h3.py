def reverse():
    file = 'input.dat'
    output = "output.dat"
    result = []
    with open(file, 'rb') as f:
        result.append(f.read())
    with open(output, 'wb') as f:
        f.write(result[0][::-1])
