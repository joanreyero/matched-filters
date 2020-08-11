from flask import Flask, send_file, make_response
from matchedFilters import MatchedFilter
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])
def build_plot():
    w = 640
    h = 360
    fov = [205.46963709898583, 0.0, 320.5,
           0.0, 205.46963709898583, 180.5,
           0.0, 0.0, 1.0]
    fov_type = 'K'
    o = [0.0, 0.0, 0.0]
    a = [1.0, 0.0, 0.0]
    mf = MatchedFilter(w, h, fov, fov_type, orientation=o, axis=a)
    bytes_plot = mf.plot()

    return send_file(bytes_plot,
                     attachment_filename='plot.png',
                     mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run()
