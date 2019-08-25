extern crate num_bigint;
extern crate num_traits;

use num_bigint::BigUint;
use num_traits::{Zero, One};

fn main() {
    let mut res: BigUint = Zero::zero();
    for i in 1..=3000 {
        res += fac(i)
    }
    print!("{}", res);
}

fn fac(n: usize) -> BigUint {
    let mut res: BigUint = One::one();
    for i in 2..=n {
        res = res * i;
    }
    res
}