var correctPass1 = "print('otwieraj')"
var correctPass2 = 'print("otwieraj")'

function returnInfo() {
    var enteredPass = document.getElementById('klucz1').value;
    
    if (enteredPass == correctPass1 || enteredPass == correctPass2) {
        alert('Brawo! Otwarte!');
    } else {
        alert('Odmowa wstępu.');
    }
}