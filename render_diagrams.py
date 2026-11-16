from html import escape
from pathlib import Path

ASSETS = Path(__file__).parent / "dist/assets"
INK = "#2b2040"
PURPLE = "#663dc1"


class Diagram:
    def __init__(self, title, description, width, height):
        self.width, self.height = width, height
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc" viewBox="0 0 {width} {height}">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
            '<defs><marker id="arrow" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L8 4 L0 8 Z" fill="#7355a2"/></marker></defs>',
            f'<rect width="{width}" height="{height}" fill="#fbf8ff" rx="14"/>',
        ]

    def text(self, x, y, value, size=17, bold=False, anchor="middle", color=INK):
        self.parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{escape(value)}</text>')

    def path(self, data, *, arrow=False, dashed=False):
        end = ' marker-end="url(#arrow)"' if arrow else ""
        dash = ' stroke-dasharray="6 5"' if dashed else ""
        self.parts.append(f'<path d="{data}" fill="none" stroke="#7355a2" stroke-width="1.7"{end}{dash}/>')

    def rect(self, x, y, w, h, *, fill="#fff", stroke="#c8b4e5", radius=9):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>')

    def box(self, x, y, w, h, label, *, strong=False):
        self.rect(x, y, w, h, fill="#eee3ff" if strong else "#fff", stroke="#a384dc" if strong else "#c8b4e5")
        lines = label.split("|")
        for i, line in enumerate(lines):
            self.text(x+w/2, y+h/2+5+(i-(len(lines)-1)/2)*17, line, 15, True)

    def event(self, x, y, end=False):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="13" fill="#f0eafa" stroke="{PURPLE}" stroke-width="{3.6 if end else 1.6}"/>')

    def gateway(self, x, y):
        self.parts.append(f'<path d="M {x} {y-23} L {x+23} {y} L {x} {y+23} L {x-23} {y} Z" fill="#f7efff" stroke="{PURPLE}" stroke-width="1.6"/>')
        self.path(f'M {x-6} {y-6} l12 12 m-12 0 l12 -12')

    def entity(self, x, y, w, heading, fields):
        h = 41+24*len(fields)+6
        self.rect(x,y,w,h)
        self.rect(x,y,w,36,fill="#ebdfff")
        self.text(x+12,y+23,heading,16,True,"start")
        for i,f in enumerate(fields):
            self.text(x+12,y+56+i*24,f,14,False,"start")

    def save(self, filename):
        (ASSETS / filename).write_text("".join(self.parts)+"</svg>", encoding="utf-8")


def grade_flow():
    d=Diagram("Grade visibility flow", "Resolve school and term, check active configuration, then use the visibility flag or show as default.", 820, 405)
    d.box(300,20,220,46,"Open term scores",strong=True)
    d.path("M 410 66 V 89",arrow=True)
    d.box(300,89,220,45,"Resolve school, year and term")
    d.path("M 410 134 V 156",arrow=True)
    d.gateway(410,180)
    d.text(410,225,"Active configuration exists?",15,True)
    d.path("M 387 180 H 168 V 255",arrow=True)
    d.text(248,169,"No",14,True)
    d.path("M 433 180 H 655 V 231",arrow=True)
    d.text(586,169,"Yes",14,True)
    d.box(65,255,206,47,"Show average by default",strong=True)
    d.gateway(655,255)
    d.text(655,307,"Show-average flag is on?",15,True)
    d.path("M 632 255 H 486 V 327",arrow=True)
    d.text(536,245,"Yes",14,True)
    d.path("M 678 255 H 769 V 327",arrow=True)
    d.text(747,245,"No",14,True)
    d.box(372,327,210,46,"Include average in response",strong=True)
    d.box(603,327,190,46,"Suppress average",strong=True)
    d.save("sms-grade-flow.svg")


