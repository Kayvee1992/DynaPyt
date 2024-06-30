def foo():
    return "example.txt"

with open(foo(), "w") as file:
    file.write("Hello, world!")
    print("content has been written to the file")

print("file has been closed")