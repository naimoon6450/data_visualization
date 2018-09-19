import json
import pygal
from pygal.style import RotateStyle
from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


#build dictionary of population data
cc_pop = {}

#print 2010 population for each country
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_pop[code] = population

cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
for cc, pop in cc_pop.items():
    if pop < 10000000:
        cc_pop1[cc] = pop
    elif pop < 1000000000:
        cc_pop2[cc] = pop
    else:
        cc_pop3[cc] = pop


#print # of countries in each level
print(len(cc_pop1), len(cc_pop2), len(cc_pop3))

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World Population in 2010, by Country'

wm.add('0-10M', cc_pop1)
wm.add('10-1B', cc_pop2)
wm.add('>1B', cc_pop3)
wm.render_to_file('world_population.svg')
