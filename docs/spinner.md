# Spinner




<div id="spin-container"></div>
<button id="random">Random</button>



<div id="meals" style="visibility: hidden;">
Grilled Buffalo Chicken Sammies
Sausage and Broccoli Pasta
Chicken Sausage on Hoagie with peppers and onions
Salmon Sushi Bowls
Boubon Maple Salmon
Crab Cakes
Stuffed Shells
Bolognese
Chicken Parm
Chicken Burgers
Chicken Scarpariello
Grilled Chicken and Sesame Noodles
Spicy Shrimp Francese
Chicken Massaman Curry
Hot Pot
Spanish Chorizo and Orecchiette
Chicken Meatballs and Spaghetti
Grilled Chicken and Pesto Pasta
Lasgana
Gnocchi with Sausage and Peas
Lamb Burgers w Tzaziki
Fish Tacos
Blackend Chicken
Mediterranean Bowls
Bahn Mi Meatballs w pickled veggies
Jambalaya
Shakshuka
Bipimbap Bowls
Chicken Teriyaki Meatballs
Chicken Milanese
Mapo Tofu
Tahini Chicken Kebabs w veggies
Shrimp Fajitas
Tomato Soup & Fancy Grilled Cheese
Chili & Baked Potatoes
Chicken Pesto Meatballs
Grilled sausages
Chicken cacciatore
Skirt Steak Fajitas
Chicken Enchiladas
Chicken Quesadillas
Stuffed Poblanos
Shrimp Scampi
Portabelo Cheese Steaks
Smash Burgers
Fritatta
BBQ Chicken Pizza
</div>




<script>
function shuffle(array) {
  let currentIndex = array.length,  randomIndex;

  // While there remain elements to shuffle.
  while (currentIndex > 0) {

    // Pick a remaining element.
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    // And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex], array[currentIndex]];
  }

  return array;
}


var myArray = document.getElementById("meals").innerHTML.split("\n");
myArray = shuffle(myArray.filter(n => n));
var count = 0;
var button = document.getElementById("random");

button.addEventListener("click", function() {
    count++;
    var selected = myArray[count % myArray.length];
    document.getElementById("spin-container").innerHTML = selected;
});
</script>