"""Full English screen reconstructions of selected Figma layouts and flows."""

from render_figma_evidence import Frame, INK, LIB, LMS, MUTED, SMS, TEST, UNI, WHITE


SCREENS = {
    "sms360": (
        ("sms360-screen-notebooks-en.svg", "School admin workspace · Homeroom notebooks", "The full workspace places academic year, grade, archive tabs and class-level actions in context."),
        ("sms360-screen-reviewers-en.svg", "School admin workspace · Assign reviewers", "The assignment screen separates the action for a whole grade from the controls for an individual class."),
    ),
    "uni360": (
        ("uni360-screen-course-sections-en.svg", "Academic operations · Course sections", "The list keeps term, lecturer, capacity and enrollment mode visible when managing sections."),
        ("uni360-screen-create-section-en.svg", "Academic operations · Create a course section", "The registration window appears in the course-section form for self-registration."),
    ),
    "elib360": (
        ("elib360-screen-library-en.svg", "Digital library · Browse resources", "The layout brings discovery, resource types, sorting and access labels together in one view."),
        ("elib360-screen-advanced-search-en.svg", "Digital library · Advanced search", "The overlay presents curriculum and education level together with their dependent fields."),
    ),
    "lms360": (
        ("lms360-screen-teacher-topics-en.svg", "Teacher workspace · Learning topics", "Search, filters and material actions remain visible as the teacher manages learning topics."),
        ("lms360-screen-speaking-practice-en.svg", "Learner workspace · Speaking practice", "The learner can compare the passage and topic modes before starting an activity."),
    ),
    "test360": (
        ("test360-screen-assessments-en.svg", "Teacher workspace · Assessment results", "Assessment filters, selection and score status appear together in the teacher workspace."),
        ("test360-screen-sync-preview-en.svg", "Teacher workspace · Review score synchronization", "The teacher can compare scores and verify the destination before synchronizing."),
    ),
    "whitestone": (
        ("white-results.webp", "High-fidelity prototype · From onboarding to results", "Original design export showing the mobile scan journey in light and dark treatments."),
        ("white-result-states.webp", "High-fidelity screens · Loading, summary and detail", "Original design export showing how results progress from loading to a severity summary and then a finding detail."),
    ),
    "heathelp": (
        ("heat-hifi.webp", "Mobile prototype · Choose a learning or quiz path", "Original design export showing the mobile start screen, activity choices and topic content."),
        ("heat-final.webp", "Desktop implementation · Home and activity choices", "The implemented layout shows how the prototype's navigation and activity choices carry across to desktop."),
    ),
}


SURFACE = "#f5f6fa"
BORDER = "#dfe3ed"


def canvas():
    frame = Frame(width=1240, height=750, background="#eef0f6")
    frame.rect(18, 18, 1204, 714, SURFACE, 13, BORDER)
    return frame


def top_bar(f, name, menu, active, accent, account, *, fill=WHITE, ink=INK, menu_spacing=126):
    f.rect(18, 18, 1204, 66, fill, 10)
    f.rect(39, 35, 32, 32, accent, 7)
    f.text(55, 57, name[0].upper(), size=17, fill=WHITE, weight=700, align="middle")
    f.text(82, 58, name, size=22, fill=ink, weight=700)
    for index, label in enumerate(menu):
        x = 236 + index * menu_spacing
        f.text(x, 57, label, size=14, fill=ink, weight=700 if active == label else 400)
        if active == label:
            f.line(x, 70, x + min(menu_spacing - 11, len(label) * 7 + 3), 70, accent if fill == WHITE else "#9bd9ff")
    f.button(1007, 34, 182, account, fill="#f1f3f8", ink=INK, height=35)


def side_nav(f, heading, items, active, tint, accent):
    f.rect(18, 84, 213, 648, WHITE)
    f.line(230, 84, 230, 732, BORDER)
    f.text(40, 126, heading, size=12, fill=MUTED, weight=700)
    for index, label in enumerate(items):
        y = 165 + index * 46
        if label == active:
            f.rect(32, y - 24, 185, 34, tint, 6)
        f.circle(49, y - 5, 4, accent if label == active else "#bcc3ce")
        f.text(61, y, label, size=14, fill=accent if label == active else INK, weight=700 if label == active else 400)


