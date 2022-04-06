export function multiToggle(elem, classes) {
  classes.forEach((cls, i) => {
    elem.classList.toggle(cls);
  });
}

export default class StringObj {
  constructor(string) {
    this.string = string;
  }
  capitalize() {
    let firstLetter = this.string.charAt(0).toUpperCase();
    let rest = this.string.slice(1);
    return `${firstLetter}${rest}`;
  }
}
