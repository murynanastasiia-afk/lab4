import streamlit as st
import sys
from pathlib import Path

root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

import controller

def render_print_page():
    st.title("🖨️ Генерація PDF звітів")

    if st.button("📊 Сформувати PDF документ", use_container_width=True):
        with st.spinner("Генерація PDF"):
            try:
                pdf_file_path = controller.generate_pdf_report()
                
                with open(pdf_file_path, "rb") as f:
                    pdf_bytes = f.read()
                
                st.success("PDF-файл успішно згенеровано!")
                
                st.download_button(
                    label="📥 Завантажити готовий звіт у PDF",
                    data=pdf_bytes,
                    file_name="tasks_report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Помилка при генерації файлу: {e}")

render_print_page()