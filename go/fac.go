package main

import "math/big"
import "fmt"

func main() {
	var res big.Int

	for i := int64(1); i<=3000;i++ {
		x := fac(i)
		res.Add(&res, x)
	}
	
	fmt.Print(&res)
}

func fac(n int64) *big.Int {
	var res big.Int

	return res.MulRange(2, n)
}

func fac_loop(n int64) *big.Int {
	res := big.NewInt(1)

	for ;n>1;n-- {
		x := big.NewInt(n)
		res.Mul(res, x)
	}
	return res
}