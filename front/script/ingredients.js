document.addEventListener('DOMContentLoaded', () => {
    const btnElement = document.querySelector(".js-start-btn")

    btnElement.addEventListener("click", () => {
        const ingredient1 = document.getElementById("ingredient1").value
        const ingredient2 = document.getElementById("ingredient2").value
        const ingredient3 = document.getElementById("ingredient3").value
        const ingredient4 = document.getElementById("ingredient4").value

        handleData(`http://${lanIP}/api/v1/update-ingredients`, (resp) => {}, null, "POST", {
            ingredient1, ingredient2, ingredient3, ingredient4
        })
    })
});