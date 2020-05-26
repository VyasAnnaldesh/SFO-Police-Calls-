# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import nltk
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import plotly
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
from plotly.grid_objs import Column, Grid
import datetime
import numpy as np
import plotly
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import datetime
import numpy as np
from IPython.display import Image
import pandas as pd
import csv
from collections import Counter 
crimeData= []
textdata= []
commonLocation=[]
commonTime=[]
disposition=[]
data = open('police-department-calls-for-service.csv','r')
data.readline()   # skip the first line
for line in data:
    # read each line
    parts = line.split(',')
    crimeData.append(parts[1])  
    commonLocation.append(parts[8])  
    commonTime.append(parts[5])
    disposition.append(parts[7])
    # break
# Pass the split_it list to instance of Counter class. 
crime = Counter(crimeData) 
location= Counter(commonLocation)  
time=Counter(commonTime)
dispos=Counter(disposition)
# most_common() frequently encountered crime, location and time  
# input values and their respective counts. 
mostOccurCrime = crime.most_common(15)
mostOccurLocation=location.most_common(15)
mostCommonTime=time.most_common(1)
mostCommonDisposition=dispos.most_common(15)
print mostOccurCrime
print mostOccurLocation
print mostCommonTime
print mostCommonDisposition
#wordcloud 
mostCrimeWord=[]
for i in mostOccurCrime:
    mostCrimeWord.append(str(i[0]))

mostCrimeWords=' '.join(mostCrimeWord)

wordcloud = WordCloud().generate(mostCrimeWords)

mostDispositionWord=[] 
for i in mostCommonDisposition:
     mostDispositionWord.append(str(i[0]))
     
mostDispositionWords= ' '.join(mostDispositionWord)

wordcloud = WordCloud().generate(mostDispositionWords)

mostCrimelocation=[]
for i in mostOccurLocation:
    mostCrimelocation.append(str(i[0]))
mostCrimelocations= ' '.join(mostCrimelocation)
wordcloud = WordCloud().generate(mostCrimelocations)
    


import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
wordcloud = WordCloud(max_font_size=41).generate(mostCrimeWords)
wordcloud = WordCloud(max_font_size=41).generate(mostDispositionWords)
wordcloud = WordCloud(max_font_size=41).generate(mostCrimelocations)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.show()

#sentimentAnaysis through external analyser 
crimeDtatsenti=41 

plt.show()

