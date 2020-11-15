function handleScroll() {
    let myNav = document.querySelector('.navbar');
    window.onscroll = function () { 
        if (document.body.scrollTop >= 5 || document.documentElement.scrollTop >= 5) {
            myNav.classList.add("bg-dark-custom");
            myNav.classList.remove("bg-transparent");
        } 
        else {
            myNav.classList.add("bg-transparent");
            myNav.classList.remove("bg-dark-custom");
        }
    }
}

function run() {
    handleScroll();
}

run()