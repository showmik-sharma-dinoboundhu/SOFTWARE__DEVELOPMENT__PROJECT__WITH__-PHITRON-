const loaddata = () =>
{
    const searchText = document.getElementById("search-box").value;
    console.log(searchText);
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?f=${searchText}`)
    .then((res) => res.json())
    .then((data) => displyadata(data.meals));
};

const displyadata = (data) =>
{
    document.getElementById("total-meals").innerText = data.length;

        const mealsContainer = document.getElementById("meals-container");

    data.forEach((meal) => 
    {
        console.log(meal);
        const card = document.createElement("div");
        card.cardlist.add("box");
        card.innerHTML = 
        `
            <img class="box-img" src="${meal.strMealThumb}" alt =""> 
            <h2>${data?.idmeal}</h2>
            <p>${meal.strInstructions.slice(0,20)}</p>
                <button onclick="displaymodal" type="button" class="btn-solid theme-primary" data-bs-toggle="dialog" data-bs-target="#exampleDialogDark">
                    Details
                </button>  
        `
        mealsContainer.appendChild(card);
    });

    

};

const displaymodal = (info) =>
    {
        console.log("hello boss");
    }


