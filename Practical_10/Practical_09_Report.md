# Practical No. 9: Implementation of OpenStack with User and Private Network Creation

## 1. Aim
To implement OpenStack with user and private network creation using DevStack in a WSL environment.

## 2. Prerequisites & Requirements
- **Operating System:** Ubuntu 24.04 LTS (Running in WSL2)
- **Hardware:** WSL2 VM with approximately 8GB total physical memory (DevStack requires at least 4GB).
- **Network:** Stable internet connection for downloading OpenStack components and repositories.
- **Disk Space:** At least 20GB of free space.

## 3. Procedure

### Step 1: Update the Ubuntu System
Open the WSL Ubuntu terminal and update the package repositories and installed packages.
```bash
sudo apt update
sudo apt -y upgrade
sudo apt -y dist-upgrade
```
Note: In WSL, instead of `sudo reboot`, we restart the WSL instance using `wsl --terminate <distro>` from a PowerShell terminal and then restart it.

### Step 2: Create a Dedicated "Stack" User
DevStack must be run as a regular user with sudo privileges. Create a new user specifically named `stack`:
```bash
sudo useradd -s /bin/bash -d /opt/stack -m stack
```
Assign password-less sudo privileges to the `stack` user:
```bash
echo "stack ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/stack
```
Switch to the `stack` user:
```bash
sudo su - stack
```

### Step 3: Install Git
Ensure Git is installed to clone the DevStack repository:
```bash
sudo apt install git -y
```

### Step 4: Download OpenStack (DevStack)
Clone the DevStack repository from GitHub:
```bash
cd /opt/stack
sudo git clone https://opendev.org/openstack/devstack
sudo chown -R stack:stack devstack
cd devstack
```

### Step 5: Create the Configuration File
Create a `local.conf` file in the `devstack` directory to store administrative passwords and the host system's IP address.
```bash
cat <<EOF > local.conf
[[local|localrc]]
# Password for KeyStone, Database, RabbitMQ and Service
ADMIN_PASSWORD=StrongAdminSecret
DATABASE_PASSWORD=\$ADMIN_PASSWORD
RABBIT_PASSWORD=\$ADMIN_PASSWORD
SERVICE_PASSWORD=\$ADMIN_PASSWORD

# Host IP (Retrieve from 'hostname -I')
HOST_IP=172.25.45.203
EOF
```

### Step 6: Execute the Installation
Start the automated DevStack installation:
```bash
./stack.sh
```
The script installs Nova (Compute), Glance (Image Service), Keystone (Identity), Cinder (Block Storage), and the Horizon Dashboard. This takes approximately 10-20 minutes.

### Step 7: Access the OpenStack Dashboard
Once the installation is complete, the terminal provides an access link. Open a browser and navigate to the Horizon Dashboard:
`http://<WSL_IP_Address>/dashboard`
Log in with the username `admin` and the password `StrongAdminSecret`.

### Step 8: Provision an Instance
1. Log into the Horizon Dashboard.
2. Navigate to **Project > Compute > Instances**.
3. Click **Launch Instance**.
4. Configure the instance (Name, Image, Flavor, Network) and deploy it.

## 4. Output / Observation
- The `stack.sh` script successfully installed core OpenStack services (Nova, Glance, Keystone).
- The Horizon Dashboard was accessible at `http://172.25.45.203/dashboard`.
- A virtual machine instance was provisioned via the web interface.

## 5. Conclusion
We successfully installed and configured a single-node OpenStack cloud environment using DevStack on a WSL instance. We learned how to manage users, configure cloud parameters, and access the Horizon management dashboard to deploy instances.
