#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && !isNaN(w) && h > 0 && !isNaN(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
