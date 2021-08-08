var correctPass1 = "print('otwieraj')"
var correctPass2 = 'print("otwieraj")'

function returnInfo() {
    var enteredPass = document.getElementById('klucz1').value;
    var badPass = document.getElementById('klucz2').value;
    
    if (enteredPass == correctPass1 || enteredPass == correctPass2) {
        alert('Brawo! Otwarte!');
    } else {
        alert('Odmowa wstępu.');
    }
}

// function postPassword() {
//     let password = document.getElementById('kluczyk').value;
//     console.log(password)
//     if (password) {
//         fetch('/dzien1', {
//             method: 'post',
//             headers: {
//                 'Accept': 'application/json, text/plain, */*',
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({pass: password}) 
//         })
//     }
// }