import streamlit as st
import datetime
from PIL import Image
import requests
from io import BytesIO

# 網站標題與說明
st.set_page_config(page_title="ANIkI 的世界", layout="centered")
st.title("ANIkI 的世界")
st.markdown("每一幅影像，都是靈魂的回聲。")

# 模擬今日日期
today = datetime.date.today().strftime("%Y-%m-%d")

# 圖片來源與講評（示範用，本地部署可改為讀取 OneDrive 圖片連結）
photo_data = [
    {
        "url": "https://storage.googleapis.com/pai-images/29a58b8a9a5e4a1f8f96007f61f9a726.jpeg",
        "title": "雪橋之晨",
        "comment": "清晨的陽光穿透雲層，映照在雪白的橋面與古建築群上。王先生精準地掌握了對稱與透視，讓觀者仿佛置身其境。"
    },
    {
        "url": "https://storage.googleapis.com/pai-images/842e6214649a46b882abdb8373a0d7c0.jpeg",
        "title": "飄雪町街",
        "comment": "漫天雪花輕灑，街道仿如夢境般靜謐。色調的冷暖交融，展現生活中的詩意與孤獨之美。"
    }
]

# 顯示每一張作品
st.subheader(f"今日作品 - {today}")
for idx, photo in enumerate(photo_data):
    st.markdown(f"### {photo['title']}")
    response = requests.get(photo['url'])
    image = Image.open(BytesIO(response.content))
    st.image(image, use_column_width=True)
    st.markdown(f"*{photo['comment']}*")
    st.markdown("---")

st.caption("版權所有 © ANIkI")
