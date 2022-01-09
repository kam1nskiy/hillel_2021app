import os

def get_names(path):
    for root, directories, files in os.walk(path, topdown=True):
        for name in files:
            print(os.path.join(root, name))
        for name in directories:
            print(os.path.join(root, name))


if __name__ == "__main__":
    path = '/Users/kaminsk1y/projects/hillel_2021app'
    get_names(path)