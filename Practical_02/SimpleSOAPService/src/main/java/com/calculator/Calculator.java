package com.calculator;

import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService
public interface Calculator {
    @WebMethod
    double add(double a, double b);
    @WebMethod
    double sub(double a, double b);
    @WebMethod
    double mul(double a, double b);
    @WebMethod
    double div(double a, double b);
    @WebMethod
    long factorial(int n);
    @WebMethod
    boolean isPrime(int n);
    @WebMethod
    double square(double a);
    @WebMethod
    double largest(double a, double b);
    @WebMethod
    double addThreeNumbers(double a, double b, double c);
    @WebMethod
    double cube(double a);
}

