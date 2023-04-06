def main():
    n=[]
    for i in range(8):
        n.append(2*i)

    def fac(a):
        result=1
        print(a,end='')
        print('!= ',end='')
        for i in range(a):
            print(i+1,end='')
            if (i!=a-1):
                print('x',end='')
            result=result*(i+1)
        print('=',end='')
        print(result)
        return result

    for i in range(8):
        fac(n[i])
if __name__ == '__main__':
    main()

