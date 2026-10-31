
// Select HTML elements
const message = document.getElementById("message");
const changeBtn = document.getElementById("changeBtn");

const countDisplay = document.getElementById("count");
const increaseBtn = document.getElementById("increaseBtn");
const decreaseBtn = document.getElementById("decreaseBtn");

// Initial counter value
let count = 0;

// Change text and colour when button is clicked
changeBtn.addEventListener("click", function () {
    message.textContent = "Great! JavaScript is working.";
    message.style.color = "#168c85";
    console.log("Text and colour changed!");
});

// Increase counter
increaseBtn.addEventListener("click", function () {
    count++;
    countDisplay.textContent = count;

    console.log("Current count:", count);
});

// Decrease counter
decreaseBtn.addEventListener("click", function () {
    count--;
    countDisplay.textContent = count;

    console.log("Current count:", count);
});
