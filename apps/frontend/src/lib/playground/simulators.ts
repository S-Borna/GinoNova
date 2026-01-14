/**
 * ============================================================================
 * PLAYGROUND ENVIRONMENT SIMULATORS
 * ============================================================================
 *
 * Simulates various DevOps environments for in-browser practice:
 * - Bash Terminal
 * - Python Executor
 * - Docker Commands
 * - Kubernetes YAML Validator
 * - Terraform HCL Validator
 *
 * @phase PLAYGROUND
 */

export type EnvironmentType = 'bash' | 'python' | 'docker' | 'kubernetes' | 'terraform'

export interface SimulationResult {
    output: string
    error?: string
    exitCode: number
    stdout?: string
    stderr?: string
}

/* ============================================================================
   BASH SIMULATOR
   ============================================================================ */

interface FileSystemEntry {
    name: string
    type: 'file' | 'directory'
    size?: number
    modified?: string
    content?: string
    permissions?: string
}

class BashSimulator {
    private currentDir = '/home/devops'
    private fileSystem: Record<string, FileSystemEntry[]> = {
        '/home/devops': [
            { name: 'projects', type: 'directory', permissions: 'drwxr-xr-x', modified: 'Jan 13 10:30' },
            { name: 'scripts', type: 'directory', permissions: 'drwxr-xr-x', modified: 'Jan 12 14:20' },
            { name: 'README.md', type: 'file', size: 1234, permissions: '-rw-r--r--', modified: 'Jan 13 09:15', content: '# Welcome to DevOps Playground\n\nThis is a simulated environment for learning DevOps commands.' },
            { name: '.bashrc', type: 'file', size: 890, permissions: '-rw-r--r--', modified: 'Jan 10 08:00' },
            { name: 'data.txt', type: 'file', size: 456, permissions: '-rw-r--r--', modified: 'Jan 11 15:30', content: 'Sample data file\nLine 2\nLine 3' },
        ],
        '/home/devops/projects': [
            { name: 'webapp', type: 'directory', permissions: 'drwxr-xr-x', modified: 'Jan 13 10:30' },
            { name: 'api', type: 'directory', permissions: 'drwxr-xr-x', modified: 'Jan 12 11:00' },
            { name: 'package.json', type: 'file', size: 567, permissions: '-rw-r--r--', modified: 'Jan 13 10:25' },
        ],
        '/home/devops/scripts': [
            { name: 'deploy.sh', type: 'file', size: 2345, permissions: '-rwxr-xr-x', modified: 'Jan 12 14:20', content: '#!/bin/bash\necho "Deploying application..."' },
            { name: 'backup.sh', type: 'file', size: 1890, permissions: '-rwxr-xr-x', modified: 'Jan 11 16:45' },
        ],
    }

    private environment: Record<string, string> = {
        USER: 'devops',
        HOME: '/home/devops',
        PATH: '/usr/local/bin:/usr/bin:/bin',
        SHELL: '/bin/bash',
        PWD: '/home/devops',
    }

    execute(command: string): SimulationResult {
        const trimmedCmd = command.trim()

        if (!trimmedCmd) {
            return { output: '', exitCode: 0 }
        }

        // Parse command and arguments
        const parts = trimmedCmd.split(/\s+/)
        const cmd = parts[0]
        const args = parts.slice(1)

        // Route to appropriate handler
        switch (cmd) {
            case 'ls':
                return this.handleLs(args)
            case 'pwd':
                return this.handlePwd()
            case 'cd':
                return this.handleCd(args)
            case 'cat':
                return this.handleCat(args)
            case 'echo':
                return this.handleEcho(args)
            case 'whoami':
                return this.handleWhoami()
            case 'date':
                return this.handleDate()
            case 'uname':
                return this.handleUname(args)
            case 'grep':
                return this.handleGrep(args)
            case 'find':
                return this.handleFind(args)
            case 'mkdir':
                return this.handleMkdir(args)
            case 'touch':
                return this.handleTouch(args)
            case 'rm':
                return this.handleRm(args)
            case 'clear':
                return { output: '__CLEAR__', exitCode: 0 }
            case 'help':
                return this.handleHelp()
            default:
                return {
                    output: `bash: ${cmd}: command not found`,
                    error: `bash: ${cmd}: command not found`,
                    exitCode: 127
                }
        }
    }

