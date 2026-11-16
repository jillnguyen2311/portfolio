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
