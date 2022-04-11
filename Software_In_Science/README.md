# Software In Science

### My ongoing journey in scientific computing

**Theme: All the code we write is software**. 

So what is software? What is the purpose of software?  Where does it live, and for how long?    
  

* **The Promise of Open Source**
    * Collaboration, outsourcing, citing code authors.

* **Why use Version Control and Open Source?**
    * Reason 1: sync your code across multiple computers (most important reason for me).  
    * Reason 2: version control (it's scary to code without it now). 
    * Reason 3: the possibility of open source software and collaborating through pull requests.
    * Git vs. Github 
    

* **Overview of Software Libraries**
    * Code breaks down into:
        * <ins>Functions</ins>
        * <ins>Files</ins>
        * <ins>Packages</ins>
    * The concept of library code vs. research code: two fundamentally different things. 
    * As an example, I have ~6 public repos for library code, and a similar number of private repos for research code. 
        * Will something be used in more than one paper?  Then it's probably a library.  
        * Is something specific to one paper? Then it's probably a research application of library code.
        * Possible idea: one repo for each data structure you use.
    * Writing TOOLS is important for completing projects faster in the future. 

* **Nuts and Bolts of Scientific Software**  
    * Types of functions: 
        * <ins>**config**</ins> - data from files into memory 
        * <ins>**input**</ins> - data from files into memory
        * <ins>**compute**</ins> - memory into memory 
        * <ins>**output**</ins> - memory into files 
        * <ins>**coordinators**</ins> - string it all together
        * <ins>**visualizing**</ins> - memory into pretty pictures. Sometimes done last.
    * Larger projects have layers of these types of functions, like fractal patterns 
    * internal data formats are extremely important (I use named tuples)
    * writing software packages
    * doesn't matter which language you use

* **Over-arching best practices for software**
    * Separate code from data from analysis (3 separate places)
    * Separate the coordination/drivers of experiments from their implementation
    * Think deeply before writing long programs: More code means more bugs
    * Abstract details away when appropriate 
    * Condense copy-pasted code into common functions    
    * However, duplicating code is okay in some cases

* **Miscellaneous tips**
    * Record your computer configuration in files. Every time you 'pip install' or 'sudo apt-get install', you should be writing it down in a type of diary. If your computer crashes or you need to nuke your operating system, you should be able to recover.  You should be able to start from a fresh installation.
    * Don't put your passwords in Github. It's amazing how many passwords are on Github.  You can search all of Github for the word 'Password' and it's scary.
    * IDEs are quite helpful (Sublime --> Atom --> PyCharm, increasing in complexity)
    * Conda Environments are your friend.
    * Github recently changed to PAT. Worth configuring to work this way. 


### Psychological shifts: 
1. Feeling comfortable putting code where other people can see it.
2. Thinking on a longer time-scale than a single project (TOOLS).
3. Contributing features and bug fixes back to the authors instead of adjusting local copy of code.
4. Dealing with illusory feelings of lack of progress when doing code re-writes or chasing down bugs.
5. Spending large amounts of time converting from one format to another.
6. Writing on forums for strangers to answer.
7. Reading more code than writing. 


### Benefits of making these shifts: 
1. Code becomes cleaner.
2. New experiments become easier and faster (investment paid off almost immediately).
3. Collaboration becomes easier.
4. Code might even be cite-able. 
5. Experiments greatly increase in complexty without becoming chaotic! 
