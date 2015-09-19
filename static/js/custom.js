$(document).ready(function () {
    $('#registerform').validate({
        rules: {
            username: {
                minlength: 3,
                required: true
            },
            email: {
                required: true,
                email: true
            },
            password: {
                minlength: 8,
                required: true
            },
            password2: {
                minlength: 8,
                required: true,
                equalTo: "#register_pwd"
            }
        },
        highlight: function (element) {
            $(element).closest('input').removeClass('valid').addClass('error');
        },
        success: function (element) {
            element.addClass('valid')
                .closest('input').removeClass('error').addClass('valid');
        }
    });
    $('#loginform').validate({
        rules: {
            username: {
                minlength: 3,
                required: true
            },
            password: {
                minlength: 8,
                required: true
            }
        },
        highlight: function (element) {
            $(element).closest('input').removeClass('valid').addClass('error');
        },
        success: function (element) {
            element.addClass('valid')
                .closest('input').removeClass('error').addClass('valid');
        }
    });
});
