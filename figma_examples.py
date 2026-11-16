"""Interactive English examples of the component behaviour shown in the Figma evidence."""

from html import escape


def panel(title, body, tone=""):
    return f'<div class="example-panel {tone}"><h4>{title}</h4>{body}</div>'


def field_preview(label, value):
    return f'<div class="example-field"><strong>{label}</strong><span>{value}</span></div>'


def score_preview(value, display):
    return f'<dl class="example-fields"><dt>Source score</dt><dd>{value}</dd><dt>Preview score</dt><dd>{display}</dd></dl>'


def resource_list(items):
    return '<ol>' + "".join(f"<li>{item}</li>" for item in items) + "</ol>"


EXAMPLES = {
    "sms360": (
        "Notification variants",
        "Compare the feedback after deleting an item. Both variants identify the outcome in text.",
        (
            ("Success", panel("Deleted successfully.", "<p>The item is removed from the list.</p>", "is-success")),
            ("Failure", panel("Deletion failed. Please try again.", "<p>The item stays in the list so the user can retry.</p>", "is-error")),
        ),
    ),
    "uni360": (
        "Conditional form fields",
        "Switch enrollment modes to see which configuration the course-section form needs.",
        (
            ("Self-registration", panel("Registration window",
                field_preview("Opens", "September 2 at 9:00 AM")
                + field_preview("Closes", "September 9 at 5:00 PM")
                + '<p>Eligible students select an open section.</p>')),
            ("Assigned enrollment", panel("Cohort assignment",
                field_preview("Cohort class", "Business Administration · Cohort 2026")
                + '<p>Academic affairs assigns the selected cohort to the section.</p>')),
        ),
    ),
    "elib360": (
        "Sort control and selected states",
        "Switch the sort order to rearrange the same set of sample resources.",
        (
            ("Newest", panel("Sorted by newest", resource_list(("Library orientation", "Reading guide", "Study skills workbook")))),
            ("Most viewed", panel("Sorted by views", resource_list(("Study skills workbook", "Library orientation", "Reading guide")))),
            ("Most downloaded", panel("Sorted by downloads", resource_list(("Reading guide", "Study skills workbook", "Library orientation")))),
        ),
    ),
    "lms360": (
        "Speaking activity cards",
        "Switch between the two activity types to see how the learner's instructions and prompt change.",
        (
            ("Read a passage", panel("Read the passage aloud", "<p>Read the provided text before recording.</p>"
                + '<blockquote>Our school library opens at eight. Students can borrow books before class.</blockquote>')),
            ("Speak about a topic", panel("Speak in your own words", "<p>Use the topic as a prompt for your recording.</p>"
                + '<blockquote>Describe a place you like to study. Explain what makes it a good place for you.</blockquote>')),
        ),
    ),
    "test360": (
        "Score conversion preview",
        "Compare rounding choices with a fictional score. The preview shows the effect before synchronization.",
        (
            ("No rounding", panel("Mathematics · Ongoing assessment 1", score_preview("8.26", "8.26"))),
            ("One decimal place", panel("Mathematics · Ongoing assessment 1", score_preview("8.26", "8.3"))),
            ("Whole number", panel("Mathematics · Ongoing assessment 1", score_preview("8.26", "8"))),
        ),
    ),
    "whitestone": (
        "Expandable result details",
        "Compare a compact result row with the detail it reveals. The example uses fictional scan content.",
        (
            ("Summary", panel("Scan finding", '<p class="example-status">Review recommended</p><p>One finding is ready to review.</p>')),
            ("Expanded", panel("Scan finding", '<p class="example-status">Review recommended</p>'
                '<p>The expanded view explains the result and identifies a relevant health resource.</p>'
                '<p><strong>Related resource</strong> · Preparing questions for a dental appointment</p>')),
        ),
    ),
    "heathelp": (
        "Quiz feedback states",
        "Compare the feedback and the next action for a correct answer and an incorrect answer.",
        (
            ("Correct", panel("Correct", '<p>The learner can continue to the next question.</p><p><strong>Next action</strong> · Continue</p>', "is-success")),
            ("Try again", panel("Incorrect", '<p>The learner stays on the same question and can choose another answer.</p>'
                '<p><strong>Next action</strong> · Try again</p>', "is-error")),
        ),
    ),
}