def page_heading(f, x, trail, title, description):
    f.text(x, 119, trail, size=13, fill=MUTED)
    f.text(x, 158, title, size=29, weight=700)
    f.text(x, 186, description, size=14, fill=MUTED)


def pill(f, x, y, width, label, background, ink):
    f.button(x, y, width, label, fill=background, ink=ink, height=26)


def screen_footer(f, x, y, count, right):
    f.text(x, y, count, size=13, fill=MUTED)
    f.button(right - 175, y - 21, 79, "Previous", fill=WHITE, ink=MUTED, outline=BORDER, height=32)
    f.button(right - 91, y - 21, 91, "Page 1 of 1", fill="#eeebf8", ink=INK, height=32)


def overlay(f, x, y, w, h):
    f.parts.append('<rect x="18" y="84" width="1204" height="648" fill="#161a2f" fill-opacity=".34"/>')
    f.rect(x, y, w, h, WHITE, 12, BORDER)
    f.text(x + w - 35, y + 40, "×", size=26, fill=MUTED)


def sms_screen(reviewers):
    f = canvas()
    top_bar(f, "SMS360", ("Teaching", "Gradebook", "Notices", "Manage", "Archived records", "Statistics"),
            "Archived records", SMS, "School administrator", menu_spacing=132)
    title = "Assign leadership reviewers" if reviewers else "Homeroom notebooks"
    page_heading(f, 49, "Archived records / Homeroom notebooks", title,
                 "Choose the grade and class scope for leadership review." if reviewers
                 else "Find notebooks for the selected academic year and grade.")
    f.button(1014, 131, 172, "Year 2025–2026", fill="#fbefe2", ink="#843b15")
    f.rect(49, 214, 1138, 456, WHITE, 10, BORDER)
    f.button(68, 232, 154, "Class notebooks", fill="#fbefe2" if reviewers else SMS, ink=SMS if reviewers else WHITE)
    f.button(230, 232, 216, "Leadership reviewers", fill=SMS if reviewers else "#fbefe2", ink=WHITE if reviewers else SMS)
    f.field(68, 302, 213, "Grade", "Grade 6", select=True)
    if reviewers:
        f.field(303, 302, 355, "Assign reviewer to the grade", "Select leadership reviewer", select=True)
        f.button(673, 302, 124, "Apply to grade")
        f.table(68, 365, [0,130,280,495,741,1100],
                ["Class", "Class size", "Homeroom teacher", "Current reviewer", "Class reviewer selection"],
                [("6A1", "40", "Teacher A", "Reviewer A", "Reviewer A  ▾"),
                 ("6A2", "39", "Teacher B", "Reviewer A", "Reviewer A  ▾"),
                 ("6A3", "41", "Teacher C", "Unassigned", "Select reviewer  ▾"),
                 ("6A4", "40", "Teacher D", "Reviewer B", "Reviewer B  ▾")],
                accent=SMS, tint="#fce4d5", row_height=43)
        f.button(996, 602, 172, "Save assignments")
    else:
        f.field(303, 302, 304, "Class", "Search by class name")
        f.table(68, 365, [0,120,257,485,722,920,1100],
                ["Class", "Class size", "Homeroom teacher", "Leadership reviewer", "Template", "Notebook"],
                [("6A1", "40", "Teacher A", "Reviewer A", "Download", "Open"),
                 ("6A2", "39", "Teacher B", "Reviewer A", "Download", "Open"),
                 ("6A3", "41", "Teacher C", "Unassigned", "Download", "Open"),
                 ("6A4", "40", "Teacher D", "Reviewer B", "Download", "Open")],
                accent=SMS, tint="#fce4d5", row_height=43)
        screen_footer(f, 69, 627, "4 classes", 1168)
    f.write("sms360-screen-reviewers-en" if reviewers else "sms360-screen-notebooks-en")


