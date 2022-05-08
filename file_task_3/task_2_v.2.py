def lens_files(arguments):
    files = list()

    for x in range(1, arguments + 1):
        filename = f"{x}.txt"
        with open(filename, encoding="utf-8") as file:
            text = [line.strip() for line in file]
            text.append(filename)
            files.append(text)

    files.sort(key=len)

    return files


def merging_files(files):
    with open('result.txt', 'w') as result:
        for text in files:
            result.write(text[-1] + '\n')
            result.write(str(len(text) - 1) + '\n')
            for t in text[:-1]:
                result.write(t + '\n')

    print("Итоговый файл создан")


if __name__ == '__main__':
    arguments = 3

    merging_files(lens_files(arguments))