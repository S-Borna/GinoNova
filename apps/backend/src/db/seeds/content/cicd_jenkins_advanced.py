"""
Jenkins Advanced - CI/CD Pipeline Mastery
==========================================

Master Jenkins for enterprise CI/CD: declarative pipelines, shared libraries,
distributed builds, and production-grade automation. Still used by 60% of companies.
"""

JENKINS_ADVANCED = {
    "title": "Jenkins Advanced - Pipeline Mastery",
    "slug": "jenkins-pipelines-advanced",
    "description": "Master Jenkins for enterprise: declarative pipelines, Jenkinsfile best practices, shared libraries, distributed builds, and production CI/CD automation.",
    "difficulty": "advanced",
    "estimated_minutes": 135,
    "xp_reward": 230,
    "order_index": 1,
    "content": r"""# Jenkins Advanced - Pipeline Mastery

## 🎯 TL;DR (30 seconds)

Jenkins is the most popular CI/CD tool (60% market share). Master declarative pipelines, shared libraries,
and distributed builds for enterprise automation. Despite newer tools, Jenkins dominates enterprise environments.

**Why this matters:** Jenkins knowledge is required in 60% of DevOps jobs. It's not sexy, but it pays the bills.

---

## 🚀 Why Jenkins for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 60% of DevOps roles require Jenkins experience
- 70% of Enterprise CI/CD uses Jenkins
- 45% of Fortune 500 standardized on Jenkins

**Salary Impact (Sweden):**
| Role | Without Jenkins | With Jenkins Mastery | Difference |
|------|----------------|---------------------|------------|
| DevOps Engineer | 45,000 SEK | 52,000 SEK | **+16%** |
| Build Engineer | 43,000 SEK | 51,000 SEK | **+19%** |
| Senior DevOps | 58,000 SEK | 68,000 SEK | **+17%** |

**Reality:** GitHub Actions and GitLab CI are trendy, but enterprises run Jenkins.

---

## 📖 THEORY: Pipeline as Code

### Declarative vs Scripted Pipelines

**Declarative (recommended):**
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
        stage('Test') {
            steps {
                sh 'make test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'make deploy'
            }
        }
    }
}
```

**Benefits:** Structured, easier to read, built-in features.

---

## 🛠️ HANDS-ON: Jenkins Setup

### Step 1: Install with Docker

```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts

# Get initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# Access: http://localhost:8080
```

---

### Step 2: Complete Production Pipeline

**`Jenkinsfile`:**
```groovy
pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'docker.io'
        IMAGE_NAME = 'myapp'
        KUBECONFIG = credentials('kubeconfig')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 1, unit: 'HOURS')
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1'
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Test') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'pytest tests/unit'
                    }
                }
                stage('Integration Tests') {
                    steps {
                        sh 'pytest tests/integration'
                    }
                }
                stage('Security Scan') {
                    steps {
                        sh 'trivy image ${IMAGE_NAME}:${BUILD_NUMBER}'
                    }
                }
            }
        }

        stage('Push to Registry') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", 'docker-credentials') {
                        docker.image("${IMAGE_NAME}:${BUILD_NUMBER}").push()
                        docker.image("${IMAGE_NAME}:${BUILD_NUMBER}").push('latest')
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            when {
                branch 'main'
            }
            steps {
                sh 'kubectl apply -f k8s/staging/ --namespace=staging'
                sh 'kubectl rollout status deployment/myapp -n staging'
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy to production?', ok: 'Deploy'
                sh 'kubectl apply -f k8s/production/ --namespace=production'
                sh 'kubectl rollout status deployment/myapp -n production'
            }
        }
    }

    post {
        always {
            junit 'test-results/**/*.xml'
            cleanWs()
        }
        success {
            slackSend(
                color: 'good',
                message: "Build #${BUILD_NUMBER} succeeded: ${BUILD_URL}"
            )
        }
        failure {
            slackSend(
                color: 'danger',
                message: "Build #${BUILD_NUMBER} failed: ${BUILD_URL}"
            )
        }
    }
}
```

---

## 🎓 Shared Libraries

### Create Reusable Pipeline Functions

**`vars/buildDockerImage.groovy`:**
```groovy
def call(String imageName, String tag = 'latest') {
    echo "Building Docker image: ${imageName}:${tag}"

    sh """
        docker build -t ${imageName}:${tag} .
        docker tag ${imageName}:${tag} ${imageName}:${BUILD_NUMBER}
    """

    return [
        name: imageName,
        tag: tag,
        buildNumber: BUILD_NUMBER
    ]
}
```

**Usage in Jenkinsfile:**
```groovy
@Library('my-shared-library') _

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    buildDockerImage('myapp', 'latest')
                }
            }
        }
    }
}
```

---

## 🎤 Interview Questions & Answers

### Question 1: Pipeline Optimization

**Interviewer:** "Jenkins pipeline takes 30 minutes. How do you speed it up?"

❌ **Weak Answer:**
> "Use faster servers."

✅ **Strong Answer:**
> "Profile first: which stage is slow? Solutions: 1) Parallel execution - run tests in parallel. 2) Caching - cache dependencies (Maven, npm). 3) Distributed builds - use multiple agents. 4) Docker layer caching - reuse unchanged layers. 5) Skip unnecessary steps - use when conditions. 6) Incremental builds - only build changed modules. 7) Move slow tests to nightly builds. Measure impact: 30min → 10min typical improvement."

**Why this impresses:** Shows optimization methodology.

---

## 📚 Flashcards

**Q: What is Jenkinsfile?**
A: Pipeline definition stored in Git alongside code.

**Q: What is a Jenkins agent?**
A: Worker machine that executes pipeline jobs.

**Q: What is a shared library?**
A: Reusable pipeline code shared across projects.

---

## 🎓 Quiz

### Question 1

**Which keyword runs stages concurrently?**

A) concurrent
B) async
C) parallel ✅
D) simultaneous

**Answer:** C ✅

**Explanation:** parallel block runs nested stages concurrently.

---

## 🌟 Why This Module Prepares You for Jobs

✅ **Jenkins expertise** - Required in 60% of DevOps roles
✅ **Pipeline mastery** - Build enterprise CI/CD
✅ **Shared libraries** - Write reusable automation
✅ **Production skills** - Handle real-world complexity
✅ **Interview confidence** - Answer Jenkins questions expertly

**Time to complete:** 2.5 hours
**Job market impact:** Required in 60% of DevOps jobs
**Salary boost:** +16-19% average

---

**Module completed!** 🎉

**Next recommended:** GitLab CI/CD - Modern pipeline automation
"""
}

# Export as MODULE dict
MODULE = {
    "id": "cicd-jenkins-advanced",
    "slug": "cicd-jenkins-advanced",
    "title": "Jenkins Pipelines Advanced",
    "description": "Master Jenkins for enterprise: declarative pipelines, Jenkinsfile best practices, shared libraries, distributed builds, and production-grade CI/CD automation.",
    "icon": "⚙️",
    "category": "cicd",
    "difficulty": "advanced",
    "estimated_hours": 12,
    "tasks": [JENKINS_ADVANCED],
}
