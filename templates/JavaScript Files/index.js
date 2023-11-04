//Navigation Bar
const barsIcon = document.querySelector(".fa-bars");
const timesIcon = document.querySelector(".fa-times");
const navLinks = document.querySelector(".navLinks");

barsIcon.addEventListener("click", function () {
    navLinks.classList.add("show");
    barsIcon.classList.add("displayNone");
    timesIcon.classList.remove("displayNone");
});

timesIcon.addEventListener("click", function () {
    navLinks.classList.remove("show");
    timesIcon.classList.add("displayNone");
    barsIcon.classList.remove("displayNone");
});


//Handling the scroll animations.
function isElementInViewport(element) {
    const rect = element.getBoundingClientRect();
    const windowHeight = window.innerHeight || document.documentElement.clientHeight;
    const featureHeight = element.offsetHeight;
    return (
        (rect.top + featureHeight * 0.2) <= windowHeight &&
        (rect.bottom - featureHeight * 0.2) >= 0
    );
}
function handleScroll() {
    const features = document.querySelectorAll('.content');

    //Adding the scroll-animations to features
    features.forEach((feature) => {
        if (isElementInViewport(feature)) {
            feature.classList.add('active');
        }
    });

    //Adding the scroll-animations to features
    const contactSection = document.querySelector('.contactBox');
    if (isElementInViewport(contactSection)) {
        contactSection.classList.add('active');
    }
}
window.addEventListener('scroll', handleScroll);
window.addEventListener('load', handleScroll);