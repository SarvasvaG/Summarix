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

 //Carousel Effects
 var members = document.getElementsByClassName("content");
 var index = 0;
 var len = members.length;

 function showMember() {
     for (var i = 0; i < len; i++)
         members[i].classList.add("hide");
     members[index % 5].classList.remove("hide");
     index++;
 };

 function startInterval() {
     x = setInterval(showMember, 3000);
 }
 
 function showPrevMember() {
     index = (index - 2);
     if (index < 0)
         index = 4;
     clearInterval(x);
     showMember();
     startInterval();
 }

 function showNextMember() {
     clearInterval(x);
     showMember();
     startInterval();
 }
 showMember();
 startInterval();

 for (var i = 0; i < len; i++) {
     members[i].addEventListener("mouseover", () => {
         clearInterval(x);
     });

     members[i].addEventListener("mouseout", () => {
         startInterval();
     });
 }

 var prevBtn = document.getElementById("prev");
 var nextBtn = document.getElementById("next");

 prevBtn.addEventListener("click", showPrevMember);
 nextBtn.addEventListener("click", showNextMember);