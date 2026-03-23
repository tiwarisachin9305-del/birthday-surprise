import streamlit as st
from datetime import datetime
from PIL import Image
import base64
import pytz

# ------------------ PAGE SETTINGS ------------------
st.set_page_config(page_title="Birthday Surprise 🎂", page_icon="🎉")

# ------------------ TITLE ------------------
st.title("🎉 Happy Birthday Medha 🎂")
st.write("May Your Day Be Filled with Happiness,love and beautiful moments wishing you endless smiles & success ahead !")


st.balloons()

# ------------------ MUSIC (AUTO PLAY) ------------------
def autoplay_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()

        md = f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)
    except:
        st.warning("Music file not found")

autoplay_audio("music.mp3")

# ------------------ COUNTDOWN (IST FIXED) ------------------
st.header("⏳ Countdown")

try:
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)

    target_date = ist.localize(datetime(2026, 3, 25, 0, 0, 0))

    remaining = target_date - now

    days = remaining.days
    hours = remaining.seconds // 3600
    minutes = (remaining.seconds % 3600) // 60

    if days >= 0:
        st.info(f"{days} days {hours} hours {minutes} minutes left 🎂")
    else:
        st.success("🎉 Happy Birthday Medha! 🎂🎉")

except:
    st.error("Countdown error")

# ------------------ MESSAGE ------------------
st.header("💬 Message")

st.write("""
Hi Medha,

On this beautiful day, I only pray to God...  
"May your birthday be as bright as your smile and as beautiful as your heart."  

Happy birthday...🎂
""")

# ------------------ SURPRISE BUTTON ------------------
if st.button("Click for a Surprise 🎁"):
    st.success("🎉 Hope this made you smile Medha! 😄💖")

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
    st.warning("Add photo1.png and photo2.png in folder")

# ------------------ FOOTER ------------------