def uni_screen(create):
    f = canvas()
    top_bar(f, "UNI360", ("Academic operations", "Teaching", "Learning resources"), "Academic operations", UNI, "Academic affairs", menu_spacing=170)
    side_nav(f, "ACADEMIC OPERATIONS", ("Academic terms", "Programs", "Cohorts", "Course sections", "Lecturer assignments"),
             "Course sections", "#fbe9ed", UNI)
    page_heading(f, 257, "Academic operations / Course sections", "Course sections",
                 "Manage term offerings, lecturers, capacity and enrollment settings.")
    f.button(1000, 134, 187, "+ Create course section", fill=UNI)
    f.rect(257, 214, 930, 460, WHITE, 10, BORDER)
    f.field(275, 257, 243, "Academic term", "Semester 1 · 2025–2026", select=True)
    f.field(538, 257, 252, "Enrollment mode", "All enrollment modes", select=True)
    f.field(809, 257, 359, "Search", "Search course sections")
    f.table(275, 320, [0,244,399,500,706,893],
            ["Course section", "Lecturer", "Capacity", "Enrollment mode", "Status"],
            [("BUS101 · Section A", "Lecturer A", "40", "Self-registration", "Open"),
             ("BUS101 · Section B", "Lecturer B", "35", "Assigned enrollment", "Draft"),
             ("MGT110 · Section A", "Lecturer C", "28", "Self-registration", "Closed"),
             ("ENG102 · Section A", "Lecturer D", "32", "Assigned enrollment", "Configured")],
            accent=UNI, tint="#f9e8ef", row_height=51)
    screen_footer(f, 276, 633, "4 course sections", 1168)
    if create:
        overlay(f, 386, 108, 665, 591)
        f.text(417, 152, "Create course section", size=25, weight=700)
        f.text(417, 176, "Configure the teaching context and registration mode.", size=14, fill=MUTED)
        f.field(417, 220, 601, "Course", "BUS101 · Introduction to Business", select=True)
        f.field(417, 291, 292, "Semester", "Semester 1 · 2025–2026", select=True)
        f.field(726, 291, 292, "Lecturer", "Select lecturer", select=True)
        f.field(417, 362, 292, "Capacity", "40")
        f.field(726, 362, 292, "Enrollment mode", "Self-registration", select=True)
        f.rect(417, 423, 601, 134, "#fdf2f5", 8)
        f.text(433, 448, "Registration window", size=16, fill=UNI, weight=700)
        f.field(433, 482, 272, "Opens", "September 2 · 9:00 AM")
        f.field(726, 482, 275, "Closes", "September 9 · 5:00 PM")
        f.text(417, 589, "The registration window applies to self-registration.", size=13, fill=MUTED)
        f.button(762, 627, 95, "Cancel", fill=WHITE, ink=INK, outline=BORDER)
        f.button(868, 627, 150, "Create section", fill=UNI)
    f.write("uni360-screen-create-section-en" if create else "uni360-screen-course-sections-en")


