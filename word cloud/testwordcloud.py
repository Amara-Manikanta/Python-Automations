import wikipedia
import re
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS,WordCloud
import numpy as np
from PIL import Image

wiki=wikipedia.page('Mother')

text=wiki.content

#print(text)

text= re.sub(r'==.*?==+','',text)
text=text.replace('\n','')
print(text)


def plot(wordcloud):
    plt.figure(figsize=(20,10))
    plt.imshow(wordcloud)
    plt.axis('off')

mask=np.array(Image.open('I-Love-You-Mother-PNG-Image.png'))
wordcloud=WordCloud(width=840,height=840,random_state=1,background_color='white'
                    ,colormap='Dark2'
                    ,mask=mask,collocations=False,stopwords=STOPWORDS).generate(text)
plot(wordcloud)
plt.show()