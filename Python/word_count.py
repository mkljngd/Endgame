def word_count(string):
    return len(string.split(' '))

if __name__ == '__main__':
    sum=0
    while(True):
        sum += word_count(input())
        print()
