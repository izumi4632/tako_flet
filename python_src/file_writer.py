class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data_list):
        with open(self.filename, "w") as file:
            for data in data_list:
                if isinstance(data, list):
                    file.write(" ".join(map(str, data)) + "\n")
                else:
                    file.write(str(data) + "\n")