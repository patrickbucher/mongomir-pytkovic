$(document).ready(function() {
    $('.search-btn').on('click', function(event) {

        var input = $('.search-form .input').val()

        $.ajax({
            url: 'http://localhost:8001/api/match?name='+input,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                console.log('success');
                console.log(data);
                $('.result-view').html('');
                data.forEach(function (item) {
                    $('.result-view').append(
                            '<div class="result">' +
                                '<div class="match-date">' +
                                    '<h3>Match Date: ' + item.date + '</h3>' +
                                '</div>' +
                                '<div class="stats">' +
                                    '<div class="team-home">' +
                                        '<div class="team-home-name">' +
                                            'Team Name' +
                                        '</div>' +
                                        '<div class="home">' +
                                            item.home_team +
                                        '</div>' +
                                    '</div>' +
                                    '<div class="team-away">' +
                                        '<div class="team-away-name">' +
                                            'Team Name' +
                                        '</div>' +
                                        '<div class="away">' +
                                            item.away_team +
                                        '</div>' +
                                    '</div>' +
                                '</div>' +
                            '</div>');
                });
                console.log('done');
            },
            fail: function (data) {
                console.log('error');
            }
        });
    });
});
