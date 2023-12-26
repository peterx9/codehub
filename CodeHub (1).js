let cart = [];

    function showSection(sectionId) {
        document.querySelectorAll('section').forEach(s => s.style.display = 'none');
        document.getElementById(sectionId).style.display = 'block';
        removeBackButton();
    }

    function showSubsection(subsectionId) {
    showSection(subsectionId);
    addBackButton(subsectionId.toLowerCase());
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


    function searchImages() {
    const searchInput = document.getElementById('search-input').value.toLowerCase();
    const images = document.querySelectorAll('.category');

    images.forEach(image => {
        const title = image.querySelector('h3').innerText.toLowerCase();
        if (title.includes(searchInput)) {
            image.style.display = 'inline-block';
        } else {
            image.style.display = 'none';
        }
    });
}

function showSection(sectionId) {
    const validSectionIds = ['pictures', 'categories', 'Anime', 'Historical places', 'Space' , 'Animals', 'Magic', 'Camping', 'Kids', 'Party' , 'Study' , 'Nature', 'Music', 'Christmas', 'Technology', 'Cars' , 'Sports' , 'Fashion'];
    if (validSectionIds.includes(sectionId)) {
        document.querySelectorAll('section').forEach(s => s.style.display = 'none');
        document.getElementById(sectionId).style.display = 'block';
        removeBackButton();
    } else {
        console.error('Invalid section ID');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    showSection('pictures');
});

function populateAllImages() {
        populateCategoryImages('Animals', 'animals-images');
        populateCategoryImages('Anime', 'anime-images');
        populateCategoryImages('Historical places', 'historical-places-images');
        populateCategoryImages('Space', 'space-images');
        populateCategoryImages('Magic', 'Magic-images');
        populateCategoryImages('Camping', 'Camping-images');
        populateCategoryImages('Kids', 'Kids-images');
        populateCategoryImages('Party', 'Party-images');
        populateCategoryImages('Study', 'Study-images');
        populateCategoryImages('Nature', 'Nature-images');
        populateCategoryImages('Music', 'Music-images');
        populateCategoryImages('Christmas', 'Christmas-images');
        populateCategoryImages('Technology', 'Technology-images');
        populateCategoryImages('Cars', 'Cars-images');
        populateCategoryImages('Sports', 'Sports-images');
        populateCategoryImages('Fashion', 'Fashion-images');
    }

    function populateCategoryImages(category, targetId) {
        const categorySection = document.getElementById(category);
        const targetUl = document.getElementById(targetId);

        const images = categorySection.querySelectorAll('img');
        images.forEach(image => {
            const li = document.createElement('li');
            li.appendChild(image.cloneNode(true));
            targetUl.appendChild(li);
        });
    }

    document.addEventListener('DOMContentLoaded', function() {
        showSection('pictures');
        populateAllImages();
    });