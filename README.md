# AutoCommit


Automatically generate new commit messages at commit time, enforcing a consistent commit message style.


## Installation


Clone this repo  
```$ git clone https://github.com/lmeller-git/autocommit```  

navigate into the repo and get the following path:  
```$ cd autocommit/appl```  
```$ pwd```  

add the appl directory to your PATH:  
```$ export PATH="$PATH:<path-to-appl>```  

You will need to login to huggingfacehub in order to use the huggingfacehub api:  
https://huggingface.co/docs/huggingface_hub/v0.28.1/quick-start


## Usage


If you want to use autocommit in your repository:  
```$ autocommit <path-to-repo>```  

Now any commits made will be rewritten.  
If you want to force your commit message, include --force_msg IN you commit message  
```$ git commit -m "<message> --force_msg"```  

If you want to disable autocommit in your repository:  
```$ autocommit --uninstall <path-to-repo>```