def notebook_erd():
    d=Diagram("Homeroom notebook ERD", "Class and academic year are parents of the notebook. A notebook owns its sections, authorizations and audit events.", 900, 494)
    d.path("M 205 93 H 310 V 176 H 329")
    d.path("M 205 336 H 310 V 271 H 329")
    d.path("M 577 180 H 638 V 67 H 680")
    d.path("M 577 225 H 680")
    d.path("M 577 270 H 638 V 374 H 680")
    for x,y,val in [(216,84,"1"),(282,167,"0..*"),(216,327,"1"),(282,262,"0..*"),(588,171,"1"),(646,57,"0..*"),(588,216,"1"),(646,216,"0..*"),(588,261,"1"),(646,364,"0..*")]:
        d.text(x,y,val,13,True,"start",PURPLE)
    d.entity(27,55,178,"Class",["PK  class_id","FK  school_id"])
    d.entity(27,298,178,"Academic year",["PK  academic_year_id","School context"])
    d.entity(329,142,248,"Homeroom notebook",["PK  notebook_id","FK  class_id","FK  academic_year_id","UQ  (class_id, academic_year_id)","School-level template"])
    d.entity(680,24,194,"Section data",["PK  section_record_id","FK  notebook_id"])
    d.entity(680,182,194,"Authorization",["PK  assignment_id","FK  notebook_id","FK  user_id"])
    d.entity(680,333,194,"Notebook audit",["PK  event_id","FK  notebook_id","Actor, action, timestamp"])
    d.text(450,473,"The unique class-year pair still resolves the same notebook when the reporting term changes.",14,True)
    d.save("sms-notebook-erd.svg")


def sequence():
    d=Diagram("UML sequence for updating grade visibility", "An administrator saves a policy in a client. The API validates role and scope, saves policy and audit if authorized, and sends a failure response otherwise.", 920, 525)
    actors=[(104,"School admin"),(328,"Web / mobile"),(553,"Grade policy API"),(795,"Policy + audit store")]
    for x,label in actors:
        d.box(x-80,23,160,38,label,strong=True)
        d.path(f"M {x} 61 V 497",dashed=True)
    d.rect(57,180,809,277,fill="none",stroke="#a58ac8",radius=0)
    d.rect(57,180,49,22,fill="#ede4fa",stroke="#a58ac8",radius=0)
    d.text(81,196,"alt",12,True)
    d.text(115,198,"[Authorized school administrator and valid term]",14,True,"start")
    d.path("M 57 366 H 866",dashed=True)
    d.text(68,389,"[Role or scope rejected]",14,True,"start")
    messages=[
        (104,328,103,"Choose term and save rule",False),
        (328,553,145,"Send scoped update",False),
        (553,795,243,"Upsert policy and append audit",False),
        (795,553,283,"Saved policy",True),
        (553,328,321,"Updated effective visibility",True),
        (328,104,351,"Confirm saved state",True),
        (553,328,418,"Return permission error",True),
        (328,104,446,"Show error; keep last saved state",True),
    ]
    for first,last,y,label,dashed in messages:
        d.path(f"M {first} {y} H {last}",arrow=True,dashed=dashed)
        d.text((first+last)/2,y-8,label,13)
    d.save("sms-policy-sequence.svg")


def lanes(diagram, labels, heights):
    left, right, top = 16, diagram.width - 16, 24
    diagram.rect(left, top, right - left, sum(heights), fill="#fff", radius=0)
    diagram.rect(left, top, 114, sum(heights), fill="#f1e7fb", radius=0)
    for label, height in zip(labels, heights):
        diagram.path(f"M {left} {top} H {right}")
        for index, line in enumerate(label.split("|")):
            diagram.text(73, top + height / 2 - 3 + index * 18, line, 15, True)
        top += height


def registration_bpmn():
    d = Diagram("UNI360 registration BPMN",
                "Academic Affairs sets a section's registration mode. Cohort assignment and student registration converge on section enrollment. Self-registration checks eligibility and seat availability. A full section can place eligible students on a waitlist.",
                1040, 523)
    lanes(d, ["Academic|Affairs", "Student", "UNI360"], [128, 110, 237])
    d.event(156, 77)
    d.path("M 169 77 H 182", arrow=True)
    d.box(182, 51, 160, 52, "Configure section|and registration mode")
    d.path("M 342 77 H 375", arrow=True)
    d.gateway(398, 77)
    d.text(398, 41, "Mode?", 14, True)
    d.path("M 421 77 H 489", arrow=True)
    d.text(455, 64, "Cohort", 13, True)
    d.box(489, 51, 163, 52, "Select cohort class")
    d.path("M 398 100 V 201 H 447", arrow=True)
    d.text(406, 173, "Self-registration", 13, True, "start")
    d.box(447, 175, 177, 52, "Select section|and submit")
    d.path("M 535 227 V 284 H 435", arrow=True)
    d.box(253, 265, 182, 50, "Check status, dates,|prerequisite and conflict")
    d.path("M 253 290 H 203 V 347", arrow=True)
    d.gateway(203, 370)
    d.text(203, 408, "Eligible?", 14, True)
    d.path("M 203 393 V 451 H 253", arrow=True)
    d.text(218, 441, "No", 13, True)
    d.box(253, 425, 182, 52, "Return the|blocking reason")
    d.path("M 435 451 H 455", arrow=True)
    d.event(468, 451, True)
    d.path("M 226 370 H 550", arrow=True)
    d.text(337, 360, "Yes", 13, True)
    d.gateway(573, 370)
    d.text(573, 335, "Seat available?", 14, True)
    d.path("M 596 370 H 751", arrow=True)
    d.text(667, 359, "Yes", 13, True)
    d.path("M 573 393 V 451 H 636", arrow=True)
    d.text(602, 440, "Full", 13, True)
    d.box(636, 425, 157, 52, "Queue eligible|student")
    d.path("M 793 451 H 857 V 396", arrow=True)
    d.text(900, 441, "Seat opens", 13, True)
    d.path("M 652 77 H 924 V 316 H 858 V 344", arrow=True)
    d.text(844, 303, "Assign cohort members", 13, True)
    d.box(751, 344, 214, 52, "Record section enrollment", strong=True)
    d.path("M 965 370 H 988", arrow=True)
    d.event(1001, 370, True)
    d.save("uni-registration-bpmn.svg")


