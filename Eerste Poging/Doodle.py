def activiteit(path, days=1):
    with open(path) as document:
        calendar = document.read().splitlines()

    for people in calendar:
        print people

def main():
    print 'working'

if __name__ == '__main__':
    activiteit('DoodleFiles/doodle1.txt')