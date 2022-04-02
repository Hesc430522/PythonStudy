def test_while():
    i =0
    while True:
        old_file = open("while.txt", 'a', encoding='utf-8')
        #old_file = open("users.csv", 'rt', encoding='utf-8')
        print(i)
        i = str(i)
        old_file.write(i)
        i +=1

    old_file.close()




