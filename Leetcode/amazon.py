
def sortf(data):
    return ''.join(data.split(' ')[1:]) + ''.join(data.split(' ')[0])

if __name__ == "__main__":
    a= ['eo first qpx', 'az0 first qpx', '09z cat hamster', '236 cat dog rabbit snake']
    print(sorted(a, key=sortf))