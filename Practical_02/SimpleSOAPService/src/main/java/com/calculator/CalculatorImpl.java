package com.calculator;
import javax.jws.WebService;

@WebService(endpointInterface = "com.calculator.Calculator")
    public class CalculatorImpl implements Calculator {
    @Override
    public double add(double a, double b) {
        return a + b;
    }
    @Override
    public double sub(double a, double b) {
        return a - b;
    }
    @Override
    public double mul(double a, double b) {
        return a * b;
    }
    @Override
    public double div(double a, double b) {
        return a / b;
    }

    @Override
    public long factorial(int n) {
        if (n < 0) return 0;
        long fact = 1;
        for (int i = 1; i <= n; i++) fact *= i;
        return fact;
    }

    @Override
    public boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    @Override
    public double square(double a) {
        return a * a;
    }

    @Override
    public double largest(double a, double b) {
        return Math.max(a, b);
    }

    @Override
    public double addThreeNumbers(double a, double b, double c) {
        return a + b + c;
    }

    @Override
    public double cube(double a) {
        return a * a * a;
    }
}
