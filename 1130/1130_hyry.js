const solution = (n, left, right) => {
  /*     01234
  12345 /22345 /33345 /44445/55555
  01234 56789 1011121314 1516171819 2021222324 ... 01234
  몫 m 0     1     2       3      4  ... m까지는 첫 숫자
  ... 이후부터는 나머지 - m 만큼 더하기
  첫 숫자 m + 1
  */
  const arr = [];
  for (let i = left; i < right + 1; i++) {
      const mok = Math.floor(i / n);
      const nameoji = i % n;
      const num = mok + 1 + (nameoji <= mok ? 0 : (nameoji - mok));
      arr.push(num); 
  }
  return arr;
}
