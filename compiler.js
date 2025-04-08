document.getElementById('runCode').addEventListener('click', function() {
    let code = document.getElementById('code').value;
    let language = document.getElementById('language').value;

    fetch('http://127.0.0.1:5004/execute', {  // ✅ Updated to port 5004
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: code, language: language })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = data.output;
    })
    .catch(error => console.error('Error:', error));
});
