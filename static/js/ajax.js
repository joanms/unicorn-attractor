$(document).ready(function () {

    $('#plus-one').click(function () {
        $.get('/cart/add_one/<id>').done(function (response) {
            console.log(response);
            $('#price').text(response.new_price);
        });
    });

})