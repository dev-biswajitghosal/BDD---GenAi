const radioButtons = document.querySelectorAll('input[type="radio"]');
const input = document.getElementById('input');
const output = document.getElementById('output');
const infoMessage = document.getElementById('info-message');
const uploadBtn = document.getElementById('upload-btn');
const fileInput = document.getElementById('file-input');

radioButtons.forEach(radioButton => {
    radioButton.addEventListener('click', () => {
        const selectedOption = document.querySelector('input[type="radio"]:checked').value;
        input.style.display = 'block';
        if (selectedOption === 'generate-bdd') {
            infoMessage.innerHTML = `<b>What Is This About :</b>
            <i>Transform Your user stories into BDD feature file scenarios seamlessly.</i>
            <br>
            <b>How To Use:</b>
            <ol>
                <li>Prepare your user stories in an Excel sheet, with each user story in a separate row.</li>
                <li>Upload the excel sheet and click on the <button class="btn btn-primary">Generate BDD</button> button.</li>
                <li>Our Gen AI engine will then generate BDD scenarios based on your user stories.</li>
                <li>After the scenarios are generated, click on the <button class="btn btn-success">Download</button> button to save the BDD scenario Excel file to your device.</li>
            </ol>
            <b>File Format:</b>
            <i>Xlsx Format</i>`
            uploadBtn.innerHTML = 'Generate BDD';
        } else if (selectedOption === 'generate-test-data') {
            infoMessage.innerHTML = `<b>Test Data Information Message</b>:
                                  <ul>
                                    <li>What is this about</li>
                                    <li>How to use it</li>
                                    <li>File format</li>
                                    </ul>`;
            uploadBtn.innerHTML = 'Generate Test Data';
        }
        output.style.display = 'none';
    });
});

uploadBtn.addEventListener('click', () => {
    output.style.display = 'block';
});