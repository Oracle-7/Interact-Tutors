$(function(){

	$('#jcrop_target').Jcrop({
		onChange: showPreview,
		onSelect: showPreview,
		aspectRatio: 1
	});

});

function showPreview(coords)
{
	var rx = 100 / coords.w;
	var ry = 100 / coords.h;

	$('#preview').css({
		width: Math.round(rx * 500) + 'px',
		height: Math.round(ry * 370) + 'px',
		marginLeft: '-' + Math.round(rx * coords.x) + 'px',
		marginTop: '-' + Math.round(ry * coords.y) + 'px'
	});
}

let currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form ...
    let x = document.getElementsByClassName("tab");
    x[n].style.display = "block";

    // ... and fix the Previous/Next buttons:
    if (n == 0)
    {
        document.getElementById("prevBtn").style.display = "none";
    }
    else
    {
        document.getElementById("prevBtn").style.display = "inline";
    }

    if (n == (x.length - 1))
    {
        document.getElementById("nextBtn").innerHTML = "Submit";
    }
    else
    {
        document.getElementById("nextBtn").innerHTML = "Next";
    }
    // ... and run a function that displays the correct step indicator:
    fixStepIndicator(n)
}

function nextPrev(n) {
    // This function will figure out which tab to display
    let x = document.getElementsByClassName("tab");

    // Exit the function if any field in the current tab is invalid:
    // if (n == 1 && !validateForm()) return false;

    // Hide the current tab:
    x[currentTab].style.display = "none";

    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;

    // if you have reached the end of the form... :
    if (currentTab >= x.length)
    {
        //...the form gets submitted:
        document.getElementById("regForm").submit();
        return false;
    }

    // Otherwise, display the correct tab:
    showTab(currentTab);
}
