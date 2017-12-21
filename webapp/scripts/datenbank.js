$(document).ready(function() {
    $('.search-btn').on('click', function(event) {

        var input = $('.search-form').find('input').val();

        $.ajax({
            url: 'http://localhost:8001/api/match?name='+input,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                console.log('success');
                console.log(data);
                console.log(JSON.parse(data.replace(/'/g, '"')));
            },
            fail: function (data) {
                console.log('error');
            }
        });
        console.log('done');
    });
});
