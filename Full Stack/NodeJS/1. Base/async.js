console.log('1. Sync start');

setTimeout(() => {
  console.log('7. Callback macrotask #1 (setTimeout 0ms)');
  setTimeout(() => console.log('10. Nested callback macrotask #2'), 0);
}, 0);

// Callback hell example
function callbackHell(cb) {
  setTimeout(() => {
    console.log('Callback Hell Step 1');
    cb();
  }, 0);
}
callbackHell(() => {
  setTimeout(() => {
    console.log('Callback Hell Step 2');
  }, 0);
});

Promise.resolve()
  .then(() => console.log('3. Promise microtask #1'));

Promise.resolve()
  .then(() => {
    console.log('4. Promise microtask #2');
    Promise.resolve().then(() => console.log('6. Nested Promise microtask'));
  });

Promise.resolve()
  .then(() => console.log('5. Promise microtask #3'));

setTimeout(() => console.log('8. Callback macrotask #3 (setTimeout 0ms)'), 0);

Promise.all([
  Promise.resolve('A').then(val => console.log('2. Promise.all A: ' + val)),
  new Promise(resolve => {
    setTimeout(() => {  // Callback inside Promise
      resolve('B');
      console.log('9. Callback in Promise resolved');
    }, 0);
  })
]).then(() => console.log('11. Promise.all complete (after all Promises)'));

console.log('12. Sync end');