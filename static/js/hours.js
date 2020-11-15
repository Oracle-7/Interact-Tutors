// Changes submit button HTML on form submission
function formLoading() {
    console.log("HERE")
    submitBtn = document.querySelector(".submit-btn");
    submitBtn.disabled = true;
    submitBtn.innerHTML = "<span class='spinner-border spinner-border-sm'></span>Please wait...";
    submitBtn.style.pointerEvents = "none";
}