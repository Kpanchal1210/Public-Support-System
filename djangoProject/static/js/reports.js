function setCategory(category) {

    const categoryField = document.getElementById("id_issue_type");
    const formSection = document.getElementById("formSection");

    if (categoryField) {
        categoryField.value = category;
    }

    if (formSection) {
        formSection.classList.add("active");

        formSection.scrollIntoView({
            behavior: "smooth"
        });
    }

    if (title) {
        title.innerText = category + " Complaint";
    }
}