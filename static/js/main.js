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
            infoMessage.innerHTML = `<b>BDD Information Message</b>:
                                  <ul>
                                    <li>What is this about</li>
                                    <li>How to use it</li>
                                    <li>File format</li>
                                    </ul>`;
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