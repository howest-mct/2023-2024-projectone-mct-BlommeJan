'use strict';

//#region ***  DOM references                           ***********
let htmlAvailableCocktails,
htmlAllCocktails,
htmlCurrentIngredients,
htmlAllIngredients,
htmlPostcard,
htmlCalibration;
//#endregion

//#region ***  SocketIO                                 ***********
const lanIP = `${window.location.hostname}:5000`;
const socketio = io(lanIP);

const listenToUI = function () {};

const listenToSocket = function () {
  socketio.on('connect', function () {
    console.log('verbonden met socket webserver');
  });
};
//#endregion

//#region ***  Callback-Visualisation - show___         ***********
const showAvailableCocktails = (arrCocktails) => {
	try {
		console.info(arrCocktails);
		let strCocktailCards = '';
    for (const cocktail of arrCocktails) {
      strCocktailCards += `
        <a href="postcard.html?cocktail=${cocktail.idDrink}">
          <div class="c-cocktails__cocktail">
            <img src="pictures/Cocktails/${cocktail.strPicture}" alt="${cocktail.strDrink} ${cocktail.strDrinkType}" class="c-cocktails__cocktail__img">
            <div class="c-cocktails__cocktail__info">
              <h2 class="c-cocktails__cocktail__info__name" class="c-cocktails__cocktail__info__name">${cocktail.strDrink}</h2>
              <div class="c-cocktails__cocktail__info__text">
                <div class="c-cocktails__cocktail__info__text__categories">
                  <span class="c-cocktails__cocktail__info__text__categories__isAlcohol">${cocktail.isAlcoholic === 1 ? "Alcoholic" : "Non alcoholic"}</span>
                  <img src="pictures/Icons/${cocktail.strDrinkType}.svg" alt="icon ${cocktail.strDrinkType}" class="c-cocktails__cocktail__info__text__categories__categoryIcon u-bigIcon">
                </div>
                <div class="c-cocktails__cocktail__info__text__ingredients">
                  <ul class="c-cocktails__cocktail__info__text__ingredients__list u-noLiStyle">
                    <li class="c-cocktails__cocktail__info__text__ingredients__list__item">${cocktail.ingredient1 ?? ""}</li>
                    <li class="c-cocktails__cocktail__info__text__ingredients__list__item">${cocktail.ingredient2 ?? ""}</li>
                    <li class="c-cocktails__cocktail__info__text__ingredients__list__item">${cocktail.ingredient3 ?? ""}</li>
                    <li class="c-cocktails__cocktail__info__text__ingredients__list__item">${cocktail.ingredient4 ?? ""}</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </a>
      `;
      htmlAvailableCocktails.innerHTML = strCocktailCards;
		}
	} catch (error) {
		console.error(error);
	}
};

const showAllCocktails = (arrCocktails) => {
	try {
		console.info(arrCocktails);
		let strCocktailCards = '';
    for (const cocktail of arrCocktails) {
      strCocktailCards += `
          <div class="c-cocktails__cocktail">
            <img src="pictures/Cocktails/${cocktail.strPicture}" alt="${cocktail.strDrink} ${cocktail.strDrinkType}" class="c-cocktails__cocktail__img">
            <div class="c-cocktails__cocktail__info">
              <h2 class="c-cocktails__cocktail__info__name" class="c-cocktails__cocktail__info__name">${cocktail.strDrink}</h2>
              <div class="c-cocktails__cocktail__info__text">
                <div class="c-cocktails__cocktail__info__text__categories">
                  <span class="c-cocktails__cocktail__info__text__categories__isAlcohol">${cocktail.isAlcoholic === 1 ? "Alcoholic" : "Non alcoholic"}</span>
                  <img src="pictures/Icons/${cocktail.strDrinkType}.svg" alt="icon ${cocktail.strDrinkType}" class="c-cocktails__cocktail__info__text__categories__categoryIcon u-bigIcon">
                </div>
                <div class="c-cocktails__cocktail__info__text__ingredients">
                  <ul class="c-cocktails__cocktail__info__text__ingredients__list u-noLiStyle">
                    <li class="c-cocktails__cocktail__info__text__ingredients__list__item">${cocktail.ingredient1 ?? ""}</li>
                    <li class="c-cocktails__cocktail__info__text__ingredients__list__item">${cocktail.ingredient2 ?? ""}</li>
                    <li class="c-cocktails__cocktail__info__text__ingredients__list__item">${cocktail.ingredient3 ?? ""}</li>
                    <li class="c-cocktails__cocktail__info__text__ingredients__list__item">${cocktail.ingredient4 ?? ""}</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
      `;
      htmlAllCocktails.innerHTML = strCocktailCards;
		}
	} catch (error) {
		console.error(error);
	}
};