def component_example(project_id):
    title, description, states = EXAMPLES[project_id]
    controls = []
    previews = []
    for index, (label, markup) in enumerate(states, start=1):
        selected = " checked" if index == 1 else ""
        controls.append(
            f'<label><input type="radio" name="example-{project_id}" value="{index}"{selected}>'
            f'<span>{escape(label)}</span></label>'
        )
        previews.append(f'<div class="example-state" data-state="{index}">{markup}</div>')
    return f"""<section class="component-example" id="figma-examples" aria-labelledby="component-example-title">
  <h3 id="component-example-title">Try the Figma component states</h3>
  <p>{escape(description)} This browser example is based on the Figma design.</p>
  <fieldset><legend>{escape(title)}</legend><div class="example-options">{"".join(controls)}</div></fieldset>
  {"".join(previews)}
</section>"""


def design_system_lab():
    return """
<section class="variant-lab" id="design-system-lab" data-variant-lab aria-labelledby="variant-lab-title">
  <h3 id="variant-lab-title">SMS360 design system lab</h3>
  <p>Inspect the button and input properties from the Figma library. Use the controls to see how each choice affects the component in a browser.</p>
  <div class="variant-grid">
    <div class="variant-card">
      <h4>Button variants</h4>
      <p>Four types · Default and disabled · Optional icons on text buttons</p>
      <div class="variant-controls">
        <label>Type
          <select id="lab-button-type">
            <option value="solid">Solid</option><option value="outline">Outline</option>
            <option value="close">Icon · close</option><option value="open">Icon · open</option>
          </select>
        </label>
        <label>State
          <select id="lab-button-state"><option value="default">Default</option><option value="disabled">Disabled</option></select>
        </label>
      </div>
      <fieldset id="lab-button-icons">
        <legend>Icon placement</legend>
        <label><input type="checkbox" id="lab-leading-icon"> Leading icon</label>
        <label><input type="checkbox" id="lab-trailing-icon"> Trailing icon</label>
      </fieldset>
      <div class="variant-stage">
        <button type="button" class="variant-button" id="lab-button-preview" data-kind="solid">Continue</button>
      </div>
      <p id="lab-button-result" class="variant-result" aria-live="polite">The default button accepts activation.</p>
    </div>
    <div class="variant-card">
      <h4>Input variants</h4>
      <p>Large and small · Default, disabled and special states</p>
      <div class="variant-controls">
        <label>Size
          <select id="lab-input-size"><option value="large">Large</option><option value="small">Small</option></select>
        </label>
        <label>State
          <select id="lab-input-state">
            <option value="default">Default</option><option value="disabled">Disabled</option>
            <option value="special">Special · Validation</option>
          </select>
        </label>
      </div>
      <fieldset>
        <legend>Optional input properties</legend>
        <label><input type="checkbox" id="lab-input-header" checked> Field label</label>
        <label><input type="checkbox" id="lab-input-icon" checked> Trailing icon</label>
        <label><input type="checkbox" id="lab-input-message-below" checked> Feedback below field</label>
        <label><input type="checkbox" id="lab-input-clear"> Clear action</label>
      </fieldset>
      <div class="variant-stage variant-input-stage">
        <div class="variant-input-heading">
          <label for="lab-input-preview" id="lab-input-label">Username</label>
          <p id="lab-input-inline-error" class="variant-error" hidden>Enter a valid username.</p>
        </div>
        <div class="variant-input-row">
          <span class="variant-input-shell">
            <input id="lab-input-preview" class="variant-input" type="text" aria-label="Username" placeholder="Enter your username" data-size="large">
            <span id="lab-input-icon-preview" class="variant-input-icon" aria-hidden="true">◉</span>
          </span>
          <button type="button" id="lab-input-clear-preview" class="variant-clear" hidden>Clear</button>
        </div>
        <p id="lab-input-error" class="variant-error" hidden>Enter a valid username.</p>
      </div>
      <p id="lab-input-result" class="variant-result" aria-live="polite">The default field accepts text input.</p>
    </div>
  </div>
</section>"""
