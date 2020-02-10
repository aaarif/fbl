$(function() {
    $('#btnSubmitLink').click(function() {
        $.ajax({
            url: '/submitProductLink',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                $.ajax({
                    url: '/detailProduct',
                    data:response,
                    type: 'GET',
                    success: function(response) {
                        console.log(response+"Ini kalau sukses");

                    },
                    error: function(error) {
                        console.log(error);
                    }
                    });
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
