with open('test.txt') as file:
    print(file.read())


test1 = "hello world"

with open('test1.txt' ,'w') as file1:
        file1.write(test1)

        with open('test1.txt' ) as file2:
            print(file2.read())