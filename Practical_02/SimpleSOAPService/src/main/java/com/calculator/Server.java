package com.calculator;

import javax.xml.ws.Endpoint;

public class Server {
    public static void main(String args[]) throws InterruptedException {
        CalculatorImpl implementor = new CalculatorImpl();
        String address = "http://localhost:8080/CalculatorService";
        Endpoint.publish(address, implementor);
        System.out.println("Server started at " + address);
        Thread.sleep(60 * 60 * 1000); 
        System.out.println("Server exiting");
        System.exit(0);
    }
}
