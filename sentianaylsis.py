
# coding: utf-8

# In[1]:


import tweepy
from tkinter import *
from time import sleep
from datetime import datetime
from textblob import TextBlob
import matplotlib.pyplot as plt



# In[2]:


consumer_key="dPHn2asjsnouBPWlc1KJwEfRT" 
consumer_secret="tD8t7qofWdYoRVhvyLuc1xvzq07IhaPeIkH3khoe9ogzWMQQ8e"
access_key="1104066488724422656-iapXTdPy2vowzH3tRHHAeUxnl8Bqdt"
access_secret="euvLKIkjRWVzMc8sfUjZNTP9HEb29SwjC8en5X2MLs3f8"


# In[3]:

#creating OAuth object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#setting the access token
auth.set_access_token(access_key, access_secret)
#creating an API Object for tweepy
api = tweepy.API(auth)


# In[4]:


#GUI
root = Tk()


# In[5]:


label1 = Label(root, text="Search")
E1 = Entry(root, bd =5) #To get single line string input.

label2 = Label(root, text="Sample Size")
E2 = Entry(root, bd =5)


# label1 = Label(root, text="Search")
# E1 = Entry(root, bd =5)
# 
# label2 = Label(root, text="Sample Size")
# E2 = Entry(root, bd =5)

# In[6]:


def getE1():
    return E1.get()


# In[7]:


def getE2():
    return E2.get()


# In[ ]:


def getData():
    getE1()
    keyword = getE1()

    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)

    #Where the tweets are stored to be plotted
    polarity_list = []
    numbers_list = []
    number = 1

    for tweet in tweepy.Cursor(api.search, keyword, lang="en").items(numberOfTweets):
        try:
            analysis = TextBlob(tweet.text)
            analysis = analysis.sentiment
            polarity = analysis.polarity
            polarity_list.append(polarity)
            numbers_list.append(number)
            number = number + 1

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
        #Plotting
    axes = plt.gca() # get current axes.
    axes.set_ylim([-1, 2])

    plt.scatter(numbers_list,polarity_list)

    averagePolarity = (sum(polarity_list))/(len(polarity_list))
    averagePolarity = "{0:.0f}%".format(averagePolarity * 100)
    time  = datetime.now().strftime("At: %H:%M\nOn: %m-%d-%y")

    plt.text(0, 1.25, "Average Sentiment:  " + str(averagePolarity) + "\n" + time, fontsize=12, bbox = dict(facecolor='none', edgecolor='black', boxstyle='square, pad = 1'))

    plt.title("Sentiment of " + keyword + " on Twitter")
    plt.xlabel("Number of Tweets")
    plt.ylabel("Sentiment")
    plt.show()
    plt.plot(kind='box',x=numbers_list,y=polarity_list)

submit = Button(root, text ="Submit", command = getData)

label1.pack()
E1.pack() # arranging
label2.pack()
E2.pack()
submit.pack(side =BOTTOM)
root.mainloop() #used to run the application in infinite loop until user closes the window.
plt.show()


# In[ ]:




