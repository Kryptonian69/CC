import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;

public class PrimeClient {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to check if it's prime: ");
        int num = sc.nextInt();

        HttpClient client = HttpClient.newHttpClient();
        String uri = "http://localhost:3000/convert";
        String requestBody = "{ \"number_to_check_prime\": " + num + " }";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(uri))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(requestBody))
                .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Result (Is Prime?): " + response.body());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
