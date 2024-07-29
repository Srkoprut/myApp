document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.card button');
    
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.card');
            card.classList.toggle('active');
        });
    });
});
