// wrapping code in an instantly invoked function expression to shield code from global scope

! (function(document) {
    let itemClassName = "carousel-picture";
        items = document.getElementsByClassName(itemClassName),
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

    // Next - Navigation handler
    function moveNext() {
        // Check if moving
        if (!moving) {
            // If last slide, reset to 0, else +1
            if (slide === (totalItems - 1)) {
                slide = 0;
            } else {
                slide++;
            }

            // Move carousel to updated slide
            moveCarouselTo(slide);
        }
    }

    // Previous - Navigation handler
    function movePrev() {
        // Check if moving
        if (!moving) {
            // If first slide, set as last slide, else -1
            if (slide === 0) {
                slide = (totalItems - 1);
            } else {
                slide--;
            }

            // Move carousel to the updated slide
            moveCarouselTo(slide);
        }
    }

    // Disable user interaction while animation is playing
    function disableInteraction() {
        // set "moving" to true while the animation is playing 
        // (0.5s = 500ms)
        moving = true;

        // setTimeout runs its function once after the provided time
        setTimeout(function() {
            moving = false
        }, 500);
    }

    function moveCarouselTo(slide) {
        // check if carousel moving, if not, allow user interaction
        if(!moving) {
            // disable interactivity
            disableInteraction();

            // update the old adjacent slides with new ones
            let newPrevious = slide - 1,
                newNext = slide + 1,
                oldPrevious = slide - 2,
                oldNext = slide + 2;

            // Check if carousel has more than 3 items
            if ((totalItems - 1) > 3) {

                // Checks and updates if new slides are out of bounds
                if (newPrevious <= 0) {
                    oldPrevious = (totalItems - 1);
                } else if (newNext >= (totalItems - 1)) {
                    oldNext = 0;
                }

                // checks and updates if slide is at beginning/end
                if (slide === 0) {
                    newPrevious = (totalItems - 1);
                    oldPrevious = (totalItems -2);
                    oldNext = (slide + 1);
                } else if (slide === (totalItems - 1)) {
                    newPrevious = (slide - 1);
                    newNext = 0;
                    oldNext = 1;
                }

                // Trigger transitions by adding/removing classes
                // Reset old next/prev elements to default classes
                items[oldPrevious].className = itemClassName;
                items[oldNext].className = itemClassName;

                // Add new classes
                items[newPrevious].className = itemClassName + " prev";
                items[slide].className = itemClassName + " active";
                items[newNext].className = itemClassName + " next";
            }
        }
    }

    function initCarousel() {
        setInitialClasses();
        setEventListeners();

        // Set moving to false so the carousel can be interacted with
        moving = false;
    }

    initCarousel();

} (document));

$('.collapse').collapse({
    toggle: true
})
