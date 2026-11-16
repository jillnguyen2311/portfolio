"""English implementation examples based on the portfolio's Figma and specification evidence."""

from render_figma_evidence import Frame, LIB, LMS, SMS, TEST, UNI, WHITE


HANDOFF = {
    "sms360": (
        ("sms360-figma-reviewer-scope-en", "Reviewer assignment at grade and class scope",
         "The same reviewer selector applies to either the selected grade or one class.",
         SMS, (
             ("Assign by grade", "Update reviewer assignments for the selected grade.",
              (("Grade", "Grade 6"), ("Reviewer", "Leadership reviewer A"), ("Scope", "All eligible classes in Grade 6")),
              "Apply to grade"),
             ("Assign by class", "Update only the selected class record.",
              (("Grade", "Grade 6"), ("Class", "6A2"), ("Reviewer", "Leadership reviewer B")),
              "Save class assignment"),
         )),
        ("sms360-figma-permission-states-en", "Edit and read-only notebook states",
         "The reviewer assignment determines whether the leadership comment can be edited.",
         SMS, (
             ("Assigned reviewer", "The comment field accepts edits.",
              (("Notebook", "Class 6A2 · School year 2025–2026"), ("Role", "Assigned leadership reviewer"),
               ("Leadership comment", "Editable")), "Save comment"),
             ("Homeroom teacher", "The same section remains readable on the class record.",
              (("Notebook", "Class 6A2 · School year 2025–2026"), ("Role", "Homeroom teacher"),
               ("Leadership comment", "Read only")), ""),
         )),
    ),
    "uni360": (
        ("uni360-figma-role-handoff-en", "Navigation and ownership by role",
         "The role map informs what users can open and which part of a course section they maintain.",
         UNI, (
             ("Academic affairs", "Configure the section and its enrollment method.",
              (("Workspace", "Academic operations"), ("Section properties", "Semester, schedule and capacity"),
               ("Enrollment", "Assign a cohort or enable self-registration")), "Edit course section"),
             ("Lecturer", "Use the section to manage instruction.",
              (("Workspace", "Assigned course sections"), ("Section properties", "View the administrator's setup"),
               ("Learning content", "Manage materials inside the section")), "Manage course content"),
         )),
        ("uni360-figma-enrollment-feedback-en", "Eligibility and waitlist feedback",
         "Different enrollment outcomes need different next steps.",
         UNI, (
             ("Prerequisite incomplete", "Show the missing requirement beside the blocked request.",
              (("Requested section", "Business Operations · Section A"), ("Eligibility check", "Prerequisite incomplete"),
               ("Result", "Enrollment request blocked")), ""),
             ("Eligible with a full section", "Where enabled, offer the waitlist to eligible students.",
              (("Requested section", "Business Operations · Section B"), ("Capacity check", "No open seats"),
               ("Result", "Waitlist available")), "Join waitlist"),
         )),
    ),
    "elib360": (
        ("elib360-figma-filter-dependencies-en", "Dependent search fields",
         "When the parent selector changes, re-evaluate the subject and textbook series.",
         LIB, (
             ("Current search", "The visible selections belong to the active curriculum.",
              (("Curriculum", "New curriculum"), ("Subject", "Mathematics"), ("Textbook series", "Series A")), "Search"),
             ("After a curriculum change", "Refresh the choices and clear any invalid selection.",
              (("Curriculum", "Previous curriculum"), ("Subject", "Choose a subject"),
               ("Textbook series", "Choose an available series")), "Search"),
         )),
        ("elib360-figma-resource-access-en", "Resource cards and access states",
         "The access rule is checked when the reader opens a resource.",
         LIB, (
             ("Community resource", "The reader can open the published item directly.",
              (("Title", "Study skills workbook"), ("Material type", "Workbook"), ("Access", "Public")), "Open resource"),
             ("School-only resource", "Prompt for a school account before opening the item.",
              (("Title", "Class reading pack"), ("Material type", "Learning material"), ("Access", "School sign-in required")),
              "Sign in with school account"),
         )),
    ),
    "lms360": (
        ("lms360-figma-speaking-setup-en", "Teacher inputs by speaking activity type",
         "A source field in the teacher's form determines what appears on the learner's card.",
         LMS, (
             ("Read a passage", "The learner receives the text the teacher provides.",
              (("Activity type", "Read a passage"), ("Content", "Passage text"), ("Learner sees", "Text to read aloud")),
              "Save activity"),
             ("Speak about a topic", "The learner receives a prompt for an open response.",
              (("Activity type", "Speak about a topic"), ("Content", "Topic prompt"), ("Learner sees", "Prompt and instructions")),
              "Save activity"),
         )),
        ("lms360-figma-guidance-handoff-en", "Instructions and recording actions",
         "The learner understands what to do before opening the recording step.",
         LMS, (
             ("Prepare to speak", "Keep guidance next to the selected activity.",
              (("Content", "A passage or a topic prompt"), ("Instructions", "Read the guidance before recording"),
               ("Next screen", "Recording controls")), "Start recording"),
             ("Review a recorded answer", "Keep the answer distinct from the instructions.",
              (("Content", "The same prompt remains visible"), ("Response", "Recorded speaking answer"),
               ("Primary action", "Submit the answer")), "Submit answer"),
         )),
    ),
    "test360": (
        ("test360-figma-session-context-en", "Grading-session form and result context",
         "The assessment and class constrain which results the teacher reviews.",
         TEST, (
             ("Set up grading", "Make the assessment and class explicit before creating a session.",
              (("Assessment", "Speaking practice 1"), ("Class", "A1"), ("Session name", "Term 1 speaking assessment")),
              "Create grading session"),
             ("Review results", "Show the grading context before score synchronization.",
              (("Assessment", "Speaking practice 1"), ("Class", "A1"), ("Results", "Review individual student attempts")),
              "Review scores"),
         )),
        ("test360-figma-score-mapping-en", "Score destination and conversion preview",
         "The same destination can be reviewed with different rounding choices.",
         TEST, (
             ("Source value", "The preview shows what will be sent to the selected destination.",
              (("Destination", "Term 1 · Mathematics · Ongoing assessment 1"), ("Rounding", "None"), ("Source → preview", "8.26 → 8.26")),
              "Review mapping"),
             ("Rounded preview", "The teacher can compare conversion before committing.",
              (("Destination", "Term 1 · Mathematics · Ongoing assessment 1"), ("Rounding", "One decimal place"),
               ("Source → preview", "8.26 → 8.3")), "Synchronize scores"),
         )),
    ),
    "whitestone": (
        ("whitestone-figma-scan-confirmation-en", "Scan confirmation and retake",
         "The source prototype separates image capture from confirmation.",
         LIB, (
             ("Review selected image", "The user can confirm that the selected image is usable.",
              (("Step", "Scan confirmation"), ("Preview", "Selected image"), ("Action", "Use this image to continue")), "Use this image"),
             ("Retake image", "Return to the camera when the selected image needs replacing.",
              (("Step", "Scan confirmation"), ("Preview", "Selected image"), ("Action", "Retake before continuing")), "Retake image"),
         )),
        ("whitestone-figma-result-handoff-en", "Result row and expanded resource",
         "The result component reveals details and a related resource from the same finding.",
         LIB, (
             ("Collapsed finding", "Keep the severity label visible in the result summary.",
              (("Result", "Illustrative scan finding"), ("Status", "Review recommended"), ("Details", "Collapsed")), "Open finding"),
             ("Expanded finding", "Reveal additional context while preserving the status.",
              (("Result", "Illustrative scan finding"), ("Status", "Review recommended"), ("Resource", "Preparing for a dental appointment")),
              "Read more"),
         )),
    ),
    "heathelp": (
        ("heathelp-figma-activity-branches-en", "Learning and quiz entry points",
         "The two actions use the same visual family and need clear destination labels.",
         SMS, (
             ("Learn by topic", "The entry leads to learning material.",
              (("Destination", "Learning content"), ("Context", "Selected topic"), ("Action", "Open information and examples")), "Learn more"),
             ("Take a topic quiz", "The entry leads to questions scoped to the selected topic.",
              (("Destination", "Quiz"), ("Context", "Selected topic"), ("Action", "Answer questions and see progress")), "Start quiz"),
         )),
        ("heathelp-figma-progress-handoff-en", "Quiz feedback and progress",
         "The feedback component communicates whether the learner should retry or continue.",
         SMS, (
             ("Answer accepted", "Show the learner the next available action.",
              (("Feedback", "Correct"), ("Progress", "Question 2 of 5"), ("Next", "Advance to the next question")), "Continue"),
             ("Retry needed", "Keep the same question in context to try a different answer.",
              (("Feedback", "Incorrect"), ("Progress", "Question 2 of 5"), ("Next", "Choose another answer")), "Try again"),
         )),
    ),
}


