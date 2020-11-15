// Changes submit button HTML on form submission
function formLoading() {
    submitBtn = document.querySelector(".submit-btn");
    submitBtn.disabled = true;
    submitBtn.innerHTML = "<span class='spinner-border spinner-border-sm'></span>Sending...";
    submitBtn.style.pointerEvents = "none";
}