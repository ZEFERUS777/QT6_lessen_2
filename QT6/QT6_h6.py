with open('plantis.csv', 'w', encoding='utf-8') as file:
    file.write('nomen;definitio;pluma;Russian nomen;familia;Russian nomen familia\n')
    while True:
        try:
            input_line = input().strip()
            if not input_line:
                break
            file.write(input_line.replace('\t', ';') + '\n')
        except EOFError:
            break
