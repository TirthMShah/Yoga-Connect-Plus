function validate_username(username) {
    pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[_$])[a-zA-Z_$0-9]{6,}$/
    msg = document.getElementById('username_description');
    check = document.getElementById('username_check');
    cross = document.getElementById('username_cross');

    if (!pattern.test(username.target.value) || username.target.value == ' ') {
        msg.style.color = 'red';
        check.setAttribute('hidden', true);
        cross.removeAttribute('hidden');
    }
    else {
        check.removeAttribute('hidden');
        cross.setAttribute('hidden', true);
        msg.style.color = 'green';
    }
}

function validate_password(password) {
    check = document.getElementById('password_check1');
    cross = document.getElementById('password_cross1');
    msg = document.getElementById('password_description')

    if (!((password.target.value.length > 5) && (password.target.value.length < 13))) {
        msg.style.color = 'red';
        check.setAttribute('hidden', true);
        cross.removeAttribute('hidden');
        document.getElementById('password1').style.borderColor = 'red';
    }
    else {
        check.removeAttribute('hidden');
        cross.setAttribute('hidden', true);
        msg.style.color = 'green';
        document.getElementById('password1').style.borderColor = 'green';

    }
}

function validate_mobile(mobile) {
    check = document.getElementById('mobile_check');
    cross = document.getElementById('mobile_cross');

    if (mobile.target.value.length == 10) {
        check.removeAttribute('hidden');
        cross.setAttribute('hidden', true);
        document.getElementById('mobile').style.borderColor = 'green';
    }
    else {
        check.setAttribute('hidden', true);
        cross.removeAttribute('hidden');
        document.getElementById('mobile').style.borderColor = 'red';

    }
}

function match_password(password1, password2) {
    check = document.getElementById('password_check');
    cross = document.getElementById('password_cross');

    if (password1.value != password2.target.value) {
        check.setAttribute('hidden', true);
        cross.removeAttribute('hidden');
        document.getElementById('password2').style.borderColor = 'red';
    }
    else {
        check.removeAttribute('hidden');
        cross.setAttribute('hidden', true);
        document.getElementById('password2').style.borderColor = 'green';
    }
}

function remove_reds(element, check, cross) {
    element.style.borderColor = 'black';
    check.setAttribute('hidden', true);
    cross.setAttribute('hidden', true);
}