    private handleLs(args: string[]): SimulationResult {
        const showAll = args.includes('-a') || args.includes('-la') || args.includes('-al')
        const longFormat = args.includes('-l') || args.includes('-la') || args.includes('-al')

        const entries = this.fileSystem[this.currentDir] || []

        if (longFormat) {
            let output = 'total 24\n'
            if (showAll) {
                output += 'drwxr-xr-x  5 devops devops 4096 Jan 13 10:30 .\n'
                output += 'drwxr-xr-x  3 root   root   4096 Jan 10 08:00 ..\n'
            }
            entries.forEach(entry => {
                const size = entry.size || 4096
                const perms = entry.permissions || (entry.type === 'directory' ? 'drwxr-xr-x' : '-rw-r--r--')
                const date = entry.modified || 'Jan 13 10:30'
                output += `${perms}  1 devops devops ${size.toString().padStart(5)} ${date} ${entry.name}\n`
            })
            return { output, exitCode: 0 }
        } else {
            const names = entries.map(e => e.name).join('  ')
            return { output: names, exitCode: 0 }
        }
    }

    private handlePwd(): SimulationResult {
        return { output: this.currentDir, exitCode: 0 }
    }

    private handleCd(args: string[]): SimulationResult {
        if (args.length === 0) {
            this.currentDir = '/home/devops'
            return { output: '', exitCode: 0 }
        }

        const target = args[0]
        let newPath: string

        if (target.startsWith('/')) {
            newPath = target
        } else if (target === '..') {
            const parts = this.currentDir.split('/').filter(p => p)
            parts.pop()
            newPath = '/' + parts.join('/')
        } else if (target === '.') {
            newPath = this.currentDir
        } else {
            newPath = `${this.currentDir}/${target}`.replace(/\/+/g, '/')
        }

        if (this.fileSystem[newPath]) {
            this.currentDir = newPath
            this.environment.PWD = newPath
            return { output: '', exitCode: 0 }
        } else {
            return {
                output: `bash: cd: ${target}: No such file or directory`,
                error: `bash: cd: ${target}: No such file or directory`,
                exitCode: 1
            }
        }
    }

    private handleCat(args: string[]): SimulationResult {
        if (args.length === 0) {
            return {
                output: 'cat: missing operand\nTry \'cat --help\' for more information.',
                exitCode: 1
            }
        }

        const fileName = args[0]
        const entries = this.fileSystem[this.currentDir] || []
        const file = entries.find(e => e.name === fileName && e.type === 'file')

        if (file && file.content) {
            return { output: file.content, exitCode: 0 }
        } else if (file) {
            return { output: `[Binary file or no content available]`, exitCode: 0 }
        } else {
            return {
                output: `cat: ${fileName}: No such file or directory`,
                error: `cat: ${fileName}: No such file or directory`,
                exitCode: 1
            }
        }
    }

    private handleEcho(args: string[]): SimulationResult {
        let output = args.join(' ')

        // Handle environment variables
        output = output.replace(/\$(\w+)/g, (match, varName) => {
            return this.environment[varName] || ''
        })

        return { output, exitCode: 0 }
    }

    private handleWhoami(): SimulationResult {
        return { output: 'devops', exitCode: 0 }
    }

    private handleDate(): SimulationResult {
        return { output: new Date().toString(), exitCode: 0 }
    }

    private handleUname(args: string[]): SimulationResult {
        if (args.includes('-a')) {
            return {
                output: 'Linux devops-playground 5.15.0-generic #1 SMP Wed Jan 10 12:00:00 UTC 2024 x86_64 GNU/Linux',
                exitCode: 0
            }
        }
        return { output: 'Linux', exitCode: 0 }
    }

    private handleGrep(args: string[]): SimulationResult {
        if (args.length < 2) {
            return {
                output: 'grep: missing pattern or file',
                exitCode: 2
            }
        }
        // Simplified grep simulation
        return {
            output: 'grep: simulated search - pattern matching would happen here',
            exitCode: 0
        }
    }

