# **Practical No. 8: Implementation of FOSS-Cloud Functionality for PaaS**

### **1. Aim**
To implement FOSS-Cloud Platform as a Service (PaaS) functionality by deploying applications with integrated runtime environments and database services using a Java-based Platform Console.

### **2. Prerequisites & Requirements**
* **Host Environment:** A system with Java Development Kit (JDK) installed.
* **Software:** Java Compiler (`javac`) and Java Runtime Environment (`java`).
* **Source Code:** `PAASConsole.java` and `FOSSPlatform.class`.
* **Hardware:** Sufficient resources to simulate a multi-instance application deployment.

### **3. Procedure**

**Step 1: Preparing the PaaS Environment**
1. Ensure the `PAASConsole.java` file is present in your working directory.
2. Open a terminal or command prompt and navigate to the directory containing the file.
3. Compile the Java source code:
   ```bash
   javac PAASConsole.java
   ```

**Step 2: Accessing the FOSS-Cloud Platform Console**
1. Execute the compiled class to launch the FOSS-Cloud PaaS management simulator:
   ```bash
   java PAASConsole
   ```
2. The console will initialize the connection and load the platform environment.

**Step 3: Platform Connection and Authentication**
1. When prompted, enter the **Platform Connection Address** (e.g., `paas.cloud.local`).
2. Provide the administrator credentials for the platform portal:
   * **Username:** `admin`
   * **Password:** `cloud123`
3. Upon successful authentication, the system grants access to application deployment services.

**Step 4: Application Deployment and Runtime Configuration**
1. Enter the **Application Name** (e.g., `CloudStoreApp`).
2. Select the required **Runtime Environment** from the provided options:
   * (e.g., `Java (Tomcat)`, `Node.js`, `Python (Django)`, or `PHP`)
3. Specify the number of **Application Instances** to deploy for horizontal scaling (e.g., `3`).

**Step 5: Database and Storage Service Configuration**
1. Select an available **Database Service** to integrate with the application (e.g., `MySQL` or `PostgreSQL`).
2. Specify the amount of additional **Storage (GB)** to allocate for the application's persistent data (e.g., `10`).
3. The platform will finalize the configuration and display the complete deployment status.

---

### **4. Output / Observation**
* The `PAASConsole` successfully managed the lifecycle of a cloud-native application deployment.
* The platform automatically configured the selected runtime and database service.
* A final status report was generated, summarizing the App Name, Runtime, Database, Instances, and total Storage allocated.

**[Insert your screenshot here showing the PAASConsole terminal output with the Final Platform Status]**

### **5. Conclusion**
We successfully implemented the Platform as a Service (PaaS) functionality within the FOSS-Cloud environment. We demonstrated the ability to provision isolated application runtimes, scale instances, and integrate database services through a centralized management interface.
