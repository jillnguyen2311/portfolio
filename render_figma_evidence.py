"""Render the English portfolio adaptations of the source Figma frames."""
from html import escape
from pathlib import Path

ASSETS = Path(__file__).parent / "dist" / "assets"
INK = "#152f49"
MUTED = "#506175"
WHITE = "#ffffff"
SMS = "#bd4c10"
SMS_BG = "#fbf6ef"
SMS_SOFT = "#fbe0cb"
UNI = "#aa1733"
LIB = "#5635ba"
LMS = "#0c4872"
TEST = "#11567a"


class Frame:
    def __init__(self, width=1040, height=620, background="#f4f5f8"):
        self.width = width
        self.height = height
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" font-family="Inter,Arial,sans-serif">']
        self.rect(0, 0, width, height, background)

    def rect(self, x, y, w, h, fill=WHITE, radius=0, stroke="none"):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')

    def line(self, x, y, end_x, end_y, stroke="#dce2e8"):
        self.parts.append(f'<path d="M{x} {y}L{end_x} {end_y}" stroke="{stroke}" fill="none"/>')

    def text(self, x, y, text, size=15, fill=INK, weight=400, align="start"):
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{align}">{escape(text)}</text>')

    def button(self, x, y, w, label, *, fill=SMS, ink=WHITE, outline="none", height=36):
        self.rect(x, y, w, height, fill, 7, outline)
        self.text(x+w/2, y+height/2+5, label, size=14, fill=ink, weight=700, align="middle")

    def field(self, x, y, w, title, value, *, outline="#dae1e7", height=38, select=False):
        self.text(x, y-7, title, size=13, fill=INK, weight=700)
        self.rect(x, y, w, height, WHITE, 6, outline)
        self.text(x+10, y+height/2+5, value, size=13, fill=MUTED)
        if select:
            self.chevron(x+w-18, y+height/2, "#60748b")

    def chevron(self, x, y, color=SMS):
        self.parts.append(f'<path d="M{x-4} {y-2}l4 4 4 -4" fill="none" stroke="{color}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>')

    def circle(self, x, y, radius, fill=SMS, stroke="none"):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}"/>')

    def table(self, x, y, edges, headers, rows, *, accent=SMS, tint=SMS_SOFT, row_height=38):
        width = edges[-1]-edges[0]
        self.rect(x, y, width, row_height, tint)
        for left, name in zip(edges, headers):
            self.text(x+left+11, y+row_height/2+5, name, size=13, fill=accent, weight=700)
        for row, values in enumerate(rows, start=1):
            top = y+row*row_height
            self.rect(x, top, width, row_height, WHITE if row % 2 else "#fcfcfd")
            self.line(x, top, x+width, top)
            for left, value in zip(edges, values):
                self.text(x+left+11, top+row_height/2+5, value, size=13, fill=INK)
        self.line(x, y+(len(rows)+1)*row_height, x+width, y+(len(rows)+1)*row_height)

    def card(self, x, y, w, h, title, caption="", accent=SMS):
        self.rect(x, y, w, h, WHITE, 13, "#dee3ea")
        self.text(x+18, y+35, title, size=19, fill=accent, weight=700)
        if caption:
            self.text(x+18, y+59, caption, size=13, fill=MUTED)

    def write(self, key):
        self.parts.append("</svg>")
        (ASSETS / f"{key}.svg").write_text("\n".join(self.parts))


def sms_header(f, active="Archived records"):
    f.rect(0, 0, f.width, 67, WHITE)
    f.line(0, 66, f.width, 66, "#e6cdb7")
    f.text(29, 39, "SMS360", size=23, fill=INK, weight=700)
    for x, label in [(139, "Home"), (197, "Teaching schedule"), (345, "Gradebook"), (445, "Notices"), (525, "Manage"), (608, "Archived records"), (745, "Statistics")]:
        selected = active == label
        f.text(x, 36, label, size=13, fill=INK if selected else MUTED, weight=700 if selected else 400)
        if selected:
            f.line(x, 46, x+105, 46, SMS)
    f.button(841, 16, 95, "2024–2025", fill=SMS_BG, ink=SMS, outline="#debfa7")
    f.button(945, 16, 79, "Admin", fill=INK)


