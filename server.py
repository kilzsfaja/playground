from flask import Flask, render_template

app = Flask(__name__) # always do this set up!


@app.route("/play", methods=["GET"])
def play():
    return render_template("index.html")


@app.route("/play/<int:num>", methods=["GET"])
def more_boxes(num):
    return render_template("index-play.html", num = num)

@app.route("/play/<int:num>/<string:color>", methods=["GET"])
def more_box_colors(num, color):
    return render_template("index-play-color.html", num = num, color = color)

if __name__ == "__main__":
    app.run(debug = True)