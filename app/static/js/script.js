document.getElementById('write-summary').addEventListener('click', function () {
    fetch('/write-summary', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ summary: '{{ summary }}' }),
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});