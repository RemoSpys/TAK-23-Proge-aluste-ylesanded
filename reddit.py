import praw
import matplotlib.pyplot as plt
import credentials

reddit = praw.Reddit(client_id= credentials.client_id, \
                     client_secret= credentials.client_secret , \
                     user_agent='RemoSpys by U/RemoSpys', \
                        )

subredditname = "Eesti"
subreddit = reddit.subreddit(subredditname)
top_subbreddit = subreddit.top()
count = 0
max = 120
print('Õnnestunud')
words = []
wordCount = {}
commonWords = {'jah', 'aga', 'ei', 'ok', 'kas', 'mina', 'millal', 'kuidas', 'ja', 'of', 'the', 'for', 'ma', 'see',
                'on', 'tal', 'nad', 'aga', 'olema', 'voib', 'sina', 'et', 'ei', 'sa', 'teie', 'ei', 'saaks', 'minu', 'nende', 
                'neile', 'nad', 'koos', 'aga', 'umbes', 'kuidas', 'seal', 'sina', 'ja', 'seal', 'Teie', 'alates', 'saada', 'lihtsalt',
                'rohkem', 'nii', 'mina', 'rohkem', 'valja', 'ule', 'mote', 'ma', 'rohkem', 'valja', 'up', 'mooned', 'kuidas', 'ule', 
                'uhel', 'mis', 'uks', 'mida', 'ei', 'saa', 'ju', 'mu', 'voiks', 'tegi', 'ei', 'tea', 'olid', 'kas', 'see', 'et',
                'see', 'on', 'See', 'ta', 'meie', 'asi', '', 'siin', 'midagi', 'voib', 'palju', 'need', 'sina', 'Kas', 'nuud',
                'mis', 'laheb', 'olid', 'me', 'olen', 'ule', 'mida', 'nemad', 'nad', 'kutsuvad', 'sa', 'ei', 'on', 'voib', 'mu', 
                'nende', 'nad', 'koos', 'aga', 'umbes', 'sooviksid', 'seal', 'Sina', 'uks', 'tema', 'tema', 'kes', 'tema', 'tema', 
                'meie', 'asi', '', 'tal', 'oli', 'tema', 'kes', 'tema', 'tema', 'mida', 'teine', 'helesinine', 'siin', 'pole', 
                'mis', 'oli', 'ma', 'ka', 'siis', 'kui', 'kui', 'motted', 'et', 'see', 'pole', 'kas', 'see', 'on', 'See', 
                'maletas', 'et', 'ta', 'on', 'Meie', 'veel', 'valja', 'ara', 'on', 'nad', 'utlesid', 'ainult', 'sooviksid', 
                'teised', 'sisse', 'Ta', 'mida', 'ma', 'et', 'et', 'see', 'mote', 'et', 'nii', 'palju', 'eesti', 'nagu', 'See',
                'ikka', 'selle', 'kes', 'Ma', 'oma', 'voi', 'vaga', 'tema', 'mingi', 'Kui', 'juba', 'seal', 'koik'}

for submission in subreddit.top(limit=10):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        count += 1
        if(count == max):
            break
        word = ""
        for letter in top_level_comment.body:
            if(letter == ' '):
                if(word and not word[-1].isalnum()):
                    word = word[:-1]
                if not word in commonWords:
                    words.append(word)
                word = ""
            else:
                word += letter
    if(count == max):
            break

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

sortedList = sorted(wordCount, key = wordCount.get, reverse = True)

keyWords = []
keyCount = []
amount = 0

for entry in sortedList:
    keyWords.append(entry)
    keyCount.append(wordCount[entry])
    amount += 1
    if (amount == 10):
        break

labels = keyWords
sizes = keyCount

plt.title('Parimad kommentaarid: r/' + subredditname)
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')

plt.savefig('diagramm.png')