from html import escape
from evidence import COMPONENTS

SRS = [
    ("HR-01", "Class notebook identity", "On first authorized access, open or create one notebook for the class and academic year using the school-level template.", "Open the same class in Term 1 and Term 2. The notebook ID is unchanged."),
    ("HR-02", "Notebook list", "Filter the school’s notebook list by grade and class. Show the teacher, enrollment, completion and assigned reviewer beside each row.", "With no classes in the selected scope, show an empty state. A failed refresh must be distinguishable from an empty result."),
    ("HR-03", "Role and section access", "Allow school administrators to manage their school’s notebooks. An assigned homeroom teacher edits their class record except the leadership comments. An assigned reviewer edits the leadership section.", "Reassign the teacher. The old teacher loses edit access and the new teacher gains it without recreating the notebook."),
    ("HR-04", "Page loading and export", "Load the section being reviewed. Produce the notebook using the saved data and selected school-level template.", "Open a term review and export the record after saving. Both use the same class-year record."),
    ("HR-05", "Change audit", "Record saved notebook changes with the relevant record, acting user and time. Keep the audit available to authorized operations staff.", "Save a notebook edit and reconcile the resulting audit with the selected record and actor."),
    ("GV-01", "School-term toggle", "Only an authorized school administrator can change the average-column policy. The first release applies one policy per school, academic year and semester.", "An administrator saves for Term 2. Term 1 and other schools retain their existing policy."),
    ("GV-02", "Effective policy", "Show the average when configuration is missing or inactive. An active configuration with the visibility flag off hides it.", "Exercise missing, inactive, active/show and active/hide configurations in both channels."),
    ("GV-03", "Audience and payload", "Resolve visibility on the backend for web and mobile. When hidden, suppress the average from the audience’s score response.", "Confirm the average is absent or null under the agreed response contract, and hidden in both interfaces."),
    ("GV-04", "Grade-policy audit", "Record a create or update with before/after snapshots, the acting administrator, timestamp and channel.", "Compare the current setting to the latest audit event after a web change and a mobile change."),
]

ROLES = [
    ("School administrator", "All classes in their school", "Manage notebook access and assign reviewers"),
    ("Principal", "All classes in their school", "Review access"),
    ("Assigned homeroom teacher", "Assigned class", "Edit eligible sections and view leadership comments"),
    ("Assigned reviewer", "Assigned notebook", "Edit the leadership comments section"),
]

SCHEMA = [
    ("Class", "class_id", "school_id", "Provides the notebook’s school scope."),
    ("Academic year", "academic_year_id", "school context", "Provides the year dimension. One year can contain several terms."),
    ("Homeroom notebook", "notebook_id", "class_id + academic_year_id", "Unique pair. The selected term never creates a new notebook."),
    ("Notebook section data", "section_record_id", "notebook_id", "Child data for reports, plans and other sections. Term-specific content can carry a reporting checkpoint."),
    ("Notebook authorization", "assignment_id", "notebook_id, user_id, access role", "Links a user to the notebook with page-level access rules."),
    ("Notebook audit", "event_id", "notebook_id, actor_id", "Stores operation, time and a change snapshot."),
    ("Grade visibility policy", "configuration_id", "school_id + academic_year_id + semester_id", "Unique policy tuple. Status and JSON flag determine the effective visibility."),
    ("Grade policy audit", "event_id", "configuration_id, actor_id", "Stores operation, before/after snapshot, time and source channel."),
]

API = [
    ("GET /example/grade-visibility", "School administrator", "Read active configuration and the effective visibility for the selected term."),
    ("POST /example/grade-visibility", "School administrator", "Validate the school-term scope, upsert settings and record a CREATE or UPDATE audit event."),
    ("GET /example/scores", "Authorized score viewer", "Resolve the effective policy and project the appropriate score fields for the audience."),
]

