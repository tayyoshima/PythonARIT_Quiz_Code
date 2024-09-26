def read_file(file):
    line = None
    if os.path.isfile(file):
        data = open(file, 'r')
        for line in data:
            print(line)