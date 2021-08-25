function rot13(str) {

  // create a Regex: /\w/g

  var regex = /\w/g;
  var alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

  // create a replacement function that shifts the letter back 13 indexes

  return str.replace(regex, function replacement(match) {
      if (alphabet.indexOf(match) < 13) {
        return alphabet[alphabet.indexOf(match) + 13];
      }
      else {
        return alphabet[alphabet.indexOf(match) - 13];
      }
    });
}

// Test
console.log(rot13("SERR PBQR PNZC"));
