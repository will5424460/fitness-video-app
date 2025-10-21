# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

app = Flask(__name__)

def convert_to_embed(url):
    if "youtube.com/shorts/" in url:
        video_id = url.split("shorts/")[-1]
        return f"https://www.youtube.com/embed/{video_id}"
    elif "watch?v=" in url:
        video_id = url.split("watch?v=")[-1]
        return f"https://www.youtube.com/embed/{video_id}"
    else:
        return url

exercises = [
    {"name": "仰臥推舉（槓鈴)", "video": "https://www.youtube.com/watch?v=5SSdbmIjNj4"},
    {"name": "雙槓臂屈伸（寬握）", "video": "https://www.youtube.com/watch?v=h_JsA3tt0vU"},
    {"name": "夾胸機 / Pec Deck", "video": "https://www.youtube.com/watch?v=YKk_gkZOGic"},
    {"name": "繩索下拉（Triceps Pushdown）", "video": "https://www.youtube.com/watch?v=dvM2IoxpTnI"},
    {"name": "繩索臂屈伸", "video": "https://www.youtube.com/watch?v=W53rZyGHLEQ"},
    {"name": "引體向上（正握）", "video": "https://www.youtube.com/watch?v=rffAYLTSMJY"},
    {"name": "槓鈴划船", "video": "https://www.youtube.com/watch?v=0CGyZUqqzIc"},
    {"name": "坐姿划船機(窄握)", "video": "https://www.youtube.com/watch?v=IjqCKVy4WXA"},
    {"name": "高位下拉（正握）", "video": "https://www.youtube.com/watch?v=wV1nVjAPGHs"},
    {"name": "面拉（Face Pull）", "video": "https://www.youtube.com/watch?v=89yerIMpGX4"},
    {"name": "啞鈴彎舉", "video": "https://www.youtube.com/watch?v=igppHAAIdT4"},
    {"name": "繩索彎舉", "video": "https://www.youtube.com/watch?v=IWu_vf_0tfo"},
    {"name": "硬舉（傳統 / 羅馬尼亞式）", "video": "https://www.youtube.com/watch?v=xQ6cLsq2bjA"},
    {"name": "腿推機（Leg Press）", "video": "https://www.youtube.com/watch?v=EotSw18oR9w"},
    {"name": "腿彎舉（Leg Curl）", "video": "https://www.youtube.com/watch?v=SgzUqJ3HCAk"},
    {"name": "腿伸展（Leg Extension）", "video": "https://www.youtube.com/watch?v=cSUYSxZHhg8"},
    {"name": "仰臥抬腿", "video": "https://www.youtube.com/watch?v=wXDnKR_GkcE"},
    {"name": "腹部捲機", "video": "https://www.youtube.com/watch?v=tTow_SbxB-E"},
    {"name": "啞鈴肩推（坐姿）", "video": "https://www.youtube.com/watch?v=usPnudgiaDA"},
    {"name": "器械肩推", "video": "https://www.youtube.com/watch?v=QlOEm34TkDs"},
    {"name": "側平舉", "video": "https://www.youtube.com/watch?v=Kl3LEzQ5Zqs"},
    {"name": "前平舉", "video": "https://www.youtube.com/watch?v=1lXa528j0Vs"},
    {"name": "反向飛鳥", "video": "https://www.youtube.com/watch?v=CizCvKdvBP0"},
]

for ex in exercises:
    ex["video"] = convert_to_embed(ex["video"])

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>健身動作介紹</title>
  <style>
    body { font-family: sans-serif; background: #f4f4f4; text-align: center; }
    .container { max-width: 900px; margin: 20px auto; }
    input { padding: 8px; width: 300px; }
    .grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 20px; }
    .card { background: white; border-radius: 10px; padding: 10px; width: 280px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
    iframe { border-radius: 8px; }
  </style>
</head>
<body>
  <div class="container">
    <h1>💪 健身動作介紹</h1>
    <form method="get" action="/">
      <input type="text" name="search" placeholder="輸入動作名稱搜尋" value="{{ keyword }}">
      <button type="submit">搜尋</button>
    </form>

    <div class="grid">
      {% for ex in exercises %}
      <div class="card">
        <h2>{{ ex.name }}</h2>
        <iframe width="260" height="150" src="{{ ex.video }}" allowfullscreen></iframe>
      </div>
      {% endfor %}
    </div>
  </div>
</body>
</html>
'''

@app.route('/')
def index():
    keyword = request.args.get("search", "")
    if keyword:
        filtered = [ex for ex in exercises if keyword.lower() in ex["name"].lower()]
    else:
        filtered = exercises
    return render_template_string(HTML_TEMPLATE, exercises=filtered, keyword=keyword)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
