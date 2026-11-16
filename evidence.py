TILES = {
    "sms360": ("sms360-signin-en.webp", "SMS360 sign-in design with role selection, localized in English"),
    "uni360": ("uni360-signin-en.webp", "UNI360 sign-in design with account selection, localized in English"),
    "elib360": ("elib360-home-en.webp", "eLib360 digital library homepage mockup, localized in English"),
    "lms360": ("lms360-signin-en.webp", "LMS360 student and teacher sign-in design, localized in English"),
    "test360": ("test360-signin-en.webp", "TEST360 student and teacher sign-in design, localized in English"),
    "vlip": ("vlip-home.webp", "Vancouver Local Immigration Partnership redesign homepage"),
    "nikato": ("nikato-home.webp", "Nikato Landscape homepage"),
    "westernstains": ("westernstains-home.webp", "Archived WesternStains Shopify homepage"),
}

FIGMA_LINKS = {
    "elib360": (
        ('eLib360 searchable library', 'https://www.figma.com/design/eGb10BeFX4qls6Fwca80yj/th%C6%B0-vi%E1%BB%87n-s%E1%BB%91?node-id=9-3883'),
    ),
    "heathelp": (
        ('HeatHelp early layout in Figma', 'https://www.figma.com/design/ayRUsUjNcsmcJcXGgo8tsE/heat-help--Copy-?node-id=0-1'),
    ),
    "lms360": (
        ('LMS360 speaking-practice screen', 'https://www.figma.com/design/ID9io0n1LmPncigXLipKUO/LMS360?node-id=2896-416'),
    ),
    "sms360": (
        ('SMS360 design system', 'https://www.figma.com/design/2pb4WTtP2zcNRDriHYq97M/QTTH---v2--editable-?node-id=5-40'),
        ('School Admin notebook screen', 'https://www.figma.com/design/2pb4WTtP2zcNRDriHYq97M/QTTH---v2--editable-?node-id=20050-196271'),
        ('Eight button variants', 'https://www.figma.com/design/2pb4WTtP2zcNRDriHYq97M/QTTH---v2--editable-?node-id=3168-6764'),
        ('Six input variants', 'https://www.figma.com/design/2pb4WTtP2zcNRDriHYq97M/QTTH---v2--editable-?node-id=3700-54354'),
        ('Popup library', 'https://www.figma.com/design/2pb4WTtP2zcNRDriHYq97M/QTTH---v2--editable-?node-id=3608-83987'),
    ),
    "test360": (
        ('TEST360 grading and score synchronization frame', 'https://www.figma.com/design/ID9io0n1LmPncigXLipKUO/LMS360?node-id=2543-664'),
    ),
    "uni360": (
        ('UNI360 course-section form', 'https://www.figma.com/design/ujeCWIQt89pIRrDYXc1vz2/UNI360--demo-ver-?node-id=292-144105'),
        ('UNI360 role and menu map', 'https://www.figma.com/board/ZRjdn6kL1j8CN8nZYEGONB/ROLE-MENU-UI-UNI.LMS360?node-id=0-1'),
    ),
    "whitestone": (
        ('WhiteStone mockup in Figma', 'https://www.figma.com/design/IWBSDejc54MY07tMDMfrtR/Mockup-for-Week-3--Copy-?node-id=210-411'),
    ),
}

FIGMA_SKILLS = {
    "sms360": ("Component variants", "Dialog and feedback states", "Permission states", "Annotated developer handoff"),
    "uni360": ("FigJam role mapping", "Conditional forms", "Create and edit layouts"),
    "whitestone": ("Wireframing", "High-fidelity prototyping", "Light and dark variants"),
    "heathelp": ("Low- and high-fidelity mockups", "Quiz feedback components", "Usability iteration"),
    "elib360": ("Information architecture", "Dependent filter states", "Dropdown variants", "Access prompts"),
    "lms360": ("Teacher and learner flows", "Activity-specific layouts", "Role-based screens"),
    "test360": ("Assessment workflow", "Score conversion previews", "Confirmation states"),
}