DECISION = [
    ("No configuration", "—", "Visible", "Default applies"),
    ("Configuration inactive", "Either value", "Visible", "Default applies"),
    ("Configuration active", "True", "Visible", "Return average"),
    ("Configuration active", "False", "Hidden", "Suppress average in the score response"),
]

ACCEPTANCE = [
    ("GV-01", "UAT-GV-01", "Admin saves Term 2 as hidden", "Only the Term 2 school policy changes."),
    ("GV-01", "UAT-GV-02", "A teacher attempts to change the policy", "Request is denied and the saved policy is unchanged."),
    ("GV-02", "UAT-GV-03", "No active configuration is found", "Average remains visible."),
    ("GV-03", "UAT-GV-04", "Active hide policy on web and mobile", "Average is hidden in both channels and absent/null in the agreed score response."),
    ("GV-04", "UAT-GV-05", "Admin creates and then updates a policy", "Both events identify the actor, time and client channel."),
    ("HR-01", "UAT-HR-01", "Switch reporting checkpoints in one academic year", "Both checkpoints resolve to the same notebook."),
    ("HR-03", "UAT-HR-02", "Reviewer opens final comments; assigned teacher opens same section", "Reviewer can edit comments. The teacher can read them."),
]

API_JSON = '''{
  "academicYear": "YEAR-DEMO",
  "semester": "TERM-2",
  "active": true,
  "showAverage": false
}'''

SCORE_JSON = '''{
  "studentRef": "STUDENT-DEMO",
  "subjectRef": "SUBJECT-DEMO",
  "componentScores": [8, 7, 9]
}'''

AUDIT_JSON = '''{
  "operation": "UPDATE",
  "actorRef": "ADMIN-DEMO",
  "channel": "WEB",
  "occurredAt": "2026-01-15T18:00:00Z",
  "before": {"active": true, "showAverage": true},
  "after":  {"active": true, "showAverage": false}
}'''


def table(headers, rows):
    head = "".join(f'<th scope="col">{escape(h)}</th>' for h in headers)
    body = "".join("<tr>"+"".join(f"<td>{escape(c)}</td>" for c in row)+"</tr>" for row in rows)
    return f'<div class="table-scroll" tabindex="0" role="region" aria-label="{escape(headers[0], quote=True)} table"><table class="artifact-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def sample_figure(asset, title, description, *, asset_path="../assets/", new_tab=False):
    source = asset_path + asset
    target = (
        f' target="_blank" rel="noopener noreferrer" aria-label="Open full-size image of {escape(title, quote=True)}"'
        if new_tab else ""
    )
    return (f'<figure class="artifact-figure"><a href="{source}"{target}>'
            f'<img src="{source}" alt="{escape(title, quote=True)}" loading="lazy"></a>'
            f'<figcaption><strong>{escape(title)}</strong><p>{escape(description)}</p></figcaption></figure>')


def section(id_, title, body):
    return f'<section class="artifact-section" id="{id_}"><h2>{escape(title)}</h2>{body}</section>'


def code_example(title, code):
    return f'<div class="code-example"><h3>{escape(title)}</h3><pre><code>{escape(code)}</code></pre></div>'


def sms_artifacts():
    return """
<section class="artifact-section" id="work-samples">
  <h2>Read the work samples</h2>
  <p>The English samples use fictional records and renamed API routes. They illustrate how the requirements, design, data model and test cases connect.</p>
  <div class="artifact-grid">
    <a class="artifact-tile" href="sms360-db-api.html"><strong>DB &amp; API workbook</strong><span>144-feature index with selected field-level database and API examples.</span><b>Browse or download →</b></a>
    <a class="artifact-tile" href="sms360-srs.html"><strong>Software requirements</strong><span>Screen-level fields, access rules and acceptance criteria.</span><b>Read SRS →</b></a>
    <a class="artifact-tile" href="sms360-data-model.html"><strong>Database specification</strong><span>Entity relationships, identifiers, uniqueness and access.</span><b>Read database spec →</b></a>
    <a class="artifact-tile" href="sms360-api.html"><strong>REST API specification</strong><span>Contract examples, default logic, audit and errors.</span><b>Read API spec →</b></a>
  </div>
</section>
""" + section("business-rules", "How a school’s policy determines grade visibility",
              sample_figure("sms-grade-flow.svg", "SMS360 grade visibility flow",
                            "The API resolves the effective school-term policy. Missing and inactive configurations take the visible-by-default path.") +
              table(("Configuration status", "Show-average flag", "Effective result", "Score response"), DECISION)) + section(
              "traceability", "Requirements-to-UAT traceability",
              "<p>These UAT cases show how each rule can be checked. The IDs are for this portfolio sample.</p>"+
              table(("Requirement", "Test", "Scenario", "Expected outcome"), ACCEPTANCE))


