function convertToRoman(num) {

  // Create an object for later conversion
  var romanNums = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    20: "XX",
    30: "XXX",
    40: "XL",
    50: "L",
    60: "LX",
    70: "LXX",
    80: "LXXX",
    90: "XC",
    100: "C",
    200: "CC",
    300: "CCC",
    400: "CD",
    500: "D",
    600: "DC",
    700: "DCC",
    800: "DCCC",
    900: "CM",
    1000: "M",
    2000: "MM",
    3000: "MMM",
  };

  // Convert number to an array
  var numArray = String(num).split("").map(function(x) {
    return Number(x);
  });
  console.log(numArray);

  //  Reverse the order of the array, explanation below
  var reverseArr = [];
  for (let i = 0; i < numArray.length; i++) {
    reverseArr.unshift(numArray[i]);
  }
  console.log(reverseArr);

  // Turn each digit into it's appropriate number
  var x = 1;
  for (let i = 0; i < reverseArr.length; i++) {
    reverseArr[i] = reverseArr[i] * x;
    x = x * 10;
  }
  console.log(reverseArr);

  // Convert the reversed array back to its original position with Roman numeral conversion
  var origArr = [];
  for (let i = 0; i < reverseArr.length; i++) {
    origArr.unshift(romanNums[reverseArr[i]]);
  }  
  console.log(origArr);

  // Combine the Roman numerals and return
  return origArr.join("");
}

// Test
console.log(convertToRoman(2014));
