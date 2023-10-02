import os

import streamlit
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader

from agent.agent_setup import agent


def main():
    if os.path.isfile('auth.yaml'):
        authenticator = build_authenticator()
        authenticator.login('Login', 'main')
        login_page(authenticator)
    else:
        streamlit.set_page_config(page_title="AI research agent", page_icon=":bird:")
        render_agent_interface()


def login_page(authenticator):
    if streamlit.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main', key='unique_key')
        render_agent_interface()
    elif streamlit.session_state["authentication_status"] is False:
        streamlit.error('Username/password is incorrect')
    elif streamlit.session_state["authentication_status"] is None:
        streamlit.warning('Please enter your username and password')


def render_agent_interface():
    streamlit.header("AI research agent :bird:")
    query = streamlit.text_input("Research goal")
    if query:
        streamlit.write("Doing research for ", query)
        result = agent({"input": query})
        streamlit.info(result['output'])


def build_authenticator():
    with open('auth.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    return authenticator


if __name__ == '__main__':
    main()
