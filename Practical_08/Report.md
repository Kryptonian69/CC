# Practical 8: Implementation of FOSS-Cloud Functionality for PaaS
**Aim:** To implement FOSS-Cloud PaaS functionality by deploying apps with runtime and database services.
**Prerequisites:** JDK, `PAASConsole.java`.
**Procedure:**
1. **Prepare:** Ensure `PAASConsole.java` is present. Compile: `javac PAASConsole.java`.
2. **Launch:** Run `java PAASConsole`.
3. **Connect/Auth:** Enter address (e.g., `paas.cloud.local`) and credentials (`admin` / `cloud123`).
4. **Deploy:** Enter App Name, select Runtime (e.g., `Java (Tomcat)`), and specify instances.
5. **Config:** Choose Database (e.g., `MySQL`) and allocate Storage (GB).

### 6. Source Code (PAASConsole.java)
Copy the code from `PAASConsole.java` into this section.

**Output:** The `PAASConsole` managed the lifecycle of a cloud-native app deployment. A status report summarized the App Name, Runtime, Database, Instances, and Storage.
**[Insert your screenshot here showing the PAASConsole terminal output with the Final Platform Status]**
**Conclusion:** We successfully implemented PaaS functionality in FOSS-Cloud, demonstrating runtime provisioning and database integration.
