function openImage(src){

    const modal = document.getElementById("imageModal");

    document.getElementById("modalImg").src = src;

    modal.classList.add("show");
}

function closeImage(){

    document.getElementById("imageModal")
            .classList.remove("show");
}

document.addEventListener("DOMContentLoaded", () => {

    const modal = document.getElementById("imageModal");

    modal.addEventListener("click", (e) => {

        if(e.target === modal){

            closeImage();
        }
    });

});