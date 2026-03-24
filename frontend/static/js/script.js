const BASE_URL = "http://127.0.0.1:5000";

let token = "";

// REGISTER
function register() {
    fetch(`${BASE_URL}/auth/register`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: document.getElementById("reg_username").value,
            password: document.getElementById("reg_password").value
        })
    })
    .then(res => res.json())
    .then(data => alert(JSON.stringify(data)));
}

// LOGIN
function login() {
    fetch(`${BASE_URL}/auth/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: document.getElementById("login_username").value,
            password: document.getElementById("login_password").value
        })
    })
    .then(res => res.json())
    .then(data => {
        token = data.access_token;
        alert("Login Successful");
    });
}

// CREATE ACCOUNT
function createAccount() {
    fetch(`${BASE_URL}/account/create`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            account_name: document.getElementById("account_name").value,
            balance: document.getElementById("initial_balance").value
        })
    })
    .then(res => res.json())
    .then(data => alert(JSON.stringify(data)));
}

// GET BALANCE
function getBalance() {
    let acc = document.getElementById("account_number").value;

    fetch(`${BASE_URL}/account/balance/${acc}`, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("balance_result").innerText =
            "Balance: " + data.balance;
    });
}

// TRANSFER
function transfer() {
    fetch(`${BASE_URL}/transaction/transfer`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            from_account: document.getElementById("from_account").value,
            to_account: document.getElementById("to_account").value,
            amount: document.getElementById("amount").value
        })
    })
    .then(res => res.json())
    .then(data => alert(JSON.stringify(data)));
}