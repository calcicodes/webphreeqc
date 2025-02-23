document.addEventListener('DOMContentLoaded', function() {
    const runButton = document.getElementById('runButton');
    const inputField = document.getElementById('codeInput');
    const outputField = document.getElementById('codeOutput');
    const outputTerminal = document.getElementById('codeOutputTerminal');

    console.log(inputField);

    runButton.addEventListener('click', function() {
        const userInput = inputField.value;

        fetch('/run', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_code: userInput })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.output.terminal);
            outputTerminal.value = data.output.terminal;
            outputField.value = data.output.output;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});