def main():
    def reverse_words(str1):
        list1=[]
        str1=str1.replace(' ','-').replace('\t','-')
        list1=str1.split('-')
        list1.reverse()
        n=len(list1)
        str2=""
        for i in range(n):
            str2=str2+list1[i]
            if(i!=n-1):
                str2=str2+" "
        return str2


        
    
    str1='Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth'
    print('original string : ')
    print(str1)
    print('reversed string : ')
    print(reverse_words(str1))

    print('\n')
    str1='Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,'
    print('original string : ')
    print(str1)
    print('reversed string : ')
    print(reverse_words(str1))
if __name__ == '__main__':
    main()

      
