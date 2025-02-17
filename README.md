# AutoCommit


Automatically generate new commit messages at commit time, enforcing a consistent commit message style.


## Installation


Clone this repo

```$ git clone https://github.com/lmeller-git/autocommit```  

Navigate into the repo and add the following path to your PATH:

```$ cd autocommit/appl && echo 'export PATH="$PATH:'"$(pwd)"'"' >> ~/.bashrc && source ~/.bashrc```  

You will need to login to huggingfacehub in order to use the huggingfacehub api:  
https://huggingface.co/docs/huggingface_hub/v0.28.1/quick-start


## Usage


If you want to use autocommit in your repository:
 
```$ autocommit init <path-to-repo>```  

Now any commits made will be rewritten.


If you want to force your commit message,

commit with the --no-verify flag, to skip all commit hooks

```$ git commit -m "<message>" --no-verify```

or include --force-msg IN your commit message to skip only the message message generation  

```$ git commit -m "<message> --force-msg"```  

If you want to disable autocommit in your repository:

```$ autocommit uninstall <path-to-repo>```
