import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

#make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

#process info about each submission
submission_ids = r.json()
submission_dicts = []
names, counts = [], []
for submission_id in submission_ids[:30]:
    #make sep API call for each submission
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
    str(submission_id) + '.json')
    submission_r = requests.get(url)
    #print(submission_r.status_code)
    response_dict = submission_r.json()
    names.append(response_dict['title'])

    submission_dict = {
    'value': response_dict.get('descendants', 0),
    'label': response_dict['title'],
    'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id)
    }
    submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)


#make visualization
my_style = LS('#333366', base_style = LCS)

my_config = pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000


chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Highly Discussed Articles by Comments'
chart.x_labels = names

chart.add('', submission_dicts)
chart.render_to_file('hn_discussions.svg')
