// wrapping code in an instantly invoked function expression to shield code from global scope

! (function(document) {
    let itemClassName = "carousel-picture";
    items = document.getElementsByClassName,
    totalItems = items.length,
    slide = 0,
    moving = true;

    // set classes
    function setInitialClasses() {
        // targets prev, current, and next items - assumes there are at least 3 items
        items[totalItems - 1].classList.add("prev");
        items[0].classList.add("active");
        items[1].classList.add("next");
    }

    // set event listeners
    function setEventListeners() {
        let next = document.getElementsByClassName("carousel-button--next")[0];
        let prev = document.getElementsByClassName("carousel-button--prev")[0];

        next.addEventListener("click", moveNext);
        prev.addEventListener("click", movePrev);
    }
} (document));