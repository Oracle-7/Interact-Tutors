// https://stackoverflow.com/questions/11365632/how-to-detect-when-the-user-presses-enter-in-an-input-field/11365682
function handleFormSubmit() {
    searchBar = document.querySelector(".search-form .dropdown")
    searchForm = document.querySelector(".search-form")

    searchForm.onkeyup = function(e) {
        if (!e) e = window.event;
        let keyCode = e.keyCode || e.which;

        if (keyCode == '13') {
            searchForm.submit();
        }
    }
}

handleFormSubmit()
