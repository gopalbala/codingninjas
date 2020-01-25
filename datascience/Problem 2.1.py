import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]


# find ranges for Votes 
limit_arr = [(x,x+99) for x in range(0,5000,100)]
limit_arr.append((5000,20000))
rating_arr = [(0,0) for x in range(0,5000,100)] 
rating_arr.append((0,0))

for i in range(len(df.Votes)):  
    votes = df.Votes.iloc[i]
    for j in range(len(limit_arr)): 
        lower = limit_arr[j][0]
        upper = limit_arr[j][1]
        if votes >= lower and votes <= upper: 
            accum_rating  = rating_arr[j][0] + df['Aggregate rating'].iloc[i]
            res_count     = rating_arr[j][1] + 1
            rating_arr[j] = (accum_rating,res_count)
            break
ave_rating = []
votes      = []
for i in range(len(rating_arr)):
    rating = rating_arr[i]
    if rating[1] > 0: 
        ave_rating.append(rating[0]/rating[1])
        votes.append((limit_arr[i][0] + limit_arr[i][1])/2)

plt.plot(votes, ave_rating)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Effect of Votes on Rating')
plt.show()
