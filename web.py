import streamlit as st
import todo_functions


# pip freeze > requirements.txt  um file automatisch erstellen zu lassen

todos = todo_functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    todo_functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo")
st.write("Enter some stuff")

st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # checkbox wird true, wenn es abgehakt wird
        todos.pop(index)
        todo_functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.session_state
