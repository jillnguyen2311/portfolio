const filters = [...document.querySelectorAll("[data-filter]")];
const projects = [...document.querySelectorAll("[data-category]")];
const status = document.querySelector("#project-count");

filters.forEach((button) => {
  button.addEventListener("click", () => {
    const category = button.dataset.filter;
    filters.forEach((filter) => {
      filter.setAttribute("aria-pressed", String(filter === button));
    });
    let count = 0;
    projects.forEach((project) => {
      project.hidden = category !== "all" && !project.dataset.category.split(" ").includes(category);
      if (!project.hidden) count += 1;
    });
    status.textContent = `${count} ${count === 1 ? "project" : "projects"} shown`;
  });
});

const variantLab = document.querySelector("[data-variant-lab]");
if (variantLab) {
  const control = (id) => variantLab.querySelector(`#${id}`);
  const buttonType = control("lab-button-type");
  const buttonState = control("lab-button-state");
  const iconControls = control("lab-button-icons");
  const leading = control("lab-leading-icon");
  const trailing = control("lab-trailing-icon");
  const sampleButton = control("lab-button-preview");
  const buttonResult = control("lab-button-result");
  const inputSize = control("lab-input-size");
  const inputState = control("lab-input-state");
  const inputHeader = control("lab-input-header");
  const inputIcon = control("lab-input-icon");
  const messageBelow = control("lab-input-message-below");
  const inputClear = control("lab-input-clear");
  const sampleInput = control("lab-input-preview");
  const inputLabel = control("lab-input-label");
  const inputIconPreview = control("lab-input-icon-preview");
  const clearPreview = control("lab-input-clear-preview");
  const inputError = control("lab-input-error");
  const inlineError = control("lab-input-inline-error");
  const inputResult = control("lab-input-result");
  const iconOnly = { open: ["+", "Open"], close: ["−", "Close"] };

  function previewButton() {
    const type = buttonType.value;
    const icon = iconOnly[type];
    iconControls.disabled = Boolean(icon);
    sampleButton.dataset.kind = type;
    sampleButton.disabled = buttonState.value === "disabled";
    sampleButton.textContent = icon ? icon[0] : `${leading.checked ? "+ " : ""}Continue${trailing.checked ? " →" : ""}`;
    sampleButton.setAttribute("aria-label", icon ? icon[1] : "Continue");
    buttonResult.textContent = sampleButton.disabled ? "The disabled button blocks activation." : "The default button accepts activation.";
  }

  function previewInput() {
    const invalid = inputState.value === "special";
    sampleInput.dataset.size = inputSize.value;
    sampleInput.disabled = inputState.value === "disabled";
    sampleInput.setAttribute("aria-invalid", String(invalid));
    inputLabel.hidden = !inputHeader.checked;
    inputIconPreview.hidden = !inputIcon.checked;
    inputIconPreview.textContent = inputSize.value === "small" ? "↕" : "◉";
    clearPreview.hidden = !inputClear.checked;
    clearPreview.disabled = sampleInput.disabled;
    inputError.hidden = !invalid || !messageBelow.checked;
    inlineError.hidden = !invalid || messageBelow.checked;
    if (invalid) sampleInput.setAttribute("aria-describedby", (messageBelow.checked ? inputError : inlineError).id);
    else sampleInput.removeAttribute("aria-describedby");
    const messages = {
      default: "The default field accepts text input.",
      disabled: "The disabled field blocks editing.",
      special: "The validation state identifies the problem and describes how to correct it."
    };
    inputResult.textContent = messages[inputState.value];
  }

  [buttonType, buttonState, leading, trailing].forEach((input) => input.addEventListener("change", previewButton));
  [inputSize, inputState, inputHeader, inputIcon, messageBelow, inputClear].forEach((input) => input.addEventListener("change", previewInput));
  sampleButton.addEventListener("click", () => {
    buttonResult.textContent = `${sampleButton.getAttribute("aria-label")} activated in the preview.`;
  });
  clearPreview.addEventListener("click", () => {
    sampleInput.value = "";
    sampleInput.focus();
    inputResult.textContent = "The sample value was cleared.";
  });
  previewButton();
  previewInput();
}
