

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert_file(lines):
    allen_word_count = 0
    allen_stiker_count = 0
    allen_photo_count = 0
    viki_word_count = 0
    viki_stiker_count = 0
    viki_photo_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_stiker_count += 1
            elif s[2] == '圖片':
                allen_photo_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        if name == 'Viki':
            if s[2] == '貼圖':
                viki_stiker_count += 1
            elif s[2] == '圖片':
                viki_photo_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)

    print('Allen說了', allen_word_count, '個字')
    print('Allen傳了', allen_stiker_count, '張貼圖')
    print('Allen傳了', allen_photo_count, '張圖片')
    print('Viki說了', viki_word_count, '個字')
    print('Viki傳了', viki_stiker_count, '張貼圖')
    print('Viki傳了', viki_photo_count, '張圖片')


def main():
    lines = read_file('[Line]Viki.txt')
    convert_file(lines)


if __name__ == '__main__':
    main()