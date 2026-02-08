const display = document.getElementById('display');
const resultDiv = document.getElementById('result');

document.querySelectorAll('[data-key]').forEach(btn => {
  btn.addEventListener('click', () => {
    display.value = (display.value || '') + btn.getAttribute('data-key');
  });
});

document.getElementById('btn-clear').addEventListener('click', () => {
  display.value = '';
  resultDiv.textContent = '';
});

document.getElementById('btn-eval').addEventListener('click', () => {
  try {
    // simple client-side evaluation using JS (note: uses JS eval)
    // Only intended for local use; server eval is available too.
    const res = eval(display.value);
    resultDiv.textContent = String(res);
  } catch (e) {
    resultDiv.textContent = 'Error: ' + e.message;
  }
});

document.getElementById('btn-eval-server').addEventListener('click', async () => {
  resultDiv.textContent = '…';
  try {
    const resp = await fetch('/eval', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ expr: display.value })
    });
    const j = await resp.json();
    if (resp.ok) resultDiv.textContent = j.result;
    else resultDiv.textContent = 'Error: ' + (j.error || resp.statusText);
  } catch (e) {
    resultDiv.textContent = 'Error: ' + e.message;
  }
});
