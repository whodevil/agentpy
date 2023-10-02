import streamlit

from agent.agent_setup import agent


def main():
    streamlit.set_page_config(page_title="AI research agent", page_icon=":bird:")
    streamlit.header("AI research agent :bird:")
    query = streamlit.text_input("Research goal")
    if query:
        streamlit.write("Doing research for ", query)
        result = agent({"input": query})
        streamlit.info(result['output'])


if __name__ == '__main__':
    main()
