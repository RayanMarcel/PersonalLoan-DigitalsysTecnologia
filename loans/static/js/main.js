document.getElementById('proposal-form').addEventListener('submit', function(event){
    event.preventDefault();

    const full_name = document.getElementById('full_name').value;
    const cpf = document.getElementById('cpf').value;
    const address = document.getElementById('address').value;
    const loan_value = document.getElementById('loan_value').value;

    fetch('/api/proposals/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            full_name: full_name,
            cpf: cpf,
            address: address,
            loan_value: loan_value,
        }),
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then((data) => {
        Swal.fire({
            icon: 'success',
            title: 'Success',
            text: 'Proposal created successfully',
        });
    })
    .catch((error) => {
        console.error('Error:', error);
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Something went wrong!',
        });
    });
});