import streamlit as st
import controller
import datetime

def render_todos_page():
    st.title("📄 Поточний список завдань")
    
    todos = controller.get_all_todos()
    clean_todos = [t.strip() for t in todos if t.strip()]
    
    selected_todo = st.selectbox("Оберіть завдання для роботи:", clean_todos)
    
    if selected_todo:
        index = clean_todos.index(selected_todo)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Дії")
            if st.button("📈 Зарахувати прогрес / Виконати", use_container_width=True):
                status = controller.finish_todo(index)
                if status == "виконано":
                    st.toast("🎉 Завдання повністю виконано і перенесено в архів!")
                elif status == "прогрес":
                    st.toast("👍 Прогрес зараховано!")
                st.rerun()
                
        with col2:
            st.subheader("📝 Редагувати")
            parts = selected_todo.split(' ', 1)
            if len(parts) >= 2:
                current_date_str = parts[0]  
                rest = parts[1].rsplit(' ', 1)
                current_task = rest[0]
                current_count = rest[1].split('/')[-1]
                
                today = datetime.date.today()
                
                try:
                    default_date = datetime.datetime.strptime(current_date_str, "%d%m").date()
                    default_date = default_date.replace(year=today.year)
                    if default_date < today:
                        default_date = today
                except ValueError:
                    default_date = today

                chosen_date = st.date_input(
                    "Змінити дату", 
                    value=default_date, 
                    min_value=today
                )
                
                new_date = chosen_date.strftime("%d%m")
                new_task = st.text_input("Змінити назву", value=current_task)
                new_count = st.number_input("Змінити ціль", min_value=1, value=int(current_count))
                
                if st.button("Зберегти зміни", use_container_width=True):
                    if new_task.strip() and len(new_date) == 4 and new_date.isdigit():
                        controller.update_todo(index, new_task.strip(), int(new_count), new_date)
                        st.success("Зміни успішно збережено!")
                        st.rerun()
                    else:
                        st.error("Некоректні дані при редагуванні!")

render_todos_page()