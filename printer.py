import os
from fpdf import FPDF
import qrcode
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FONTS_DIR = BASE_DIR / "assets" / "fonts"
IMAGES_DIR = BASE_DIR / "assets" / "images"
REPORTS_DIR = BASE_DIR / "reports"

class TaskPrinter:
    def __init__(self, current_tasks, archived_tasks):
        self.current_tasks = current_tasks
        self.archived_tasks = archived_tasks
        
        IMAGES_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    def generate_qr(self, text="Мій Менеджер Завдань"):
        qr_path = IMAGES_DIR / "qr.png"
        qr = qrcode.QRCode(version=None, box_size=10, border=2)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(qr_path)
        return qr_path

    def create_report(self, output_filename):
        pdf = FPDF(orientation='P', unit='mm', format='a4')
        pdf.set_auto_page_break(False, 0)
        
        font_path = FONTS_DIR / "KobzarKS_v1-020.otf"
        
        if font_path.exists():
            pdf.add_font("KobzarUA", '', str(font_path))
            font_name = "KobzarUA"
        else:
            font_name = "Helvetica"

        pdf.add_page()
        
        pdf.set_font(font_name, '', 24)
        pdf.set_text_color(0, 50, 100)
        pdf.cell(w=0, h=15, text="Звіт про виконання завдань", align='C', new_x="LMARGIN", new_y="NEXT")
        pdf.set_draw_color(0, 50, 100)
        pdf.set_line_width(0.5)
        pdf.line(10, 25, 200, 25)
        pdf.ln(5)

        logo_png = IMAGES_DIR / "logo.png"
        if logo_png.exists():
            with pdf.local_context(fill_opacity=0.15):
                pdf.image(logo_png, x=pdf.w / 2 - 50, y=pdf.h / 2 - 50, w=100)

        pdf.set_font(font_name, '', 16)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=10, text=" Поточні активні завдання:", new_x="LMARGIN", new_y="NEXT")
        
        pdf.set_font(font_name, '', 12)
        pdf.set_fill_color(230, 240, 250)
        pdf.cell(w=30, h=8, border=1, text="Дата", align='C', fill=True)
        pdf.cell(w=110, h=8, border=1, text="Назва завдання", align='L', fill=True)
        pdf.cell(w=50, h=8, border=1, text="Статус / Прогрес", align='C', fill=True, new_x="LMARGIN", new_y="NEXT")

        for task in self.current_tasks:
            text = task.strip()
            if not text:
                continue
            parts = text.split(' ', 1)
            date_part = parts[0] if len(parts) > 0 else "-"
            
            task_name = "Невідоме завдання"
            progress_part = "-"
            if len(parts) > 1:
                sub_parts = parts[1].rsplit(' ', 1)
                task_name = sub_parts[0] if len(sub_parts) > 0 else parts[1]
                progress_part = sub_parts[1] if len(sub_parts) > 1 else "В процесі"

            pdf.cell(w=30, h=8, border=1, text=date_part, align='C')
            pdf.cell(w=110, h=8, border=1, text=task_name, align='L')
            pdf.cell(w=50, h=8, border=1, text=f"Активне ({progress_part})", align='C', new_x="LMARGIN", new_y="NEXT")

        pdf.ln(10)

        pdf.set_font(font_name, '', 16)
        pdf.cell(w=0, h=10, text=" Архів виконаних завдань:", new_x="LMARGIN", new_y="NEXT")
        
        pdf.set_font(font_name, '', 12)
        for idx, arch_task in enumerate(self.archived_tasks):
            arch_text = arch_task.strip()
            if arch_text:
                pdf.cell(w=0, h=8, border=1, text=f"  ✓  {arch_text}", align='L', new_x="LMARGIN", new_y="NEXT")

        qr_info = f"Active: {len(self.current_tasks)}, Archived: {len(self.archived_tasks)}"
        qr_img_path = self.generate_qr(qr_info)
        pdf.image(qr_img_path, x=10, y=pdf.h - 45, w=35)

        pdf.set_font(font_name, '', 10)
        pdf.set_text_color(100, 100, 100)
        pdf.set_dash_pattern(dash=2, gap=2)
        pdf.line(10, pdf.h - 48, 200, pdf.h - 48)
        pdf.set_dash_pattern()

        pdf.output(str(output_filename))