    private handleFind(args: string[]): SimulationResult {
        const entries = this.fileSystem[this.currentDir] || []
        const output = entries.map(e => `./${e.name}`).join('\n')
        return { output, exitCode: 0 }
    }

    private handleMkdir(args: string[]): SimulationResult {
        if (args.length === 0) {
            return { output: 'mkdir: missing operand', exitCode: 1 }
        }
        return { output: '', exitCode: 0 }
    }

    private handleTouch(args: string[]): SimulationResult {
        if (args.length === 0) {
            return { output: 'touch: missing file operand', exitCode: 1 }
        }
        return { output: '', exitCode: 0 }
    }

    private handleRm(args: string[]): SimulationResult {
        if (args.length === 0) {
            return { output: 'rm: missing operand', exitCode: 1 }
        }
        return { output: '', exitCode: 0 }
    }

    private handleHelp(): SimulationResult {
        return {
            output: `Available commands:
  ls [-la]          - List directory contents
  pwd               - Print working directory
  cd <dir>          - Change directory
  cat <file>        - Display file contents
  echo <text>       - Display text
  whoami            - Print current user
  date              - Display current date and time
  uname [-a]        - Print system information
  grep <pattern>    - Search for patterns
  find              - Find files
  mkdir <dir>       - Create directory
  touch <file>      - Create empty file
  rm <file>         - Remove file
  clear             - Clear terminal
  help              - Show this help message`,
            exitCode: 0
        }
    }
}

/* ============================================================================
   DOCKER SIMULATOR
   ============================================================================ */

class DockerSimulator {
    private containers = [
        { id: 'a1b2c3d4', name: 'webapp', image: 'nginx:latest', status: 'Up 2 hours', ports: '0.0.0.0:8080->80/tcp' },
        { id: 'e5f6g7h8', name: 'database', image: 'postgres:14', status: 'Up 5 hours', ports: '5432/tcp' },
    ]

    private images = [
        { repository: 'nginx', tag: 'latest', id: 'abc123def456', created: '2 weeks ago', size: '142MB' },
        { repository: 'postgres', tag: '14', id: 'ghi789jkl012', created: '3 weeks ago', size: '376MB' },
        { repository: 'node', tag: '18-alpine', id: 'mno345pqr678', created: '1 week ago', size: '174MB' },
    ]

    execute(command: string): SimulationResult {
        const parts = command.trim().split(/\s+/)

        if (parts[0] !== 'docker') {
            return {
                output: 'Command must start with "docker"',
                exitCode: 1
            }
        }

        const subcommand = parts[1]
        const args = parts.slice(2)

        switch (subcommand) {
            case 'ps':
                return this.handlePs(args)
            case 'images':
                return this.handleImages()
            case 'run':
                return this.handleRun(args)
            case 'stop':
                return this.handleStop(args)
            case 'rm':
                return this.handleRm(args)
            case 'pull':
                return this.handlePull(args)
            case 'build':
                return this.handleBuild(args)
            case 'logs':
                return this.handleLogs(args)
            case 'exec':
                return this.handleExec(args)
            case '--version':
            case 'version':
                return { output: 'Docker version 24.0.7, build afdd53b', exitCode: 0 }
            case 'help':
                return this.handleHelp()
            default:
                return {
                    output: `docker: '${subcommand}' is not a docker command.\nSee 'docker --help'`,
                    exitCode: 1
                }
        }
    }

    private handlePs(args: string[]): SimulationResult {
        const showAll = args.includes('-a') || args.includes('--all')

        let output = 'CONTAINER ID   IMAGE              COMMAND                  CREATED        STATUS         PORTS                    NAMES\n'
        this.containers.forEach(c => {
            output += `${c.id}       ${c.image.padEnd(18)} "docker-entrypoint.s…"   2 hours ago    ${c.status.padEnd(14)} ${c.ports.padEnd(24)} ${c.name}\n`
        })

        return { output, exitCode: 0 }
    }

    private handleImages(): SimulationResult {
        let output = 'REPOSITORY   TAG          IMAGE ID       CREATED        SIZE\n'
        this.images.forEach(img => {
            output += `${img.repository.padEnd(12)} ${img.tag.padEnd(12)} ${img.id}   ${img.created.padEnd(14)} ${img.size}\n`
        })
        return { output, exitCode: 0 }
    }

