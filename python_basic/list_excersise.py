#CARA RAVA
print("CARA RAVA")
jan=2200
feb=2350
mar=2600
apr=2130
may=2190
exp=[jan,feb,mar,apr,may]

a=exp[1]-exp[0]
print('In Feb, this much extra was spent compared to Jan:',a)

b=exp[0]+exp[1]+exp[2]
print('In Expense for this quarter:',b)

c=2000 in exp
print('Did I spent exactly $2000 in any month?',c)

jun=1980
exp.append(jun)
print("Expenses at the end of June:",exp)

exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp)

#CARA DEFAULT
print("CARA DEFAULT")
exps = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:",exps[1]-exps[0]) # 150

# 2. Find out your total expense in first quarter (first three months) of the year
print("Expense for first quarter:",exps[0]+exps[1]+exps[2]) # 7150

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in exps) # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exps.append(1980)
print("Expenses at the end of June:",exps) # [2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exps[3] = exps[3] - 200
print("Expenses after 200$ return in April:",exps) # [2200, 2350, 2600, 1930, 2190, 1980]

print('QUIZ')
L = [10,20,30,25,32,45,50]

L.append(20)
L.append(32)
print(L)
print(L.count(32))