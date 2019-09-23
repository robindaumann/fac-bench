package main

import "math/big"
import "fmt"

func main() {
	res := big.NewInt(0)

	for i := int64(1); i <= 3000; i++ {
		x := fac_loop(i)
		res.Add(res, x)
	}

	fmt.Print(res)
}

func fac(n int64) *big.Int {
	var res big.Int

	return res.MulRange(2, n)
}

func fac_loop(n int64) *big.Int {
	res := big.NewInt(1)
	b := big.NewInt(0)

	for u := uint64(n); u > 1; u-- {
		b.SetUint64(u)
		res.Mul(res, b)
	}

	return res
}
