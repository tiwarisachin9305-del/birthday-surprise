import streamlit as st
from datetime import datetime
from PIL import Image
import base64

# ------------------ PAGE SETTINGS ------------------
st.set_page_config(page_title="Birthday Surprise 🎂", page_icon="🎉")

# ------------------ TITLE ------------------
st.title("🎉 Happy Birthday Medha 🎂")
st.write("May Your Day Be Filled with Happiness,love and beautiful moments wishing you endless smiles & success ahead !")

st.balloons()

# ------------------ MUSIC (AUTO PLAY) ------------------
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()

    md = f"""
    <audio autoplay loop>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

autoplay_audio("music.mp3")

# ------------------ COUNTDOWN ------------------
st.header("⏳ Countdown")

target_date = datetime(2026, 3, 25)   # 👉 TEST DATE (baad me 25 kar dena)
now = datetime.now()

remaining = target_date - now

days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60

if days >= 0:
    st.info(f"{days} days {hours} hours {minutes} minutes left 🎂")
else:
    st.success("🎉 The surprise day has arrived!")

# ------------------ MESSAGE ------------------
st.header("💬 Message")

st.write("""
Hi Medha,

On This Beautiful Day, I Only Pray To God...
"May Your Birthday Be As Bright As Your Smile.And As Beautiful As Your Heart."
Happy Burthday...
""")

# ------------------ SURPRISE BUTTON ------------------
if st.button("Click for a Surprise 🎁"):
    st.success("🎉 Hope this made you smile Medha! 😄")

# ------------------ QUIZ ------------------
st.header("🎮 Small Fun Quiz")

q1 = st.radio(
    "What do you think this project is made with?",
    ("Python", "Java", "C++")
)

if st.button("Submit Answer"):
    if q1 == "Python":
        st.success("Correct! 😄")
    else:
        st.error("Oops! Try again 😅")

# ------------------ PHOTOS ------------------
st.header("📸 Some Memories")

try:
    image1 = Image.open("photo1.jpg")
    image2 = Image.open("photo2.jpg")

    st.image(image1, caption="Memory 1")
    st.image(image2, caption="Memory 2")

except:
    st.warning("Add photo1.jpg and photo2.jpg in folder")

# ------------------ FOOTER ------------------
