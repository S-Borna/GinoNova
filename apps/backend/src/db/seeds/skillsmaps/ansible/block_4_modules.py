# =============================================================================
# BLOCK 4: MODULES & COLLECTIONS (Noder 13-16)
# =============================================================================

NODE_13_CORE_MODULES = {
    "node_id": 13,
    "title": "Core Modules Deep Dive",
    "slug": "core-modules",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [5],
    "content": '''
# Core Modules Deep Dive

Essentiella Ansible modules.

## File Modules

```yaml
# file - Manage files and directories
- name: Create directory
  file:
    path: /opt/app
    state: directory
    owner: deploy
    group: deploy
    mode: '0755'
    recurse: true

- name: Create symlink
  file:
    src: /opt/app/current
    dest: /var/www/app
    state: link

- name: Delete file
  file:
    path: /tmp/garbage
    state: absent

# lineinfile - Ensure line in file
- name: Add to config
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^PermitRootLogin'
    line: 'PermitRootLogin no'
    backup: true

# blockinfile - Insert block of text
- name: Add config block
  blockinfile:
    path: /etc/nginx/nginx.conf
    marker: "# {mark} ANSIBLE MANAGED BLOCK"
    block: |
      upstream backend {
          server 127.0.0.1:8080;
      }
```

## Command Modules

```yaml
# command - Execute command (no shell)
- name: Run script
  command: /opt/scripts/deploy.sh
  args:
    chdir: /opt/app
    creates: /opt/app/.deployed

# shell - Execute via shell
- name: Pipeline command
  shell: cat /var/log/app.log | grep ERROR | wc -l
  register: error_count

# script - Run local script remotely
- name: Run local script
  script: scripts/setup.sh
  args:
    creates: /opt/app/.setup_complete

# raw - Execute without Python
- name: Bootstrap Python
  raw: apt-get install -y python3
  when: ansible_python_interpreter is not defined
```

## System Modules

```yaml
# systemd
- name: Reload and restart
  systemd:
    name: nginx
    state: restarted
    daemon_reload: true
    enabled: true

# cron
- name: Add cron job
  cron:
    name: "Backup database"
    minute: "0"
    hour: "2"
    job: "/opt/scripts/backup.sh"
    user: postgres

# sysctl
- name: Set kernel param
  sysctl:
    name: net.ipv4.ip_forward
    value: '1'
    sysctl_set: true
    reload: true

# hostname
- name: Set hostname
  hostname:
    name: "{{ inventory_hostname }}"
```

## Package Modules

```yaml
# apt
- name: Install with apt
  apt:
    name:
      - nginx
      - python3-pip
    state: present
    update_cache: true
    cache_valid_time: 3600

# apt_repository
- name: Add repo
  apt_repository:
    repo: ppa:nginx/stable
    state: present

# pip
- name: Install Python packages
  pip:
    name:
      - flask
      - gunicorn
    virtualenv: /opt/app/venv
```

| Category | Modules |
|----------|---------|
| Files | file, copy, template, lineinfile |
| Commands | command, shell, script, raw |
| System | systemd, cron, user, group |
| Packages | apt, yum, pip, npm |
| Network | uri, get_url, firewalld |

**Nästa steg:** Node 14 - Cloud Modules
''',
}

