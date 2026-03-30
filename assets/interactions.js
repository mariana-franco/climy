// Melhorias de interação e gestos para Climy

// Double-tap para atualizar
let lastTap = 0;
document.addEventListener('touchend', function(e) {
    const now = Date.now();
    if (now - lastTap <= 300) {
        // Double tap detectado
        const refreshBtn = document.querySelector('button[title*="Atualizar"]');
        if (refreshBtn) {
            refreshBtn.click();
        }
    }
    lastTap = now;
});

// Swipe horizontal para navegar entre cards
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', function(e) {
    touchStartX = e.changedTouches[0].screenX;
});

document.addEventListener('touchend', function(e) {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
});

function handleSwipe() {
    const swipeThreshold = 50;
    const horizontalCards = document.querySelectorAll('[style*="overflow-x:auto"]');

    if (touchStartX - touchEndX > swipeThreshold) {
        // Swipe para esquerda
        horizontalCards.forEach(card => {
            card.scrollBy({ left: 100, behavior: 'smooth' });
        });
    }

    if (touchEndX - touchStartX > swipeThreshold) {
        // Swipe para direita
        horizontalCards.forEach(card => {
            card.scrollBy({ left: -100, behavior: 'smooth' });
        });
    }
}

// Pull to refresh (mobile)
let touchStartY = 0;
let touchCurrentY = 0;
let pullThreshold = 100;

document.addEventListener('touchstart', function(e) {
    if (window.scrollY === 0) {
        touchStartY = e.changedTouches[0].screenY;
    }
});

document.addEventListener('touchmove', function(e) {
    if (window.scrollY === 0) {
        touchCurrentY = e.changedTouches[0].screenY;
    }
});

document.addEventListener('touchend', function(e) {
    if (window.scrollY === 0 && touchCurrentY - touchStartY > pullThreshold) {
        // Pull to refresh ativado
        const refreshBtn = document.querySelector('button[title*="Atualizar"]');
        if (refreshBtn) {
            refreshBtn.click();
        }
    }
    touchStartY = 0;
    touchCurrentY = 0;
});

// Keyboard navigation
document.addEventListener('keydown', function(e) {
    // R para refresh
    if (e.key === 'r' && !e.ctrlKey && !e.metaKey) {
        const refreshBtn = document.querySelector('button[title*="Atualizar"]');
        if (refreshBtn) {
            refreshBtn.click();
        }
    }

    // Escape para limpar busca
    if (e.key === 'Escape') {
        const otherCityBtn = document.querySelector('button[title*="Outra cidade"]');
        if (otherCityBtn) {
            otherCityBtn.click();
        }
    }
});

// Feedback visual ao carregar
document.addEventListener('DOMContentLoaded', function() {
    // Adicionar classe de loading nos cards
    const heroCard = document.querySelector('.hero');
    if (heroCard) {
        heroCard.style.opacity = '0';
        setTimeout(() => {
            heroCard.style.transition = 'opacity 0.3s ease';
            heroCard.style.opacity = '1';
        }, 100);
    }
});

// Lazy loading para emojis
if ('IntersectionObserver' in window) {
    const emojiObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('emoji-loaded');
            }
        });
    });

    document.querySelectorAll('.emoji-anim').forEach(emoji => {
        emojiObserver.observe(emoji);
    });
}
