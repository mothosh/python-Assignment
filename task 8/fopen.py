f = open("customers.txt", "w")
f.write("Customer1: Ann - 0712345678\n")
f.write("Customer2: Brian - 0723456789\n")
f.close()

f = open("customers.txt", "r")
data = f.read()
print(data)
f.close()
