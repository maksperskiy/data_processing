import os
import numpy as np
import pickle

FILES_FOLDER = ''

x = []
y = []


def start(folder):
    files = os.listdir(path=folder + "Annotation_files/")
    # print(len(files))
    # print(files[0])

    for file in files:
        file = open('Annotation_files/'+file, 'r')
        file = file.readlines()
        # print(f)
        video_array = []
        # МБ надо конкретное число строк?!

        # print("len file", len(file))
        last_line = file[-10].replace('\n', '')

        if (int((last_line.split(','))[2])) > int((last_line.split(','))[3]) + 50 or len(file) > 350:
            # print('lose')
            continue
        y_done = False
        for line in file:
            line = line.replace("\n", "")
            if line.isdigit() or not line:
                if not y_done:
                    y.append(1 if line != "0" else 0)
                    y_done = True
                continue
            line = line.split(",")
            # print(f,
            #       line[0],
            #       #line[1],
            #       #line[2],
            #       #line[3],
            #       #line[4],
            #       #line[5],
            #       round((int(line[2])/int(line[3])), 4) if int(line[2]) and int(line[3]) else 0
            #       )
            video_array.append(round((int(line[2]) / int(line[3])), 6) if int(line[2]) and
                                                                          int(line[3]) and
                                                                          0 < (int(line[2]) / int(line[3])) < 12
                               else 0)
        while len(video_array) > 300:
            video_array.pop()
        while len(video_array) < 300:
            video_array.append(0)
        # print(len(video_array), video_array)
        x.append(video_array)

    for el in x:
        print(el)
    print(len(x))
    print(len(y))
    x_norm = normalize_data(x)
    for el in x_norm:
        print(el)
    data_to_object(x_norm, 'x.txt')


def normalize_data(data):
    result = []
    for el in data:
        line_max = max(el)
        line_min = min(el)
        line_result = []
        for i in el:
            line_result.append((i-line_min)/(line_max-line_min))
        result.append(line_result)
    return result


def data_to_object(data, path):
    file = open(path, 'wb')
    pickle.dump(data, file)
    file.close()


if __name__ == "__main__":
    start(FILES_FOLDER)
