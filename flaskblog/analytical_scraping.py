import re
import requests
from bs4 import BeautifulSoup

def attach(target, a):
    final_answer = target[0].text
    for x in range(1, a):
        final_answer = final_answer + " <br/><br/> " + target[x].text
    return final_answer

first_site = requests.get('https://crunchprep.com/gre-analytical-writing-guide')
second_site = requests.get('https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/sample_responses')
third_site =  requests.get('https://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/sample_responses')
fourth_site = requests.get('https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool')
fiveth_site = requests.get('https://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/pool')


soup = BeautifulSoup(first_site.text, 'html.parser')
soup2 = BeautifulSoup(second_site.text, 'html.parser')
soup3 = BeautifulSoup(third_site.text, 'html.parser')
soup4 = BeautifulSoup(fourth_site.text, 'html.parser')
soup5 = BeautifulSoup(fiveth_site.text, 'html.parser')




h3 = soup.select('.awa-guide #one .container .content-width h3')
questions = [h3[0].text, h3[2].text, h3[3].text, h3[5].text, h3[7].text]

p = soup.select('.awa-guide #one .container .content-width p')
bulletins = soup.select('.awa-guide #one .container .content-width h4')
ans = [p[4].text, bulletins[0:7], p[16].text[0:434], bulletins[7:14], p[48].text[0:285] + '<br/>' + p[50].text[0:172] + '<br/><br/><b>' + p[51].text[0:130] + '</b>' ]

#issue sample question
e_question1 = soup2.select('.wrap-scroll #main-contents .callout-box p em')
e_answer_headings = soup2.select('.wrap-scroll #main-contents h2')
e_answers1 = soup2.select('.wrap-scroll #main-contents p')

questions2 = [e_question1[0].text + '<br/><br/>' + e_question1[1].text ]
answer_headings = e_answer_headings[0:2]
answers1 = [attach(e_answers1[4:10], 6), attach(e_answers1[13:17], 4) ]

#argument sample question
e_question2 = soup3.select('.wrap-scroll #main-contents .callout-box p span')
e_answers2 = soup3.select('.wrap-scroll #main-contents p')

questions3 = [e_question2[0].text + '<br/><br/>' + e_question2[1].text ]
answers2 = [attach(e_answers2[4:9], 5), attach(e_answers2[15:21], 6)]

#issue sample topics
first_para = soup4.select('.wrap-scroll #main-contents p')
sample_questions1 = [attach(first_para[2:4], 2), attach(first_para[4:6], 2), attach(first_para[6:8], 2) ]
sample_questions2 = [attach(first_para[2:4], 2), attach(first_para[4:6], 2), attach(first_para[6:8], 2)]






