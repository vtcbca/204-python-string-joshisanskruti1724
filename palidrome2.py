a=input("enter any string:")
l=list(a.split())
c=0
for i in l:
    b=l[c][::-1]
  if l[c]==b:
      c=c+1
      print(l(C))
print("total{} palidrome word in string {}".format(c,l[c]))
