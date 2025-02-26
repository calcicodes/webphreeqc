// object for storing output data
const outputData = {
    'terminal': 'Output from the terminal window after running the code will be displayed here (useful to see error messages).',
    'output': 'PHREEQC output will be displayed here.',
    'selected_output': 'Output from any SELECTED_OUTPUT block will be displayed here.' 
};

// run code and save output data
document.addEventListener('DOMContentLoaded', function() {
    const runButton = document.getElementById('runButton');
    const inputField = document.getElementById('codeInput');
    const databaseName = document.getElementById('databaseSelector');
    const outputSelector = document.getElementById('outputSelector');
    const outputField = document.getElementById('codeOutput');

    runButton.addEventListener('click', function() {
        const userInput = inputField.value;
        const outputVariable = outputSelector.value;

        fetch('/run', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_code: userInput, database: databaseName.value })
        })
        .then(response => response.json())
        .then(data => {
            for (let item of Object.keys(data.output)) {
                outputData[item] = data.output[item];
            };
            outputField.value = outputData[outputVariable];
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

// select output to view
document.addEventListener('DOMContentLoaded', function() {
    const outputSelector = document.getElementById('outputSelector');
    const outputField = document.getElementById('codeOutput');

    outputSelector.value = outputSelector.options[0].value;
    outputField.value = outputData[outputSelector.value];

    outputSelector.addEventListener('change', function() {
        outputField.value = outputData[outputSelector.value];
    });
});

// update template code
document.addEventListener('DOMContentLoaded', function() {
    const inputSelector = document.getElementById('inputSelector');
    const inputField = document.getElementById('codeInput');

    // Handle template change
    inputSelector.addEventListener('change', function() {
        const template = inputSelector.value;
        const templateCode = template;
        inputField.value = templateCode;
    });
});

// update database view
document.addEventListener('DOMContentLoaded', function() {
    const databaseSelector = document.getElementById('databaseSelector');
    const databaseView = document.getElementById('databaseView');

    // Handle database change
    databaseSelector.addEventListener('change', function() {
        const database = databaseSelector.value;
        fetch(`/get_database/${database}`)
            .then(response => response.json())
            .then(data => {
                databaseView.value = data.database;
            })
            .catch(error => {
                console.error('Error:', error);
                databaseView.value = 'Error: could not load database';
            });
    });
});
