from flask import Flask, request
import streamlit as st


app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post_request():
    message_body = request.form['body']
    # message_sid = request.form['sid']
    print(f'Received message: {message_body}')
    st.write(f'Received message: {message_body}')
    # st.write(f"Conversation SID: {message_sid}")
    st.write("Full message:")
    st.write(request.form)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)