# program to print your name N times where N is the first two digits of your SID
name = input("Enter your name: ")
sid = input("Enter your SID: ")
N = int(sid[:2])

for i in range(N):
  print(name)
