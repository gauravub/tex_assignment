from alchemy import app, Location
from flask import render_template


@app.route('/location/<int:page_num>')
def thread(page_num):
    resp = []
    threads = Location.query.paginate(per_page=3, page=page_num, error_out=True)
    return render_template('results.html', threads=threads)

if __name__=='__main__':
    app.run(debug=True)