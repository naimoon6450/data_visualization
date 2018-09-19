from die import Die
import pygal

#create a 6sided Die
die1 = Die()
die2 = Die(10)
#make some rolls and store results

results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

#analyze results
freq = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    freq_count = results.count(value)
    freq.append(freq_count)

hist = pygal.Bar()
hist.title = "Rolling Die 1k Times"
hist.x_labels = ['2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', freq)
hist.render_to_file('die_visual.svg')
