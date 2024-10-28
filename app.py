from flask import Flask, render_template, jsonify
from datetime import datetime
import time

app = Flask(__name__)

class CyclicList:
    def __init__(self, elements):
        self.elements = elements
        self.size = len(elements)

    def get_element(self, index):
        return self.elements[index % self.size]

class AnalogClock:
    def __init__(self):
        self.seconds = CyclicList(list(range(60)))
        self.minutes = CyclicList(list(range(60)))
        self.hours = CyclicList(list(range(12)))

    def get_current_time(self):
        current_time = time.localtime()
        second = self.seconds.get_element(current_time.tm_sec)
        minute = self.minutes.get_element(current_time.tm_min)
        hour = self.hours.get_element(current_time.tm_hour % 12)
        return hour, minute, second

@app.route('/')
def home():
    return render_template('clock.html')  

@app.route('/time')
def get_time():
    clock = AnalogClock()
    hour, minute, second = clock.get_current_time() 
    time_string = f"{hour:02}:{minute:02}:{second:02}"  
    return jsonify(time=time_string)

if __name__ == '__main__':
    app.run(debug=True)
    