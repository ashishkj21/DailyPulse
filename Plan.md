# Project Plan

### **Category: Environment Setup**  
**Task: Project Initialization**  
- Subtasks:  
  - Create GitHub repository.  
  - Set up project structure with backend and integrations folders.  

**Task: Environment Configuration**  
- Subtasks:  
  - Install FastAPI and PostgreSQL.  
  - Configure Slack Bolt SDK or Langchain.  

**Task: Tool Integration**  
- Subtasks:  
  - Connect Linear to GitHub.  
  - Test syncing issues between Linear and GitHub.  

---

### **Category: Basic Conversation Intelligence**  
**Task: Natural Language Parsing**  
- Subtasks:  
  - Implement extraction logic for accomplishments.  
  - Parse plans from text.  
  - Parse blockers from text.  

**Task: Follow-Up Questions**  
- Subtasks:  
  - Create logic to identify vague responses.  
  - Implement dynamic question generation for clarification.  

**Task: Blocker Identification**  
- Subtasks:  
  - Define keywords and phrases for blockers.  
  - Highlight blockers during update parsing.  

**Task: Writing Style Preferences**  
- Subtasks:  
  - Add functionality to store user preferences.  
  - Apply preferences to formatted outputs.  

---

### **Category: Drafting Updates (GitHub Integration)**  
**Task: GitHub API Integration**  
- Subtasks:  
  - Set up authentication for GitHub API.  
  - Fetch recent commits, PRs, and reviews.  

**Task: Draft Generation**  
- Subtasks:  
  - Use GitHub data to create standup update drafts.  
  - Ensure drafts include meaningful activity summaries.  

**Task: Edit Functionality**  
- Subtasks:  
  - Build a simple interface for editing drafts.  
  - Enable saving edited drafts.  

---

### **Category: User Experience**  
**Task: Slack Integration**  
- Subtasks:  
  - Create a basic Slack bot.  
  - Add message-based interaction.  

**Task: Daily Notifications**  
- Subtasks:  
  - Implement a scheduler for daily reminders.  
  - Customize reminders based on user history.  

**Task: Date-Specific Updates**  
- Subtasks:  
  - Add date-picker functionality in Slack.  
  - Fetch updates for specified dates.  

---

### **Category: Memory Across Sessions**  
**Task: Session Memory**  
- Subtasks:  
  - Design database schema to store user updates.  
  - Implement retrieval of previous updates.  

**Task: Follow-Up on Blockers**  
- Subtasks:  
  - Identify unresolved blockers.  
  - Create follow-up prompts based on blocker history.  

**Task: Format Preferences Memory**  
- Subtasks:  
  - Save formatting preferences (e.g., bullet points).  
  - Apply preferences in future interactions.  

---

### **Category: Testing & Demo Preparation**  
**Task: Functional Testing**  
- Subtasks:  
  - Write test cases for parsing logic.  
  - Test GitHub integration and Slack bot.  

**Task: Demo Flow Design**  
- Subtasks:  
  - Plan and script demo interactions.  
  - Include GitHub integration and memory features in the demo.  

---

### **Frontend**  
(Not necessary for Slack bot-only interactions, but if required for admin panels or dashboards):
- **React** or **Next.js**: For creating any interface to configure bot settings.  
- **Tailwind CSS**: For styling, if needed.  

---

### **Backend**  
- **FastAPI**: For building a scalable REST API. It’s lightweight, modern, and supports async operations.  
- **LangChain**: For integrating LLM-powered workflows like text parsing and response generation.  
- **NVIDIA NeMo Inference Server (NVIDIA NIM)**: For high-performance LLM execution if you want to leverage NVIDIA's ecosystem for hosting large models.  
- **Slack Bolt SDK (Python)**: To interact with Slack's API and implement Slack-specific bot functionalities.  

---

### **Database**  
- **PostgreSQL**: For storing user data, preferences, and session memory.  
- **Redis**: For caching (optional, but useful for storing temporary user sessions or responses).  

---

### **LLM Integration**  
- **OpenAI GPT API** (or another provider): For language generation and understanding.  
- **Hugging Face Models**: If you prefer running models locally or want custom fine-tuned options.  

---

### **Deployment**  
- **Docker**: To containerize the application for consistent deployment.  
- **Kubernetes** (optional): For scaling the application if needed in production.  
- **AWS/GCP/Azure**: For hosting.  
- **NVIDIA GPUs**: Recommended if using NeMo for LLM inferencing.  

---

### **Other Tools**  
- **Linear**: For task management.  
- **GitHub Actions**: For CI/CD pipelines.  

---

### Key Considerations:  
The NVIDIA blog code (https://developer.nvidia.com/blog/create-a-custom-slackbot-llm-agent-with-nvidia-nim-and-langchain/) highlights the use of NeMo and LangChain for LLM-powered workflows. We can:  
- Use **NVIDIA NIM** for running high-performance GPT models.  
- Employ **LangChain** to structure workflows (e.g., chaining Slack updates with memory retrieval). 