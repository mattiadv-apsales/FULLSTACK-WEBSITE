function switchTab(tab) {
    const slider = document.getElementById('slider');
    const tabs = document.querySelectorAll('.tab');
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    tabs.forEach(t => t.classList.remove('active'));

    if (tab === 'login') {
        tabs[0].classList.add('active');
        slider.classList.remove('right');
        loginForm.classList.add('active');
        registerForm.classList.remove('active');
    } else {
        tabs[1].classList.add('active');
        slider.classList.add('right');
        registerForm.classList.add('active');
        loginForm.classList.remove('active');
    }
}

function togglePassword(id) {
    const input = document.getElementById(id);
    input.type = input.type === 'password' ? 'text' : 'password';
}


// ------------------------------------------------------------------------------------

let reg_button = document.getElementById("regi");

reg_button.addEventListener("click", function() {
    let name = document.getElementById("reg-name").value;
    let email = document.getElementById("reg-email").value;
    let password = document.getElementById("reg-password").value;
    let check_password = document.getElementById("confirm-password").value;
    let successEl = document.getElementById("success");

    successEl.innerText = "";

    if (password !== check_password) {
        document.getElementById("success").innerText = "Le password non corrispondono.";
        return;
    }

    if (!email.includes("@") || !email.includes(".")) {
        document.getElementById("success").innerText = "Inserisci un'email valida.";
        return;
    }

    if (password.length < 6) {
        document.getElementById("success").innerText = "La password deve essere lunga almeno 6 caratteri.";
        return;
    }

    if (email.includes("@") && email.includes(".") && password.length >= 6 & name.length >= 3) {
        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: name, email: email, password: password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.email) {
                document.getElementById("reg-name").value = "";
                document.getElementById("reg-email").value = "";
                document.getElementById("reg-password").value = "";
                window.location.href = data.redirect;
            } else {
                document.getElementById("success").innerText = data.error;
            }
        })
    } else {
        document.getElementById("success").innerText = "Inserisci dati validi.";
    }
});

let ac = document.getElementById("access");

ac.addEventListener("click", function() {
    let email = document.getElementById("login-email").value;
    let password = document.getElementById("login-password").value;

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.email) {
            document.getElementById("login-email").value = "";
            document.getElementById("login-password").value = "";
            window.location.href = data.redirect + "?email=" + data.email;
        } else {
            document.getElementById("login-error").innerText = data.error;
        }
    })
})