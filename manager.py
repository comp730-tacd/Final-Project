# This program will check if a file exists, then either create or write to it.
# This logic can be used to save the game.

from pathlib import Path


def save(save_content):
    save_file = "/tmp/test.csv"
    my_file = Path(save_file)
    if not my_file.is_file():
        # if file does not exists, create it
        f = open(save_file, "x")
    f = open(save_file, "a")
    f.write(save_content)
    f.close()

def load(save_file):
    with open(save_file, "r") as f:
        load_content = f.read()
    print(load_content)
    return(load_content)


if __name__ == '__main__':
    save_content = "test,test,test\n"
    save(save_content)
    save_file = "/tmp/test.csv"
    load(save_file)