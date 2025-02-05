# AutoCommit

automatically generate new commit messages on push, enforcing a consistent commit message style.

## Usage
Include a commit-check in your CI pipeline. This should match one of the supplied yaml files in the repo.

force your messages via 
```git commit -m <msg> --force-msg```

automatically rewrite commit messgaed by setting env variable
``````
