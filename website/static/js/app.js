$(document).ready(function() {
    $(document).on('click', '#next', function() {
        var count = $(this).attr("data-count");

        req = $.ajax({
            url : "/next/"+(parseInt(count)+1)+"/",
            type : "POST"
        });

        req.done(function(data) {
            console.log(data);
            $(".content").html(data);
        });
    });
});