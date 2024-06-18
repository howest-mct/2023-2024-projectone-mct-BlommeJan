addEventListener('DOMContentLoaded', () => {
    console.log("DOM loaded")
    const cocktails = document.querySelector(".js-cocktails")

    let Content = ""
    handleData(`http://${lanIP}/api/v1/cocktails/`, (resp) => {
        console.log(resp)
        
        for (const cocktail of resp) {
            content =+ 
                `
                <div class="c-cocktails__cocktail">
                  <img src="pictures/Cocktails/${cocktail["strPicture"]}" alt="Martini cocktail" class="c-cocktails__cocktail__img">
                  <div class="c-cocktails__cocktail__info">
                    <h2 class="c-cocktails__cocktail__info__name" class="c-cocktails__cocktail__info__name">Martini</h2>
                    <div class="c-cocktails__cocktail__info__text">
                      <div class="c-cocktails__cocktail__info__text__categories">
                        <span class="c-cocktails__cocktail__info__text__categories__isAlcohol">Alcoholic</span>
                        <img src="pictures/Icons/Cocktail.svg" alt="icon cocktail" class="c-cocktails__cocktail__info__text__categories__categoryIcon u-bigIcon">
                      </div>
                      <div class="c-cocktails__cocktail__info__text__ingredients">
                        <ul class="c-cocktails__cocktail__info__text__ingredients__list u-noLiStyle">
                          <li class="c-cocktails__cocktail__info__text__ingredients__list__item">Gin</li>
                          <li class="c-cocktails__cocktail__info__text__ingredients__list__item">Dry vermouth</li>
                          <li class="c-cocktails__cocktail__info__text__ingredients__list__item">Olives</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
                `
        }
        cocktails.innerHTML = content
        
    })

});