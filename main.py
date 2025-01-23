import streamlit as st
import os
from team_leader_agent import TeamLeaderAgent


def initialize_agent():
    # Get API key from environment
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai_api_key:
        st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        st.stop()
    
    # Create knowledge_base directory if it doesn't exist
    if not os.path.exists("knowledge_base"):
        os.makedirs("knowledge_base")
        st.warning("Created empty knowledge_base directory. Please add your .txt files there.")
        st.stop()
    
    try:
        return TeamLeaderAgent(
            docs_path="./knowledge_base",
            openai_api_key=openai_api_key
        )
    except Exception as e:
        st.error(f"Error initializing agent: {str(e)}")
        st.stop()


def main():
    st.set_page_config(
        page_title="Team Leader Assistant",
        page_icon="👨‍💼",
        layout="wide"
    )

    # Sidebar
    with st.sidebar:
        st.title("Settings")
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("---")
        st.markdown("""
        ### Topics you can ask about:
        - Code Review Guidelines
        - Architecture Decisions
        - Team Management
        - Technical Challenges
        - Incident Response
        - Development Workflow
        """)

    # Main content
    st.title("💡 Team Leader Assistant")
    st.markdown("""
    Ask questions to get guidance from your team leader. The responses are based on the 
    team's documentation and best practices stored in the knowledge base.
    """)

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Initialize agent
    if "agent" not in st.session_state:
        with st.spinner("Initializing Team Leader Assistant..."):
            st.session_state.agent = initialize_agent()

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask your question here...", key="chat_input"):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.agent.get_response(prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    if st.button("Retry"):
                        st.rerun()


if __name__ == "__main__":
    main() 