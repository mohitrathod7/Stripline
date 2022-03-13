// Hide and Remove Flashed messages ---------------------------------------------------------------
$(document).ready(function($){
    setTimeout(function() {
        $('.flash').remove();
    }, 5000);
});


// --------------------------------------- Flash progress  --------------------------------------- 
window.onload = function() {
    loading()
}

function loading(){
    var loading = false;

    if (loading == false){
        loading = true;

        var progress = document.getElementsByClassName("progress")[0];
        var width = 0;
        var id = setInterval(frame, 1);

        function frame(){
            if (width.toFixed(1) >= 100){
                clearInterval(id);
                $(".flash").remove();
                loading = false;
            }
            else if (width < 99.9){
                width = width + 0.1;
                progress.style.width = width + "%";
            }
        }
    }
}