NODE_14_CLOUD_MODULES = {
    "node_id": 14,
    "title": "Cloud Modules",
    "slug": "cloud-modules",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [13],
    "content": '''
# Cloud Modules

Ansible för AWS, Azure, GCP.

## AWS (amazon.aws collection)

```bash
# Installera
ansible-galaxy collection install amazon.aws
pip install boto3 botocore
```

```yaml
- hosts: localhost
  collections:
    - amazon.aws
  tasks:
    # EC2 Instance
    - name: Launch EC2
      amazon.aws.ec2_instance:
        name: web-server
        instance_type: t3.micro
        image_id: ami-0c55b159cbfafe1f0
        key_name: my-key
        vpc_subnet_id: subnet-123456
        security_group: web-sg
        state: running
        tags:
          Environment: production

    # S3 Bucket
    - name: Create S3 bucket
      amazon.aws.s3_bucket:
        name: my-unique-bucket
        state: present
        versioning: true

    # Security Group
    - name: Create SG
      amazon.aws.ec2_security_group:
        name: web-sg
        description: Web server SG
        vpc_id: vpc-123456
        rules:
          - proto: tcp
            ports: 80
            cidr_ip: 0.0.0.0/0
```

## Azure (azure.azcollection)

```bash
ansible-galaxy collection install azure.azcollection
pip install azure-mgmt-compute azure-identity
```

```yaml
- hosts: localhost
  collections:
    - azure.azcollection
  tasks:
    - name: Create VM
      azure.azcollection.azure_rm_virtualmachine:
        resource_group: myResourceGroup
        name: myVM
        vm_size: Standard_DS1_v2
        admin_username: azureuser
        ssh_password_enabled: false
        ssh_public_keys:
          - path: /home/azureuser/.ssh/authorized_keys
            key_data: "{{ ssh_key }}"
        image:
          offer: UbuntuServer
          publisher: Canonical
          sku: '18.04-LTS'
          version: latest
```

## GCP (google.cloud)

```bash
ansible-galaxy collection install google.cloud
pip install google-auth
```

```yaml
- hosts: localhost
  collections:
    - google.cloud
  tasks:
    - name: Create instance
      google.cloud.gcp_compute_instance:
        name: web-instance
        machine_type: n1-standard-1
        zone: europe-north1-a
        project: my-project
        auth_kind: serviceaccount
        service_account_file: /path/to/sa.json
        disks:
          - auto_delete: true
            boot: true
            initialize_params:
              source_image: projects/ubuntu-os-cloud/global/images/family/ubuntu-2004-lts
```

## Dynamic Inventory

```yaml
# aws_ec2.yml
plugin: amazon.aws.aws_ec2
regions:
  - eu-north-1
filters:
  tag:Environment: production
keyed_groups:
  - key: tags.Role
    prefix: role
compose:
  ansible_host: public_ip_address
```

```bash
ansible-inventory -i aws_ec2.yml --graph
```

| Cloud | Collection |
|-------|------------|
| AWS | amazon.aws |
| Azure | azure.azcollection |
| GCP | google.cloud |
| DigitalOcean | community.digitalocean |
| Hetzner | hetzner.hcloud |

**Nästa steg:** Node 15 - Container Modules
''',
}

NODE_15_CONTAINER_MODULES = {
    "node_id": 15,
    "title": "Container Modules",
    "slug": "container-modules",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [13],
    "content": '''
# Container Modules

Docker och Kubernetes med Ansible.

## Docker (community.docker)

```bash
ansible-galaxy collection install community.docker
pip install docker
```

```yaml
- hosts: docker_hosts
  collections:
    - community.docker
  tasks:
    # Pull image
    - name: Pull nginx image
      community.docker.docker_image:
        name: nginx
        tag: latest
        source: pull

    # Run container
    - name: Start nginx container
      community.docker.docker_container:
        name: web
        image: nginx:latest
        ports:
          - "80:80"
          - "443:443"
        volumes:
          - /opt/nginx/html:/usr/share/nginx/html:ro
        env:
          NGINX_HOST: example.com
        restart_policy: unless-stopped
        state: started

    # Docker network
    - name: Create network
      community.docker.docker_network:
        name: app_network
        driver: bridge

    # Docker compose
    - name: Deploy with compose
      community.docker.docker_compose_v2:
        project_src: /opt/app
        state: present
```

## Docker Build

```yaml
- name: Build image
  community.docker.docker_image:
    name: myapp
    tag: "{{ version }}"
    source: build
    build:
      path: /opt/app
      dockerfile: Dockerfile
      pull: true

- name: Push to registry
  community.docker.docker_image:
    name: myapp
    tag: "{{ version }}"
    repository: registry.example.com/myapp
    push: true
    source: local
```

## Kubernetes (kubernetes.core)

```bash
ansible-galaxy collection install kubernetes.core
pip install kubernetes
```

```yaml
- hosts: localhost
  collections:
    - kubernetes.core
  tasks:
    # Apply manifest
    - name: Create deployment
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: apps/v1
          kind: Deployment
          metadata:
            name: nginx
            namespace: default
          spec:
            replicas: 3
            selector:
              matchLabels:
                app: nginx
            template:
              metadata:
                labels:
                  app: nginx
              spec:
                containers:
                  - name: nginx
                    image: nginx:latest
                    ports:
                      - containerPort: 80

    # From file
    - name: Apply manifest file
      kubernetes.core.k8s:
        state: present
        src: /path/to/manifest.yml

    # Helm chart
    - name: Deploy with Helm
      kubernetes.core.helm:
        name: myrelease
        chart_ref: stable/nginx
        release_namespace: default
        values:
          replicaCount: 3
```

| Module | Funktion |
|--------|----------|
| docker_container | Hantera containers |
| docker_image | Build/pull images |
| docker_compose_v2 | Docker Compose |
| k8s | Kubernetes resources |
| helm | Helm charts |

**Nästa steg:** Node 16 - Custom Modules
''',
}

