import random
questions=[]

a=open('questions.txt', 'r')

for line in a:
    b=line.strip().split(';')  #strip ashorebs damatebit ragaceebs(\n, " ", a.sh) roca vkitxulobt lines filedan
    questions.append(b)

name = input("name: ")
n = int(input("number of questions: "))
score=0
for i in range(n):
        index = random.randint(0, 1000)
        q = questions[index]
        if q[1]==q[5]:
          anwser='A'
        elif q[2]==q[5]:
          anwser='B'
        elif q[3]==q[5]:
          anwser='C'
        elif q[4]==q[5]:
          anwser='D'
        
        print(f"\nQuestion {i+1}: {q[0]}")
        print("A.", q[1])
        print("B.", q[2])
        print("C.", q[3])
        print("D.", q[4])
        ans = input("Your anwser:")
        if ans.upper() == anwser:
            score+=1
        else:
             continue

print(f"Score - {score}/{n}")

b=open('data.txt', 'a')

b.write(f"{name},{score}/{n}\n")
            