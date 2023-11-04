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

//File Upload
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

//Word Count
const textArea = document.getElementById('textArea');
const wordCount1 = document.getElementById('wordCount1');
if (textArea) {
    const text = textArea.value;
    const words = text.split(/\s+/).filter(word => word.length > 0);
    wordCount1.textContent = words.length + "/10000 words";
}
textArea.addEventListener('input', function () {
    if (textArea) {
        const text = textArea.value;
        const words = text.split(/\s+/).filter(word => word.length > 0);
        wordCount1.textContent = words.length + "/10000 words";
    }
});

const wordCount2 = document.getElementById('wordCount2');
const outputText = document.getElementsByClassName("outputBox")[0].textContent;
const words = outputText.split(/\s+/).filter(word => word.length > 0);
wordCount2.textContent = words.length + "/10000 words";

//Clipboard Copy
const btn = document.getElementById("copyToClipboard");
btn.addEventListener("click", () => {
    const cb = navigator.clipboard;
    cb.writeText(outputText);
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
            z.changeVal = s1;
        }

        if (id == s2) {
            x.classList.remove(s4);
            y.classList.add(s4);
            z.changeVal = s2;
        }
        console.log(z);
    }

    x.addEventListener("click", function () { toggleButtons(x.id); });
    y.addEventListener("click", function () { toggleButtons(y.id); });
}

decideModesOptions("paragraph", "keyPoints", "mode", "checked", "value");
decideModesOptions("extractive", "abstractive", "option", "checked", "value");