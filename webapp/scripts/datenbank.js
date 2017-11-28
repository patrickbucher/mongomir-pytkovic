$(document).ready(function() {


    $('.search-btn').on('click', function(event) {
        var data = 'birthday';
        $.ajax({
            url: 'https://localhost:8000/match',
            type: "GET",
            data: data,
            dataType: 'json',
            success: function (data) {
                alert(data);
            },
            fail: function (data) {
                alert(data);
            }
        });
        console.log(data);
    });




});