def sms_homeroom(reviewers):
    f = Frame(height=583, background=SMS_BG)
    sms_header(f)
    f.text(49, 112, "Archived records  /  Homeroom notebook", size=16, fill=INK, weight=700)
    for x, w, label, selected in [(48, 176, "Class notebooks", not reviewers), (224, 198, "Leadership reviewers", reviewers)]:
        f.button(x, 137, w, label, fill=SMS if selected else SMS_SOFT, ink=WHITE if selected else SMS, height=42)
    f.field(48, 224, 190, "Select grade", "Grade 6", outline="#e4c7ad", select=True)
    if reviewers:
        f.rect(49, 289, 18, 18, SMS, 4)
        f.text(58, 303, "✓", size=13, fill=WHITE, weight=700, align="middle")
        f.text(76, 303, "Assign the same reviewer to this grade", size=15, weight=700)
        f.field(400, 281, 282, "", "Choose leadership reviewer", outline="#e4c7ad", select=True)
        f.field(702, 281, 215, "", "Position", outline="#e4c7ad")
        f.table(48, 343, [0,140,266,704,936], ["Grade", "Class", "Leadership reviewer", "Position"], [
            ("6", "6A1", "Choose reviewer  ⌄", "—"), ("6", "6A2", "Choose reviewer  ⌄", "—"),
            ("6", "6A3", "Choose reviewer  ⌄", "—"), ("6", "6A4", "Choose reviewer  ⌄", "—"),
            ("6", "6A5", "Choose reviewer  ⌄", "—")])
        f.write("sms-reviewer-assignments-en")
    else:
        f.table(48, 291, [0,59,146,250,421,582,747,936], ["No.", "Class", "Enrollment", "Homeroom teacher", "Leadership reviewer", "Download template", "Open notebook"], [
            ("1", "6A1", "40", "Teacher A", "Reviewer A", "↓", "Open  ›"),
            ("2", "6A2", "40", "Teacher B", "Reviewer B", "↓", "Open  ›"),
            ("3", "6A3", "40", "Teacher C", "Unassigned", "↓", "Open  ›"),
            ("4", "6A4", "40", "Teacher D", "Unassigned", "↓", "Open  ›"),
            ("5", "6A5", "40", "Teacher E", "Reviewer B", "↓", "Open  ›"),
            ("6", "6A6", "40", "Teacher F", "Reviewer A", "↓", "Open  ›"),
        ])
        f.write("sms-homeroom-records-en")


def sms_actions():
    f = Frame(height=470, background=SMS_BG)
    f.card(22, 24, 996, 421, "Button component set", "Four button types, two states and optional icons on either side.")
    for index, (kind, content, styles) in enumerate([
        ("Solid", "Sign in", [("#cc5000", WHITE, "none"), ("#dbe5e8", "#6d7e8d", "none")]),
        ("Outline", "Sign in", [(WHITE, SMS, "#c6865d"), ("#dbe5e8", "#6d7e8d", "none")]),
        ("Icon · close", "−", [("#fffaf4", SMS, "#e8cbb7"), ("#dbe5e8", "#6d7e8d", "none")]),
        ("Icon · open", "+", [("#fffaf4", SMS, "#e8cbb7"), ("#dbe5e8", "#6d7e8d", "none")]),
    ]):
        x = 179+202*index
        f.text(x+72, 122, kind, size=14, weight=700, align="middle")
        for row, (bg, ink, outline) in enumerate(styles):
            y = 146+69*row
            w = 43 if index > 1 else 146
            f.button(x+(146-w)/2, y, w, content, fill=bg, ink=ink, outline=outline, height=44)
    f.text(51, 174, "Default", size=14, weight=700)
    f.text(51, 243, "Disabled", size=14, weight=700)
    f.line(51, 292, 989, 292)
    f.text(51, 324, "Optional icons", size=15, weight=700)
    for i, (title, label) in enumerate([
        ("Text only", "Continue"),
        ("Leading icon", "+ Add setting"),
        ("Trailing icon", "View details  ›"),
        ("Both icons", "↓  Export  ›"),
    ]):
        x = 51 + i*237
        f.text(x, 359, title, size=12, fill=MUTED)
        f.button(x, 372, 206, label)
    f.write("sms-action-family-en")


