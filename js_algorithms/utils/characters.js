/**
 * isalnum checks if the string contains only alphanumeric characters.
 *
 * @param {string} s
 * @return {boolean}
 */
function isalnum(s) {
  return isalpha(s) || isdigit(s);
}

/**
 * isdigit checks if a singular character is numeric.
 *
 * @param {string} s
 * @return {boolean}
 */
function isdigit(s) {
  const ascii = s.charCodeAt(0);
  return ascii >= 48 && ascii <= 57;
}

/**
 * isalpha checks if a singular character is alphabetic
 *
 * @param s
 * @return {boolean}
 */
function isalpha(s) {
  return islower(s) || isupper(s);
}

/**
 * islower checks if a singular character is alphabetic
 *
 * @param s
 * @return {boolean}
 */
function islower(s) {
  const ascii = s.charCodeAt(0);
  return ascii >= 97 && ascii <= 122;
}

/**
 * isupper checks if a singular character is alphabetic
 *
 * @param s
 * @return {boolean}
 */
function isupper(s) {
  const ascii = s.charCodeAt(0);
  return ascii >= 65 && ascii <= 90;
}

module.exports = {
  isalnum,
  isalpha,
  isupper,
  islower,
  isdigit,
};
