console.log('main.js loaded');
const radioButtons = document.querySelectorAll('input[type="radio"]');
const bddInput = document.getElementById('bdd-input');
const testInput = document.getElementById('test-input');
const output = document.getElementById('output');
const bddInfoMessage = document.getElementById('bdd-info-message');
const testInfoMessage = document.getElementById('test-info-message');
const uploadBtn = document.getElementById('upload-btn');
const fileInput = document.getElementById('file-input');

radioButtons.forEach(radioButton => {
    radioButton.addEventListener('click', () => {
        const selectedOption = document.querySelector('input[type="radio"]:checked').value;
        if (selectedOption === 'generate-bdd') {
            testInput.style.display = 'none';
            bddInput.style.display = 'block';
            bddInfoMessage.innerHTML = `<b>What Is This About :</b>
            <i>Transform Your user stories into BDD feature file scenarios seamlessly.</i>
            <br>
            <b>How To Use:</b>
            <ol>
                <li>Prepare your user stories in an Excel sheet, with each user story in a separate row.</li>
                <li>Upload the excel sheet and click on the <button class="btn btn-danger">Generate BDD From Jira</button> button.</li>
                <li>Our Gen AI engine will then generate BDD scenarios based on your user stories.</li>
                <li>After the scenarios are generated, click on the <button class="btn btn-dark">Download</button> button to save the BDD scenario Excel file to your device.</li>
            </ol>
            <b>File Format:</b>
            <i>Xlsx Format</i>`
        } else if (selectedOption === 'generate-test-data') {
            bddInput.style.display = 'none';
            testInput.style.display = 'block';
            testInfoMessage.innerHTML = `<b>What Is This About :</b>
            <i>Generate Test Data for a LOB.</i>
            <br>
            <b>How To Use:</b>
            <ol>
                <li>Select LOB of your Choice</li>
                <li>Select state of your Choice</li>
                <li>Enter number of test cases you want to generate</li>
                <li>Click on the <button class="btn btn-danger">Generate Test Data</button> button.</li>
                <li>Our Gen AI engine will then generate test cases based on your input.</li>
                <li>After the test cases are generated, click on the <button class="btn btn-dark">Download</button> button to save the Test Case Excel file to your device.</li>
            </ol>
            `;
        }
        output.style.display = 'none';
    });
});

// Function to show loader when form is submitted
    document.getElementById("myForm").addEventListener("submit", function(event) {

      // Show loader
      document.getElementById("loader").classList.remove("hidden");
    });

    document.getElementById("myTestForm").addEventListener("submit", function(event) {

      // Show loader
      document.getElementById("loader").classList.remove("hidden");
    });