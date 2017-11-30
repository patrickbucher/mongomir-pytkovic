$(document).ready(function() {
    $('.search-btn').on('click', function(event) {
        console.log('click');
        $.ajax({
            url: 'http://localhost:8000/match',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                console.log('success');
                console.log(data);
            },
            fail: function (data) {
                console.log('error');
            }
        });
        console.log('done');
    });
});
