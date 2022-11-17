import streamlit as st
import functions


todos = functions.get_todos()

# st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my to-do app.")
st.write("This app is o increase your <b>productivity</b>",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add a new to-do",
              label_visibility="collapsed",
              placeholder="Add a new to-do",
              on_change=add_todo,
              key="new_todo")


# st.session_state
