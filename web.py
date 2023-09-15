import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

# twicking the checkbox to delete items
for index, todo in enumerate(todos):
    # 1st argument names checkbox, 2nd argument(attribute) names the key
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # remove deleted item from checkbox list
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo", label_visibility='collapsed',
              placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

