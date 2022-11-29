function solution(stones, k) {
  const N = stones.length;

  const check = (mid) => {
    let cnt = 0;
    for (let i = 0; i < N; i++) {
      if (stones[i] - mid >= 0) {
        cnt = 0;
      } else {
        cnt += 1;
        if (cnt === k) return false; 
      } 
    }
    return true;
  };

  let left = 1e10;
  let right = 0;

  for (let i = 0 ; i < N; i++) {
    left = Math.min(left, stones[i]);
    right = Math.max(right, stones[i]);
  }

  let maxCnt = 0;
  while (left <= right) {
    const mid = parseInt((left + right) / 2);
    if (check(mid)) {
      maxCnt = Math.max(maxCnt, mid);
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return maxCnt;
}
