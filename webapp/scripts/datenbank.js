$(document).ready(function() {
    $('.search-btn').on('click', function(event) {
        $.ajax({
            url: 'http://192.168.99.100:8000/match',
            type: "GET",
            dataType: 'json',
            crossDomain: true,
            success: function (data) {
                console.log('success');
                console.dir(data);
            },
            fail: function (data) {
                console.log('error');
            }
        });
    });
});