const showCurrentIngredients = (arrIngredients) => {
	try {
		console.info(arrIngredients);
		let strIngredientCards = '';
    for (const ingredient of arrIngredients) {
      strIngredientCards += `
        <div class="c-ingredients__all__ingredient">
          <img src="pictures/Ingredients/${ingredient.ingredient_picture}" alt="${ingredient.category_name}" class="c-ingredients__all__ingredient__img">
          <div class="c-ingredients__all__ingredient__text">
            <p class="c-ingredients__all__ingredient__text__name">${ingredient.category_name}</p>
            <p class="c-ingredients__all__ingredient__text__category">${ingredient.ingredient_name}</p>
          </div>
        </div>
      `;
      htmlCurrentIngredients.innerHTML = strIngredientCards;
		}
	} catch (error) {
		console.error(error);
	}
};

const showAllIngredients = (arrIngredients) => {
  try {
    console.info(arrIngredients);
		let strIngredientCards = '';
    for (const ingredient of arrIngredients) {
      strIngredientCards += `
        <div class="c-ingredients__all__ingredient">
          <img src="pictures/Ingredients/${ingredient.ingredient_picture}" alt="${ingredient.category_name}" class="c-ingredients__all__ingredient__img">
          <div class="c-ingredients__all__ingredient__text">
            <p class="c-ingredients__all__ingredient__text__name">${ingredient.category_name}</p>
            <p class="c-ingredients__all__ingredient__text__category">${ingredient.ingredient_name}</p>
          </div>
        </div>
      `;
      htmlAllIngredients.innerHTML = strIngredientCards;
		}
	} catch (error) {
		console.error(error);
	}
};

const showCocktailInfo = (CocktailInfo) => {
  try {
    console.info(CocktailInfo);
    let strPostcard = '';

    strPostcard += `
      <div class="c-postcard__content__text">
        <div class="c-postcard__content__text__short">
          <div class="c-postcard__content__text__short__info">
              <div class="c-postcard__content__text__short__info__name">
                  <span class="u-meta">Name: </span><span>${CocktailInfo.strDrink}</span>
              </div>
              <div class="c-postcard__content__text__short__info__type">
                  <span class="u-meta">Type: </span><span>${CocktailInfo.idDrinkType}</span>
              </div>
              <div class="c-postcard__content__text__short__info__alcoholic">
                  <span class="u-meta">Alcoholic: </span><span>${CocktailInfo.isAlcoholic === 1 ? "Yes" : "No"}</span>
              </div>
              <div class="c-postcard__content__text__short__info__glass">
                  <span class="u-meta">Glass: </span><span>${CocktailInfo.idGlass}</span>
              </div>
              <div class="c-postcard__content__text__short__info__color">
                  <span class="u-meta">Color: </span><span>${CocktailInfo.idColor}</span>
              </div>
          </div>
          <div class="c-postcard__content__text__short__ingredients">
              <span class="u-meta">Ingredients</span>
              <ul class="u-noLiStyle">
                  <li>${CocktailInfo.ingredient1 ?? ""}</li>
                  <li>${CocktailInfo.ingredient2 ?? ""}</li>
                  <li>${CocktailInfo.ingredient3 ?? ""}</li>
                  <li>${CocktailInfo.ingredient4 ?? ""}</li>
                  <li>${CocktailInfo.ingredient5 ?? ""}</li>
                  <li>${CocktailInfo.ingredient6 ?? ""}</li>
                  <li>${CocktailInfo.ingredient7 ?? ""}</li>
                  <li>${CocktailInfo.ingredient8 ?? ""}</li>
                  <li>${CocktailInfo.ingredient9 ?? ""}</li>
              </ul>
          </div>
        </div>
        <div class="c-postcard__content__text__long">
          <span class="u-meta">Instructions</span>
          <p>${CocktailInfo.strInstructions}</p>
        </div>
      </div>
      <div class="c-postcard__content__btns">
        <div class="c-postcard__content__btns__img">
          <img class="c-postcard__content__btns__img" src="pictures/Cocktails/${CocktailInfo.strPicture}" alt="${CocktailInfo.strDrink}">
        </div>
        <div class="c-postcard__content__btns__btns">
          <button class="c-postcard__content__btns__btns__edit c-postcard__content__btns__btns__btn">EDIT</button>
          <button class="c-postcard__content__btns__btns__delete c-postcard__content__btns__btns__btn">DELETE</button>
          <button class="c-postcard__content__btns__btns__start c-postcard__content__btns__btns__btn js-start-btn">START</button>
        </div>
      </div>
    `;
    htmlPostcard.innerHTML = strPostcard;
    listenToStartButton();
  } catch (error) {
    console.error(error);
  }
};

