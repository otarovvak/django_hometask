const tagButtons = document.querySelectorAll('.tag-buttons button');
tagButtons.forEach(button => {
    button.addEventListener('click', () => {
        button.classList.toggle('active');
        filterProducts();
    });
});

//filter on selected tags/category/search
function filterProducts() {
    const selectedTags = [...document.querySelectorAll('.tag-buttons button.active')]
        .map(button => button.dataset.tag.toLowerCase());
    const searchQuery = document.getElementById('search').value.toLowerCase();
    const selectedCategory = document.getElementById('category').value.toLowerCase();

    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        const category = card.querySelector('.category').textContent.toLowerCase();
        const description = card.querySelector('.product-info p').textContent.toLowerCase();
        const tags = [...card.querySelectorAll('.tags span')]
            .map(tag => tag.textContent.toLowerCase());

        const matchesCategory = selectedCategory === '' || category.includes(selectedCategory);
        const matchesTags = selectedTags.every(tag => tags.includes(tag));
        const matchesSearch = description.includes(searchQuery);

        if (matchesCategory && matchesTags && matchesSearch) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
}

document.getElementById('category').addEventListener('change', filterProducts);
document.getElementById('search').addEventListener('input', filterProducts);

// Reset all filters
document.getElementById('resetFilters').addEventListener('click', () => {
    document.getElementById('category').value = '';
    
    document.getElementById('search').value = '';
    
    tagButtons.forEach(button => button.classList.remove('active'));
    
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => card.style.display = '');
});
