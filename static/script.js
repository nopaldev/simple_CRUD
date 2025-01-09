// Confirm delete function
function confirmDelete() {
    return confirm('Apakah Anda yakin ingin menghapus data ini?');
}

// Add fade-in animation to table rows
document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('.data-row');
    rows.forEach((row, index) => {
        row.style.animationDelay = `${index * 0.1}s`;
    });
});

// Add ripple effect to buttons
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', function(e) {
        const ripple = document.createElement('div');
        ripple.classList.add('ripple');
        this.appendChild(ripple);
        
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
});

// Add hover effect to table rows
document.querySelectorAll('.data-row').forEach(row => {
    row.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.01)';
        this.style.transition = 'transform 0.2s ease';
    });
    
    row.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
    });
});