def homeroom_bpmn():
    d = Diagram("SMS360 homeroom-record workflow",
                "The administrator selects the year and class. SMS360 opens an existing class-year notebook or creates one with its school-level template. The homeroom teacher records content and assigned leadership can review and comment.",
                1030, 555)
    lanes(d, ["School Admin", "SMS360", "Homeroom|teacher", "Assigned|leadership"], [106, 172, 106, 123])
    d.event(156, 77)
    d.path("M 169 77 H 182", arrow=True)
    d.box(182, 51, 164, 52, "Filter by grade|and open a class")
    d.path("M 346 77 H 374", arrow=True)
    d.box(374, 51, 197, 52, "Set reviewer for a grade|or individual class")
    d.path("M 264 103 V 154", arrow=True)
    d.box(182, 154, 164, 52, "Resolve class|and academic year")
    d.path("M 346 180 H 391", arrow=True)
    d.gateway(414, 180)
    d.text(414, 144, "Notebook exists?", 14, True)
    d.path("M 437 180 H 659 V 202", arrow=True)
    d.text(494, 170, "Yes", 13, True)
    d.path("M 414 203 V 253 H 444", arrow=True)
    d.text(430, 242, "No", 13, True)
    d.box(444, 227, 159, 52, "Create notebook with|school-level template")
    d.path("M 603 253 H 637 V 228 H 659", arrow=True)
    d.box(659, 202, 197, 52, "Open same notebook|when term changes", strong=True)
    d.path("M 757 254 V 329", arrow=True)
    d.box(659, 329, 197, 52, "Edit entitled sections|and submit a record")
    d.path("M 472 103 V 465 H 659", arrow=True, dashed=True)
    d.text(563, 453, "Assigned reviewer", 13, True)
    d.path("M 757 381 V 439", arrow=True)
    d.box(659, 439, 230, 52, "Review checkpoint and|save final comment")
    d.path("M 889 465 H 932", arrow=True)
    d.event(945, 465, True)
    d.text(560, 521, "The reviewer assignment controls who can edit the leadership comment.", 14, True)
    d.save("sms-homeroom-bpmn.svg")


def university_erd():
    d=Diagram("UNI360 enrollment ERD", "Programs have cohort classes, courses have sections, and student enrollment associates a student with a section.", 900, 492)
    d.path("M 218 91 H 338")
    d.path("M 558 91 H 676")
    d.path("M 218 341 H 338")
    d.path("M 558 341 H 676")
    d.path("M 775 146 V 290")
    for x,y,label in [(230,81,"1"),(300,81,"0..*"),(569,81,"1"),(639,81,"0..*"),(229,331,"1"),(301,331,"0..*"),(568,331,"1"),(638,331,"0..*"),(790,167,"1"),(790,277,"0..*")]:
        d.text(x,y,label,13,True,"start",PURPLE)
    d.entity(27,40,191,"Program",["PK  program_id","FK  major_id"])
    d.entity(338,40,220,"Cohort class",["PK  cohort_class_id","FK  program_id"])
    d.entity(676,40,198,"Student",["PK  student_id","FK  cohort_class_id"])
    d.entity(27,290,191,"Course",["PK  course_id","FK  department_id"])
    d.entity(338,290,220,"Course section",["PK  section_id","FK  course_id","FK  semester_id"])
    d.entity(676,290,198,"Enrollment",["PK  enrollment_id","FK  student_id","FK  section_id"])
    d.text(450,464,"Cohort membership groups students. Enrollment links each student to a scheduled course section.",14,True)
    d.save("uni-enrollment-erd.svg")


