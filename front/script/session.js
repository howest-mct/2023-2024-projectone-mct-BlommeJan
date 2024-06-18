socketio.on("BTF_temp", (body) => {
    const tempElement = document.querySelector(".js-temp")

    tempElement.innerHTML = `${body.temp}°C`
})

document.addEventListener('DOMContentLoaded', () => {
    console.log("DOM loaded")
    const historyTable = document.querySelector(".js-history-table")

    let historyContent = ""
    handleData(`http://${lanIP}/api/v1/history/`, (resp) => {
        console.log(resp)
        historyContent =+ `
        <tr class="c-session__hist__history__table__table__head">
            <th class="c-session__hist__history__table__table__head__header">Cocktail</th>
            <th class="c-session__hist__history__table__table__head__header">Date</th>
        </tr>
        `

        for (const history of resp) {
            console.log(history["strDrink"])
            historyContent += `
            <tr class="c-session__hist__history__table__table__row">
                <td class="c-session__hist__history__table__table__row__data">${history["strDrink"]}</td>
                <td class="c-session__hist__history__table__table__row__data">${history["dateTime"]}</td>
            </tr>
            `
        }
        historyTable.innerHTML = historyContent
    })

});

