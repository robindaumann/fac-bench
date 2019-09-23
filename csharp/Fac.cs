using System;
using System.Numerics;

namespace csharp
{
    class Fac
    {
        static void Main(string[] args)
        {
            BigInteger res = new BigInteger(0);

            for (int i = 1; i <= 3000; i++)
            {
                res += fac(i);
            }
            Console.Write(res);
        }

        static BigInteger fac(int n)
        {
            BigInteger res = new BigInteger(1);

            for (; n > 1; n--)
            {
                res *= n;
            }

            return res;
        }
    }
}
