import os
from fpdf import FPDF

class PDFRoadmapGenerator(FPDF):
    def __init__(self, skill_data):
        super().__init__()
        self.skill_data = skill_data
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        # Running header on every page (except first page if we want, but fine on all pages)
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(100, 116, 139) # slate-500
        self.cell(0, 8, 'SkillPath AI - Learning Roadmap Generator', border=0, ln=0, align='L')
        self.set_font('Helvetica', 'I', 9)
        self.cell(0, 8, 'Production-Ready Curriculum', border=0, ln=1, align='R')
        self.set_draw_color(226, 232, 240) # slate-200
        self.set_line_width(0.5)
        self.line(10, 16, 200, 16)
        self.ln(6)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(148, 163, 184) # slate-400
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', border=0, ln=0, align='C')
        
    def generate(self):
        self.alias_nb_pages()
        self.add_page()
        
        # Skill Title Section
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(79, 70, 229) # indigo-600
        self.cell(0, 12, self.skill_data.get('skill_name', '').upper() + " ROADMAP", ln=True, align='L')
        
        # Accent horizontal bar
        self.set_draw_color(79, 70, 229)
        self.set_line_width(1.0)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)
        
        # Meta info Box
        self.set_fill_color(248, 250, 252) # slate-50
        self.set_draw_color(226, 232, 240) # slate-200
        self.set_line_width(0.5)
        
        # Retrieve info
        duration = self.skill_data.get('estimated_duration', 'N/A')
        daily_time = self.skill_data.get('daily_study_time', 'N/A')
        outcome = self.skill_data.get('expected_outcome', 'N/A')
        
        # Calculate expected height for outcome to draw bounding box properly
        # Or simply write it as lines
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(71, 85, 105)
        self.cell(40, 6, "Estimated Duration:", ln=False)
        self.set_font('Helvetica', '', 10)
        self.cell(50, 6, duration, ln=False)
        
        self.set_font('Helvetica', 'B', 10)
        self.cell(35, 6, "Daily Study Time:", ln=False)
        self.set_font('Helvetica', '', 10)
        self.cell(0, 6, daily_time, ln=True)
        
        self.ln(2)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(71, 85, 105)
        self.cell(0, 6, "Expected Outcome:", ln=True)
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(30, 41, 59)
        self.multi_cell(0, 5, outcome)
        self.ln(6)
        
        # Learning Phases Section
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(79, 70, 229) # indigo-600
        self.cell(0, 8, "LEARNING PHASES", ln=True)
        self.ln(2)
        
        phases = self.skill_data.get('phases', [])
        for i, phase in enumerate(phases):
            # Page overflow protection
            if self.get_y() > 240:
                self.add_page()
                
            # Phase Title
            self.set_font('Helvetica', 'B', 12)
            self.set_text_color(17, 24, 39) # slate-900
            self.cell(0, 6, phase.get('phase_title', f"Phase {i+1}"), ln=True)
            
            # Phase Duration
            p_dur = phase.get('duration', '')
            if p_dur:
                self.set_font('Helvetica', 'I', 9.5)
                self.set_text_color(100, 116, 139) # slate-500
                self.cell(0, 5, f"Duration: {p_dur}", ln=True)
                
            self.ln(2)
            
            # Topics & Subtopics
            self.set_font('Helvetica', 'B', 10)
            self.set_text_color(30, 41, 59)
            self.cell(0, 5, "Topics & Sub-topics:", ln=True)
            
            for topic in phase.get('topics', []):
                topic_name = topic.get('name', '')
                subtopics = ", ".join(topic.get('subtopics', []))
                
                # Check page boundary
                if self.get_y() > 260:
                    self.add_page()
                
                self.set_x(15)
                self.set_font('Helvetica', 'B', 9.5)
                self.set_text_color(71, 85, 105)
                self.cell(5, 5, "-", ln=False)
                self.cell(0, 5, topic_name, ln=True)
                
                self.set_x(20)
                self.set_font('Helvetica', '', 9)
                self.set_text_color(100, 116, 139)
                self.multi_cell(0, 4.5, subtopics)
                self.ln(1.5)
            
            # Practice Schedule
            if self.get_y() > 260:
                self.add_page()
                
            self.set_x(10)
            self.set_font('Helvetica', 'B', 10)
            self.set_text_color(30, 41, 59)
            self.cell(38, 5, "Practice Schedule: ", ln=False)
            self.set_font('Helvetica', '', 9.5)
            self.set_text_color(71, 85, 105)
            self.multi_cell(0, 5, phase.get('practice_schedule', 'N/A'))
            
            # Mini Project
            mini_proj = phase.get('mini_project', {})
            if mini_proj:
                if self.get_y() > 260:
                    self.add_page()
                self.set_x(10)
                self.set_font('Helvetica', 'B', 10)
                self.set_text_color(30, 41, 59)
                self.cell(26, 5, "Mini Project: ", ln=False)
                self.set_font('Helvetica', 'B', 9.5)
                self.set_text_color(79, 70, 229)
                self.cell(0, 5, mini_proj.get('title', 'N/A'), ln=True)
                
                self.set_x(15)
                self.set_font('Helvetica', 'I', 9)
                self.set_text_color(100, 116, 139)
                self.multi_cell(0, 4.5, mini_proj.get('description', ''))
                self.ln(1)
            
            # Milestone
            if self.get_y() > 260:
                self.add_page()
            self.set_x(10)
            self.set_font('Helvetica', 'B', 10)
            self.set_text_color(30, 41, 59)
            self.cell(22, 5, "Milestone: ", ln=False)
            self.set_font('Helvetica', '', 9.5)
            self.set_text_color(71, 85, 105)
            self.multi_cell(0, 5, phase.get('milestone', 'N/A'))
            
            # Decorative divider between phases
            self.ln(4)
            self.set_draw_color(241, 245, 249) # slate-100
            self.set_line_width(0.5)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(4)
            
        # Major Projects
        major_projects = self.skill_data.get('major_projects', [])
        if major_projects:
            if self.get_y() > 220:
                self.add_page()
                
            self.set_font('Helvetica', 'B', 14)
            self.set_text_color(79, 70, 229)
            self.cell(0, 8, "MAJOR CAPSTONE PROJECTS", ln=True)
            
            self.set_draw_color(79, 70, 229)
            self.set_line_width(0.5)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(4)
            
            for project in major_projects:
                if self.get_y() > 250:
                    self.add_page()
                self.set_font('Helvetica', 'B', 11)
                self.set_text_color(17, 24, 39)
                self.cell(0, 5, project.get('title', ''), ln=True)
                self.set_font('Helvetica', '', 9.5)
                self.set_text_color(71, 85, 105)
                self.multi_cell(0, 4.5, project.get('description', ''))
                self.ln(3)

def generate_roadmap_pdf(skill_data, output_path):
    pdf = PDFRoadmapGenerator(skill_data)
    pdf.generate()
    pdf.output(output_path)