FIGMA_REVIEW = {
    "sms360": (
        "I used the shared Figma library to specify the homeroom notebook and reviewer assignment. I linked numbered "
        "screen controls to their data, actions, permissions and acceptance criteria. The eight button and six input "
        "variants show how reusable controls carry across the notebook, scoped assignments and read-only states."
    ),
    "uni360": (
        "I mapped user roles and enrollment rules to the course-section interface. The create and edit layouts show "
        "when semester, lecturer, capacity and registration controls apply. The FigJam role map gives developers "
        "a reference for which navigation each role should see."
    ),
    "elib360": (
        "I defined the catalogue structure and access rules. The advanced-search design shows how curriculum changes "
        "the subjects and textbook series available, and how education level constrains grade. The resource-card "
        "flow shows where school-only access is checked."
    ),
    "lms360": (
        "I mapped the teacher setup and student practice flows. The Figma screens show how an activity type governs "
        "the instructions, passage or topic the learner sees before recording. The teacher-facing list shows "
        "how materials can be filtered, reviewed and managed."
    ),
    "test360": (
        "I contributed to the design of the assessment workflow. The grading-session screens establish the "
        "assessment and class, while the synchronization preview exposes the mapped term, subject and column. "
        "The side-by-side results let teachers review conversion and rounding before committing."
    ),
    "whitestone": (
        "I used team personas and wireframes to work through the oral-health results flow. The design boards show "
        "early alternatives, shared components, severity labels and loading and result states. I carried the result "
        "and related resource patterns into the Next.js implementation."
    ),
    "heathelp": (
        "I worked with the team on early wireframes and high-fidelity flows for learning and quizzes. The mockups "
        "show topic selection, navigation, quiz progress and answer feedback. Usability sessions showed that "
        "Learn More and Quiz looked too similar, which gave the team a specific issue to address."
    ),
}

ROLES = {
    "sms360": (
        "SMS360 connects school administration to teacher tasks and student or guardian views. This case follows the staff roles in the homeroom notebook, then applies the same role-first analysis to the electronic gradebook.",
        (
            ("School administrator", "Maintains class records and assigns leadership reviewers.", "Class and grade filters, notebook and download actions, grade-wide and individual assignment controls."),
            ("Principal", "Can view notebooks across the school.", "School-wide read access. Editing the final comment follows reviewer assignment."),
            ("Assigned leadership reviewer", "Enters the leadership comment for notebooks assigned to them.", "Edit permission on the final section of an assigned notebook."),
            ("Assigned homeroom teacher", "Maintains the assigned class notebook and reads leadership feedback.", "Class-scoped section editing and read access to leadership comments."),
            ("Subject teacher", "Records grades within a teaching assignment and permitted entry window.", "Edit and view permissions scoped by assignment and period."),
            ("Student or authorized guardian", "Reads results released for that student.", "Released data scoped to the student and guardian relationship."),
        ),
    ),
    "uni360": (
        "UNI360 separates institutional organization, academic operations and delivery. The role map connects authorization scope with menu visibility.",
        (
            ("System administrator", "Administers platform configuration and member institutions.", "Platform-level management."),
            ("Academic affairs / school admin", "Sets up training structures, terms, cohorts, scheduled sections and assignments.", "Administration forms and controls with school scope."),
            ("Academic leadership", "Oversees the institution, faculty, department or program.", "Visibility scoped to the academic structure assigned to the role."),
            ("Lecturer", "Manages activities and materials inside an assigned section.", "Course-content editing. Academic affairs owns the setup of administrator-created sections."),
            ("Student", "Accesses assigned sections or self-registers where enabled.", "Separate My Classes and eligible registration views."),
        ),
    ),
    "lms360": (
        "LMS360 is the learning workspace in the product suite. The design shows distinct teacher and student surfaces, including preparing and using speaking activities.",
        (
            ("Student", "Opens speaking practice and chooses an exercise type.", "Guidance and distinct options for reading a passage or speaking from a topic."),
            ("Teacher", "Uses teacher-side creation and exercise details.", "Inputs suited to the activity type and an interface distinct from the learner view."),
            ("School administrator", "Uses school administration surfaces in the broader platform design.", "Role-specific navigation with administrative tasks separated from learning or teaching."),
        ),
    ),
    "test360": (
        "TEST360 separates the learner’s attempt from grading and gradebook operations.",
        (
            ("Student", "Completes a speaking activity and uses the student-facing result views.", "Attempt and student information screens."),
            ("Teacher", "Sets up the grading session, inspects results and checks score conversion.", "Grading controls, statistics and a separate synchronization preview."),
        ),
    ),
    "elib360": (
        "eLib360 combines community discovery with materials restricted to schools.",
        (
            ("Visitor or learner", "Searches by curriculum, level and subject and browses resource groups.", "Search filters, resource categories and results."),
            ("School-account user", "Accesses materials scoped to a school.", "Sign-in and school access checks at the resource boundary."),
            ("Community contributor", "Submits resources under the proposed account and moderation rules.", "Submission and review states as applicable."),
        ),
    ),
}

