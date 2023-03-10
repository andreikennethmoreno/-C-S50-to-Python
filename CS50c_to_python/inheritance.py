import random
blood_types = ['A', 'B', 'O']

offspring = set()
child = set()

for i in range(2):
    for j in range(2):
        rand_allele1 = random.choice(blood_types)
        rand_allele2 = random.choice(blood_types) 
        offspring.add(rand_allele1)
        offspring.add(rand_allele2)
        print(f'        Grandparent (Generation 2): blood type {rand_allele1}{rand_allele2}')
    for j in range(1):
        rand_allele3 = random.choice(list(offspring)) 
        rand_allele4 = random.choice(list(offspring))
        child.add(rand_allele3)
        child.add(rand_allele4)
        print(f'    Parent (Generation 1): blood type {rand_allele3}{rand_allele4}')
rand_allele5 = random.choice(list(child))
rand_allele6 = random.choice(list(child))
print(f'Child (Generation 0): blood type {rand_allele5}{rand_allele6}')
