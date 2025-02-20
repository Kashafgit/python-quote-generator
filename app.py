import streamlit as st
import random

quotes = [
    "😊Try not to become a man of success, but rather try to become a man of value.👍",
    "❤😊If you want to live a happy life, tie it to a goal, not to people or things✨",
    "💡Imagination is more important than knowledge.🎊",
    "💲All our dreams can come true, if we have the courage to pursue them.💙",
    "(❁´◡`❁)You must be the change you wish to see in the world.💡",
    "😊💙The purpose of our lives is to be happy✌",
    "✌💡Life is what happens when you're busy making other plans🙌",
    "🦾🧠Success is stumbling from failure to failure with no loss of enthusiasm👩‍💻",
    "🤑💲Money and success don't change people; they merely amplify what is already there👍",
    
]

st.title("Random Quote Generator✨❤")

st.write("Click the button to get a new quoote")

if st.button("Generate Quote"):
    random_quote = random.choice(quotes)
    st.success(random_quote)