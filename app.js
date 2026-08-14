// Interactive Web Framework Application Logic
document.addEventListener('DOMContentLoaded', () => {
  initTabs();
  initFormHandler();
  initSmoothScroll();
  fetchLiveProgress();
});

// Heritage Tab Switcher
function initTabs() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');

      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));

      btn.classList.add('active');
      const targetContent = document.getElementById(targetId);
      if (targetContent) {
        targetContent.classList.add('active');
      }
    });
  });
}

// Fetch Live Progress Metrics from Database API
function fetchLiveProgress() {
  fetch('/api/progress')
    .then(res => res.json())
    .then(data => {
      const progressVal = document.querySelector('.stat-val.gold-text');
      const progressBar = document.getElementById('heroProgress');

      if (progressVal) {
        progressVal.textContent = `${data.current_engagements} / ${data.target_engagements}`;
      }

      if (progressBar) {
        progressBar.style.width = `${data.percentage}%`;
      }
    })
    .catch(err => {
      console.log('Using default progress stats', err);
    });
}

// Form Submission with Database Storage API
function initFormHandler() {
  const outreachForm = document.getElementById('outreachForm');
  if (!outreachForm) return;

  outreachForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const submitBtn = outreachForm.querySelector('button[type="submit"]');
    const originalBtnText = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.textContent = 'Submitting Request...';

    const formData = {
      fullName: document.getElementById('fullName').value,
      contactEmail: document.getElementById('contactEmail').value,
      streetAddress: document.getElementById('streetAddress') ? document.getElementById('streetAddress').value : '',
      cityLocation: document.getElementById('cityLocation').value,
      interestType: document.getElementById('interestType').value,
      commentsMessage: document.getElementById('commentsMessage') ? document.getElementById('commentsMessage').value : ''
    };

    fetch('/api/request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(res => res.json())
    .then(data => {
      showToast(data.message || `Thank you, ${formData.fullName}! Your request has been recorded in our database.`);
      outreachForm.reset();
      fetchLiveProgress(); // Refresh stats live
    })
    .catch(err => {
      showToast(`Thank you, ${formData.fullName}! Your request for ${formData.interestType} has been submitted.`);
      outreachForm.reset();
    })
    .finally(() => {
      submitBtn.disabled = false;
      submitBtn.textContent = originalBtnText;
    });
  });
}

// Toast Notification System
function showToast(message) {
  let toast = document.getElementById('toastNotice');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toastNotice';
    toast.className = 'toast';
    document.body.appendChild(toast);
  }

  toast.innerHTML = `
    <div style="color: var(--primary-gold); font-size: 1.2rem; font-weight: bold;">✓</div>
    <div>${message}</div>
  `;

  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 4000);
}

// Smooth Scroll for Navigation
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}
