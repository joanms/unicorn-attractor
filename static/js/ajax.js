$(document).ready(function () {

    $("#plus-one").click(function () {
        $.ajax({
            url: '/cart/add_one/<id>',
            data: {
                'new_price': new_price
            },
            dataType: 'json',
            success: function (data) {
                console.log(response);
                $("#price").html(new_price);
            });
    });
});