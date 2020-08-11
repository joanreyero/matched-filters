from flask import Flask, send_file, Response
from flask_cors import CORS
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matchedFilters import MatchedFilter
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
CORS(app)

@app.route('/plot', methods=['GET'])
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
    fig = mf.plot()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run()
