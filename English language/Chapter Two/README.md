## ⭕️ The topics we discuss in this chapter:

- [Concept of IDE & text editor](#concept-of-ide--text-editor)
- [Install Python](#-how-to-install-python)



# 💎Concept of IDE & Text Editor
> IDE and Text Editors are programs that developers use to write, edit, and manage programs and provide them with various features.
However, there are differences between the two, which we will discuss below

### **Concept IDE** =>
- An Integrated Development Environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE typically consists of a source code editor, build automation tools, and a debugger. It can also include features like version control integration, graphical user interface (GUI) builders, and many other tools that help simplify and automate the software development process.

### **Concept Text Editor** =>
- A text editor is a software application used for editing plain text files. Unlike an IDE, a text editor does not have any built-in features for compiling or debugging code. Text editors are used mainly by developers who prefer lightweight, customizable tools for writing code. Some popular text editors include Atom, Sublime Text, and Visual Studio Code.

---
##### 🔹While both IDEs and text editors can be used for writing code, the main difference between them is that IDEs provide a more comprehensive set of tools designed specifically for software development, while text editors offer a more minimalistic approach with fewer built-in features. Ultimately, the choice between using an IDE or a text editor comes down to personal preference and the specific needs of the developer.
---

</br>

![Alt text](../../src/ProgrammingEditors.jpg)

</br>

## 💢The difference between IDE and text editor

1. IDE (Integrated Development Environment) is an integrated development environment that includes tools such as coding, debugging, compiling, and testing. These tools are automatically synchronized with each other and help programmers quickly build complex programs.

2. Text Editor is a program used for editing and writing programming code. These tools typically only have text editing capabilities and do not have any other tools such as debuggers, compilers, and testers.

3. IDEs are typically used for complex and large projects, while Text Editors are used for smaller and simpler projects.

4. IDEs have the ability to detect code errors and help programmers run the program better and faster, while Text Editors do not have this capability.

5. IDEs are usually designed for specific programming languages such as Java, C++, and Python, while Text Editors can be used for all programming languages.

***

</br>

# 🐍 How to Install Python
> In this article, we will teach you how to install Python on Windows. Unlike other operating systems such as Mac OS and Linux, the Python programming language is not installed by default on the Windows operating system. However, this does not mean that this programming language will not be useful for Windows users or that Windows users will not be able to program their own applications using this language.

## Step 1 — Downloading the Python Installer
1. Go to the official Python download page for Windows.

2. Find a stable Python 3 release. This tutorial was tested with Python version 3.10.10.

3. Click the appropriate link for your system to download the executable file: Windows installer (64-bit) or Windows installer (32-bit).

![Alt text](../../src/1.png)

## Step 2 — Running the Executable Installer
1. After the installer is downloaded, double-click the .exe file, for example python-3.10.10-amd64.exe, to run the Python installer.

2. Select the Install launcher for all users checkbox, which enables all users of the computer to access the Python launcher application.

3. Select the Add python.exe to PATH checkbox, which enables users to launch Python from the command line.

![Alt text](../../src/2.png)

4. If you’re just getting started with Python and you want to install it with default features as described in the dialog, then click Install Now and go to Step 4 - Verify the Python Installation. To install other optional and advanced features, click Customize installation and continue.

5. The Optional Features include common tools and resources for Python and you can install all of them, even if you don’t plan to use them.

![Alt text](../../src/3.png)

**Select some or all of the following options:**

- Documentation: recommended
- pip: recommended if you want to install other Python packages, such as NumPy or pandas
- tcl/tk and IDLE: recommended if you plan to use IDLE or follow tutorials that use it
- Python test suite: recommended for testing and learning
- py launcher and for all users: recommended to enable users to launch Python from the command line

6. Click Next.
7. The Advanced Options dialog displays.

![Alt text](../../src/4.png)

**Select the options that suit your requirements:**

- Install for all users: recommended if you’re not the only user on this computer
- Associate files with Python: recommended, because this option associates all the Python file types with the launcher or editor
- Create shortcuts for installed applications: recommended to enable shortcuts for Python applications
- Add Python to environment variables: recommended to enable launching Python
- Precompile standard library: not required, it might down the installation
- Download debugging symbols and Download debug binaries: recommended only if you plan to create C or C++ extensions
- Make note of the Python installation directory in case you need to reference it later.

8. Click Install to start the installation.
9. After the installation is complete, a Setup was successful message displays.

![Alt text](../../src/5.png)

Step 3 — Verify the Python Installation
You can verify whether the Python installation is successful either through the command line or through the Integrated Development Environment (IDLE) application, if you chose to install it.

Go to Start and enter cmd in the search bar. Click Command Prompt.

Enter the following command in the command prompt:
```
python --version
```
An example of the output is:
```
Output
Python 3.10.10
```
