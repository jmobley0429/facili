export function multiToggle(elem, classes) {
  classes.forEach((cls, i) => {
    elem.classList.toggle(cls);
  });
}
