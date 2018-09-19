from die import Die
import pygal

#create a 6sided Die
die = Die()

#make some rolls and store results

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#analyze results
freq = []
for value in range(1, die.num_sides+1):
    freq_count = results.count(value)
    freq.append(freq_count)

hist = pygal.Bar()
hist.title = "Rolling Die 1k Times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', freq)
hist.render_to_file('die_visual.svg')