    private handleRun(args: string[]): SimulationResult {
        if (args.length === 0) {
            return { output: 'docker: "run" requires at least 1 argument.', exitCode: 125 }
        }
        const image = args[args.length - 1]
        const containerId = Math.random().toString(36).substr(2, 12)
        return {
            output: `${containerId}\nContainer started successfully!`,
            exitCode: 0
        }
    }

    private handleStop(args: string[]): SimulationResult {
        if (args.length === 0) {
            return { output: 'docker: "stop" requires at least 1 argument.', exitCode: 125 }
        }
        return { output: args[0], exitCode: 0 }
    }

    private handleRm(args: string[]): SimulationResult {
        if (args.length === 0) {
            return { output: 'docker: "rm" requires at least 1 argument.', exitCode: 125 }
        }
        return { output: args[0], exitCode: 0 }
    }

    private handlePull(args: string[]): SimulationResult {
        if (args.length === 0) {
            return { output: 'docker: "pull" requires at least 1 argument.', exitCode: 125 }
        }
        const image = args[0]
        return {
            output: `Using default tag: latest
latest: Pulling from library/${image}
Digest: sha256:abc123...
Status: Downloaded newer image for ${image}:latest`,
            exitCode: 0
        }
    }

    private handleBuild(args: string[]): SimulationResult {
        return {
            output: `[+] Building 2.3s (8/8) FINISHED
 => [internal] load build definition
 => => transferring dockerfile
 => [internal] load .dockerignore
 => [1/3] FROM docker.io/library/node:18-alpine
 => [2/3] WORKDIR /app
 => [3/3] COPY package*.json ./
 => exporting to image
 => => exporting layers
 => => writing image sha256:abc123...
Successfully built abc123def456`,
            exitCode: 0
        }
    }

    private handleLogs(args: string[]): SimulationResult {
        if (args.length === 0) {
            return { output: 'docker: "logs" requires at least 1 argument.', exitCode: 125 }
        }
        return {
            output: `2024-01-13T10:30:00.000Z Server started on port 3000
2024-01-13T10:30:05.000Z Database connected
2024-01-13T10:31:00.000Z Received request GET /api/health`,
            exitCode: 0
        }
    }

    private handleExec(args: string[]): SimulationResult {
        if (args.length < 2) {
            return { output: 'docker: "exec" requires at least 2 arguments.', exitCode: 125 }
        }
        return { output: 'Command executed in container', exitCode: 0 }
    }

    private handleHelp(): SimulationResult {
        return {
            output: `Docker Commands:
  ps              List containers
  images          List images
  run             Run a command in a new container
  stop            Stop one or more running containers
  rm              Remove one or more containers
  pull            Pull an image from a registry
  build           Build an image from a Dockerfile
  logs            Fetch the logs of a container
  exec            Run a command in a running container
  version         Show the Docker version information`,
            exitCode: 0
        }
    }
}

/* ============================================================================
   KUBERNETES YAML VALIDATOR
   ============================================================================ */

