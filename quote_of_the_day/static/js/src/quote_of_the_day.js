/* Javascript for QuoteOfTheDayXBlock. */
function QuoteOfTheDayXBlock(runtime, element) {

    var handlerUrl = runtime.handlerUrl(element, 'save_to_favorites');

    $('.star', element).click(function(ev) {
        var $quoteWrapper = $(this).parent();
        var quoteAuthor = $quoteWrapper.find(".author").text();
        var quoteText = $quoteWrapper.find(".text").text();
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"author": quoteAuthor, "text": quoteText}),
            success: function(data) {
                if (data.success) {
                    alert(data.message);
                    window.location = window.location;
                }
                else { alert(data.message); }
            }
        });
    });
}
