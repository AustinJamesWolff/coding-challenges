function telephoneCheck(str) {

  // Create a regex that checks for US valid phone numbers in any format
  var regex = /^(1)?\s*(\d{3}|\(\d{3}\))\s*-?(\d{3})\s*-?(\d){4}$/g;

  return regex.test(str);
}

// Test
console.log(telephoneCheck("555-555-5555"));
console.log(telephoneCheck("1(555)555-5555"));
console.log(telephoneCheck("0 (757) 622-7382"));
console.log(telephoneCheck("-1 (757) 622-7382"));
