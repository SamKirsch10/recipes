// The wake lock sentinel.
let wakeLock = null;

// Function that attempts to request a screen wake lock.
const requestWakeLock = async () => {
  try {
    wakeLock = await navigator.wakeLock.request();
    wakeLock.addEventListener('release', () => {
      console.log('Screen Wake Lock released:', wakeLock.released);
    });
    console.log('Screen Wake Lock released:', wakeLock.released);
  } catch (err) {
    console.error(`${err.name}, ${err.message}`);
  }
};

// Place in header (do not use async or defer)
document.addEventListener('readystatechange', event => {
  switch (document.readyState) {
    case "complete":
      var checkbox = document.querySelector('.slider_input');
      checkbox.addEventListener('change', (event) => {
        if (event.currentTarget.checked) {
          requestWakeLock();
        } else {
          wakeLock.release();
          wakeLock = null;
        }
      })
      break;
  }
});

// Request a screen wake lock…
// requestWakeLock();
// // …and release it again after 5s.
// window.setTimeout(() => {
//   wakeLock.release();
//   wakeLock = null;
// }, 5000);