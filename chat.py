def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert_file(lines):
    new = []
    name = None
    for line in lines:
        if line == 'Allen':
            name = line
            # continue, 這裡也可以用continue, 但下面就不用else:
        elif line == 'Tom':
            name = line
            # continue
        else:
            if name: 
                new.append(name + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert_file(lines)
    write_file('output.txt', lines)

if __name__ == '__main__':
    main()