DOCS = {
    "sms360-srs": (
        "Software requirements specification",
        "Homeroom notebook and school-wide average-score visibility.",
        lambda: (
            section("scope", "Scope and users",
                "<p>Homeroom teachers maintain one record across several checkpoints. School administrators configure access and review. School leaders review or sign the final section according to their assignment. The electronic gradebook also needed a school-wide control for incomplete averages.</p>") +
            section("permissions", "Notebook permissions", table(("Role", "Row scope", "Allowed actions"), ROLES)) +
            section("fields", "Homeroom notebook list · screen specification", table(
                ("UI element", "Source", "Behaviour"), [
                    ("Grade and class filters", "School class register", "Limit results to the selected scope and retain the academic-year context."),
                    ("Class", "Class register", "Display class name and open the associated notebook on View details."),
                    ("Class enrollment", "Current class roster", "Display the current class enrollment count."),
                    ("Homeroom teacher", "Staff assignment", "Show the assigned teacher and reflect any assignment changes."),
                    ("Completion and reviewer", "Notebook state and reviewer assignment", "Show status and assigned leadership reviewer for each class."),
                    ("Download / Export", "Class-year notebook and export template", "Make export available within the user’s role and class scope."),
                ])) +
            section("functional", "Functional requirements and acceptance criteria", table(
                ("ID", "Requirement", "System behaviour", "Acceptance check"), SRS)) +
            section("quality", "Quality requirements", "<ul><li>Load notebook sections on demand.</li><li>Keep edits scoped to the authorized school and class.</li><li>Distinguish an empty result from a processing failure and preserve saved state on a failed update.</li></ul>")
        )
    ),
    "sms360-data-model": (
        "Database specification",
        "Why a notebook belongs to a class and academic year, and how a grade policy belongs to a particular semester.",
        lambda: (
            section("erd", "Logical entity relationships", sample_figure(
                "sms-notebook-erd.svg", "Homeroom notebook entity relationship diagram",
                "A class and academic year resolve to one notebook. Reporting sections, reviewer assignments and audit events attach to that notebook.")) +
            section("dictionary", "Data dictionary", table(("Entity", "Primary key", "Scope or foreign keys", "Rule"), SCHEMA)) +
            section("lifecycle", "Record lifecycle and constraints",
                "<ul><li>On first notebook access, resolve the school-scoped class and year, then create or return the existing notebook under the class-year uniqueness constraint.</li><li>The term selection determines the reporting content. The class-year key continues to resolve the same notebook.</li><li>Selector fields and identities originate in the school’s academic data. Existing notebook history remains associated with the original record.</li><li>Notebook and grade-policy changes have separate audit trails because their scopes and payloads differ.</li></ul>") +
            section("validation", "SQL validation sample", "<p>This sample checks the class-year invariant on the illustrative schema.</p>"+code_example("Duplicate notebook check",
                "SELECT class_id, academic_year_id, COUNT(*) AS notebook_count\nFROM homeroom_notebook\nGROUP BY class_id, academic_year_id\nHAVING COUNT(*) > 1;"))
        )
    ),
    "sms360-api": (
        "REST API specification",
        "Manage the term’s grade-visibility rule and apply it consistently to the score response.",
        lambda: (
            section("operations", "Operations", "<p>Routes and JSON fields below are representative. School scope is resolved from authenticated context and term parameters are validated against that school.</p>"+
                table(("Operation", "Authorized caller", "Purpose"), API)) +
            section("contract", "Representative request, response and audit", '<div class="code-grid">'+code_example("Save grade visibility · request",API_JSON)+code_example("Hidden average · score response", SCORE_JSON)+code_example("Policy update · audit record", AUDIT_JSON)+"</div>") +
            section("decision", "Rule resolution", table(("Configuration", "Visibility flag", "Effective result", "Payload rule"), DECISION)) +
            section("responses", "Response and error examples", table(
                ("Scenario", "Illustrative response", "Consumer action"), [
                    ("Valid read or update", "200 OK", "Apply the effective visibility returned for the selected term."),
                    ("Missing or invalid term data", "400 Bad Request", "Identify the invalid field. Preserve the previous setting."),
                    ("Session missing or invalid", "401 Unauthorized", "Authenticate before retrieving protected data."),
                    ("Role or school scope fails validation", "403 Forbidden", "Reject the update without writing a configuration."),
                    ("Temporary service failure", "5xx", "Keep the last confirmed configuration and surface a retry path."),
                ])) +
            section("audit", "Verification and diagnosis", "<p>For a saved change, reconcile school, academic year, semester, actor and client channel with the audit event. When diagnosing a missing conduct score, I treated the successful HTTP status separately from the empty JSON result, then identified the required score-copy step described in the response.</p>")
        )
    ),
}

