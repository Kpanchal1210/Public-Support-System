document.addEventListener("DOMContentLoaded", function () {

    const buttons = document.querySelectorAll(".filter-buttons button");
    const rows = document.querySelectorAll(".issue-row");

    buttons.forEach(button => {
        button.addEventListener("click", function () {

            // remove active from all
            buttons.forEach(btn => btn.classList.remove("active"));

            // add active to clicked
            this.classList.add("active");

            const type = this.innerText.toLowerCase().replace(" ", "_");

            rows.forEach(row => {

                if (type === "all") {
                    row.style.display = "";
                } 
                else if (type === "escalated") {
                    row.style.display = row.classList.contains("escalated") ? "" : "none";
                } 
                else {
                    row.style.display = row.classList.contains(type) ? "" : "none";
                }

            });

        });
    });

});