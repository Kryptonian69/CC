import java.util.Scanner;

class FOSSCloudMultiUser {

    String connection = "Default-Cloud";
    String correctUser = "admin";
    String correctPass = "cloud123";

    String vsiName;
    int cpu, ram, storage;

    Scanner sc = new Scanner(System.in);

    void openCloud() {
        System.out.println("\nConnecting to FOSS Cloud...");
        System.out.println("Cloud Environment Loaded");
    }

    void changeConnection() {
        System.out.print("\nEnter Cloud Connection Address: ");
        connection = sc.next();
        System.out.println("Connected to: " + connection);
    }

    boolean authentication() {
        System.out.println("\n=== CLOUD AUTHENTICATION ===");
        System.out.print("Username: ");
        String u = sc.next();
        System.out.print("Password: ");
        String p = sc.next();

        if(u.equals(correctUser) && p.equals(correctPass)) {
            System.out.println("Login Successful");
            return true;
        } else {
            System.out.println("Authentication Failed");
            return false;
        }
    }

    void createVSI() {
        System.out.println("\n=== CREATE VSI ===");
        System.out.print("Enter VSI Name: ");
        vsiName = sc.next();
        System.out.print("CPU cores: ");
        cpu = sc.nextInt();
        System.out.print("RAM (GB): ");
        ram = sc.nextInt();
        storage = 10;
        System.out.println("VSI Created Successfully");
    }

    void createUsers() {
        System.out.println("\n=== USER MANAGEMENT ===");
        System.out.print("How many users to create? (min 2): ");
        int n = sc.nextInt();
        for(int i=1; i<=n; i++) {
            System.out.print("Enter name for User " + i + ": ");
            String name = sc.next();
            System.out.println("User '" + name + "' successfully created in VM.");
        }
    }

    void showResult() {
        System.out.println("\n===== FINAL CLOUD STATUS =====");
        System.out.println("Connection : " + connection);
        System.out.println("VSI Name   : " + vsiName);
        System.out.println("CPU        : " + cpu + " cores");
        System.out.println("RAM        : " + ram + " GB");
        System.out.println("Cloud Deployment Completed with Multiple Users");
    }
}

public class CloudConsoleMultiUser {
    public static void main(String[] args) {
        FOSSCloudMultiUser cloud = new FOSSCloudMultiUser();
        cloud.openCloud();
        cloud.changeConnection();

        if(cloud.authentication()) {
            cloud.createVSI();
            cloud.createUsers();
            cloud.showResult();
        } else {
            System.out.println("Access Denied");
        }
    }
}
