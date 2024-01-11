from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = 'd095ca647af955e6df735431b2bb9f39374fa8e3e7e5c86e0892b6ff6042702c'

def URLSearch(params, headers):
    response = requests.get('https://www.virustotal.com/vtapi/v2/url/report',
                            params=params, headers=headers)
    json_response = {}
    if response.ok:
        json_response = response.json()
        return json_response


@app.route('/', methods=['GET', 'POST'])
def url_search():
    json_response = {}
    if request.method == 'POST':
        url = request.form['url']

        params = {'apikey': API_KEY, 'resource': url}
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "gzip,  My Python requests library example client or username"}
        json_response = URLSearch(params, headers)
        return render_template('index.html', json_response=json_response)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

