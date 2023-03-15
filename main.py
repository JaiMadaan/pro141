from flask import Flask, jsonify, request

#from demographic_filtering import output
#from content_filtering import get_recommendations
liked_articles = []
not_liked_articles = []
all_articles=[]


app = Flask(__name__)



@app.route("/get-aritcle")
def get_article():
    article_data = {
        "title": all_articles[0][19],
        "poster_link": all_articles[0][27],
        "release_date": all_articles[0][13] or "N/A",        
        "rating": all_articles[0][20],
        "overview": all_articles[0][9]
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-articles", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/not_liked_articles", methods=["POST"])
def not_liked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()