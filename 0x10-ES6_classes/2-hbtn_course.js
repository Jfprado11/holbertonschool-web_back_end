export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw TypeError('Students must be a array of Strings');
    }
    if (typeof length === 'number') {
      this._length = length;
    } else {
      throw TypeError('Length must be a number');
    }
    if (Array.isArray(students)) {
      this._students = students;
    } else {
      throw TypeError('Students must be a array of Strings');
    }
  }

  get name() {
    return this._name;
  }

  set name(newValue) {
    if (typeof newValue === 'string') {
      this._name = newValue;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  get length() {
    return this._length;
  }

  set length(newValue) {
    if (typeof newValue === 'number') {
      this._length = newValue;
    } else {
      throw TypeError('Length must be a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(newValue) {
    if (Array.isArray(newValue)) {
      this._students = newValue;
    } else {
      throw TypeError('Students must be a array of Strings');
    }
  }
}
