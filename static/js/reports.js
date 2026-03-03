function setCategory(category) {
    const categoryField = document.getElementById("id_issue_type");
    const formSection = document.getElementById("formSection");
    const title = document.getElementById("deptTitle");

    categoryField.value = category;

    formSection.classList.add("active");

    title.innerText = category + " Complaint";

    formSection.scrollIntoView({
        behavior: "smooth"
    });
}