GALLERIES = {
    "sms360": [
        ("Homeroom workspace", [
            ("sms-homeroom-records-en.svg", "Class notebook list", "Grade filtering sits above the class table, with distinct actions for opening a notebook and downloading its template."),
            ("sms-reviewer-assignments-en.svg", "Leadership reviewer assignment", "The grade-wide control and class-level selectors apply the same assignment pattern at different scopes."),
        ]),
        ("Component library", [
            ("sms-button-source-en.webp", "Complete button set · Figma capture", "The original eight variants are shown together. The four text labels have been translated to English."),
            ("sms-action-family-en.svg", "Button properties and icon combinations", "The set combines four types with default and disabled states. Leading and trailing icons are controlled separately."),
            ("sms-input-source-en.webp", "Complete input set · Figma capture", "Large and small inputs are shown in default, disabled and special states. Field labels and validation text are translated into English."),
            ("sms-forms-dialogs-en.svg", "Forms and dialogs", "Date fields, selectors and role-sensitive editing support two school administration tasks."),
            ("sms-navigation-family-en.svg", "Header, tabs and role menus", "Three header variants and a two-state tab component serve administrator, teacher and student workspaces."),
            ("sms-page-templates-en.svg", "Reusable page templates", "Form, record and list structures use a shared page shell and maintain context as the user moves between tasks."),
            ("sms-error-templates-en.svg", "Error and recovery templates", "403, 404 and 500 are distinct states. Each message tells users what they can do next."),
        ]),
    ],
    "uni360": [
        ("Academic operations", [
            ("uni-course-section-variants-en.svg", "Course-section form variants", "The form layout distinguishes both create and edit variants and shows which registration controls depend on the selected mode."),
            ("uni-cohort-operations-en.svg", "Cohort records and related tabs", "The class list and detail wireframes keep cohort membership, program, intake and lecturer information easy to locate."),
        ]),
    ],
    "elib360": [
        ("Resource discovery", [
            ("elib-advanced-search-en.svg", "Advanced search overlay", "Two levels of dependent filters make the relationship between curriculum, subject, textbook series, education level and grade visible."),
            ("elib-results-access-en.svg", "Resource cards and school access", "Resource cards preserve browsing context. Restricted items prompt users for school access on opening."),
        ]),
    ],
    "lms360": [
        ("Teacher and learner workspaces", [
            ("lms-teacher-learning-topics-en.svg", "Teacher topic and material list", "Grade and subject filtering, material actions and review counts in the teacher’s workspace. Sample rows use fictional data."),
            ("lms-speaking-mode-frames-en.svg", "Speaking-practice setup and learner cards", "The teacher’s selected activity type determines whether learners see a passage or topic. The cards and guidance set expectations before recording."),
        ]),
    ],
    "test360": [
        ("Grading and synchronization", [
            ("test-grading-session-en.svg", "Grading-session setup and results", "The grading session identifies the assessment and class before the teacher reviews individual scores."),
            ("test-score-sync-preview-en.svg", "Score synchronization preview", "The teacher checks five mapping controls and compares source and converted scores before committing. The sample uses fictional student data."),
        ]),
    ],
    "whitestone": [
        ("Components and prototype", [
            ("white-components.webp", "Shared component board", "The original design export groups actions, inputs, status indicators and navigation."),
            ("white-component-details.webp", "Navigation and result components", "A closer look at navigation, the severity indicator and the expandable recommendation in light and dark variants."),
            ("white-style.webp", "Visual variations", "The board explores different colour treatments and their application across common screens."),
            ("white-wireframes.webp", "Wireframe alternatives", "Several structures helped the team review the steps before progressing to the high-fidelity design."),
            ("white-results.webp", "High-fidelity prototype", "Two versions of the complete path from onboarding to scanning and results."),
            ("white-result-states.webp", "Loading, result and detail states", "Three adjacent states show how the product moves from processing to the result summary and supporting guidance."),
        ]),
        ("Results screen close-ups", [
            ("white-figma-results-summary.webp", "Results summary · Figma capture", "Severity labels and grouped findings help users understand the scan before opening a detail."),
            ("white-figma-results-detail.webp", "Expanded finding · Figma capture", "Opening a finding highlights the corresponding area and reveals guidance with a link to read more."),
        ]),
    ],
    "heathelp": [
        ("Wireframes, components and implementation", [
            ("heat-lowfi.webp", "Low-fidelity mockups", "The team laid out screens and navigation before refining the visual style."),
            ("heat-hifi.webp", "High-fidelity prototype", "The flow branches between learning content and topic quizzes."),
            ("heat-topic-choice.webp", "Activity chooser and learning cards", "A detail view shows the quiz entry points and the adjacent expandable topic content."),
            ("heat-progress.webp", "Progress indicator", "The component gives learners a consistent signal of where they are in the quiz."),
            ("heat-buttons.webp", "Button and feedback components", "The design library groups quiz selection, correct and incorrect feedback, and the continue action."),
            ("heat-final.webp", "Implemented experience", "The product homepage reflects the navigation and activity choices explored in the mockups."),
        ]),
    ],
}


