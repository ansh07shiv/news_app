from flask import Flask, render_template, request, redirect, url_for
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='590b8b622fc944bfacf8c3afdf5dd01d')
    
app = Flask(__name__)
@app.route("/", methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':  
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'ansh07shiv' and password == '1234':
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/news", methods = ['GET', 'POST'])
def news():
    source = request.form['source']
    top_headlines = newsapi.get_top_headlines(sources=source,language='en',)
    titles = []
    desc = []
    img = []
    url = []
    for i in range(top_headlines['totalResults']):
        titles.append(top_headlines['articles'][i]['title'])
        desc.append(top_headlines['articles'][i]['description'])
        img.append(top_headlines['articles'][i]['urlToImage'])
        url.append(top_headlines['articles'][i]['url'])
    ans = []
    ans.append(titles)
    ans.append(desc)
    ans.append(img)
    ans.append(url)
    return render_template('news.html', ans = ans)
if __name__ == '__main__':
    app.run(host='localhost', debug=True)