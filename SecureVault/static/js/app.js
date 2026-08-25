// ============================================
// TOGGLE PASSWORD VISIBILITY
// ============================================
function togglePassword(button) {
    const span = button.closest('tr').querySelector('.password-cell');
    if (!span) return;
    if (span.innerText === '••••••••') {
        span.innerText = span.dataset.password;
        button.innerHTML = '<i class="bi bi-eye-slash-fill"></i>';
    } else {
        span.innerText = '••••••••';
        button.innerHTML = '<i class="bi bi-eye-fill"></i>';
    }
}

// ============================================
// TOGGLE NEW PASSWORD VISIBILITY (add form)
// ============================================
function toggleNewPassword() {
    const input = document.getElementById('newPassword');
    const icon = document.getElementById('passwordToggleIcon');
    if (input.type === 'password') {
        input.type = 'text';
        icon.className = 'bi bi-eye-slash-fill';
    } else {
        input.type = 'password';
        icon.className = 'bi bi-eye-fill';
    }
}

// ============================================
// COPY PASSWORD
// ============================================
function copyPassword(button) {
    const span = button.closest('tr').querySelector('.password-cell');
    if (!span) return;
    const pwd = span.dataset.password || '';
    navigator.clipboard.writeText(pwd).then(() => {
        showToast('Password copied!', 'bi-clipboard-check');
    }).catch(() => {
        const textArea = document.createElement('textarea');
        textArea.value = pwd;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        textArea.remove();
        showToast('Password copied!', 'bi-clipboard-check');
    });
}

// ============================================
// EDIT PASSWORD (placeholder)
// ============================================
function editPassword(button) {
    showToast('Edit feature coming soon!', 'bi-pencil-fill');
}

// ============================================
// SEARCH / FILTER
// ============================================
const search = document.getElementById('searchBox');
if (search) {
    search.addEventListener('keyup', function() {
        const value = this.value.toLowerCase().trim();
        const rows = document.querySelectorAll('#accountsBody tr');
        rows.forEach(row => {
            const text = row.innerText.toLowerCase();
            row.style.display = text.includes(value) ? '' : 'none';
        });
    });
}

// ============================================
// PASSWORD GENERATOR
// ============================================
let generatorVisible = false;

function generateStrongPassword() {
    const card = document.getElementById('generatorCard');
    if (card.style.display === 'none' || card.style.display === '') {
        card.style.display = 'block';
        generatorVisible = true;
        generatePassword();
    } else {
        card.style.display = 'none';
        generatorVisible = false;
    }
}

function updateLengthDisplay(val) {
    document.getElementById('lengthDisplay').innerText = val;
}

function generatePassword() {
    const length = parseInt(document.getElementById('passwordLength').value);
    const charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?';
    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        password += charset[randomIndex];
    }
    document.getElementById('generatedPassword').value = password;
}

function copyGeneratedPassword() {
    const input = document.getElementById('generatedPassword');
    if (!input.value) return;
    navigator.clipboard.writeText(input.value).then(() => {
        showToast('Password copied!', 'bi-clipboard-check');
    }).catch(() => {
        input.select();
        document.execCommand('copy');
        showToast('Password copied!', 'bi-clipboard-check');
    });
}

function useGeneratedPassword() {
    const input = document.getElementById('generatedPassword');
    if (!input.value) return;
    const passwordField = document.getElementById('newPassword');
    passwordField.value = input.value;
    document.getElementById('generatorCard').style.display = 'none';
    generatorVisible = false;
    showToast('Password applied!', 'bi-check2-circle');
}

// ============================================
// EXPORT DATA
// ============================================
function exportData() {
    showToast('Exporting data... (CSV coming soon)', 'bi-download');
}

// ============================================
// TOAST
// ============================================
function showToast(message, icon = 'bi-shield-check') {
    const existing = document.querySelector('.toast-cyber');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.className = 'toast-cyber';
    toast.innerHTML = `<i class="bi ${icon}"></i> ${message}`;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// ============================================
// SESSION TIMER
// ============================================
(function startSessionTimer() {
    let seconds = 0;
    const timerEl = document.getElementById('sessionTime');
    if (timerEl) {
        setInterval(() => {
            seconds++;
            const mins = String(Math.floor(seconds / 60)).padStart(2, '0');
            const secs = String(seconds % 60).padStart(2, '0');
            timerEl.innerText = `${mins}:${secs}`;
        }, 1000);
    }
})();

// ============================================
// AUTO-UPDATE STATISTICS
// ============================================
(function updateStats() {
    const rows = document.querySelectorAll('#accountsBody tr');
    let total = rows.length;
    let strong = 0, weak = 0;

    rows.forEach((row, index) => {
        const pwdSpan = row.querySelector('.password-cell');
        if (pwdSpan) {
            const pwd = pwdSpan.dataset.password || '';
            const hasUpper = /[A-Z]/.test(pwd);
            const hasSpecial = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(pwd);
            const lengthOk = pwd.length >= 10;
            
            const strengthEl = document.getElementById(`strength-${index + 1}`);
            if (strengthEl) {
                if (lengthOk && hasUpper && hasSpecial) {
                    strengthEl.className = 'strength-indicator strong';
                    strong++;
                } else {
                    strengthEl.className = 'strength-indicator weak';
                    weak++;
                }
            }
        }
    });

    const strongEl = document.getElementById('strongCount');
    const weakEl = document.getElementById('weakCount');
    const totalEl = document.getElementById('totalCount');
    const scoreEl = document.getElementById('score');

    if (strongEl) strongEl.innerText = strong;
    if (weakEl) weakEl.innerText = weak;
    if (totalEl) totalEl.innerText = total;

    let score = total ? Math.round((strong / total) * 100) : 100;
    if (scoreEl) scoreEl.innerText = score + '%';
})();

// ============================================
// KEYBOARD SHORTCUTS
// ============================================
document.addEventListener('keydown', function(e) {
    // Ctrl + G = Generate Password
    if (e.ctrlKey && e.key === 'g') {
        e.preventDefault();
        generateStrongPassword();
    }
    // Ctrl + F = Focus Search
    if (e.ctrlKey && e.key === 'f') {
        e.preventDefault();
        document.getElementById('searchBox').focus();
    }
});