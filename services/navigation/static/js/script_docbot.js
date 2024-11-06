const headers = document.querySelectorAll('[data-name="accordeon-title"]');

headers.forEach(function(item) {
    item.addEventListener('click', function() {
        const content = this.nextElementSibling;

        if (content.classList.contains('show')) {
            content.classList.remove('show');
            setTimeout(() => {
                content.style.maxHeight = '0'; // Устанавливаем max-height на 0
                content.style.opacity = '0'; // Устанавливаем прозрачность
            }, 10); // Небольшая задержка для анимации
        } else {
            content.classList.remove('hidden'); // Убираем класс hidden
            content.style.maxHeight = content.scrollHeight + 'px'; // Устанавливаем max-height на реальную высоту
            content.style.opacity = '1'; // Устанавливаем прозрачность
            
            requestAnimationFrame(() => {
                content.classList.add('show'); // Добавляем класс show для анимации
            });
        }
    });
});
