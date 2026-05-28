import streamlit as st
import controller
import time
import datetime

def render_add_page():
    st.title("➕ Створення нового завдання")
    st.write("Заповніть форму нижче:")

    today = datetime.date.today()
    
    chosen_date = st.date_input(
        "Оберіть дату виконання:", 
        value=today, 
        min_value=today
    )
    task = st.text_input("Назва завдання:")
    count = st.number_input("Цільова кількість повторень :", min_value=1, step=1, value=1)

    if st.button("Додати у список"):
        if not task.strip():
            st.error("Назва завдання не може бути порожньою!")
        else:
            date_str = chosen_date.strftime("%d%m")
            
            success = controller.create_todo(task.strip(), int(count), date_str)
            
            if success:
                st.success(f"Завдання '{task}' успішно додано на {chosen_date.strftime('%d.%m')}!")
                time.sleep(1)
                st.rerun()

render_add_page()