def sms_navigation():
    f = Frame(height=541, background=SMS_BG)
    sms_header(f)
    f.button(33, 95, 158, "Class notebooks", height=37)
    f.button(191, 95, 168, "Leadership reviewers", fill=SMS_SOFT, ink=SMS, height=37)
    f.text(34, 172, "Role-specific menu examples", size=19, fill=INK, weight=700)
    menus = [
        ("School admin", ["Teaching schedule", "Gradebook", "Notices", "Manage", "Archived records", "Statistics", "Support"]),
        ("Teacher", ["Teaching schedule", "Gradebook", "Notices", "Homeroom notebook"]),
        ("Student", ["Timetable", "Gradebook", "Notices"]),
    ]
    for i, (label, items) in enumerate(menus):
        x = 32+330*i
        f.card(x, 196, 311, 305, label)
        for row, item in enumerate(items):
            y = 235+34*row
            if row == 0:
                f.rect(x+13, y+8, 285, 29, SMS_SOFT, 4)
            f.circle(x+28, y+22, 4, "#cf7846")
            f.text(x+41, y+27, item, size=14, weight=700 if row == 0 else 400)
    f.write("sms-navigation-family-en")


def sms_forms():
    f = Frame(height=526, background=SMS_BG)
    f.card(24, 24, 478, 473, "Grade entry and visibility", "Gradebook settings dialog")
    f.field(42, 115, 440, "Scope", "Grade 6", select=True)
    f.field(42, 180, 440, "Grade-entry window", "Midyear grade entry", select=True)
    f.field(42, 245, 209, "Start", "2025-01-08")
    f.field(273, 245, 209, "End", "2025-01-24")
    f.rect(42, 306, 440, 49, "#fff2e7", 6)
    f.text(54, 336, "Validate period, window order and overlapping settings.", size=13, fill=SMS)
    f.text(42, 389, "Entry permissions and grade visibility are separate.", size=14, weight=700)
    f.button(261, 432, 104, "Cancel", fill=WHITE, ink=MUTED, outline="#d5dde5")
    f.button(376, 432, 106, "Save setting")
    f.card(520, 24, 496, 473, "Leadership comments", "Homeroom notebook section")
    f.field(538, 115, 460, "Reporting checkpoint", "End of year", select=True)
    f.text(538, 181, "Final comments", size=13, weight=700)
    f.rect(538, 196, 460, 120, WHITE, 6, "#dae1e7")
    f.text(551, 223, "Add the school leadership review for this class.", size=13, fill=MUTED)
    f.rect(538, 333, 460, 47, "#f1f4f7", 6)
    f.text(550, 361, "Edit access: assigned leadership reviewer", size=13, fill=INK)
    f.button(777, 432, 103, "Cancel", fill=WHITE, ink=MUTED, outline="#d5dde5")
    f.button(891, 432, 107, "Save comment")
    f.write("sms-forms-dialogs-en")


def sms_states():
    f = Frame(height=430, background=SMS_BG)
    f.text(25, 43, "Error and recovery templates", size=22, fill=INK, weight=700)
    for idx, (code, name, label, action) in enumerate([
        ("404", "Page not found", "Return to an available part of the product.", "Back to home"),
        ("403", "Access denied", "Check your role and access to this page.", "Back to home"),
        ("500", "Something went wrong", "Retry when the service is available.", "Try again"),
    ]):
        x = 24+339*idx
        f.rect(x, 77, 315, 316, WHITE, 14, "#f0d5bf")
        f.circle(x+157, 159, 53, SMS_SOFT)
        f.text(x+157, 180, code, size=56, fill=INK, weight=700, align="middle")
        f.text(x+157, 245, name, size=22, fill=INK, weight=700, align="middle")
        f.text(x+157, 277, label, size=13, fill=MUTED, align="middle")
        f.button(x+89, 312, 137, action)
    f.write("sms-error-templates-en")


def sms_templates():
    f = Frame(height=390, background=SMS_BG)
    f.text(25, 42, "Reusable page templates", size=21, weight=700)
    templates = [
        ("Form and reference", ["Academic year", "Class", "Academic term"], ["Current context", "Record reference", "Form guidance"]),
        ("Scrollable record", ["Class organization", "Homeroom plans", "Review checkpoints"], ["Class information", "Teacher roster", "Leadership comments"]),
        ("List and filters", ["Grade level", "Class", "Status"], ["Row", "Class", "Action"]),
    ]
    for i, (title, controls, details) in enumerate(templates):
        x = 23+i*338
        f.card(x, 67, 318, 294, title)
        f.rect(x+16, 122, 285, 22, "#f9f1e7", 4)
        f.text(x+24, 138, "SMS360  /  School admin", size=11, fill=SMS, weight=700)
        for row, field in enumerate(controls):
            ry = 166+36*row
            f.rect(x+16, ry, 126, 25, WHITE, 4, "#e7d6c7")
            f.text(x+23, ry+17, field, size=11)
            f.rect(x+151, ry, 150, 25, "#f8fafc", 4)
            f.text(x+159, ry+17, details[row], size=11, fill=MUTED)
        f.rect(x+16, 286, 285, 52, SMS, 3)
        f.text(x+29, 317, "School management system", size=12, fill=WHITE, weight=700)
    f.write("sms-page-templates-en")