export function validateKubernetesYAML(yaml: string): SimulationResult {
    try {
        // Basic YAML structure check
        const lines = yaml.split('\n')
        const errors: string[] = []

        // Check for required fields in a Deployment
        if (yaml.includes('kind: Deployment')) {
            if (!yaml.includes('apiVersion:')) {
                errors.push('Missing required field: apiVersion')
            }
            if (!yaml.includes('metadata:')) {
                errors.push('Missing required field: metadata')
            }
            if (!yaml.includes('spec:')) {
                errors.push('Missing required field: spec')
            }
            if (yaml.includes('spec:') && !yaml.includes('replicas:')) {
                errors.push('Warning: replicas not specified (will default to 1)')
            }
            if (!yaml.includes('selector:')) {
                errors.push('Missing required field: spec.selector')
            }
            if (!yaml.includes('template:')) {
                errors.push('Missing required field: spec.template')
            }
        }

        // Check for required fields in a Service
        if (yaml.includes('kind: Service')) {
            if (!yaml.includes('ports:')) {
                errors.push('Missing required field: spec.ports')
            }
        }

        // Check for common mistakes
        if (yaml.includes('image:') && yaml.match(/image:\s*$/m)) {
            errors.push('image field is empty')
        }

        // Check indentation issues
        let prevIndent = 0
        lines.forEach((line, idx) => {
            if (line.trim() && !line.trim().startsWith('#')) {
                const indent = line.search(/\S/)
                if (indent > 0 && indent % 2 !== 0) {
                    errors.push(`Line ${idx + 1}: Invalid indentation (should be multiples of 2)`)
                }
            }
        })

        if (errors.length > 0) {
            return {
                output: '',
                error: 'Validation Errors:\n' + errors.map(e => `  • ${e}`).join('\n'),
                exitCode: 1
            }
        }

        return {
            output: `✓ YAML validation successful!

Kubernetes resources found:
${yaml.includes('kind: Deployment') ? '  • Deployment' : ''}
${yaml.includes('kind: Service') ? '  • Service' : ''}
${yaml.includes('kind: Pod') ? '  • Pod' : ''}
${yaml.includes('kind: ConfigMap') ? '  • ConfigMap' : ''}

The YAML is valid and can be applied to a cluster.`,
            exitCode: 0
        }

    } catch (error) {
        return {
            output: '',
            error: `YAML Parse Error: ${error instanceof Error ? error.message : 'Invalid YAML syntax'}`,
            exitCode: 1
        }
    }
}

/* ============================================================================
   TERRAFORM HCL VALIDATOR
   ============================================================================ */

export function validateTerraformHCL(hcl: string): SimulationResult {
    try {
        const errors: string[] = []
        const warnings: string[] = []

        // Check for basic structure
        if (!hcl.includes('resource') && !hcl.includes('variable') && !hcl.includes('output') && !hcl.includes('module')) {
            errors.push('No Terraform resources, variables, or modules found')
        }

        // Check for provider configuration
        if (hcl.includes('resource') && !hcl.includes('provider')) {
            warnings.push('No provider configuration found')
        }

        // Check for unclosed braces
        const openBraces = (hcl.match(/{/g) || []).length
        const closeBraces = (hcl.match(/}/g) || []).length
        if (openBraces !== closeBraces) {
            errors.push(`Unmatched braces: ${openBraces} opening, ${closeBraces} closing`)
        }

        // Check for common AWS resource patterns
        if (hcl.includes('aws_instance') && !hcl.includes('ami')) {
            errors.push('aws_instance requires "ami" argument')
        }
        if (hcl.includes('aws_instance') && !hcl.includes('instance_type')) {
            errors.push('aws_instance requires "instance_type" argument')
        }

        // Check for variables without defaults
        const variableMatches = hcl.matchAll(/variable\s+"(\w+)"\s*{([^}]*)}/g)
        for (const match of variableMatches) {
            const varName = match[1]
            const varBody = match[2]
            if (!varBody.includes('default') && !varBody.includes('type')) {
                warnings.push(`Variable "${varName}" has no type or default value`)
            }
        }

        if (errors.length > 0) {
            return {
                output: '',
                error: 'Validation Errors:\n' + errors.map(e => `  • ${e}`).join('\n'),
                exitCode: 1
            }
        }

        let output = '✓ HCL validation successful!\n\n'

        if (warnings.length > 0) {
            output += 'Warnings:\n' + warnings.map(w => `  ⚠ ${w}`).join('\n') + '\n\n'
        }

        output += 'Terraform configuration is valid.'

        return { output, exitCode: 0 }

    } catch (error) {
        return {
            output: '',
            error: `HCL Parse Error: ${error instanceof Error ? error.message : 'Invalid HCL syntax'}`,
            exitCode: 1
        }
    }
}

/* ============================================================================
   MAIN EXECUTOR
   ============================================================================ */

// Singleton instances
const bashSimulator = new BashSimulator()
const dockerSimulator = new DockerSimulator()

