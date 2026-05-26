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

/* SUCCESS TOAST */

document.addEventListener("DOMContentLoaded", function () {

    const form =
        document.querySelector("form");

    const toast =
        document.getElementById("successToast");


    form.addEventListener("submit", function(e){

        if(!form.checkValidity()){

            return;
        }

        e.preventDefault();

        toast.classList.add("show");


        setTimeout(() => {

            toast.classList.remove("show");

            form.submit();

        }, 2200);

    });

});