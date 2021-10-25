from flask import Flask, jsonify
import csv

allArticles = []

with open("articles.csv", encoding = "utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticles = data[1:]

liked_articles = []
unliked_articles = []

app = Flask(__name__)

@app.route("/")
def home_page():
    return jsonify({
        "Message": "Go to '/get-article', '/liked-article' or '/unliked-article'"
    })

@app.route("/get-article")
def getArticle():
    return jsonify({
        "data": allArticles[0],
        "status": "Success!"
    })

@app.route("/liked-article", methods = ["POST"])
def likedArticle():
    article = allArticles[0]
    liked_articles.append(article)
    allArticles.pop(0)
    return jsonify({
        "status": "Success!"
    }), 201

@app.route("/unliked-article", methods = ["POST"])
def unlikedArticle():
    article = allArticles[0]
    unliked_articles.append(article)
    allArticles.pop(0)
    return jsonify({
        "status": "Success!"
    }), 201

if __name__ == "__main__":
    app.run()