# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 11:27:41 2017

@author: LR050891
"""

import newspaper
cnn_paper = newspaper.build('http://www.ndtv.com')

article_url=[]
for article in cnn_paper.articles:
    article_url.append(article.url)
#print article_url[0]    
#for category in cnn_paper.category_urls():
 #    print(category)
article = cnn_paper.articles[10]

article.download()
#print article.html
article.parse()
article.nlp()
print article.summary