def elib_screen(search):
    f = canvas()
    top_bar(f, "eLib360", ("Home", "Library", "Interactive learning", "Simulations"), "Library", LIB,
            "English · EN", menu_spacing=150)
    f.rect(48, 113, 1138, 152, "#eee7ff", 12)
    f.text(70, 153, "Digital library", size=27, fill=LIB, weight=700)
    f.text(70, 181, "Discover books, teaching materials and interactive learning resources.", size=15)
    f.field(70, 207, 582, "Search library", "Search titles, authors or keywords")
    f.button(664, 207, 108, "Search", fill=LIB, height=38)
    f.button(784, 207, 165, "Advanced search", fill=WHITE, ink=LIB, outline="#d7cbf5", height=38)
    f.rect(48, 287, 234, 395, WHITE, 10, BORDER)
    f.text(66, 320, "Browse by type", size=17, weight=700)
    for i, label in enumerate(("All resources", "Textbooks", "Teaching materials", "Videos", "Interactive resources")):
        y = 358 + i * 42
        if i == 0:
            f.rect(62, y - 24, 206, 34, "#f1e9ff", 5)
        f.text(74, y, label, size=14, fill=LIB if i == 0 else INK, weight=700 if i == 0 else 400)
    f.text(307, 326, "Library results", size=22, weight=700)
    f.field(989, 320, 197, "Sort by", "Newest", select=True)
    books = (
        ("Study skills workbook", "Workbook", "Public", "#d8e8ff", "#254e79"),
        ("Class reading pack", "Learning material", "School only", "#efe4ff", LIB),
        ("Introduction to ratios", "Interactive resource", "Public", "#dceee6", "#1d6149"),
    )
    for i, (title, kind, access, cover, color) in enumerate(books):
        x = 307 + i * 298
        f.rect(x, 379, 279, 288, WHITE, 9, BORDER)
        f.rect(x + 12, 390, 255, 113, cover, 7)
        f.rect(x + 109, 405, 61, 82, color, 5)
        f.line(x + 119, 420, x + 157, 420, WHITE)
        f.line(x + 119, 431, x + 157, 431, WHITE)
        f.text(x + 15, 531, kind, size=13, fill=MUTED)
        f.text(x + 15, 555, title, size=16, weight=700)
        pill(f, x + 15, 567, 92, access, "#f4effe", LIB)
        f.button(x + 15, 615, 151, "Open resource", fill=LIB)
    if search:
        overlay(f, 292, 130, 656, 491)
        f.text(325, 175, "Advanced search", size=25, weight=700)
        f.text(325, 202, "Use the curriculum and education level to narrow your results.", size=14, fill=MUTED)
        f.field(325, 249, 275, "Curriculum", "New curriculum", select=True)
        f.field(624, 249, 289, "Education level", "Lower secondary", select=True)
        f.field(325, 323, 275, "Subject", "Mathematics", select=True)
        f.field(624, 323, 289, "Grade", "Grade 6", select=True)
        f.field(325, 397, 588, "Textbook series", "All applicable series", select=True)
        f.rect(325, 453, 588, 44, "#f3edff", 7)
        f.text(338, 480, "Changing the curriculum can reset the subject and series.", size=13, fill=LIB)
        f.button(676, 548, 99, "Reset", fill=WHITE, ink=LIB, outline=BORDER)
        f.button(786, 548, 127, "Apply filters", fill=LIB)
    f.write("elib360-screen-advanced-search-en" if search else "elib360-screen-library-en")


def lms_screen(learner):
    f = canvas()
    top_bar(f, "LMS360", ("Learning", "Resources", "Activities", "Results"), "Activities", "#247bac",
            "Learner account" if learner else "Teacher account", fill=LMS, ink=WHITE)
    if learner:
        page_heading(f, 48, "Learning / Speaking practice", "Speaking practice",
                     "Choose an activity type and review its instructions before recording.")
        f.rect(48, 218, 1138, 60, "#eaf4fb", 8)
        f.text(67, 256, "How it works", size=16, fill=LMS, weight=700)
        f.text(208, 256, "Choose a mode, review the prompt and record your response.", size=14, fill=LMS)
        methods = (
            ("Read a passage", "Practice reading provided text aloud.", "Example passage",
             "Our school library opens at eight.", "Choose passage"),
            ("Speak about a topic", "Plan and record an original response.", "Example topic",
             "Describe a place you like to study.", "Choose topic"),
        )
        for i, (title, detail, label, example, action) in enumerate(methods):
            x = 48 + i * 578
            f.card(x, 301, 560, 349, title, detail, LMS)
            f.rect(x + 20, 404, 520, 110, "#f0f7fc", 10)
            f.text(x + 38, 440, label, size=14, fill=LMS, weight=700)
            f.text(x + 38, 471, example, size=17)
            f.button(x + 20, 567, 157, action, fill=LMS)
        f.write("lms360-screen-speaking-practice-en")
        return
    side_nav(f, "TEACHER WORKSPACE", ("Dashboard", "Learning topics", "My materials", "Review results", "Online classes"),
             "Learning topics", "#eaf4fb", LMS)
    page_heading(f, 257, "Teacher workspace / Materials", "Learning topics",
                 "Filter topics, add materials and review the items ready for use.")
    f.button(1004, 134, 182, "+ Create learning topic", fill=LMS)
    f.rect(257, 214, 930, 473, WHITE, 10, BORDER)
    for x, w, label, value in ((275, 184, "Grade", "All grades"), (476, 200, "Subject", "All subjects"),
                               (693, 475, "Search", "Search learning topics")):
        f.field(x, 261, w, label, value, select=label != "Search")
    f.table(275, 327, [0,239,432,571,746,893],
            ["Learning topic", "Materials", "Actions", "Created", "Approved"],
            [("Grade 4 Mathematics", "Add material", "Edit · View", "14 Oct 2025", "0 of 5"),
             ("Grade 9 Literature", "Add material", "Edit · View", "13 Sep 2025", "0 of 5"),
             ("Vietnamese Studies", "Add material", "Edit · View", "20 Aug 2025", "2 of 3"),
             ("Speaking practice", "Add material", "Edit · View", "07 Jul 2025", "1 of 3")],
            accent=LMS, tint="#e1f0fa", row_height=50)
    screen_footer(f, 275, 640, "4 learning topics", 1168)
    f.write("lms360-screen-teacher-topics-en")


