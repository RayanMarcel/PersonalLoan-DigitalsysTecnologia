document.getElementById('proposal-form').addEventListener('submit', function(event){
    event.preventDefault();

    const full_name = document.getElementById('full_name').value;
    const cpf = document.getElementById('cpf').value;
    const address = document.getElementById('address').value;
    const loan_value = document.getElementById('loan_value').value;

    fetch('/api/propoals/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/jason',
        },
        body: JSON.stringify({
            full_name: full_name,
            cpf: cpf,
            address: address,
            loan_value: loan_value,
        }),
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});