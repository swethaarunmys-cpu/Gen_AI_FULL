# Install Docker and Run docker-compose.yml on Debian (Google Cloud VM)

## Prerequisites

* Debian VM running on Google Cloud Platform (GCP)
* SSH access to the VM
* A `docker-compose.yml` file already available on the server
* External IP assigned to the VM
* Firewall rule allowing required ports (for example 80, 443, 5678, etc.)

---

# Step 1: Connect to the VM

From your local machine:

```bash
ssh username@EXTERNAL_IP
```

Example:

```bash
ssh debian@34.100.xxx.xxx
```

---

# Step 2: Update Debian

```bash
sudo apt update
sudo apt upgrade -y
```

---

# Step 3: Install Docker

```bash
sudo apt install -y ca-certificates curl gnupg lsb-release
```

Add Docker GPG key:

```bash
sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/debian/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

Add Docker repository:

```bash
echo \
"deb [arch=$(dpkg --print-architecture) \
signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/debian \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Update package list:

```bash
sudo apt update
```

Install Docker Engine:

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

---

# Step 4: Verify Installation

Check Docker:

```bash
docker --version
```

Check Compose:

```bash
docker compose version
```

Expected output:

```bash
Docker version xx.xx.xx
Docker Compose version xx.xx.xx
```

---

# Step 5: Enable Docker Service

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

Verify:

```bash
sudo systemctl status docker
```

---

# Step 6: Allow Current User to Run Docker

```bash
sudo usermod -aG docker $USER
```

Logout and reconnect:

```bash
exit
```

SSH again:

```bash
ssh username@EXTERNAL_IP
```

Verify:

```bash
docker ps
```

---

# Step 7: Navigate to Project Directory

Example:

```bash
cd ~/n8n-docker
```

Check file:

```bash
ls
```

Expected:

```bash
docker-compose.yml
```

---

# Step 8: Review External IP Configuration

Open the compose file:

```bash
nano docker-compose.yml
```

Ensure any environment variables use your VM's External IP or Domain.

Example:

```yaml
environment:
  - N8N_HOST=34.100.xxx.xxx
  - WEBHOOK_URL=http://34.100.xxx.xxx:5678/
```

If you own a domain:

```yaml
environment:
  - N8N_HOST=n8n.example.com
  - WEBHOOK_URL=https://n8n.example.com/
```

---

# Step 9: Start Containers

Run:

```bash
docker compose up -d
```

Check running containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

---

# Step 10: Verify Container

Check:

```bash
docker ps
```

You should see your container running.

---

# Step 11: Open Firewall Ports on GCP

Go to:

```text
Google Cloud Console
→ VPC Network
→ Firewall
→ Create Firewall Rule
```

Allow required ports:

| Service | Port |
| ------- | ---- |
| HTTP    | 80   |
| HTTPS   | 443  |
| n8n     | 5678 |

Example rule:

```text
Direction: Ingress
Action: Allow
Targets: All instances
Source IP Ranges: 0.0.0.0/0
Protocols and Ports:
tcp:80,tcp:443,tcp:5678
```

---

# Step 12: Access Application

If using IP:

```text
http://EXTERNAL_IP:5678
```

Example:

```text
http://34.100.xxx.xxx:5678
```

If using domain:

```text
https://your-domain.com
```

---

# Useful Commands

Start containers:

```bash
docker compose up -d
```

Stop containers:

```bash
docker compose down
```

Restart containers:

```bash
docker compose restart
```

View logs:

```bash
docker compose logs -f
```

View running containers:

```bash
docker ps
```

---

# Troubleshooting

### Docker Compose Not Found

Install plugin:

```bash
sudo apt install docker-compose-plugin -y
```

Check:

```bash
docker compose version
```

### Container Not Starting

Check logs:

```bash
docker compose logs -f
```

### Port Not Reachable

Verify:

```bash
sudo ss -tulpn | grep 5678
```

Check GCP Firewall rules.

### Verify External IP

```bash
curl ifconfig.me
```

Compare with GCP VM External IP.
