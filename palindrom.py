def main():
 s=int(input(""))
 temp=s
 rev=0
 while(s>0):
    dig=s%10
    rev=rev*10+dig
    s=s//10
 if(temp==rev):
    print("yes")
 else:
    print("no")

if __name__ == '__main__':
    main()