COMPONENTS = {
    "sms360": (
        ("Role-based navigation", "The design-system board groups menu sets for administrators, teachers and students, plus headers and tabs.", "Review the same screen shell against each role’s action scope."),
        ("Record and reviewer tabs", "The adjacent pages expose the notebook list and reviewer assignments. Academic-year and grade context determine which classes are shown.", "Specify the grade-scoped batch control separately from changing a single class."),
        ("School Admin table", "The list shows class, class size, homeroom teacher, assigned reviewer, download and open actions.", "The workbook maps the visible fields to their sources and states which roles may use the actions."),
        ("Button variants", "Four types have default and disabled states. Leading and trailing icons are optional.", "Specify which actions are available by role, and when prerequisites leave the action disabled."),
        ("Input and feedback patterns", "Large and small inputs each have default, disabled and special states. The system also includes confirmation dialogs and error screens.", "Identify validation text, field state and recovery for each task."),
    ),
    "uni360": (
        ("Role/menu board", "The FigJam source maps administration, academic leadership, lecturers and students to their menus.", "Review navigation scope before specifying individual screens."),
        ("Course-section form variants", "Academic operations contains separate forms for sections with assigned enrollment and learner self-registration.", "Make enrollment ownership explicit and vary the relevant inputs by mode."),
        ("Cohort versus course section", "The board contains separate cohort lists, student and lecturer details, and course-section operations.", "Keep cohort membership separate from the enrollment record and the section’s schedule."),
    ),
    "elib360": (
        ("Curriculum and level selectors", "Advanced search defaults to the new curriculum. Subject and book series follow curriculum, while grade follows education level.", "Refresh dependent options and clear invalid selections after the parent control changes."),
        ("Results and resource navigation", "The board includes the library homepage, search overlay and separate listing views.", "Carry categories and applied filters through the search journey."),
        ("School resource entry", "The specification distinguishes community materials from school-only items.", "Evaluate access where the learner attempts to open the resource."),
    ),
    "lms360": (
        ("Speaking activity cards", "The learning screen offers reading a supplied passage and speaking freely on a topic.", "Clearly label the mode and the type of content it requires."),
        ("Guidance and reusable actions", "The board has usage guidance, speaker icons and compact buttons around the practice flow.", "Keep the instruction state separate from the student’s submission action."),
        ("Teacher and student frames", "The teacher-side create view is separate from the learner’s exercise screens.", "Trace prompt or passage inputs to what the learner sees."),
    ),
    "test360": (
        ("Grading-session dialogue", "The assessment board shows exam, class and session-name controls.", "Identify the grading context before retrieving or working with results."),
        ("Synchronization selectors", "The preview contains term, target score column, subject, score selection and rounding.", "Treat the destination and calculation method as distinct decisions."),
        ("Source and converted score table", "The Figma frame displays source and converted results side by side.", "Let the teacher inspect the proposed mapping before synchronizing."),
    ),
    "whitestone": (
        ("Capture and image confirmation", "The board shows scanning and how the user moves from the camera to the selected image.", "Give users a clear point to accept the image or retake it."),
        ("Result and resource patterns", "Design exports show reusable result elements, severity treatments and related resources.", "Maintain readable status labels and a clear path from findings to education."),
        ("Reusable UI and variants", "The exported team boards include navigation, buttons and colour and size variations.", "Carry visual and interaction decisions into the Next.js components."),
    ),
    "heathelp": (
        ("Topic and destination actions", "The boards place Learn More and Quiz in the same family of interactions.", "Usability feedback called for clearer destination labels and quiz scope."),
        ("Progress and answer actions", "The exported boards show separate progress indicators and button variants.", "Carry consistent progress and action states across topic quizzes."),
        ("Back and home controls", "The low- and high-fidelity exports show movement between information, quiz and home.", "Check that a user can return from each stage without losing orientation."),
    ),
}