def uni_sections():
    f = Frame(height=645, background="#fbf4f6")
    variants = [
        ("Create course section", "Self-registration", "Set the window and constraints"),
        ("Edit course section", "Self-registration", "Review the existing setup"),
        ("Create course section", "Cohort assignment", "Select the cohort to assign"),
    ]
    for i, (title, mode, note) in enumerate(variants):
        x = 21+341*i
        f.card(x, 22, 316, 598, title, note, UNI)
        for idx, (label, sample) in enumerate([("Course", "Introduction to Business"), ("Section name", "Business · Section 01"), ("Lecturer", "Select lecturer"), ("Term", "Term 1  ·  2025–2026")]):
            f.field(x+17, 106+55*idx, 282, label, sample, height=33, select=idx in (0, 2, 3))
        f.rect(x+17, 319, 282, 34, "#122c4e", 4)
        f.text(x+28, 342, "Enrollment setup", size=13, fill=WHITE, weight=700)
        f.field(x+17, 380, 282, "Registration mode", mode, height=34, select=True)
        if i < 2:
            f.field(x+17, 440, 129, "Opens", "2025-08-11", height=35)
            f.field(x+166, 440, 133, "Closes", "2025-08-29", height=35)
            f.field(x+17, 499, 282, "Capacity", "40 seats", height=34)
        else:
            f.field(x+17, 440, 282, "Cohort class", "Select cohort class", height=35, select=True)
            f.field(x+17, 499, 282, "Schedule format", "Fixed schedule", height=34, select=True)
        f.button(x+17, 557, 78, "Cancel", fill=WHITE, ink=UNI, outline="#ead3d6")
        f.button(x+107, 557, 192, "Save course section", fill=UNI)
    f.write("uni-course-section-variants-en")


def uni_cohorts():
    f = Frame(height=498, background="#fbf4f6")
    f.card(20, 23, 606, 448, "Cohort class list", "Administrative view", UNI)
    f.field(39, 120, 270, "Program", "Select a program", height=35, select=True)
    f.field(328, 120, 278, "Intake year", "2025", height=35, select=True)
    f.table(39, 186, [0,174,350,450,567], ["Cohort", "Program", "Students", "Details"],
            [("BUS-2025-A", "Business", "40", "View"),
             ("BUS-2025-B", "Business", "37", "View"),
             ("CS-2025-A", "Computing", "38", "View"),
             ("CS-2025-B", "Computing", "42", "View")], accent=UNI, tint="#fae2e7")
    f.card(646, 23, 374, 448, "Cohort class details", "Related records", UNI)
    f.field(666, 120, 335, "Selected cohort", "BUS-2025-A", height=35)
    for x, w, label, chosen in [(666, 103, "Profile", True), (777, 103, "Students", False), (888, 113, "Lecturers", False)]:
        f.button(x, 190, w, label, fill=UNI if chosen else "#fae2e7", ink=WHITE if chosen else UNI)
    for i,(label, value) in enumerate([("Program", "Business"), ("Intake year", "2025"), ("Student roster", "40 students"), ("Homeroom lecturer", "Assigned lecturer")]):
        y = 262+40*i
        f.text(666, y, label, size=13, weight=700)
        f.text(814, y, value, size=13, fill=MUTED)
        f.line(666, y+11, 1000, y+11)
    f.write("uni-cohort-operations-en")