NODE_16_CUSTOM_MODULES = {
    "node_id": 16,
    "title": "Custom Modules & Plugins",
    "slug": "custom-modules",
    "estimated_minutes": 55,
    "xp_reward": 160,
    "prerequisites": [13],
    "content": '''
# Custom Modules & Plugins

Skapa egna Ansible-moduler.

## Module Basics

```python
# library/my_module.py
#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            state=dict(type='str', default='present', choices=['present', 'absent']),
        ),
        supports_check_mode=True
    )

    name = module.params['name']
    state = module.params['state']

    # Check mode
    if module.check_mode:
        module.exit_json(changed=True)

    # Din logik här
    result = dict(
        changed=True,
        name=name,
        state=state,
        message=f"Resource {name} is {state}"
    )

    module.exit_json(**result)

if __name__ == '__main__':
    main()
```

## Använda Custom Module

```yaml
# Struktur
project/
├── library/
│   └── my_module.py
└── playbook.yml
```

```yaml
# playbook.yml
- hosts: all
  tasks:
    - name: Use custom module
      my_module:
        name: test_resource
        state: present
      register: result

    - debug:
        var: result
```

## Module med API-anrop

```python
# library/api_resource.py
#!/usr/bin/python

import json
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api_url=dict(type='str', required=True),
            api_key=dict(type='str', required=True, no_log=True),
            name=dict(type='str', required=True),
            state=dict(type='str', default='present'),
        ),
    )

    headers = {
        'Authorization': f"Bearer {module.params['api_key']}",
        'Content-Type': 'application/json'
    }

    response, info = fetch_url(
        module,
        module.params['api_url'],
        headers=headers,
        method='GET'
    )

    if info['status'] != 200:
        module.fail_json(msg=f"API error: {info['status']}")

    data = json.loads(response.read())
    module.exit_json(changed=False, data=data)

if __name__ == '__main__':
    main()
```

## Custom Filter Plugin

```python
# filter_plugins/my_filters.py

def reverse_string(value):
    return value[::-1]

def add_prefix(value, prefix):
    return f"{prefix}{value}"

class FilterModule:
    def filters(self):
        return {
            'reverse_string': reverse_string,
            'add_prefix': add_prefix,
        }
```

```yaml
# Använda filter
- debug:
    msg: "{{ 'hello' | reverse_string }}"  # olleh

- debug:
    msg: "{{ 'app' | add_prefix('prod-') }}"  # prod-app
```

## Custom Lookup Plugin

```python
# lookup_plugins/my_lookup.py

from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        result = []
        for term in terms:
            result.append(term.upper())
        return result
```

```yaml
- debug:
    msg: "{{ lookup('my_lookup', 'hello') }}"  # HELLO
```

| Plugin Type | Sökväg | Användning |
|-------------|--------|-----------|
| Modules | library/ | Nya tasks |
| Filters | filter_plugins/ | Data transformation |
| Lookups | lookup_plugins/ | Data retrieval |
| Callbacks | callback_plugins/ | Output formatting |

**Nästa steg:** Node 17 - Testing Ansible
''',
}

ANSIBLE_BLOCK_4 = [
    NODE_13_CORE_MODULES,
    NODE_14_CLOUD_MODULES,
    NODE_15_CONTAINER_MODULES,
    NODE_16_CUSTOM_MODULES,
]
