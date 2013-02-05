$(document).ready(function() {
    $(".news-area").delegate("h4.title a", "click", function(evt) {
        evt.preventDefault();
        var entry_block = $(this).closest(".news-item").find("p.entry");
        if (entry_block.css("display") === "block") {
            entry_block.fadeOut(100);
        } else {
            entry_block.fadeIn(100);
        }
    });
})