let cart = [];

function showSection(sectionId) {
    document.querySelectorAll('section').forEach(s => s.style.display = 'none');
    document.getElementById(sectionId).style.display = 'block';
    removeBackButton();
}

function showSubsection(subsectionId) {
    showSection(subsectionId);
    addBackButton(subsectionId);
}

function addBackButton(subsectionId) {
    if (!document.getElementById('backButton')) {
        const backButton = document.createElement('button');
        backButton.id = 'backButton';
        backButton.innerText = 'Back to the home page';
        backButton.onclick = () => showSection('pictures');
        const subsection = document.getElementById(subsectionId);
        subsection.insertBefore(backButton, subsection.firstChild);
    }
}

function removeBackButton() {
    const backButton = document.getElementById('backButton');
    if (backButton) {
        backButton.parentNode.removeChild(backButton);
    }
}