const showIngredientOptions = (arrIngredients) => {
	try {
		console.info(arrIngredients);
		let strDropdowns = '';
		let strDropdown = '';
    // <select class="c-dropdowns_dropdown" id="ingredient1">
    //   <option value="ingredient1-option1">Ingredient 1 Option 1</option>
    //   <option value="ingredient1-option2">Ingredient 1 Option 2</option>
    //   <option value="ingredient1-option3">Ingredient 1 Option 3</option>
    // </select>

    for (const ingredient of arrIngredients) {
      strDropdown += `
        <option value="${ingredient.ingredient_id}">${ingredient.ingredient_name}</option>
      `;
		}

    for (let i = 1; i < 5; i++) {
      strDropdowns += `
        <select class="c-dropdowns_dropdown" id="ingredient${i}">
        ${strDropdown}
        </select>
      `;
      htmlCalibration.innerHTML = strDropdowns;
    }

	} catch (error) {
		console.error(error);
	}
};
//#endregion

//#region ***  Event Listeners - listenTo___            ***********
const listenToStartButton = () => {
  const urlParams = new URLSearchParams(window.location.search);
  const cocktail = urlParams.get('cocktail');
	console.log('listeningToStartButton');
	document.querySelector('.js-start-btn').addEventListener('click', function () {
		socketio.emit('F2B_start_cocktail', {idDrink: cocktail});
	});
};
//#endregion

//#region ***  Callback-No Visualisation - callback___  ***********
const showError = (error) => {
	console.error(error);
};
//#endregion

//#region ***  Data Access - get___                     ***********
const getAvailableCocktails = () => {
	const url = `http://${lanIP}/api/v1/cocktails/available/`;
	handleData(url, showAvailableCocktails, showError);
};

const getAllCocktails = () => {
	const url = `http://${lanIP}/api/v1/cocktails/`;
	handleData(url, showAllCocktails, showError);
};

const getCurrentIngredients = () => {
	const url = `http://${lanIP}/api/v1/ingredients/current/`;
	handleData(url, showCurrentIngredients, showError);
};

const getAllIngredients = () => {
	const url = `http://${lanIP}/api/v1/ingredients/`;
	handleData(url, showAllIngredients, showError);
};

const getCocktailInfo = () => {
  const urlParams = new URLSearchParams(window.location.search);
  const cocktail = urlParams.get('cocktail');
	const url = `http://${lanIP}/api/v1/cocktail/${cocktail}/`;
	handleData(url, showCocktailInfo, showError);
};

const getIngredientOptions = () => {
  const url = `http://${lanIP}/api/v1/ingredients/`;
	handleData(url, showIngredientOptions, showError);
};
//#endregion

const init = () => {
  console.info('DOM geladen');
  listenToUI();
  listenToSocket();

  	// Get some DOM, we created empty earlier.
	htmlAvailableCocktails = document.querySelector('.js-available-cocktails');
	htmlAllCocktails = document.querySelector('.js-all-cocktails');
	htmlCurrentIngredients = document.querySelector('.js-current-ingredients');
	htmlAllIngredients = document.querySelector('.js-all-ingredients');
	htmlPostcard = document.querySelector('.js-postcard');
  htmlCalibration = document.querySelector('.js-calibration');

	if (htmlAvailableCocktails) {
		getAvailableCocktails();
	} if (htmlAllCocktails) {
    getAllCocktails();
  } if (htmlCurrentIngredients) {
    getCurrentIngredients();
  } if (htmlAllIngredients) {
    getAllIngredients();
  } if (htmlPostcard) {
    getCocktailInfo();
    socketio.on('B2F_success', function () {
    location.href = "index.html"
  });
  } if (htmlCalibration) {
    getIngredientOptions();
    const btnCalibrateIngredient = document.querySelector(".js-ingredient-btn");
    btnCalibrateIngredient.addEventListener("click", () => {
      const ingredient1 = document.getElementById("ingredient1").value
      const ingredient2 = document.getElementById("ingredient2").value
      const ingredient3 = document.getElementById("ingredient3").value
      const ingredient4 = document.getElementById("ingredient4").value
      socketio.emit('F2B_update_ingredients', {ingredient1: ingredient1, ingredient2: ingredient2, ingredient3: ingredient3, ingredient4: ingredient4});
    })
    const btnCleanPumps = document.querySelector(".js-clean-pumps-btn");
    btnCleanPumps.addEventListener("click", () => {
      socketio.emit('F2B_clean_pumps');
    })
  }
};

document.addEventListener('DOMContentLoaded', init);
