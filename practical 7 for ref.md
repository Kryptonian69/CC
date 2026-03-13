# **Practical No. 7: Implementation of FOSS-Cloud Functionality for VSI and IaaS**

### **1\. Aim**

To implement FOSS-Cloud functionality to provide Virtual Server Infrastructure (VSI) and Infrastructure as a Service (IaaS) by configuring a cloud node and provisioning virtual machines.

### **2\. Prerequisites & Requirements**

* **Host Environment:** A dedicated physical node or hypervisor with sufficient resources (RAM, CPU, and Storage) to host the FOSS-Cloud server.  
* **Software:** FOSS-Cloud Server OS.  
* **Management Tools:** A modern web browser (to access the FOSS-Cloud Web Interface) and a SPICE (Simple Protocol for Independent Computing Environments) client for remote desktop access.  
* **Guest Image:** A bootable Linux ISO (e.g., Elementary OS).

### **3\. Procedure**

**Step 1: Accessing the FOSS-Cloud Dashboard**

After the initial installation of the FOSS-Cloud server node, the environment is managed remotely.

1. Open a web browser on the client machine.  
2. Enter the static IP address of the FOSS-Cloud server.  
3. Log in to the administrator portal using the default FOSS-Cloud credentials.

**Step 2: Storage and Media Management**

To provision a virtual machine, the installation media must first be available in the cloud storage pool.

1. Navigate to the **Storage** or **Media** section of the dashboard.  
2. Upload the Guest OS ISO (e.g., Elementary OS) from the local machine to the FOSS-Cloud server repository.

**Step 3: Creating a Virtual Machine Profile (IaaS Configuration)**

Infrastructure as a Service (IaaS) requires defining the hardware constraints for the virtual instances.

1. Navigate to the **Virtual Machines (VM)** section and create a new VM template.  
2. Allocate the required computing resources:  
   * **CPU Cores:** (e.g., 2 vCPUs)  
   * **Memory (RAM):** (e.g., 2048 MB)  
   * **Storage Disk:** (e.g., 20 GB Virtual Hard Drive)  
3. Attach the previously uploaded ISO file to the virtual CD/DVD drive of this profile.

**Step 4: Provisioning the Instance**

1. Select the newly created virtual machine profile.  
2. Click **Start** or **Launch** to initialize the VM on the cloud node. The FOSS-Cloud hypervisor will allocate the physical resources and boot the machine.

**Step 5: Remote Connection via SPICE Client**

1. Once the virtual machine's status shows as "Running," click the console or display icon.  
2. The FOSS-Cloud portal will generate a connection file or launch a native web-viewer using the SPICE protocol.  
3. Connect to the instance to view the live desktop environment and complete the Guest OS installation.

---

### **4\. Output / Observation**

* The FOSS-Cloud web interface successfully allowed for the centralized management of virtual resources.  
* An IaaS template was successfully created, and the virtual instance was deployed without requiring direct access to the underlying hardware.  
* The SPICE client successfully established a low-latency remote display connection to the running virtual machine.

**\[Insert your screenshot here showing the FOSS-Cloud Dashboard\]**

**\[Insert your screenshot here showing the Guest OS running via the SPICE remote connection\]**

### **5\. Conclusion**

We successfully implemented and navigated the FOSS-Cloud infrastructure. We demonstrated the core principles of Infrastructure as a Service (IaaS) and Virtual Server Infrastructure (VSI) by configuring hardware templates, managing cloud storage, and remotely provisioning a virtual machine through a web-based administration console