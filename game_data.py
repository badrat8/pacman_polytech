import settings


def write_in_file():
    file = open("Leaders.txt", "w")
    for i in range(len(settings.LEADERS)):
        file.write(str(settings.LEADERS[i]) + "\n")
    file.close()