def elib_filters():
    f = Frame(height=509, background="#bcb4d4")
    f.rect(0, 0, f.width, 70, "#f1e8fb")
    f.button(22, 17, 132, "eLib360", fill=LIB)
    f.field(179, 18, 438, "", "Search learning resources", outline="#d6c9ee")
    f.button(631, 18, 90, "Search", fill="#b247a6")
    f.button(895, 18, 120, "Sign in", fill="#f6be20", ink="#473100")
    f.rect(46, 103, 948, 375, WHITE, 14, "#ded1f1")
    f.text(74, 143, "Advanced search", size=22, fill=LIB, weight=700)
    f.text(961, 142, "×", size=24, fill=LIB, weight=700)
    f.field(366, 193, 308, "Curriculum", "New curriculum", outline="#d7c9ee", select=True)
    f.field(74, 261, 276, "Education level", "Secondary education", outline="#d7c9ee", select=True)
    f.field(381, 261, 276, "Subject", "All subjects", outline="#d7c9ee", select=True)
    f.field(688, 261, 276, "Book series", "All series", outline="#d7c9ee", select=True)
    f.field(74, 333, 276, "Grade", "Grade 6", outline="#d7c9ee", select=True)
    f.field(381, 333, 276, "Resource type", "All types", outline="#d7c9ee", select=True)
    f.field(688, 333, 276, "Resource scope", "All resources", outline="#d7c9ee", select=True)
    f.button(441, 405, 160, "Search resources", fill="#b247a6")
    f.write("elib-advanced-search-en")


def elib_resources():
    f = Frame(height=472, background="#f3edf9")
    f.card(21, 22, 636, 428, "Library results", "Selected filters carry forward into the search results.", LIB)
    for i, name in enumerate(["New curriculum", "Grade 6", "Mathematics"]):
        f.button(41+i*145, 103, 135, name, fill="#f2e9fe", ink=LIB, height=33)
    cards = [("Textbook", "Grade 6 mathematics"), ("School resource", "Mathematics exercises"), ("Interactive resource", "Practice activity")]
    for i, (kind, title) in enumerate(cards):
        x = 40+i*199
        f.rect(x, 159, 185, 246, WHITE, 10, "#e4d9ee")
        f.rect(x+11, 171, 163, 110, ["#f8dcc9", "#e1d9fa", "#d8eafa"][i], 7)
        f.rect(x+58, 188, 67, 72, ["#c88562", "#957acf", "#5796bd"][i], 4)
        f.line(x+70, 209, x+110, 209, WHITE)
        f.line(x+70, 223, x+104, 223, WHITE)
        f.text(x+12, 306, kind, size=12, fill=LIB, weight=700)
        f.text(x+12, 333, title, size=13, weight=700)
        f.button(x+13, 353, 158, "View resource", fill="#f2e9fe", ink=LIB, height=32)
    f.card(678, 22, 341, 428, "School-only material", "Account check at the resource boundary.", LIB)
    f.circle(746, 160, 37, "#eee4fc")
    f.rect(732, 151, 28, 23, LIB, 4)
    f.parts.append('<path d="M737 151v-5a9 9 0 0118 0v5" fill="none" stroke="#5635ba" stroke-width="3"/>')
    f.text(702, 239, "Sign in with a school account", size=17, fill=INK, weight=700)
    f.text(702, 271, "Open this resource through your school.", size=13, fill=MUTED)
    f.button(702, 315, 293, "School sign-in", fill=LIB)
    f.button(702, 367, 293, "Back to results", fill=WHITE, ink=LIB, outline="#e3d8f1")
    f.write("elib-results-access-en")


def lms_activity_list():
    f = Frame(height=489, background="#eef4f9")
    f.rect(0, 0, f.width, 66, LMS)
    f.button(24, 17, 118, "LMS360", fill="#c82538")
    f.text(165, 43, "Teacher workspace", size=14, fill=WHITE, weight=700)
    f.text(1018, 43, "Teacher", size=14, fill=WHITE, weight=700, align="end")
    f.rect(0, 66, 201, 423, "#073d62")
    for i, label in enumerate(["Statistics", "Review materials", "Resource library", "Personal workspace", "Created courses", "Shared courses", "Online teaching"]):
        y = 101+i*47
        if i == 4:
            f.rect(13, y-23, 174, 34, "#3b6382", 4)
        f.text(24, y, label, size=13, fill=WHITE, weight=700 if i == 4 else 400)
    f.text(222, 102, "Learning topics", size=20, fill=LMS, weight=700)
    f.field(222, 146, 156, "Grade", "All grades", select=True)
    f.field(388, 146, 156, "Subject", "All subjects", select=True)
    f.field(554, 146, 198, "Search", "Name of learning topic")
    f.button(796, 146, 222, "Create learning topic", fill=LMS)
    f.table(222, 219, [0,48,215,370,497,637,796], ["No.", "Topic", "Create materials", "Actions", "Created", "Approved"],
            [("1", "Speaking practice", "Add material", "Edit  ·  View", "Mar 24, 2025", "0/5"),
             ("2", "Reading practice", "Add material", "Edit  ·  View", "Mar 26, 2025", "0/3"),
             ("3", "Class discussion", "Add material", "Edit  ·  View", "Mar 27, 2025", "0/2"),
             ("4", "Review activity", "Add material", "Edit  ·  View", "Mar 29, 2025", "0/6"),
             ("5", "Language arts", "Add material", "Edit  ·  View", "Mar 29, 2025", "0/3")], accent=LMS, tint="#dfeaf5")
    f.write("lms-teacher-learning-topics-en")


