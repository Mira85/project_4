// wrapping code in an instantly invoked function expression to shield code from global scope

! (function(document) {
    let itemClassName = "carousel-picture";
    items = document.getElementsByClassName,
    totalItems = items.length,
    slide = 0,
    moving = true;
} (document));