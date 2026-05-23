function setCategory(category){

    const categoryField =
        document.getElementById("id_issue_type");

    const formSection =
        document.getElementById("formSection");

    const title =
        document.getElementById("deptTitle");


    /* SET CATEGORY */

    if(categoryField){

        categoryField.value = category;
    }


    /* SHOW FORM */

    if(formSection){

        formSection.classList.add("active");

        formSection.scrollIntoView({

            behavior:"smooth"

        });
    }


    /* UPDATE TITLE */

    if(title){

        const formattedCategory =

            category.charAt(0).toUpperCase() +
            category.slice(1);

        title.innerText =
            formattedCategory + " Complaint";
    }
}



/* TOGGLE EXTRA DEPARTMENTS */

function toggleDepartments(){

    const extraDepartments =
        document.getElementById("extraDepartments");

    const moreText =
        document.getElementById("moreText");

    extraDepartments.classList.toggle("active");


    if(extraDepartments.classList.contains("active")){

        moreText.innerHTML =
            "➖ Show Less";

    }else{

        moreText.innerHTML =
            "➕ More Services";
    }
}



/* SEARCH FILTER */

const searchInput =
    document.getElementById("deptSearch");


searchInput.addEventListener("keyup", function(){

    const searchValue =
        this.value.toLowerCase();

    const panels =
        document.querySelectorAll(".dept-panel");


    panels.forEach(panel => {

        const text =
            panel.innerText.toLowerCase();


        if(text.includes(searchValue)){

            panel.style.display = "flex";

        }else{

            panel.style.display = "none";
        }

    });

});



/* SUCCESS TOAST */

const form =
    document.querySelector("form");


form.addEventListener("submit", function(e){

    e.preventDefault();

    const toast =
        document.getElementById("successToast");


    toast.classList.add("show");


    setTimeout(() => {

        toast.classList.remove("show");

        form.submit();

    }, 2200);

});