def test_screen(preview):
    f = canvas()
    top_bar(f, "TEST360", ("Assessments", "Grading", "Results"), "Results", "#8b5003", "Teacher account")
    side_nav(f, "ASSESSMENT WORKSPACE", ("Assessment list", "Grading sessions", "Assessment results", "Score synchronization"),
             "Assessment results", "#ffefc3", "#795003")
    page_heading(f, 257, "Results / Teacher workspace", "Assessment results",
                 "Find an assessment and review its scores before synchronizing.")
    f.button(1007, 134, 180, "Synchronize scores", fill="#f2b83e", ink="#322405")
    f.rect(257, 213, 930, 471, WHITE, 10, BORDER)
    for i, (label, value) in enumerate((("Term", "Term 1"), ("Class", "All classes"), ("Subject", "All subjects"), ("Status", "All statuses"))):
        f.field(275 + i * 226, 259, 215, label, value, select=True)
    f.table(275, 326, [0,94,342,497,601,893],
            ["Select", "Assessment", "Subject", "Class", "Score status"],
            [("✓", "Speaking practice 1", "Mathematics", "A1", ""),
             ("□", "Unit review", "Mathematics", "A2", ""),
             ("□", "Writing practice", "Literature", "A1", ""),
             ("□", "Reading check", "Literature", "A2", "")],
            accent="#67430f", tint="#ffeab7", row_height=49)
    for i, (label, fill, ink) in enumerate((("Scores finalized", "#e2f5e8", "#205b39"), ("Ready to finalize", "#ffefdb", "#873b16"),
                                             ("Scores finalized", "#e2f5e8", "#205b39"), ("Ready to finalize", "#ffefdb", "#873b16"))):
        pill(f, 887, 385 + i * 49, 142, label, fill, ink)
    screen_footer(f, 275, 646, "4 assessments · 1 selected", 1168)
    if preview:
        overlay(f, 247, 127, 876, 557)
        f.text(279, 170, "Review score synchronization", size=26, weight=700)
        f.text(279, 195, "Verify the destination and review converted values before saving.", size=14, fill=MUTED)
        f.field(279, 247, 248, "Term", "Term 1", select=True)
        f.field(545, 247, 264, "Subject", "Mathematics", select=True)
        f.field(827, 247, 266, "Destination column", "Ongoing assessment 1", select=True)
        f.field(279, 322, 382, "Score selection", "Highest score", select=True)
        f.field(680, 322, 413, "Rounding", "One decimal place", select=True)
        f.table(279, 394, [0,263,429,624,814], ["Learner", "Class", "Source score", "Converted score"],
                [("Student A", "A1", "8.26", "8.3"), ("Student B", "A1", "7.74", "7.7"), ("Student C", "A1", "9.02", "9.0")],
                accent=TEST, tint="#ffeab7", row_height=43)
        f.button(815, 609, 88, "Cancel", fill=WHITE, ink=INK, outline=BORDER)
        f.button(914, 609, 179, "Synchronize scores", fill="#f2b83e", ink="#322405")
    f.write("test360-screen-sync-preview-en" if preview else "test360-screen-assessments-en")


if __name__ == "__main__":
    for render in (sms_screen, uni_screen, elib_screen, lms_screen, test_screen):
        render(False)
        render(True)
