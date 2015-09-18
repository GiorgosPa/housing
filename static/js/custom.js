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
                minlength: 3,
                required: true
            },
            password2: {
                minlength: 3,
                required: true,
                equalTo: "#register_pwd"
            }
        },
        highlight: function (element) {
            $(element).closest('.form-group').removeClass('valid').addClass('error');
        },
        success: function (element) {
            element.addClass('valid')
                .closest('.form-group').removeClass('error').addClass('valid');
        }
    });
    $('#loginform').validate({
        rules: {
            username: {
                minlength: 3,
                required: true
            },
            password: {
                minlength: 3,
                required: true
            }
        },
        highlight: function (element) {
            $(element).closest('.form-group').removeClass('valid').addClass('error');
        },
        success: function (element) {
            element.addClass('valid')
                .closest('.form-group').removeClass('error').addClass('valid');
        }
    });
});
