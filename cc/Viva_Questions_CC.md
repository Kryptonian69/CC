# Cloud Computing & Web Services Viva Quick Reference (One-Liners)

This guide covers all key terms, acronyms, and concepts from the CC practicals.

## 1. Web Services Foundations
*   **Web Service:** A software system designed to support interoperable machine-to-machine interaction over a network.
*   **SOA (Service Oriented Architecture):** A style of software design where services are provided to the other components by application components, through a communication protocol over a network.
*   **WSDL (Web Services Description Language):** An XML-based language used for describing the functionality offered by a web service.
*   **UDDI (Universal Description, Discovery, and Integration):** An XML-based registry for businesses worldwide to list themselves on the Internet.
*   **XML (Extensible Markup Language):** A markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
*   **JSON (JavaScript Object Notation):** A lightweight data-interchange format often used in RESTful services.

## 2. SOAP (Simple Object Access Protocol)
*   **SOAP:** A protocol specification for exchanging structured information in the implementation of web services in computer networks.
*   **Envelope:** The root element of a SOAP message that defines the XML document as a SOAP message.
*   **Header:** An optional element in SOAP that contains application-specific information (e.g., authentication).
*   **Body:** The mandatory element in SOAP that contains the actual message being sent.
*   **MTOM (Message Transmission Optimization Mechanism):** A method for efficiently sending binary data to and from web services.

## 3. REST (Representational State Transfer)
*   **REST:** An architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other.
*   **Statelessness:** A core REST constraint where the server does not store any state about the client session on the server side.
*   **HTTP Methods:**
    *   **GET:** Retrieve data from a server.
    *   **POST:** Send data to a server to create a resource.
    *   **PUT:** Update an existing resource.
    *   **DELETE:** Remove a resource.
*   **Endpoint:** A specific URL where an API or service can be accessed by a client application.

## 4. Virtualization & Infrastructure
*   **Virtualization:** The process of creating a virtual version of something, such as a server, storage device, network, or operating system.
*   **Hypervisor:** A piece of computer software, firmware, or hardware that creates and runs virtual machines (e.g., KVM, VMware, Hyper-V).
*   **KVM (Kernel-based Virtual Machine):** A virtualization module in the Linux kernel that allows the kernel to function as a hypervisor.
*   **Type 1 Hypervisor:** A hypervisor that runs directly on the host's hardware (e.g., Proxmox, Xen).
*   **Type 2 Hypervisor:** A hypervisor that runs on a conventional operating system (e.g., VirtualBox, VMware Workstation).
*   **Network Bridge:** A device that connects multiple network segments together, often used in KVM to give VMs their own IP on the physical network.

## 5. Cloud Computing Models
*   **Cloud Computing:** The on-demand availability of computer system resources, especially data storage and computing power, without direct active management by the user.
*   **IaaS (Infrastructure as a Service):** Provides virtualized computing resources over the internet (e.g., AWS EC2, Openstack).
*   **PaaS (Platform as a Service):** Provides a platform allowing customers to develop, run, and manage applications without the complexity of building the infrastructure (e.g., Google App Engine, Heroku).
*   **SaaS (Software as a Service):** Provides software applications over the internet on a subscription basis (e.g., Gmail, Salesforce).
*   **Public Cloud:** Services offered by third-party providers over the public internet (e.g., AWS, Azure, GCP).
*   **Private Cloud:** Computing services offered either over the internet or a private internal network and only to select users instead of the general public.

## 6. Advanced Tools
*   **Openstack:** A free and open-source software platform for cloud computing, mostly deployed as IaaS.
*   **FOSS-Cloud:** An open-source cloud computing solution that offers VSI (Virtual Server Infrastructure).
*   **AWS Flow Framework:** A library for building distributed applications on AWS using workflows.
*   **Workflow:** A sequence of industrial, administrative, or other processes through which a piece of work passes from initiation to completion.
