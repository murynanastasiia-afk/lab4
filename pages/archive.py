import streamlit as st
import controller

def render_archive_page():
    st.title("📁 Архів виконаних завдань")

    archived = controller.get_archived_todos()
    clean_archived = [item.strip() for item in archived if item.strip()]

    if not clean_archived:
        st.info("Архів порожній")
    else:
        for item in clean_archived:
            st.success(f"✔️ {item}")

render_archive_page()