def handoff_frame(title, description, height=474):
    frame = Frame(height=height, background="#f5f2f9")
    frame.text(26, 40, title, size=26, weight=700)
    frame.text(26, 67, description, size=15)
    return frame


def score_mapping_board(title, description, accent, examples):
    f = handoff_frame(title, description, height=441)
    f.card(25, 92, 990, 323, "Synchronization preview", "Changing the rounding rule keeps the same destination.", accent)
    f.field(49, 186, 426, "Destination", "Term 1 · Mathematics · Ongoing assessment 1")
    f.field(495, 186, 233, "Score selection", "Highest score", select=True)
    f.field(747, 186, 242, "Rounding", "One decimal place", select=True)
    f.table(49, 255, [0,315,505,701,940],
            ["Sample learner", "Source score", "No rounding", "One decimal place"],
            [("Student A", "8.26", "8.26", "8.3"), ("Student B", "7.74", "7.74", "7.7")],
            accent=accent, tint="#ffe6a5", row_height=34)
    f.button(790, 371, 199, examples[1][3], fill="#fbb83c", ink="#382708")
    return f


def result_row_board(title, description, accent, examples):
    f = handoff_frame(title, description, height=504)
    for i, (heading, detail, _, action) in enumerate(examples):
        x = 25 + i * 505
        f.card(x, 93, 485, 379, heading, detail, accent)
        phone = x + 87
        f.rect(phone, 169, 310, 280, "#fbf9ff", 20, "#d6c7ef")
        f.rect(phone + 6, 175, 298, 49, "#5635ba", 14)
        f.text(phone + 22, 205, "Your results", size=17, fill=WHITE, weight=700)
        f.rect(phone + 14, 241, 282, 172 if i else 100, WHITE, 10, "#ddcff1")
        f.rect(phone + 24, 252, 135, 23, "#fae9bd", 6)
        f.text(phone + 32, 268, "Review recommended", size=12, fill="#563a00", weight=700)
        f.text(phone + 24, 295, "Illustrative scan finding", size=16, weight=700)
        f.text(phone + 269, 296, "−" if i else "+", size=20, fill=accent, weight=700)
        if i:
            f.line(phone + 24, 306, phone + 278, 306)
            f.text(phone + 24, 330, "Related resource", size=14, weight=700)
            f.text(phone + 24, 350, "Preparing for a dental appointment", size=13)
        f.text(phone + 24, 387 if i else 321, action, size=14, fill=accent, weight=700)
    return f


