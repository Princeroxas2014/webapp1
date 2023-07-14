import streamlit as stream
import Functions

todos = Functions.get_todos()


def add_todo():
    todo = stream.session_state["new_todo"] + '\n'
    todos.append(todo)
    Functions.write_todos(todos)


stream.title('To-do List, (except levin he lazy)')
stream.subheader('This is my to do app')
stream.write("this app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = stream.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del stream.session_state[todo]
        stream.experimental_rerun()

stream.text_input(label="todo field", placeholder="add a new todo",
                  on_change=add_todo, key="new_todo", label_visibility="hidden")
