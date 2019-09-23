import java.math.BigInteger;

class Fac {
    public static void main(String[] args) {
        BigInteger res = BigInteger.ZERO;

        for(int i = 1; i<=3000;i++) {
            res = res.add(fac(i));
        }

        System.out.print(res);
    }

    private static BigInteger fac(int n) {
        BigInteger res = BigInteger.ONE;

        for(BigInteger big = BigInteger.valueOf(n);
            !big.equals(BigInteger.ONE);
            big = big.subtract(BigInteger.ONE)) {
            res = res.multiply(big);
        }

        return res;
    }
}