export function executeCode(
    code: string,
    environment: EnvironmentType
): SimulationResult {
    try {
        switch (environment) {
            case 'bash':
                return bashSimulator.execute(code)

            case 'docker':
                return dockerSimulator.execute(code)

            case 'kubernetes':
                return validateKubernetesYAML(code)

            case 'terraform':
                return validateTerraformHCL(code)

            case 'python':
                // Python execution will be handled by Pyodide in the component
                return {
                    output: 'Python code will be executed by Pyodide runtime',
                    exitCode: 0
                }

            default:
                return {
                    output: `Unknown environment: ${environment}`,
                    error: `Unknown environment: ${environment}`,
                    exitCode: 1
                }
        }
    } catch (error) {
        return {
            output: '',
            error: error instanceof Error ? error.message : 'Unknown error',
            exitCode: 1
        }
    }
}

/* ============================================================================
   SAMPLE CODE SNIPPETS
   ============================================================================ */

export const sampleSnippets: Record<EnvironmentType, Record<string, string>> = {
    bash: {
        'Hello World': 'echo "Hello, DevOps World!"',
        'List Files': 'ls -la',
        'File Navigation': 'pwd\nls\ncd projects\npwd\nls',
        'Environment Variables': 'echo $USER\necho $HOME\necho $PATH',
        'File Operations': 'cat README.md\ngrep "DevOps" README.md',
        'System Info': 'whoami\ndate\nuname -a',
    },
    python: {
        'Hello World': `print("Hello, DevOps World!")`,
        'Variables & Types': `name = "DevOps"
age = 5
skills = ["Docker", "K8s", "AWS"]

print(f"Learning {name} for {age} years")
print(f"Skills: {', '.join(skills)}")`,
        'Functions': `def deploy_app(environment):
    print(f"Deploying to {environment}...")
    return f"{environment} deployment successful!"

result = deploy_app("production")
print(result)`,
        'Parse Log': `log = """
2024-01-13 10:30:00 INFO: Server started
2024-01-13 10:30:05 ERROR: Database connection failed
2024-01-13 10:31:00 INFO: Retrying connection
2024-01-13 10:31:05 ERROR: Connection timeout
"""

errors = [line for line in log.split('\\n') if 'ERROR' in line]
print(f"Found {len(errors)} errors:")
for error in errors:
    print(f"  • {error.strip()}")`,
        'List Comprehension': `# Generate list of server IPs
servers = [f"192.168.1.{i}" for i in range(10, 20)]
print("Server IPs:", servers)

# Filter even numbers
evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", evens)`,
    },
    docker: {
        'Basic Commands': 'docker --version\ndocker ps\ndocker images',
        'Run Container': 'docker run -d -p 8080:80 --name webapp nginx:latest\ndocker ps',
        'Container Management': 'docker ps\ndocker stop webapp\ndocker rm webapp',
        'Image Operations': 'docker images\ndocker pull redis:alpine\ndocker images',
        'Container Logs': 'docker logs webapp',
        'Build Image': 'docker build -t myapp:1.0 .',
    },
    kubernetes: {
        'Simple Pod': `apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80`,
        'Deployment': `apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp-deployment
  labels:
    app: webapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        image: nginx:latest
        ports:
        - containerPort: 80
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"`,
        'Service': `apiVersion: v1
kind: Service
metadata:
  name: webapp-service
spec:
  selector:
    app: webapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: LoadBalancer`,
        'ConfigMap': `apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_url: "postgresql://db:5432/app"
  log_level: "info"
  max_connections: "100"`,
    },
    terraform: {
        'AWS EC2 Instance': `resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "WebServer"
    Environment = "Development"
  }
}

output "instance_id" {
  value = aws_instance.web.id
}`,
        'Variables': `variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "instance_count" {
  description = "Number of instances"
  type        = number
  default     = 2
}`,
        'VPC Configuration': `resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "public-subnet"
  }
}`,
        'S3 Bucket': `resource "aws_s3_bucket" "data" {
  bucket = "my-devops-data-bucket"

  tags = {
    Environment = "Production"
    Purpose     = "Data Storage"
  }
}

resource "aws_s3_bucket_versioning" "data" {
  bucket = aws_s3_bucket.data.id

  versioning_configuration {
    status = "Enabled"
  }
}`,
    },
}
