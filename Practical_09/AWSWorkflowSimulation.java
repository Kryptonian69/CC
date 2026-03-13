import java.util.Scanner;

class AWSWorkflow {
    void defineContract() {
        System.out.println("\n[Workflow] Step 1: Defining Activity Contracts...");
        System.out.println("Contract Created: Interface GreeterActivity { void printHello(); }");
    }

    void implementActivity() {
        System.out.println("[Activity] Step 2: Implementing GreeterActivity...");
        System.out.println("Logic: System.out.println(\"Hello World\");");
    }

    void coordinateWorkflow() {
        System.out.println("[Coordinator] Step 3: Initializing Coordination Logic...");
        System.out.println("Scheduling GreeterActivity execution...");
    }

    void startWorker() {
        System.out.println("[Worker] Step 4: Starting Worker Program...");
        System.out.println("Worker is now polling for tasks from AWS SWF...");
    }

    void execute() {
        System.out.println("\n=== WORKFLOW EXECUTION START ===");
        System.out.println("GreeterActivity: Hello World");
        System.out.println("=== WORKFLOW EXECUTION COMPLETED ===");
    }
}

public class AWSWorkflowSimulation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        AWSWorkflow aws = new AWSWorkflow();

        System.out.println("=== AWS Flow Framework Simulation ===");
        System.out.println("This program simulates the AWS Flow Framework lifecycle.");
        System.out.print("\nPress Enter to start the automated AWS Flow process...");
        sc.nextLine();

        aws.defineContract();
        aws.implementActivity();
        aws.coordinateWorkflow();
        aws.startWorker();
        aws.execute();
    }
}
