function palindrome(str) {

  // trim whitespace, make lowercase
  var stringA = str.toLowerCase().trim();
  var noNonAlpha = /[^a-zA-Z0-9]/g; 

  // removes non-alphanumerics
  stringA = stringA.replace(noNonAlpha, ""); 
  
  // returns array of new string
  var stringASplit = stringA.split("");
  var stringBSplit = [];

  // copies original array to new array in reverse order
  for (let i = 0; i < stringASplit.length; i++) { 
    stringBSplit.unshift(stringASplit[i]);
  }

  // joins new array into a string
  var stringB = stringBSplit.join(""); 

  // check if original string matches its inverse (a palindrome)
  return stringA === stringB ? true : false;

}


// Tests. First 3 should be true, last should be false.
console.log(palindrome("eye"));
console.log(palindrome("My age is 0, 0 si ega ym."));
console.log(palindrome("0_0 (: /-\ :) 0-0"));
console.log(palindrome("five|\_/|four"));
