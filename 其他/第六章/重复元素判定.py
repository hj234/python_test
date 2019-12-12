'''
水.....
'''
def main(a):
    return len(a)==len(set(a))
a=[1,2,3,4,5,6]
b=[2,2,3,4,5,6]
print(main(a),main(b))