def design_gallery(project_id, figma_sources):
    groups = GALLERIES[project_id]
    localized = project_id in {"sms360", "uni360", "elib360", "lms360", "test360"}
    context = (
        '<p class="sample-note">The images below include English translations and annotated adaptations of the Figma layouts. The sample screens use fictional records. '
        'The original design files contain the complete collections and prototype details.</p>'
        if localized else ""
    )
    galleries = []
    for title, entries in groups:
        figures = "".join(sample_figure(*entry, new_tab=True) for entry in entries)
        galleries.append(f'<h3>{escape(title)}</h3><div class="gallery">{figures}</div>')
    pattern_table = table(("Figma pattern", "What the source shows", "Handoff decision"), COMPONENTS[project_id])
    return section("design-evidence", "Figma designs and handoff", figma_sources + context + "".join(galleries) + pattern_table)


def case_extras(project_id, figma_sources=""):
    gallery_html = design_gallery(project_id, figma_sources) if project_id in GALLERIES else ""
    if project_id == "sms360":
        return (gallery_html + sms_artifacts() +
                section("homeroom-flow", "BPMN · a homeroom notebook across the school year",
                        sample_figure("sms-homeroom-bpmn.svg", "School Admin, SMS360, Homeroom teacher and Assigned leadership swimlanes",
                                      "Models the relationship between notebook creation (SMS-08-01), reviewer assignment (SMS-08-02), final comments (SMS-08-11) and checkpoint reviews (SMS-08-21).")) +
                section("uml-sequence", "UML sequence · saving a school policy",
                        sample_figure("sms-policy-sequence.svg", "UML sequence for an authorized or denied update",
                                      "The client sends one scoped update. The validated path saves the policy and audit. The rejected path preserves the confirmed state.")) +
                section("notebook-erd", "ERD · preserving notebook identity",
                        sample_figure("sms-notebook-erd.svg", "Class-year notebook ERD",
                                      "Link the notebook to the class and year. Relate reporting content, authorizations and changes to the notebook.")))
    if project_id == "uni360":
        return (gallery_html + section("registration-bpmn", "BPMN · cohort assignment and self-registration",
                                      sample_figure("uni-registration-bpmn.svg", "Academic Affairs, student and UNI360 swimlanes",
                                                    "The registration mode determines the entry path. Self-registration checks active status, timing, prerequisites and schedule. Where the waitlist applies, an eligible student can queue for a seat.")) +
                section("enrollment-erd", "ERD · cohort membership and section enrollment",
                        sample_figure("uni-enrollment-erd.svg", "Logical enrollment data model",
                                      "A cohort class groups students over time. Enrollment records connect students to scheduled course sections.") ) +
                section("uat", "UAT · registration decisions", table(("Scenario", "Rule verified", "Expected"), [
                    ("Prerequisite unfinished", "Required prior course", "Block request and identify the missing prerequisite."),
                    ("Section full", "Capacity and waitlist", "Queue the eligible student where the waitlist applies."),
                    ("Seat becomes available", "Waitlist promotion", "Promote the next eligible student per waitlist order."),
                    ("Schedule overlaps", "Timetable validation", "Block request and explain the conflict."),
                    ("Checks pass", "Valid section and eligibility", "Create enrollment and show a confirmation."),
                ])))
    if project_id == "elib360":
        return gallery_html + section("catalog-flow", "Workflow · search and resource access",
                                      sample_figure("elib-search-flow.svg", "Dependent filters and the school-only access rule",
                                                    "Curriculum drives subject and series, education level drives grade, and resource scope determines whether school access is needed.")) + section("filter-rules", "Search and access rules", table(("Trigger", "Rule", "Result"), [
            ("Change curriculum", "Subject and series follow the selected curriculum.", "Refresh dependent options and clear inapplicable selections."),
            ("Open school-only material", "Access depends on the associated school account.", "Require school sign-in if necessary."),
            ("Open linked interactive resource", "The learning platform owns the experience.", "Follow the resource to LMS360."),
        ]))
    if project_id == "lms360":
        return gallery_html + section("speaking-flow", "Workflow · teacher setup to student practice",
                                      sample_figure("lms-speaking-flow.svg", "Speaking-practice setup and the two learner paths",
                                                    "The activity type determines whether teachers supply a passage or a topic and what the learner sees before practice.")) + section("requirements", "Campaign placement handoff", table(("Input", "Review question", "Acceptance check"), [
            ("Placement and device", "Which template is approved for this surface and device?", "Validate banner or pop-up rendering for each target."),
            ("Campaign destination", "Where should the approved placement send prospective learners?", "Verify the same approved destination from each applicable surface."),
            ("Publish and review", "Which stakeholder provides the content and who confirms placement?", "Compare the published placement to the approved request."),
        ]))
    if project_id == "test360":
        return gallery_html + section("score-flow", "Workflow · review and synchronize converted scores",
                                      sample_figure("test-score-flow.svg", "Grading context, score destination and preview",
                                                    "The preview lets the teacher check target term, subject and column alongside the effect of calculation and rounding before synchronization."))
    return gallery_html