CASES = {
    "sms360": [
        ("What the workspace covers", "SMS360 supports teaching assignments, electronic grades and school records. The School Admin workbook indexes 144 functions across 15 product areas. The homeroom notebook is a representative feature because the same record supports different actions for administrators, teachers and school leadership."),
        ("My contribution and handoff", "I translated operating rules into role-based UI, annotated Figma screen specifications, data rules and API samples. The notebook spec ties numbered controls to their data sources, actions and acceptance criteria. It distinguishes what staff can see, what they can edit and which record each action affects."),
        ("One notebook across reporting checkpoints", "The DB design identifies a notebook by class and academic year and creates it on first access. Term selection changes the reporting content within that notebook. The primary and secondary templates can be different while the notebook identity stays stable."),
        ("Reviewer assignment and section permissions", "The administrator selects a grade and may assign eligible leadership for the whole grade or for individual classes. Assignment grants permission to edit the final leadership comment. A teacher maintains the eligible sections for their class and can read the leadership section."),
        ("Separate gradebook decisions", [
            "SMS-03-05 specifies grade-entry and visibility settings. Entry windows and edit and view permissions are separate controls.",
            "SMS-03-07 covers the result columns released to students and authorized guardians.",
            "The separate average-column rollout used a school, year and term policy. Its default applies when an active setting is missing.",
        ]),
        ("What to validate", "Open the same class in two reporting periods and compare its notebook ID. Reassign the leadership reviewer and verify that the former and current reviewers see the correct actions. Test grades that are editable, viewable and released as separate states."),
    ],
    "uni360": [
        ("How the academic structure works", "A faculty contains majors and departments. Majors contain programs, departments own courses, and a course can serve multiple programs. Cohorts group students, while course sections carry the lecturer assignment, schedule and term registration."),
        ("Create the section before enrollment", "Academic affairs configures the semester, lecturer, capacity and enrollment mode. There are fixed-schedule and self-paced section formats. For admin-created sections, the admin controls section configuration and the lecturer controls learning content inside it."),
        ("Assigned enrollment and self-registration", "Assigned enrollment brings students in from a cohort. Self-registration lets the student request an open section. The specification checks eligibility, prerequisites, scheduling and registration deadline. Its waitlist design handles capacity and promotes a waiting student when a place becomes available."),
        ("The data model behind the UI", "Cohort membership and section enrollment are separate relationships. Enrollment is unique per student and course section. Tests therefore attach to a particular request and can verify whether the result is blocked, enrolled or waitlisted."),
    ],
    "lms360": [
        ("What the learning workspace does", "The LMS360 designs include the homepage, online learning, teacher setup and student practice views. This case shows how the speaking-practice experience connects the teacher’s setup to the student’s activity."),
        ("Two modes in the speaking-practice flow", "A student reads a supplied passage or speaks freely about a topic. Usage guidance and activity cards orient the student before selecting an exercise. Teacher-facing frames separate setting up the exercise from completing it."),
        ("A separate admissions workstream", "The placement brief defines the request owner, banner or popup format, location, mobile and desktop dimensions, display window and destination. The measurement requirements distinguish impressions, clicks and qualified leads, so each approved format can be tested against its expected action."),
    ],
    "elib360": [
        ("What the catalogue organizes", "The library source describes searchable materials across education levels, school-only resources, community materials and interactive resources that link into LMS360."),
        ("How advanced search behaves", "New curriculum is the default. Subject and textbook series depend on curriculum, and grade depends on education level. The overlay therefore needs to update dependent values when a parent selector changes and remove invalid selections."),
        ("Separate browsing, permission and contribution", "The design applies school-account access at the resource boundary. The proposal also distinguishes moderation for a later community registration path from the rules for school-issued accounts."),
    ],
    "test360": [
        ("From assessment attempt to gradebook", "The Figma page contains teacher grading sessions, student result details and transfer to the gradebook. The student’s attempt and the teacher’s grade synchronization sit in distinct views."),
        ("Review conversion before synchronizing", "The teacher chooses the term, target column, subject, score-selection method and rounding. The grid displays source and converted scores before the sync action. Validation can compare different methods and rounding against the same inputs and verify the mapped destination."),
    ],
}
