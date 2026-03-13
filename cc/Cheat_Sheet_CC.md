# Cloud Computing & Web Services Practical Cheat Sheet

Use this guide to quickly identify which practical folder to use based on the keywords in your exam slip and what specific changes you need to make.

| Exam Question Keywords | Use This Folder | Key Changes Needed |
| :--- | :--- | :--- |
| "Currency Conversion", "Rupees to Dollar", "1 USD = 75 INR", "Java Client", ".NET Client" | **Practical_01** | Update `conversionRate` in `server.js`; update `amount_in_rs` in `JavaClient.java` or `Program.cs`. |
| "Fahrenheit to Celsius", "Temperature Conversion", "Formula: C = (F - 32) * 5/9" | **Practical_01** | Modify `server.js` logic to the temperature formula; update client request variable names. |
| "Factorial", "Prime Number", "Logic in Web Service", "JAVA / .NET interface" | **Practical_01** | Replace the conversion logic in `server.js` with a loop for Factorial or a Prime check function. |
| "Simple SOAP Service", "Multiplication", "Addition of three numbers", "Calculator", "Square", "Cube" | **Practical_02** | Update the `@WebMethod` logic in the Java file (e.g., `return a * b;` or `return n * n;`). |
| "REST Service", "CRUD", "Student", "Employee", "Product", "Player", "City", "Database" | **Practical_03** | Update the data dictionary/list in `app.py` with the fields mentioned (e.g., `Name`, `Age`, `Department`). |
| "Google Search API", "Google Map RESTful", "Consume Web Service" | **Practical_04** | Update the API endpoint URL or the search query parameters in `map_search.py`. |
| "MTOM", "Upload image/video", "Download image/video", "Message Transmission Optimization" | **Practical_06** | Change the file types allowed or the `uploads/` path in `server.js`. |
| "KVM", "Virtual Machine", "Network Bridge", "TrueConf Server", "Proxmox" | **Practical_07** | Follow the steps in `instructions.md`. Change the VM Name, RAM (Memory), or ISO file path in the GUI. |
| "FOSS-Cloud", "VSI", "Virtual Server Infrastructure", "Storage pool", "Create users" | **Practical7fake** | Update `CloudConsole.java` or `VSI` logic to match the requested number of users or memory size. |
| "Openstack", "Private network creation", "User creation in Openstack" | **Practical_09** | Refer to `prac.txt` or `Practical_09_Report.md` for the specific CLI commands or setup steps. |
| "AWS Flow Framework", "Hello World workflow", "Activities", "Coordination logic" | **Practical_08** | Update the string in `PAASConsole.java` from "Hello World" to whatever the slip asks for. |

---
### Quick Tip for the Exam:
*   **For Web Services (P1-P3):** Most logic changes happen in the `server.js` (Node), `app.py` (Python), or the main `.java` file in the SOAP service.
*   **For Clients:** Ensure the port number in your client matches the port the service is running on (usually 3000, 5000, or 8080).
*   **For Cloud (P7-P9):** These are usually configuration-heavy. Keep your `instructions.md` or `Reports` open to copy-paste commands.
