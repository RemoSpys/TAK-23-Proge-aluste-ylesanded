import praw
import matplotlib.pyplot as plt
import credentials


# Reddit autentimine
reddit = praw.Reddit(client_id= credentials.client_id, \
                     client_secret= credentials.client_secret , \
                     user_agent='RemoSpys by U/RemoSpys', \
                        )

# Subredditi info
subredditname = "Eesti"
subreddit = reddit.subreddit(subredditname)

# Top-postituste hankimine
top_subbreddit = subreddit.top()
count = 0
max = 120
print('Õnnestunud')
words = []
wordCount = {}

# Sõnade loenduriks ühised sõnad, mida välja jätta
commonWords = {'jah', 'aga', 'ei', 'ok', 'kas', 'mina', 'millal', 'kuidas', 'ja', 'of', 'the', 'for', 'ma', 'see',
                'on', 'tal', 'nad', 'aga', 'olema', 'voib', 'sina', 'et', 'ei', 'sa', 'teie', 'ei', 'saaks', 'minu', 'nende', 
                'neile', 'nad', 'koos', 'aga', 'umbes', 'kuidas', 'seal', 'sina', 'ja', 'seal', 'Teie', 'alates', 'saada', 'lihtsalt',
                'rohkem', 'nii', 'mina', 'rohkem', 'valja', 'ule', 'mote', 'ma', 'rohkem', 'valja', 'up', 'mooned', 'kuidas', 'ule', 
                'uhel', 'mis', 'uks', 'mida', 'ei', 'saa', 'ju', 'mu', 'voiks', 'tegi', 'ei', 'tea', 'olid', 'kas', 'see', 'et',
                'see', 'on', 'See', 'ta', 'meie', 'asi', '', 'siin', 'midagi', 'voib', 'palju', 'need', 'sina', 'Kas', 'nuud',
                'mis', 'it', 'a', 'me', 'olen', 'ule', 'mida', 'nemad', 'nad', 'kutsuvad', 'sa', 'ei', 'on', 'voib', 'mu', 
                'nende', 'nad', 'koos', 'aga', 'umbes', 'sooviksid', 'seal', 'Sina', 'uks', 'tema', 'tema', 'kes', 'tema', 'tema', 
                'meie', 'asi', '', 'tal', 'oli', 'tema', 'kes', 'tema', 'tema', 'mida', 'teine', 'helesinine', 'siin', 'pole', 
                'mis', 'oli', 'ma', 'ka', 'siis', 'kui', 'kui', 'motted', 'et', 'see', 'pole', 'kas', 'see', 'on', 'See', 
                'maletas', 'et', 'ta', 'on', 'Meie', 'veel', 'valja', 'ara', 'on', 'nad', 'utlesid', 'ainult', 'sooviksid', 
                'teised', 'sisse', 'Ta', 'mida', 'ma', 'et', 'et', 'see', 'mote', 'et', 'nii', 'palju', 'eesti', 'nagu', 'See',
                'ikka', 'selle', 'kes', 'Ma', 'oma', 'voi', 'vaga', 'tema', 'mingi', 'Kui', 'juba', 'seal', 'koik'
                'yes', 'but', 'no', 'ok', 'do', 'work', 'to', 'did', 'Very', 'whether', 'I', 'when', 'how', 'and', 'of', 'the', 'for', 'I', 'this',
                'is', 'he/she/it', 'they', 'but', 'to be', 'can', 'you', 'that', 'not', 'is', 'you', 'your', 'not', 'could', 'my', 'those', 
                'to them', 'they', 'together', 'but', 'about', 'how', 'there', 'you', 'and', 'there', 'You', 'from', 'send', 'just',
                'more', 'so', 'I', 'more', 'out', 'over', 'thought', 'I', 'more', 'out', 'up', 'moons', 'how', 'over', 
                'one', 'what', 'one', 'what', 'not', 'can', 'know', 'my', 'could', 'made', 'not', 'know', 'were', 'whether', 'this', 'that',
                'this', 'is', 'This', 'he/she/it', 'our', 'thing', '', 'here', 'something', 'can', 'many', 'these', 'you', 'Are', 'now',
                'what', 'goes', 'were', 'we', 'am', 'over', 'what', 'they', 'they', 'call', 'you', 'not', 'is', 'can', 'my', 
                'those', 'they', 'together', 'but', 'about', 'wish', 'there', 'You', 'one', 'he/she/it', 'he/she/it', 'who', 'he/she/it', 'he/she/it', 
                'our', 'thing', '', 'he/she/it', 'was', 'he/she/it', 'who', 'he/she/it', 'he/she/it', 'what', 'another', 'light blue', 'here', 'is not', 
                'what', 'was', 'I', 'also', 'then', 'when', 'when', 'thoughts', 'that', 'this', 'is not', 'whether', 'this', 'is', 'This', 
                'remembered', 'that', 'he/she/it', 'is', 'Our', 'still', 'out', 'off', 'is', 'they', 'said', 'only', 'wish', 
                'others', 'in', 'He/she', 'what', 'I', 'that', 'that', 'this', 'thought', 'that', 'so', 'much', 'Estonian', 'like', 'This',
                'still', 'this', 'who', 'I', 'own', 'or', 'very', 'he/she/it', 'some', 'If', 'already', 'there', 'all'}

# Liigu üle top-postituste ja nende kommentaaride
for submission in subreddit.top(limit=10):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        count += 1
        if(count == max):
            break
        word = ""

      # Teksti jagamine sõnadeks
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

# Sõnade esinemiste loendamine
for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

# Sõnade järjestamine esinemiste arvu järgi
sortedList = sorted(wordCount, key = wordCount.get, reverse = True)

# Top 10 sõna ja esinemiste arvu saamine
keyWords = []
keyCount = []
amount = 0

for entry in sortedList:
    keyWords.append(entry)
    keyCount.append(wordCount[entry])
    amount += 1
    if (amount == 10):
        break

# Andmete visualiseerimine pie chart'ina
labels = keyWords
sizes = keyCount

plt.title('Parimad kommentaarid: r/' + subredditname)
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')

# Salvesta diagramm faili
plt.savefig('diagramm.png')
