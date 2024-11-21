// age.js
function updateAge() {
    const birthDate = new Date('2003-06-16'); // Remplace avec ta date de naissance
    const today = new Date();
    let age = today.getFullYear() - birthDate.getFullYear();
    const m = today.getMonth() - birthDate.getMonth();
    
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    document.getElementById('age').textContent = age;
}

updateAge();  // Appelle la fonction pour mettre à jour l'âge