def lms_speaking_modes():
    f = Frame(height=473, background="#edf4f8")
    f.card(20, 23, 490, 424, "Create speaking practice", "Teacher setup", LMS)
    f.field(40, 116, 450, "Activity title", "Speaking practice: a class presentation")
    f.field(40, 179, 450, "Practice type", "Read a supplied passage", select=True)
    f.field(40, 245, 450, "Passage or topic", "Add the material the student will see", height=63)
    f.button(292, 370, 197, "Create activity", fill=LMS)
    f.card(530, 23, 490, 424, "Speaking practice", "Learner activity choices", LMS)
    for y, title, description in [(126, "Read a supplied passage", "Open the passage and read it aloud."), (229, "Speak freely about a topic", "Read the prompt and record your response.")]:
        f.rect(549, y, 451, 86, "#e6f1fb", 10)
        f.circle(578, y+42, 13, "#b6d9f3")
        f.text(604, y+33, title, size=16, fill=LMS, weight=700)
        f.text(604, y+58, description, size=13, fill=MUTED)
        f.text(977, y+49, "›", size=21, fill=LMS, weight=700, align="end")
    f.button(549, 370, 172, "Usage guidance", fill=WHITE, ink=LMS, outline="#d1dce6")
    f.write("lms-speaking-mode-frames-en")


def test_score_preview():
    f = Frame(height=455, background="#edf4f7")
    f.card(19, 24, 1001, 407, "Review and synchronize", "Preview the destination and converted values.", TEST)
    options = [("Term", "Term 1"), ("Score column", "Ongoing assessment 1"), ("Subject", "Mathematics"), ("Score selection", "Highest score"), ("Rounding", "None")]
    for i, (label, value) in enumerate(options):
        f.field(39+i*195, 130, 181, label, value, select=True, outline="#c6d6df")
    f.table(39, 197, [0,56,206,390,485,670,956],
            ["No.", "Student ID", "Student", "Class", "Source score", "Converted score"],
            [("1", "STUDENT-001", "Student A", "A1", "9.5", "9.5"),
             ("2", "STUDENT-002", "Student B", "A1", "8.5", "8.5"),
             ("3", "STUDENT-003", "Student C", "A1", "9.0", "9.0")], accent=TEST, tint="#ffe6a5")
    f.button(438, 366, 164, "Synchronize", fill="#fbb83c", ink="#302515")
    f.write("test-score-sync-preview-en")


def test_grading_setup():
    f = Frame(height=515, background="#fbf6e9")
    f.card(22, 29, 474, 451, "Create grading session", "Teacher grading setup", TEST)
    f.field(43, 137, 433, "Assessment", "Select assessment", select=True)
    f.field(43, 207, 433, "Class", "Select class", select=True)
    f.field(43, 277, 433, "Session name", "Speaking practice · Term 1")
    f.button(253, 392, 96, "Cancel", fill=WHITE, ink=MUTED, outline="#d8e2e7")
    f.button(362, 392, 113, "Create", fill="#fbb83c", ink="#302515")
    f.card(518, 29, 499, 451, "Grading results", "Review student attempts before opening the sync preview.", TEST)
    f.table(539, 137, [0,140,241,345,458], ["Student", "Class", "Score", "Details"],
            [("Student A", "A1", "9.5", "View"),
             ("Student B", "A1", "8.5", "View"),
             ("Student C", "A1", "9.0", "View")], accent=TEST, tint="#ffe6a5")
    f.button(539, 392, 177, "Review scores", fill="#fff1cd", ink=TEST)
    f.button(745, 392, 250, "Open synchronization preview", fill="#fbb83c", ink="#302515")
    f.write("test-grading-session-en")


if __name__ == "__main__":
    sms_homeroom(reviewers=False)
    sms_homeroom(reviewers=True)
    sms_actions()
    sms_navigation()
    sms_forms()
    sms_states()
    sms_templates()
    uni_sections()
    uni_cohorts()
    elib_filters()
    elib_resources()
    lms_activity_list()
    lms_speaking_modes()
    test_score_preview()
    test_grading_setup()