def quiz_feedback_board(title, description, accent, examples):
    f = handoff_frame(title, description, height=440)
    for i, (heading, detail, _, action) in enumerate(examples):
        x = 25 + i * 505
        tone = "#9e302a" if i else "#146345"
        f.card(x, 94, 485, 317, heading, detail, accent)
        f.text(x + 20, 195, "Question 2 of 5", size=15, weight=700)
        f.rect(x + 20, 208, 445, 11, "#eee8eb", 5)
        f.rect(x + 20, 208, 178, 11, accent, 5)
        f.rect(x + 20, 244, 445, 54, "#fff0ed" if i else "#ecf8ef", 9)
        f.text(x + 35, 277, "Incorrect · Choose another answer" if i else "Correct · Ready for the next question",
               size=16, fill=tone, weight=700)
        f.button(x + 20, 332, 158, action, fill=accent)
    return f


SPECIAL_BOARDS = {
    "test360-figma-score-mapping-en": score_mapping_board,
    "whitestone-figma-result-handoff-en": result_row_board,
    "heathelp-figma-progress-handoff-en": quiz_feedback_board,
}


def render_handoff_boards():
    for boards in HANDOFF.values():
        for key, title, description, accent, examples in boards:
            if key in SPECIAL_BOARDS:
                SPECIAL_BOARDS[key](title, description, accent, examples).write(key)
                continue
            frame = handoff_frame(title, description)
            for i, (heading, detail, fields, action) in enumerate(examples):
                x = 25 + i * 505
                frame.card(x, 94, 485, 357, heading, detail, accent)
                for j, (label, value) in enumerate(fields):
                    frame.field(x + 18, 197 + j * 62, 449, label, value)
                if action:
                    frame.button(x + 18, 396, 220, action, fill=accent)
            frame.write(key)


if __name__ == "__main__":
    render_handoff_boards()
