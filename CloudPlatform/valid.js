//validation code for login

var email = document.forms['form']['email'];
var password = document.forms['form']['password'];

var email_error = document.getElementById('email_error');
var pass_error = document.getElementById('pass_error');

var checkbox = document.getElementById('password_input');

email.addEventListener('textInput', email_verify);
password.addEventListener('textInput', pass_verify)

function validated(){
    if(!(email.value.includes('@'))){                  //Future Dev: check email against database to see if its registered
        email.style.border = "1px solid red";
        email_error.style.display = "block";
        email.focus();
        return false;   
    }
    if(password.value != "password"){                       //Future Dev: check password against email 
        password.style.border = "1px solid red";
        pass_error.style.display = "block";
        password.focus();
        return false;
    }
}

function email_verify(){
    if(email.value.length >=8){
        email.style.border = "1 px solid green"
        email_error.style.display = "none";
        return true;
    }
}

function pass_verify(){
    if( password.value.length >=8){
        password.style.border = "1 px solid green"
        pass_error.style.display = "none";
        return true;
    }
}

function show_password(){
    if(password.type === 'password'){
        password.type = "text";
    }else{
        password.type = "password";
    }
}