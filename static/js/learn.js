$(function() {
    $(".show-operation-modal").click(function() {
        var url = $(".show-operation-modal").attr("data-url");
        $.ajax({
            type: "GET",
            url: url,
            success: function(page) {
                $("#operation-modal .modal-body").html(page);
                $("#operation-modal").modal("show");
            }
        });
    });
});
