try:
    file = open("example.txt", "w")
    with file:
        file.write("Hello, world!")
        print("content has been written to the file")

    file.write("Hello, world again!")
except Exception as e:
    print("An error occurred: ", e)




