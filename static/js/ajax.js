$(document).ready(function(){
    
    $('#plus-one').click(function() {
        $.get('/cart/add_one/<id>').done(function(response) {
            // result goes here
            console.log(response);
            // response = {
            //     'new_price': '6'
            // }
            
            // $('#price').text(response.new_price);
        });
    });

    $('#minus-one').click(function() {
        $.get('/cart/subtract_one/<id>').done(function(response) {
            // result goes here
            console.log(response);
            // response = {
            //     'new_price': '6'
            // }
            
            // $('#price').text(response.new_price);
        });
    });

    
})