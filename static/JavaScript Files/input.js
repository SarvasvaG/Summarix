//Navigation Bar
const barsIcon = document.querySelector(".fa-bars");
const timesIcon = document.querySelector(".fa-times");
const navLinks = document.querySelector(".navLinks");

barsIcon.addEventListener("click", function () {
    navLinks.classList.add("show");
    barsIcon.style.display = "none";
    timesIcon.style.display = "block";
});

timesIcon.addEventListener("click", function () {
    navLinks.classList.remove("show");
    timesIcon.style.display = "none";
    barsIcon.style.display = "block";
});

// Trigger the file input and update the button's text with the selected file name
const fileInput = document.getElementById("documentUpload");
const customUploadButton = document.getElementById("customUploadButton");
const fileName = document.getElementById("fileName");

fileInput.addEventListener("change", function () {
    if (fileInput.files.length > 0) {
        fileName.textContent = " " + fileInput.files[0].name;
    }
});

customUploadButton.addEventListener("click", function () {
    fileInput.click();
});

//Displaying the Word Count
const textArea = document.getElementById('textArea');
const wordCount = document.getElementById('wordCount');
const currWords = document.getElementById('currWords');

function checkWordCount() {
    if (textArea) {
        const text = textArea.value;
        const words = text.split(/\s+/).filter(word => word.length > 0);
        wordCount.textContent = words.length + "/10000 words";

        if (words.length > 10000) {
            wordCount.textContent = words.length + "/10000 words !!";
            wordCount.classList.add("red");
        }

        else {
            wordCount.textContent = words.length + "/10000 words";
            wordCount.classList.remove("red");
        }

        currWords.value = words.length;
    }
}

checkWordCount();
textArea.addEventListener('input', function () {
    checkWordCount();
});

//Checkboxes for paragraph and key points
function decideModesOptions(s1, s2, s3, s4) {
    var x = document.getElementById(s1);
    var y = document.getElementById(s2);
    var z = document.getElementById(s3);
    function toggleButtons(id) {
        if (id == s1) {
            x.classList.add(s4);
            y.classList.remove(s4);
            z.value = s1;
        }

        if (id == s2) {
            x.classList.remove(s4);
            y.classList.add(s4);
            z.value = s2;
        }

        console.log(z);
    }
    x.addEventListener("click", function () { toggleButtons(x.id); });
    y.addEventListener("click", function () { toggleButtons(y.id); });
}

decideModesOptions("paragraph", "keyPoints", "mode", "checked");
decideModesOptions("extractive", "abstractive", "option", "checked");