def library_flow():
    d = Diagram("eLib360 advanced search and access",
                "The advanced search starts with the new curriculum. Subject and series follow curriculum, grade follows education level. School-only material opens only with the required account.",
                870, 383)
    d.box(25, 38, 178, 54, "Open advanced search")
    d.path("M 203 65 H 236", arrow=True)
    d.box(236, 38, 183, 54, "Set curriculum|Default: new")
    d.path("M 419 65 H 450", arrow=True)
    d.box(450, 38, 176, 54, "Refresh subject and|textbook series")
    d.box(236, 129, 183, 54, "Set education level")
    d.path("M 419 156 H 450", arrow=True)
    d.box(450, 129, 176, 54, "Refresh grade")
    d.path("M 626 65 H 664 V 113 H 689", arrow=True)
    d.path("M 626 156 H 664 V 113")
    d.box(689, 86, 155, 54, "Search and select|a result", strong=True)
    d.path("M 766 140 V 222 H 606", arrow=True)
    d.gateway(583, 222)
    d.text(583, 197, "School-only?", 14, True)
    d.path("M 560 222 H 318 V 285", arrow=True)
    d.text(418, 212, "Yes", 13, True)
    d.box(228, 285, 180, 52, "Check school|account access")
    d.path("M 408 311 H 486", arrow=True)
    d.text(446, 299, "Allowed", 13, True)
    d.path("M 583 245 V 285", arrow=True)
    d.text(609, 266, "No", 13, True)
    d.box(486, 285, 194, 52, "Open material", strong=True)
    d.path("M 228 311 H 215", arrow=True)
    d.box(29, 285, 185, 52, "Require school sign-in")
    d.text(118, 273, "Access required", 13, True)
    d.save("elib-search-flow.svg")


def speaking_flow():
    d = Diagram("LMS360 speaking practice flow",
                "A teacher configures either reading a supplied passage or speaking on a topic. The learner chooses the activity and sees the corresponding passage or topic instructions.",
                905, 355)
    lanes(d, ["Teacher", "Student"], [146, 160])
    d.box(151, 70, 189, 52, "Create speaking|practice activity")
    d.path("M 340 96 H 367", arrow=True)
    d.gateway(390, 96)
    d.text(390, 58, "Practice type?", 14, True)
    d.path("M 413 96 H 457 V 66 H 490", arrow=True)
    d.path("M 457 96 V 130 H 490", arrow=True)
    d.box(490, 43, 164, 46, "Set the reading passage")
    d.box(490, 107, 164, 46, "Set the speaking topic")
    d.path("M 654 66 H 703 V 213", arrow=True)
    d.path("M 654 130 H 703")
    d.box(606, 213, 194, 50, "Open available activity|and read guidance", strong=True)
    d.path("M 606 238 H 509", arrow=True)
    d.gateway(486, 238)
    d.text(486, 208, "Mode?", 14, True)
    d.path("M 463 238 H 348 V 214", arrow=True)
    d.box(154, 189, 194, 50, "Read the supplied|passage aloud")
    d.path("M 486 261 V 294 H 348", arrow=True)
    d.box(154, 269, 194, 50, "Speak freely on|the selected topic")
    d.save("lms-speaking-flow.svg")


def scores_flow():
    d = Diagram("TEST360 teacher score synchronization",
                "A teacher selects a grading session and a destination term, subject and score column. The conversion preview shows source and rounded results. Review can return to inputs or continue to synchronization.",
                915, 347)
    d.box(29, 39, 166, 51, "Open grading session")
    d.path("M 195 65 H 227", arrow=True)
    d.box(227, 39, 189, 51, "Select target term,|subject and column")
    d.path("M 416 65 H 448", arrow=True)
    d.box(448, 39, 175, 51, "Set score method|and rounding")
    d.path("M 623 65 H 653", arrow=True)
    d.box(653, 39, 210, 51, "Compare source and|converted results", strong=True)
    d.path("M 758 90 V 144", arrow=True)
    d.gateway(758, 167)
    d.text(758, 215, "Confirm target and results?", 14, True)
    d.path("M 735 167 H 322 V 90", arrow=True)
    d.text(481, 156, "Adjust selections", 13, True)
    d.path("M 758 190 V 241", arrow=True)
    d.box(653, 241, 210, 51, "Synchronize to|selected grade column", strong=True)
    d.save("test-score-flow.svg")


if __name__ == "__main__":
    for render in (grade_flow, notebook_erd, sequence, registration_bpmn, homeroom_bpmn, university_erd, library_flow, speaking_flow, scores_flow):
        render()
